from fastapi import APIRouter, Depends
from starlette import status

from .schemas import MessageScheme
from .service import Service
from .builder import service_builder


router = APIRouter()


@router.get(
    "/messages",
    status_code=status.HTTP_200_OK,
    response_model=list[MessageScheme],
)
def get_all_messages(
        service: Service = Depends(service_builder)
):
    """View return all messages"""
    return service.get_all_messages()


@router.post(
    "/message",
    status_code=status.HTTP_201_CREATED,
)
def add_message(
        message: MessageScheme,
        service: Service = Depends(service_builder),
):
    """View for insert message"""
    service.add_message(message)
