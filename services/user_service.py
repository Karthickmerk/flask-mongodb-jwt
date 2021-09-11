from pymongo.message import query
from common.common_utils import make_id
from db.db_utils import fetch_from_db, post_to_db, update_to_db,fetch_all_from_db
from flask import make_response
from  werkzeug.security import generate_password_hash, check_password_hash
from services.common_service import get_access_token
default_index = "users"

def register(json_data):
    email = json_data['email']
    query = {"email":email}
    is_already_user= fetch_from_db(index=default_index,query=query)
    if not is_already_user:
        user_data = {
            "_id" : make_id(api=default_index),
            "user_name":json_data['user_name'],
            "email" : json_data['email'],
            "password" : generate_password_hash(json_data['password'])
        }
        result = post_to_db(index=default_index ,data=user_data)
        if not result:
            return {"code":500, "msg":"something went wrong!"}
        else:
            return result
    return {"code":400, "msg":"Already registered!"}

def login(json_data):
    email = json_data['email']
    query = {"email":email}
    user_data = fetch_from_db(index=default_index,query=query)
    password = user_data['password']
    if check_password_hash(password, json_data['password']):
        token = get_access_token(user_id=user_data['_id'])
        return token