from typing import Type, Dict, List
from src.data.find_user import FindUser
from src.data.find_car import FindCar
from src.data.interfaces import CarRepositoryInterface as CarRepository
from src.domain.use_cases import RegisterCar as RegistercarInterface
from src.domain.models import Users, Cars


class RegisterCar(RegistercarInterface):
    """ Class to define use case: Register Car """

    def __init__(self, car_repository: List[CarRepository], find_user: Type[FindUser], find_car: Type[FindCar]):
        self.car_repository = car_repository
        self.find_user = find_user
        self.find_car = find_car

    def registry(
        self, model: str, color: str, user_information: Dict[int, str]
        ) -> Dict[bool, Cars]:
        """Registry Car
        :param - model: car model
               - color: type of the color
               - user_information: Dictionaty with user_id and/or user_name
        :return - Dictionaty with informations of the process
        """

        response = None

        # Validating entry and trying to find an user
        validate_entry = isinstance(color, str) and isinstance(model, str)
        user = self.__find_user_information(user_information)
        user_has_less_than_three_cars = self.__numbers_of_cars_by_user(user)
        checker = validate_entry and user["Success"] and user_has_less_than_three_cars
        if checker:
            response = self.car_repository.insert_car(
                model=model, color=color, user_id=user_information["user_id"]
            )

        return {"Success": checker, "Data": response}

    def __find_user_information(
        self, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        """Check user Infos and select user
        :param - user_information: Dictionary with user_id and/or user_name
        :return - Dictionary with the response of find_use use case
        """

        user_founded = None
        user_params = user_information.keys()

        if "user_id" in user_params and "user_name" in user_params:
            user_founded = self.find_user.by_id_and_name(
                user_information["user_id"], user_information["user_name"]
            )

        elif "user_id" not in user_params and "user_name" in user_params:
            user_founded = self.find_user.by_name(user_information["user_name"])

        elif "user_id" in user_params and "user_name" not in user_params:
            user_founded = self.find_user.by_id(user_information["user_id"])

        else:
            return {"Success": False, "Data": None}

        return user_founded


    def __numbers_of_cars_by_user(
        self, user_information: Users) -> Dict[bool, List[Users]]:
        """Check user Infos and select user
        :param - user_information: Dictionary with user_id and/or user_name
        :return - Dictionary with the response of find_use use case
        """
        cars_by_user = self.find_car.by_user_id(user_id=user_information["Data"][0].id)
        if cars_by_user["Data"] is not None:
            return len(cars_by_user["Data"]) <= 3
        return True
