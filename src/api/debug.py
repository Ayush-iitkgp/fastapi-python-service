from fastapi import APIRouter
from starlette import status
router = APIRouter()


@router.get(
    path='/', status_code=status.HTTP_200_OK,
)
async def test():
    return 'success'