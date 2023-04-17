import requests

from flask import Flask
from flask_restx import Api, Resource

from src.server.instace import server

app, api = server.app, server.api

@api.route('/pokemon')
class Pokemon(Resource):
    def get(self, ):
        response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
        return response.json(), response.status_code