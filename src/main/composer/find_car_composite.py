from src.infra.repo.car_repository import CarRepository
from src.presenters.controllers import FindCarController
from src.data.find_car import FindCar


def find_car_composer() -> FindCarController:
    """Composing Find Car Route
    :param - None
    :return - Object with Find Car Route
    """

    repository = CarRepository()
    use_case = FindCar(repository)
    find_car_route = FindCarController(use_case)

    return find_car_route
