from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient
import jwt #Utilizar: pip install pyjwt[crypto]
from BaseModels import UserBaseModels
from fastapi import HTTPException

def Authorization(email, password):
    with MongoClient() as client:
        db = client["schedule"]
        specific_user = db.user_credentials.find_one({"email":email})
        try:
            if specific_user["password"] == password:
                payload_data = {
                    "email": email
                }
                token= jwt.encode(
                    payload = payload_data,
                    key = 'group3Authorize'
                )
                return {"message":token}
            else:
                raise HTTPException(status_code=400, detail="Error - Wrong credentials. Try again")
        except:
            raise HTTPException(status_code=400, detail="Error - Wrong credentials. Try again")

def GetByEmail(email):
    with MongoClient() as client:
        db = client["schedule"]
        specific_user = db.user_schedules.find_one({"email":email})
        try:
            return specific_user["schedules"]
        except:
            raise HTTPException(status_code=404, detail="Error - User not found")

def Create(request: UserBaseModels.User):
    with MongoClient() as client:
        db = client["schedule"]
        db.user_credentials.insert_one(jsonable_encoder(request))

        return {"message":"User Created"}
