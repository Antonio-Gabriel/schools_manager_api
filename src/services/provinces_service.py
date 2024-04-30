import json
from pathlib import Path

from realpath import SRC_DIR

from src.services.interfaces.provinces_service_interface import (
    ProvincesServiceInterface
)


class ProvincesService(ProvincesServiceInterface):
    def __init__(self) -> None:
        self.__provinces = json.loads(
            Path(f"{SRC_DIR}/data/provinces.json").read_text())

    def find_province(self, name: str):
        """get province by name"""
        provinces = self.__provinces["Angola"]["Provincias"]
        province = next(
            (p for p in provinces if p["nome"].capitalize() == name.capitalize()), None)
        return province

    def get_provinces(self):
        """get provinces"""
        provinces = self.__provinces["Angola"]["Provincias"]
        return provinces
