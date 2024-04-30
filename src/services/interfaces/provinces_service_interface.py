from abc import ABC, abstractmethod


class ProvincesServiceInterface(ABC):
    """provinces interface"""

    @abstractmethod
    def find_province(self, name: str):
        """get province by name"""
        raise NotImplemented("Method not implemented")

    @abstractmethod
    def get_provinces(self):
        """get provinces"""
        raise NotImplemented("Method not implemented")
