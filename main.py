import jwt
from jwt import DecodeError

#Global variables
secret = 'acelera'

def create_token(data, secret):
    return jwt.encode(data, secret, algorithm='HS256')

def verify_signature(token):
    #Try to decode token and return a deciphered information
    try:
        information = jwt.decode(token, secret, algorithms='HS256')
        return information
    # If the token is Invalid, it returns the error message.
    except DecodeError:
        return {"error": 2}
        

#Reference website: https://medium.com/trainingcenter/json-web-tokens-explicado-dba4ae3a9579