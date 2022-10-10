from src.infra.repo.car_repository import CarRepository
from src.infra.repo.user_repository import UserRepository
from src.data.register_car import RegisterCar
from src.data.find_user import FindUser
from src.data.find_car import FindCar
from src.presenters.controllers import RegisterCarController


def register_car_composer() -> RegisterCarController:
    """Composing Register Car Route
    :param - None
    :return - Object with Register Car Route
    """

    repository = CarRepository()
    find_user_use_case = FindUser(UserRepository())
    find_car_use_case = FindCar(CarRepository())
    use_case = RegisterCar(repository, find_user_use_case, find_car_use_case)
    register_car_route = RegisterCarController(use_case)

    return register_car_route
