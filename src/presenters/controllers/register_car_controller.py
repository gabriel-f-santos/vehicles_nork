from typing import Type
from src.main.interface import RouteInterface
from src.domain.use_cases import RegisterCar
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class RegisterCarController(RouteInterface):
    """ Class to Define Route to register_car use case """

    def __init__(self, register_car_use_case: Type[RegisterCar]):
        self.register_car_use_case = register_car_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Method to call use case """

        response = None

        body_params = http_request.body.keys()

        if (
            "model" in body_params
            and "color" in body_params
            and "user_information" in body_params
        ):
            user_information_params = http_request.body["user_information"].keys()
            if (
                "user_id" in user_information_params
                or "user_name" in user_information_params
            ):

                model = http_request.body["model"]
                color = http_request.body["color"]
                user_information = http_request.body["user_information"]


                response = self.register_car_use_case.registry(
                    model=model,
                    color=color,
                    user_information=user_information,
                )

            else:
                response = {"Success": False, "Data": None}

        else:
            response = {"Success": False, "Data": None}

        if response["Success"] is False:
            https_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=https_error["status_code"], body=https_error["body"]
            )

        return HttpResponse(status_code=200, body=response["Data"])
