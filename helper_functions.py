import json

from database import *
import sqlite3 as sql

from flask_login import UserMixin



# Create user associated with patient
def create_language(name,prefix):
    language_entry = Language(name=name,prefix=prefix)
    db.session.add(language_entry)
    db.session.commit()
    return language_entry



def create_list_group(promptId,groupId):
    prompt = db.session.query(Prompt).filter(Prompt.promptId==promptId).first()
    group = db.session.query(GroupOfPrompt).filter(GroupOfPrompt.groupOfPromptId==groupId).first()
    list_group_entry = ListGroup(groupOfPrompt =group.groupOfPromptId,prompt=prompt.promptId)
    db.session.add(list_group_entry)
    db.session.commit()
    return  list_group_entry


def create_type_of_media(name,extension):
    tom_entry = TypeOfMedia(nameMedia=name,extension=extension)
    db.session.add(tom_entry)
    db.session.commit()
    return tom_entry



def create_patient(username, password, firstName, lastName, languageId,e, expertId, dob, sex):
    #con = sql.connect("sqlite:///static/speechDB.sqlite")

    username_exists = db.session.query(User).filter(User.username==username).first() is not None
    if username_exists:
        print("Sorry, username is taken")
    else:

        user_entry = User(username=username,password=password,confirmed=False)

        # get language
        language = db.session.query(Language).filter(Language.languageId == languageId).first()
        # get expert
        expert = db.session.query(Expert).filter(Expert.expertId == expertId).first()
        patient_entry = Patient(firstName = firstName, lastName=lastName, language=language, e=e, expertId=expert.expertId, dob=dob, sex=sex, user=user_entry)
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
    dict = {'username':user.username,'password':user.password}
    if user is not None:
        return user
    else:
        print("User not found")
        return -1


# get user by userId (used for login user_loader)
def get_user_by_id(user_id):
    user = db.session.query(User).filter(User.userId== user_id).first()
    if user is not None:
        return user
    else:
        return None


def add_prompt_to_group(groupName,prompt):
    # get the group
    group = db.session.query(GroupOfPrompt).filter(GroupOfPrompt.name==groupName).first()
    # get the prompt
    prompt = db.session.query(Prompt).filter(Prompt.promptId==prompt).first()
    last_id = get_list_group_id() # get last id from list_group table
    list_group = ListGroup()
    list_group.listGroupId= last_id+1
    list_group.groupOfPromptId=group.groupOfPromptId
    list_group.promptId=prompt.promptId

    prompt.groupOfPrompt.append(list_group)
    db.session.commit()

    return list_group

def get_list_group_id():
    id = db.session.query(ListGroup).order_by(ListGroup.listGroupId.desc()).first()
    #print(id.listGroupId)
    return id.listGroupId

def create_asg(group_id,date_of_asg,sop,expertN,expert_id,patient_id):
    # get expert
    expert = db.session.query(Expert).filter(Expert.expertId==expert_id).first()
    # get patient
    # actually patient id is the user id, so we have to join the two tables together
    patient = db.session.query(Patient).join(User, Patient.userId==User.userId).filter(User.userId==patient_id).first()
    print("patient id is :", patient.patientId)
    #get group of Prompts
    group = db.session.query(GroupOfPrompt).filter(GroupOfPrompt.groupOfPromptId==group_id).first()
    asg_entry = Assignment(groupOfPromptsId=group.groupOfPromptId,dateOfAssignment=date_of_asg,stateOfPrompt=sop,expertNote=expertN,expertId=expert.expertId,patientId=patient.patientId)
    db.session.add(asg_entry)
    db.session.commit()
    print(asg_entry)
    return asg_entry

def create_media(media_note,file_path,asg,prompt,type_media):
    # get assignment
    asg_id = db.session.query(Assignment).filter(Assignment.assignmentId==asg).first()
    # get prompt
    prompt_id = db.session.query(Prompt).filter(Prompt.promptId==prompt).first()
    # get type of media
    type_media_id = db.session.query(TypeOfMedia).filter(TypeOfMedia.typeOfMediaId==type_media).first()
    media_entry = Media(mediaNote=media_note,filePath=file_path,assignmentId=asg_id.assignmentId,promptId =prompt_id.promptId, typeOfMediaId=type_media_id.typeOfMediaId)
    db.session.add(media_entry)
    db.session.commit()
    print(media_entry)
    return media_entry

def get_expert(username):
    user_name = db.session.query(User).filter(User.username==username).first()
    if user_name is not None:
        #user exists, therefore we can get id
        user_id = user_name.userId
        # get email
        e = db.session.query(Expert).filter(Expert.userId==user_id).first()
        print("email: ",e.e)
        print("User id is:", user_id)


    else:
        print("Username does not exist")
        return -1

    return user_id

# get all media files for a given patient
def get_media_file(username):
    user_name = db.session.query(User).filter(User.username==username).first()
    patient = db.session.query(Patient).filter(Patient.userId==user_name.userId).first() # get patient
    #print(patient.patientId)
    media_file = db.session.query(Media,Assignment).join(Assignment,Assignment.assignmentId==Media.assignmentId).filter(Assignment.patientId==patient.patientId).all()
    print(media_file)
    for m, asg in media_file:
        print("Media Id:{} MediaNote: {} filePath: {} Media.assignmentId:{} promptId: {} typeOfMediaId: {} Assignments.assignmetId: {} dateOfAssignment:{} stateOfPrompt:{} expertNote:{} groupOfPromptsId: {} expertId: {} patientId: {}"
        .format(m.mediaId,m.mediaNote,m.filePath,m.assignmentId,m.promptId,m.typeOfMediaId,asg.assignmentId,asg.dateOfAssignment,asg.stateOfPrompt,asg.expertNote,asg.groupOfPromptsId,asg.expertId,asg.patientId) )



    return media_file




