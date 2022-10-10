import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from src.infra.config import Base


class CarColor(enum.Enum):
    """ Defining car color """

    yellow = "yellow"
    blue = "blue"
    gray = "gray"


class CarModel(enum.Enum):
    """ Defining car model """

    hatch = "hatch"
    sedan = "sedan"
    convertible = "convertible"


class Cars(Base):
    """ Cars Entity """

    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    model = Column(Enum(CarModel), nullable=False)
    color = Column(Enum(CarColor), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Car: [model={self.model}, color={self.color}, user_id={self.user_id}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.model == other.model
            and self.color == other.color
            and self.user_id == other.user_id
        ):
            return True
        return False
