from typing import Dict, List, Type
from src.data.interfaces import CarRepositoryInterface as CarRepository
from src.domain.use_cases import FindCar as FindCarInterface
from src.domain.models import Cars


class FindCar(FindCarInterface):
    """ Class to define usecase: Find Car """

    def __init__(self, car_repository: Type[CarRepository]):
        self.car_repository = car_repository

    def by_car_id(self, car_id: int) -> Dict[bool, List[Cars]]:
        """Select Car By car_id
        :param - car_id: id of the car
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(car_id, int)

        if validate_entry:
            response = self.car_repository.select_car(car_id=car_id)

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Cars]]:
        """Select Car By user_id
        :param - user_id: id of the user owne of the car
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.car_repository.select_car(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_car_id_and_user_id(
        self, car_id: int, user_id: int
    ) -> Dict[bool, List[Cars]]:
        """Select Car By user_id
        :param - user_id: id of the user owne of the car
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int) and isinstance(car_id, int)

        if validate_entry:
            response = self.car_repository.select_car(car_id=car_id, user_id=user_id)

        return {"Success": validate_entry, "Data": response}
