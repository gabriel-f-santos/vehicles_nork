from flask import Blueprint, jsonify, request
from src.main.composer import (
    register_user_composer,
    register_car_composer,
    find_car_composer,
    find_user_composer,
)
from src.main.adapter import flask_adapter

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api/users", methods=["POST"])
def register_user():
    """ register user route """

    message = {}
    response = flask_adapter(request=request, api_route=register_user_composer())

    if response.status_code < 300:
        message = {
            "type": "users",
            "id": response.body.id,
            "attributest": {"name": response.body.name},
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/cars", methods=["POST"])
def register_cars():
    """ register cars route """

    message = {}
    response = flask_adapter(request=request, api_route=register_car_composer())

    if response.status_code < 300:
        message = {
            "type": "cars",
            "id": response.body.id,
            "attributes": {
                "model": response.body.model,
                "color": response.body.color,
            },
            "relationships": {"owner": {"type": "users", "id": response.body.user_id}},
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/cars", methods=["GET"])
def finder_cars():
    """ find cars route """

    message = {}
    response = flask_adapter(request=request, api_route=find_car_composer())

    if response.status_code < 300:
        message = []

        for element in response.body:
            message.append(
                {
                    "type": "cars",
                    "id": element.id,
                    "attributest": {
                        "model": element.model.value,
                        "color": element.color.value,
                    },
                    "relationships": {
                        "owner": {"type": "users", "id": element.user_id}
                    },
                }
            )

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/users", methods=["GET"])
def finder_users():
    """ find users route """

    message = {}
    response = flask_adapter(request=request, api_route=find_user_composer())

    if response.status_code < 300:
        message = []

        for element in response.body:
            message.append(
                {
                    "type": "users",
                    "id": element.id,
                    "attributest": {"name": element.name},
                }
            )

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )
