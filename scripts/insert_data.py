import asyncio
import json
from datetime import datetime
from src.db.repositories.pnl import PnlRepository
from src.db.repositories.currency import CurrencyRepository
from src.models.currency import InCurrencySchema
from src.models.pnl import InPnlSchema
import uuid
from src.db.session import async_session

aw = asyncio.get_event_loop().run_until_complete


async def main():
    with open('data/financial_data.json') as json_file:
        data = json.load(json_file)
        async with async_session() as db:
            async with db.begin_nested():
                currency_repository = CurrencyRepository(db_session=db)
                currency_data = data["pnl"]["MXN"]
                currency = InCurrencySchema(currency_code=currency_data["currency"])
                inserted_currency = await currency_repository.create(values=currency, commit=False)

                pnl_repository = PnlRepository(db_session=db)
                pnl_data = currency_data["data"]
                for data_key, data_value in pnl_data.items():
                    for report_date_str, value in data_value.items():
                        report_date = datetime.strptime(report_date_str, "%Y-%m-%d").date()
                        pnl = InPnlSchema(currency_id=inserted_currency.id, data_key=data_key,
                                        data_value=value, report_date=report_date)
                        await pnl_repository.create(values=pnl, commit=False)
                await db.commit()

aw(main())
