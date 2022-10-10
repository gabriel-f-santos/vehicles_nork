# pylint: disable=E1101

from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.data.interfaces import CarRepositoryInterface
from src.domain.models import Cars
from src.infra.config import DBConnectionHandler
from src.infra.entities import Cars as CarsModel


class CarRepository(CarRepositoryInterface):
    """ Class to manage Car Repository """

    @classmethod
    def insert_car(cls, model: str, color: str, user_id: int) -> Cars:
        """
        Insert data in CarsEntity entity
        :param acepted
               - model: car model
               - color: car color
               - user_id: id of the owner (FK)
        :return - tuple with new car inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_car = CarsModel(model=model, color=color, user_id=user_id)
                db_connection.session.add(new_car)
                db_connection.session.commit()

                return Cars(
                    id=new_car.id,
                    model=new_car.model.value,
                    color=new_car.color.value,
                    user_id=new_car.user_id,
                )

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_car(cls, car_id: int = None, user_id: int = None) -> List[Cars]:
        """
        Select data in CarsEntity entity by id and/or user_id
        :param - car_id: Id of the car registry
               - user_ud: Id of the owner
        :return - List with Cars selected
        """

        try:

            query_data = None

            if car_id and not user_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(CarsModel)
                        .filter_by(id=car_id)
                        .one()
                    )
                    query_data = [data]

            elif not car_id and user_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(CarsModel)
                        .filter_by(user_id=user_id)
                        .all()
                    )
                    query_data = data

            elif car_id and user_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(CarsModel)
                        .filter_by(id=car_id, user_id=user_id)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

        return None
