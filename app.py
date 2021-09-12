from flask import Flask, jsonify, url_for, redirect, request
from flask_restful import Api
from flask_jwt_extended import JWTManager

from api.template_api import  Template_API, Template_single
from api.users_api import Users,Login

app = Flask(__name__)

api = Api(app)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)



api.add_resource(Template_API, "/api")
api.add_resource(Template_single, "/api/<string:id>")


api.add_resource(Users, "/user")
api.add_resource(Login, "/login")

if __name__ == "__main__":
    app.run(debug=True)