from typing import Optional
from abc import ABC, abstractmethod


class Controller(ABC):
    """handler"""

    @abstractmethod
    def handle(self, request: Optional[any] = None):
        """controller handling"""

        raise NotImplementedError("Method not implemented")
