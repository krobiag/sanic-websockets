from sanic.blueprints import Blueprint
from sanic.response import json
from sanic_ext import serializer
from sanic_ext import openapi
import random

from backend.data import test_car, test_success, test_car_makes
from backend.models import Car, Status, ApiOkResponse
from backend.serializer import api_response_serializer
from backend.socket import sio

blueprint = Blueprint('Car', '/car')


@blueprint.get("/", strict_slashes=False)
@openapi.summary("Fetches all cars")
@openapi.description("Really gets the job done fetching these cars.")
@openapi.response(200, {"application/json": Car}, description="Array of Cars")
@openapi.response(500, {"application/json": ApiOkResponse})
@serializer(api_response_serializer)
def car_list(request):
    return [test_car]


@blueprint.get("/<car_id:int>", strict_slashes=True)
@openapi.summary("Fetches a car")
@openapi.response(200, {"application/json": Car})
@openapi.response(404, {"application/json": ApiOkResponse})
@serializer(api_response_serializer)
def car_get(request, car_id):
    return test_car


@blueprint.put("/<car_id:int>", strict_slashes=True)
@openapi.summary("Updates a car")
@openapi.body(
    {"application/json": Car},
    description="Body description",
    required=True,
)
@openapi.parameter("AUTHORIZATION", str, location="header")
@openapi.response(200, {"application/json": Car})
def car_put(request, car_id):
    return json(test_car)


@blueprint.delete("/<car_id:int>", strict_slashes=True)
@openapi.summary("Deletes a car")
@openapi.response(204, {"application/json": Status})
def car_delete(request, car_id):
    return json(test_success)


@blueprint.get("/get_random_car", strict_slashes=False)
async def visit_random_country_generator(request):
    await sio.emit('visit_random_country_generator', {'message': 'visit_random_country_generator', "data": random.choice(test_car_makes)})
    return json({"message": "go to http://localhost:3000 and keep refreshing this page"})
