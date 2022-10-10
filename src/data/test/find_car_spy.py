from typing import Dict, List
from src.domain.models import Cars
from src.domain.test import mock_car


class FindCarSpy:
    """ Class to mock usecase: Find Car """

    def __init__(self, car_repository: any):
        self.car_repository = car_repository
        self.by_car_id_param = {}
        self.by_user_id_param = {}
        self.by_car_id_and_user_id_param = {}

    def by_car_id(self, car_id: int) -> Dict[bool, List[Cars]]:
        """ Select Car By car_id """

        self.by_car_id_param["car_id"] = car_id
        response = None
        validate_entry = isinstance(car_id, int)

        if validate_entry:
            response = [mock_car()]

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Cars]]:
        """ Select Car By user_id """

        self.by_user_id_param["user_id"] = user_id
        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = [mock_car()]

        return {"Success": validate_entry, "Data": response}

    def by_car_id_and_user_id(
        self, car_id: int, user_id: int
    ) -> Dict[bool, List[Cars]]:
        """ Select Car By user_id """

        self.by_car_id_and_user_id_param["car_id"] = car_id
        self.by_car_id_and_user_id_param["user_id"] = user_id
        response = None
        validate_entry = isinstance(user_id, int) and isinstance(car_id, int)

        if validate_entry:
            response = [mock_car()]

        return {"Success": validate_entry, "Data": response}
