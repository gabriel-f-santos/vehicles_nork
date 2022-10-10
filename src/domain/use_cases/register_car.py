from abc import ABC, abstractclassmethod
from typing import Dict
from src.domain.models import Cars


class RegisterCar(ABC):
    """ Interface to FindCar use case """

    @abstractclassmethod
    def registry(
        cls, model: str, color: str, user_information: Dict[int, str]) -> Dict[bool, Cars]:
        """ use case """

        raise Exception("Should implement method: registry")
