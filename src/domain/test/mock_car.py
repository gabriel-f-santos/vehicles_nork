from faker import Faker
from src.domain.models import Cars

faker = Faker()


def mock_car() -> Cars:
    """Mocking Car
    :param - None
    :return - Fake Car registry
    """

    return Cars(
        id=faker.random_number(digits=5),
        color="yellow",
        model="sedan",
        user_id=faker.random_number(digits=5),
    )
