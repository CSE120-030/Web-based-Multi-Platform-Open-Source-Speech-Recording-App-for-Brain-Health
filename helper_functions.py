import json

from database import *
from flask_login import UserMixin


def create_language(name, prefix):
    """Prefix should be the first three letters of the language (lowercase)."""
    language_entry = Language(name=name,
                              prefix=prefix)
    db.session.add(language_entry)
    db.session.commit()
    return language_entry


def create_list_group(prompt_id, group_id):
    prompt = db.session.query(Prompt).filter(Prompt.promptId == prompt_id).first()
    group = db.session.query(GroupOfPrompt).filter(GroupOfPrompt.groupOfPromptId == group_id).first()
    list_group_entry = ListGroup(groupOfPrompt=group.groupOfPromptId,
                                 prompt=prompt.promptId)
    db.session.add(list_group_entry)
    db.session.commit()
    return list_group_entry


def create_type_of_media(name, extension):
    tom_entry = TypeOfMedia(nameMedia=name,
                            extension=extension)
    db.session.add(tom_entry)
    db.session.commit()
    return tom_entry


def create_patient(username, password, first_name, last_name, language_id, e, expert_id, dob, sex):
    username_exists = db.session.query(User).filter(User.username == username).first() is not None
    if username_exists:
        print("Sorry, username is taken")
    else:
        user_entry = User(username=username,
                          password=password)
        # get language
        language = db.session.query(Language).filter(Language.languageId == language_id).first()
        # get expert
        expert = db.session.query(Expert).filter(Expert.expertId == expert_id).first()
        patient_entry = Patient(firstName=first_name,
                                lastName=last_name,
                                language=language,
                                e=e,
                                expertId=expert.expertId,
                                dob=dob,
                                sex=sex,
                                user=user_entry)
        db.session.add(patient_entry)
        db.session.commit()
        return patient_entry


def create_image(name, file_path):
    image_entry = Image(filePath=file_path,
                        name=name)
    db.session.add(image_entry)
    db.session.commit()
    return image_entry


def create_group_of_prompt(name):  # group of prompts
    gop_entry = GroupOfPrompt(name=name)
    db.session.add(gop_entry)
    db.session.commit()
    return gop_entry


def create_type_of_prompt(name, description):
    top_entry = TypeOfPrompt(name=name,
                             description=description)
    db.session.add(top_entry)
    db.session.commit()
    return top_entry


def create_expert(username, password, first_name, last_name, license_number, e):
    username_exists = db.session.query(User).filter(User.username == username).first() is not None
    if username_exists:
        print("Sorry, username is taken")
    else:
        user_entry = User(username=username,
                          password=password)
        expert_entry = Expert(firstName=first_name,
                              lastName=last_name,
                              licenseNumber=license_number,
                              e=e,
                              user=user_entry)
        db.session.add(expert_entry)
        db.session.commit()
        return expert_entry


# Get user given username (used for login)
def get_user_by_name(username):
    user = db.session.query(User).filter(User.username == username).first()
    print(user)
    dict = {'username': user.username, 'password': user.password}
    if user is not None:
        return user
    else:
        print("User not found")
        return -1


def get_user_by_id(user_id):
    """Used for login user_loader."""
    user = db.session.query(User).filter(User.userId == user_id).first()
    if user is not None:
        return user
    else:
        return None


def add_prompt_to_group(group_name, prompt):
    # get the group
    group = db.session.query(GroupOfPrompt).filter(GroupOfPrompt.name == group_name).first()
    # get the prompt
    prompt = db.session.query(Prompt).filter(Prompt.promptId == prompt).first()
    last_id = get_list_group_id()
    list_group = ListGroup()
    list_group.listGroupId = last_id+1
    list_group.groupOfPromptId = group.groupOfPromptId
    list_group.promptId = prompt.promptId

    prompt.groupOfPrompt.append(list_group)
    db.session.commit()

    return list_group


def get_list_group_id():
    list_group_id = db.session.query(ListGroup).order_by(ListGroup.listGroupId.desc()).first()
    #print(id.listGroupId)
    return list_group_id.listGroupId


def create_asg(group_id, date_of_asg, sop, expert_note, expert_id, patient_id):
    # get expert
    expert = db.session.query(Expert).filter(Expert.expertId == expert_id).first()
    # get patient
    patient = db.session.query(Patient).filter(Patient.patientId == patient_id).first()
    #get group of Prompts
    group = db.session.query(GroupOfPrompt).filter(GroupOfPrompt.groupOfPromptId == group_id).first()

    asg_entry = Assignment(groupOfPromptsId=group.groupOfPromptId,
                           dateOfAssignment=date_of_asg,
                           stateOfPrompt=sop,
                           expertNote=expert_note,
                           expertId=expert.expertId,
                           patientId=patient.patientId)
    db.session.add(asg_entry)
    db.session.commit()
    print(asg_entry)
    return asg_entry


def create_media(media_note, file_path, asg, prompt, type_media):
    # get assignment
    asg_id = db.session.query(Assignment).filter(Assignment.assignmentId == asg).first()
    # get prompt
    prompt_id = db.session.query(Prompt).filter(Prompt.promptId == prompt).first()
    # get type of media
    type_media_id = db.session.query(TypeOfMedia).filter(TypeOfMedia.typeOfMediaId == type_media).first()
    media_entry = Media(mediaNote=media_note,
                        filePath=file_path,
                        assignmentId=asg_id.assignmentId,
                        promptId=prompt_id.promptId,
                        typeOfMediaId=type_media_id.typeOfMediaId)
    db.session.add(media_entry)
    db.session.commit()
    print(media_entry)
    return media_entry


def get_expert(username):
    user_name = db.session.query(User).filter(User.username == username).first()
    if user_name is not None:
        # user exists, therefore we can get id
        user_id = user_name.userId
        # get email
        e = db.session.query(Expert).filter(Expert.userId == user_id).first()
        print("email: ", e.e)
        print("User id is:", user_id)
    else:
        print("Username does not exist")
        return -1

    return user_id


# get all media files for a given patient
def get_media_file(username):
    user_name = db.session.query(User).filter(User.username == username).first()
    patient = db.session.query(Patient).filter(Patient.userId == user_name.userId).first()  # get patient
    # print(patient.patientId)
    media_file = db.session.query(Media, Assignment)
    media_file.join(Assignment, Assignment.assignmentId == Media.assignmentId)
    media_file.filter(Assignment.patientId==patient.patientId).all()
    # print(media_file)
    for m, asg in media_file:
        print("Media Id:{} MediaNote: {} filePath: {} Media.assignmentId:{} promptId: {} typeOfMediaId: {} Assignments.assignmetId: {} dateOfAssignment:{} stateOfPrompt:{} expertNote:{} groupOfPromptsId: {} expertId: {} patientId: {}"
        .format(m.mediaId,m.mediaNote,m.filePath,m.assignmentId,m.promptId,m.typeOfMediaId,asg.assignmentId,asg.dateOfAssignment,asg.stateOfPrompt,asg.expertNote,asg.groupOfPromptsId,asg.expertId,asg.patientId) )
    return media_file




