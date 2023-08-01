from fastapi import APIRouter
from fastapi import Request

router = APIRouter()


@router.get(
    path='/test',
    description='test router',
)
async def test(
    request: Request,
):
    return 'success'