
from flask_restful import Resource,request
from flask import redirect,url_for,jsonify,Flask
from db.db_utils import post_to_db, update_to_db,delete_from_db
from services.template_service import get_service, update_service,post_service,get_all_service
from functools import wraps
from services.common_service import token_required
from flask_jwt_extended import get_jwt_identity,jwt_required
import jwt

app = Flask(__name__)

APP_URL = "http://127.0.0.1:5000"

class Template_API(Resource):
    @jwt_required()
    def get(self):
        index = "name_"
        result = get_all_service(index)
        current_user = get_jwt_identity()['email']
        print(current_user)
        return jsonify({"result": result })

    def post(self):
        json_data = request.get_json()
        result = post_service(index="name_",data=json_data)
        return {"result": result }

class Template_single(Resource):
    def get(self):
        result = get_service(id=id)
        return jsonify({"result": result })

    def put(self, id):
        data = request.get_json()
        id = request.args.get('id')
        result = update_service(data=data,id=id)
        return result

    def delete(self, id):
        id = request.args.get('id')
        result = delete_from_db(id=id)
        return result

