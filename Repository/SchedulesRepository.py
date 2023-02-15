from pymongo import MongoClient
from BaseModels import SchedulesBaseModels
from Repository import UserRepository
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException

def ListAllShedules():
    with MongoClient() as client:
        db = client["schedule"]
        data = db.user_schedules.find({})
        users_schedules = []
        users_schedules = [{"email": user["email"], "schedules":user["schedules"]} for user in data]
        return users_schedules

def Create(request: SchedulesBaseModels.Schedules):
    schedules = UserRepository.GetByEmail(request.email)
    if schedules:
        with MongoClient() as client:
           db = client["schedule"]
           schedules.extend(request.schedules)
           db.user_schedules.update_one({'email':request.email}, {'$set':{'schedules':jsonable_encoder(schedules)}})     
    else:
        with MongoClient() as client:
            db = client["schedule"]
            db.user_schedules.insert_one(jsonable_encoder(request))
    return {'message':'Schedule Createad'}

def GetSchedulesByEmail(email):
    with MongoClient() as client:
        db = client["schedule"]
        specific_user = db.user_schedules.find_one({"email":email})
        try:
            return {"email": email, "schedules":specific_user["schedules"]}
        except:
            raise HTTPException(status_code=404, detail="Error - User not found")
