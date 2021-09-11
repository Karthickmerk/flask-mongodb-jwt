from flask import Flask, jsonify, url_for, redirect, request
from flask_restful import Api, Resource


from api.template_api import  Template_API, Template_single

app = Flask(__name__)

api = Api(app)

api.add_resource(Template_API, "/api")
api.add_resource(Template_single, "/api/<string:id>")

if __name__ == "__main__":
    app.run(debug=True)