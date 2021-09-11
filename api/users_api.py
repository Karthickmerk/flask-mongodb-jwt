
from services.common_service import token_required
from flask_restful import Resource,request
from flask import redirect,url_for,jsonify,Flask
from db.db_utils import post_to_db, update_to_db,delete_from_db
from services.template_service import get_service, update_service,post_service,get_all_service
from services.user_service import register, login



class Users(Resource):
    def post(self):
        json_data = request.get_json()
        result = register(json_data=json_data)
        return result

class Login(Resource):
    def post(self):
        json_data = request.get_json()
        result = login(json_data=json_data)
        return result        