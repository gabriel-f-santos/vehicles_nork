from faker import Faker
from src.infra.test import CarRepositorySpy
from .find import FindCar

faker = Faker()


def test_by_car_id():
    """ Testing car_id method in FindCar """

    car_repo = CarRepositorySpy()
    find_car = FindCar(car_repo)

    attribute = {"car_id": faker.random_number(digits=2)}
    response = find_car.by_car_id(car_id=attribute["car_id"])

    # Testing Input
    assert car_repo.select_car_param["car_id"] == attribute["car_id"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]

