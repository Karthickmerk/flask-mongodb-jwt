
from db.db_utils import fetch_from_db
import jwt
from functools import wraps
from flask import redirect,url_for,jsonify,Flask,request
import os
from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.getenv('jwt_key')

app = Flask(__name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, SECRET_KEY)
            current_user=fetch_from_db(index='users',id=id)
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users contex to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated

def get_access_token(user_id):
    token = jwt.encode({'user_id': user_id}, SECRET_KEY)
    return token