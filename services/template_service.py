from db.db_utils import fetch_from_db, post_to_db, update_to_db,fetch_all_from_db
from flask import make_response

def get_service(id):
    data = fetch_from_db(id=id)
    return data
def get_all_service(index):
    data = fetch_all_from_db(index)
    return data

def update_service(id,data):
    data = update_to_db(data=data,id=id)
    return data

def post_service(index,data):
    index = "name_"
    result = post_to_db(index,data)
    return result