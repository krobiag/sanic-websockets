from datetime import date

from sanic_ext import openapi

class ApiResponse:
    success = openapi.Boolean()
    request_id = openapi.String()
    status = openapi.Integer()
    data = openapi.String()

class ApiOkResponse:
    success = openapi.Boolean()
    request_id = openapi.String()
    status = openapi.Integer()
    data = openapi.String()

class Manufacturer:
    id: openapi.Integer()
    name = openapi.String()
    start_date = openapi.Date()


class Driver:
    id: openapi.Integer()
    name = openapi.String()
    birthday = openapi.Date()


class Car:
    id: openapi.Integer()
    on = openapi.Boolean()
    doors = openapi.Integer()
    color = openapi.String()
    make = Manufacturer
    driver = Driver
    passengers = openapi.Array(Driver, required=["name", "birthday"])


class Garage:
    spaces = openapi.Integer()
    cars = [Car]


class Status:
    success = openapi.Boolean()


class Station:
    location = openapi.String(description="location")
    contact = openapi.Integer(description="phone number")
    
