from database import *
from flask_login import UserMixin

# Create user associated with patient
def create_language(name,prefix):
    language_entry = Language(name=name,prefix=prefix)
    db.session.add(language_entry)
    db.session.commit()
    return language_entry

def create_prompt(description, languageId, expertId, imageId,topId):
    prompt_entry = Prompt(descriptionPrompt=description,language=languageId,expert=expertId,image=imageId,typeOfPrompt=topId)
    db.session.add(prompt_entry)
    db.session.commit()
    return prompt_entry

def create_type_of_media(name,extension):
    tom_entry = TypeOfMedia(nameMedia=name,extension=extension)
    db.session.add(tom_entry)
    db.session.commit()
    return tom_entry



def create_patient(username, password, firstName, lastName, languageId,email, expertId, dob, sex):
    username_exists = db.session.query(User).filter(User.username==username).first() is not None
    if username_exists:
        print("Sorry, username is taken")
    else:
        user_entry = User(username=username,password=password)
        patient_entry = Patient(firstName = firstName, lastName=lastName, language=languageId,email=email,expertId=expertId,dob=dob,sex=sex,user=user_entry)
        db.session.add(patient_entry)
        db.session.commit()
        return patient_entry

def create_image(name, filePath):
    image_entry = Image(filePath=filePath, name=name)
    db.session.add(image_entry)
    db.session.commit()
    return image_entry

def create_group_of_prompt(name): # group of prompts
    gop_entry = GroupOfPrompt(name=name)
    db.session.add(gop_entry)
    db.session.commit()
    return gop_entry

def create_type_of_prompt(name, description):
    top_entry  = TypeOfPrompt(name=name,description=description)
    db.session.add(top_entry)
    db.session.commit()
    return top_entry

def create_expert(username, password, firstName, lastName, licenseNumber, e):
    username_exists = db.session.query(User).filter(User.username == username).first() is not None
    if username_exists:
        print("Sorry, username is taken")
    else:
        user_entry = User(username=username, password=password)
        expert_entry = Expert(firstName=firstName, lastName=lastName,licenseNumber=licenseNumber,e=e,user=user_entry)
        db.session.add(expert_entry)
        db.session.commit()
        return expert_entry




# Get user given username (used for login)
def get_user_by_name(username):
    user = db.session.query(User).filter(User.username == username).first()
    print(user)
    if user is not None:
        return user
    else:
        print("User not found")
        return -1


# get user by userId (used for login user_loader)
def get_user_by_id(user_id):
    user = db.session.query(User).filter(User.id == user_id).first()
    if user is not None:
        return user
    else:
        return None


