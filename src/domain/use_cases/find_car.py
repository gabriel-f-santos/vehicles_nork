from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Cars


class FindCar(ABC):
    """ Interface to FindCar use case """

    @abstractmethod
    def by_car_id(self, car_id: int) -> Dict[bool, List[Cars]]:
        """ Specific case """

        raise Exception("Should implement method: by_car_id")

    @abstractmethod
    def by_user_id(self, user_id: int) -> Dict[bool, List[Cars]]:
        """ Specific case """

        raise Exception("Should implement method: by_user_id")

    @abstractmethod
    def by_car_id_and_user_id(
        self, car_id: int, user_id: int
    ) -> Dict[bool, List[Cars]]:
        """ Specific case """

        raise Exception("Should implement method: by_car_id_and_user_id")
