from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Cars


class CarRepositoryInterface(ABC):
    """ Interface to Car Repository """

    @abstractmethod
    def insert_car(self, model: str, color: str, user_id: int) -> Cars:
        """ abstractmethod insert car """

        raise Exception("Method not implemented")

    @abstractmethod
    def select_car(self, car_id: int=None, user_id: int=None) -> List[Cars]:
        """ abstractmethod select car """

        raise Exception("Method not implemented")
