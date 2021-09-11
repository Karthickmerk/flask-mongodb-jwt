from flask_pymongo import PyMongo
from flask import Flask, jsonify
from common.common_utils import make_id
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'testdb'
app.config['MONGO_URI'] = os.getenv('mongo_db_uri')
mongo = PyMongo(app)


def fetch_all_from_db(index):
    fetched_data=[]
    table = mongo.db[index]
    result = table.find()
    for res in result:
        fetched_data.append(res)
    return fetched_data

def fetch_from_db(index=None,query=None,id=id):
    if query is None:
        query = {"_id":id}
    table = mongo.db[index]
    result = table.find_one(query)
    return result


def post_to_db(index,data):
    table = mongo.db[index ]
    if not data:
        data = {"msg": "ERROR"}
        return jsonify(data)
    else:
        id = make_id(api=index)
        data.update({"_id":id})
        if id:
            if table.find_one({"id": id}):
                return {"msg": "tweet already exists."}
            else:
                result = table.insert(data)
                if result:
                    return {"msg": "User creted", "data":result}
        else:
            return {"msg": "id number missing"}

def update_to_db(data,id):
    res = mongo.db.name_.find_one_and_update({'_id': id}, {'$set': data})
    if res:
        result = {
            "code": 200,
            "result": res,
            "msg": "Updated Successfully!"
        } 
        return result
    else:
        result = {
            "code": 500,
            "msg": "Something wrong!"
        } 
    return result


def delete_from_db(id):
    result= mongo.db.name_.find_one_and_delete({'id': id})
    return result