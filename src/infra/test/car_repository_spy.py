from typing import List
from src.domain.models import Cars
from src.domain.test import mock_car


class CarRepositorySpy:
    """ Spy to Car Repository """

    def __init__(self):
        self.insert_car_param = {}
        self.select_car_param = {}

    def insert_car(self, model: str, color: str, user_id: int) -> Cars:
        """ Spy all the attributes """

        self.insert_car_param["model"] = model
        self.insert_car_param["color"] = color
        self.insert_car_param["user_id"] = user_id

        return mock_car()

    def select_car(self, car_id: int=None, user_id: int=None) -> List[Cars]:
        """ Spy all the attributes """

        self.select_car_param["car_id"] = car_id
        self.select_car_param["user_id"] = user_id

        return [mock_car()]
