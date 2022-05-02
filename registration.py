from database import *
from flask_login import current_user


from helper_functions import *
from token_2 import *
from flask import url_for
#from app import *
from flask_mail import Message, Mail
import datetime

def get_languages():
    control = 0
    languages_to_return = []
    languages = db.session.query(Language).all()
    for i in languages:
        languages_data= {'language_id':languages[control].languageId,'name':languages[control].name,'prefix':languages[control].prefix}
        control += 1
        languages_to_return.append(languages_data)
    print(languages_to_return)

    return languages_to_return

def getExpert():
    expert=0
    if current_user.is_authenticated:
        expert = current_user.get_id()
        return expert
    return

def register_patient(patient_info):
    #print("about to register a patient. patient info \n")
    #print(type(patient_info))
    print(patient_info)
    #print(type(patient_info['dob']))
    format_str = '%Y-%m-%d'
    datetime_obj = datetime.datetime.strptime(patient_info['dob'],format_str)
    #print(type(datetime_obj.date()))
    #print(datetime_obj.date())
    # create_patient(username="patient2",password="1234",firstName="fName",lastName="lName",languageId=language,e="1234@asd.com",expertId=expert,dob=d,sex="M")
    create_patient(firstName=patient_info['first_name'],lastName=patient_info['last_name'],languageId=patient_info['language'],e=patient_info['email'],username=patient_info['user_name'],password=patient_info['password'],dob =datetime_obj ,sex=patient_info['sex'],expertId=getExpert())



    #print("patient was added successfully")



