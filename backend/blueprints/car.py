from sanic.blueprints import Blueprint
from sanic.response import json, html
from sanic_ext import serializer
from sanic_ext import openapi
from sanic_ext.extensions.openapi.definitions import RequestBody, Response
from sanic_ext.extensions.openapi.types import Schema
from sanic import Sanic, Websocket, Request

from backend.data import test_car, test_success
from backend.models import Car, Status, ApiOkResponse, ApiResponse
from backend.serializer import api_response_serializer

blueprint = Blueprint('Car', '/car')


@blueprint.get("/", strict_slashes=False)
@openapi.summary("Fetches all cars")
@openapi.description("Really gets the job done fetching these cars.")
@openapi.response(200, {"application/json": Car}, description="Array of Cars")
@openapi.response(500, {"application/json": ApiOkResponse})
@serializer(api_response_serializer)
def car_list(request):
    # """Fetches all cars

    # Really gets the job done fetching these cars.

    # openapi:
    # ---
    # responses:
    #   '200':
    #     description: Just some dots
    #     content:
    #         application/json:
    #             schema:
    #                 oneOf:
    #                     - $ref: '#/components/schemas/Car'
    #                     - $ref: '#/components/schemas/Dog'
    #                     - $ref: '#/components/schemas/Hamster'
    # """
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

# @blueprint.get('/html2', strict_slashes=False)
# @openapi.no_autodoc
# async def handle_request(request):
#   return html("""
#     <html>
#         <head>
#             <script>
#                 var ws = new WebSocket("ws://" + location.host + '/car/feed');
#                 ws.onmessage = function (event) {
#                     console.log(event.data); document.body.innerHTML += "<div>" + event.data + "</div>";
#                 };
#                 ws.onclose = function (event) {
#                     document.body.innerHTML += "<div>closed</div>";
#                 };
#                 ws.onerror = function(err) {
#                     console.error(">>>err", err)
#                 };

#                 ws.onopen = function(err) {
#                     console.log(">>>open", ws)
#                     document.body.innerHTML += "<div>Connection open</div>";
#                 };

#                 var test = () => {
#                     ws.send("Howdy!!")
#                 };
#             </script>
#         </head>
#         <body>
#             <h1>Hello socket!</h1>
#             <p>hello</p>
#             <p><button onclick="test()">Send</button></p>
#         </body>
#     </html>""")
