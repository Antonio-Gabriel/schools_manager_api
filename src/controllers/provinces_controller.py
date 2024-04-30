
from typing import Optional, Type

from src.controllers.controller import Controller
from src.services.provinces_service import ProvincesService


class GetProvincesController(Controller):
    def handle(self, request: Optional[any] = None):
        provinces_service = ProvincesService()
        provinces = provinces_service.get_provinces()
        return provinces
