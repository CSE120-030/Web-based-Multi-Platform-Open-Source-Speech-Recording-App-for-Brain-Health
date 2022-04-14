from datetime import *
from flask_login import current_user
from helper_functions import *


from flask import flash
from flask_paginate import *
from copy import deepcopy

# list to save id of prompts to be completed
prompt_info = []
list_prompt_id = []
queue_control = 0

class assignment:
    def __init__(self, asg_counter=-1):
        self.asg_counter = asg_counter

    def get_asg_counter(self):
        return self.asg_counter
    def set_asg_counter(self, asg_counter):
        self.asg_counter = asg_counter



def asg_to_do(asg_name): # this function returns all the prompts associated with one assignment
    #prompt_info=[]
    #print(asg_name["group_name"])
    global prompt_info
    group_id = db.session.query(GroupOfPrompt).filter(GroupOfPrompt.name==asg_name["group_name"]).first()
    # get list of prompts
    #db.session.query(ListGroup)
    list_prompt = db.session.query(ListGroup).filter(ListGroup.groupOfPromptId==group_id.groupOfPromptId).all() # this is the list of asg to be completed
    print(len(list_prompt))
    control=0
    for i in list_prompt:
        list_prompt_id.append(list_prompt[control].promptId)
        control+=1
    print(list_prompt_id)
    print("about to iterate prompt list ")
    print("list_prompt_id length:",len(list_prompt_id))
    for item in list_prompt_id:
        prompt = db.session.query(Prompt).filter(Prompt.promptId == item).first()
        prompt_dict = {'promptId':prompt.promptId, 'description':prompt.descriptionPrompt, 'imageId':prompt.imageId}

        prompt_info.append(prompt_dict)
        #prompt_info.append(prompt_dict)
    print("list to be returned: ")
    print(prompt_info)
    return (prompt_info)


def load_prompt_photo(imageId):
    print("imageId to be shown",imageId)
    image_name  = db.session.query(Image).filter(Image.imageId==imageId).first()
    print("name is:",image_name.name)

    return image_name.name

def get_prompt_from_list(prompt_id):
    new_prompt_id = int(prompt_id)  # convert to int
    dict_to_return=[]
    global prompt_info
    print("prompt length info",len(prompt_info))
    print("in get prompt list function")
    try:
        if 0 <= new_prompt_id < len(prompt_info): # make sure the index is in range
            #print("prompt info hard coded:", prompt_info[new_prompt_id])
            dict_to_return.append(prompt_info[new_prompt_id])
            print(dict_to_return)
            load_prompt_photo(dict_to_return[0]["imageId"])
            return dict_to_return
    except:

            print("list is empty")
            return "empty"

    #i = next((item for item in prompt_info if item["promptId"] == new_prompt_id), None)
    #print(i)
    # about to print queue
    #get_queue_from_prompt_list()
    #return prompt_info[new_prompt_id]
    #return i

def get_queue_from_prompt_list(): #this method is to be returned to the front end. This method returns only the ids of the prompts
    print("in get queue function")
    print(len(prompt_info))
    prompt_id_queue=[]
    global queue_control
    queue_control +=1
    # transverse array of dictionaries
    for i in prompt_info:
        if i is not None and queue_control==1:
            prompt_id_queue.append(i["promptId"])
    print("printing queue")
    print(prompt_id_queue)
    return prompt_id_queue

def get_assignments():
    asg = assignment()
    # see if assignment has been created for this patient
    patient = get_patient_id()
    asg_created = db.session.query(Assignment).join(Patient).filter(Patient.userId==patient).first() #db.session.query(Assignment).filter(Assignment.patientIdId==patient).first()
    #print(str(asg_created))
    if asg_created is not None:
        # assignment has been created
        print("Assingment has been created")
        # show list of prompts to be completed
        # get user id for patient
        user_id_patient = db.session.query(Patient).filter(Patient.userId==patient).first()
        assignments_to_show =db.session.query(Assignment,GroupOfPrompt).join(GroupOfPrompt,GroupOfPrompt.groupOfPromptId==Assignment.groupOfPromptsId).filter(Assignment.patientId ==user_id_patient.patientId).all()
        dict_to_return = []
        for i in assignments_to_show:

            print("test:",i[0].assignmentId)
            asg.asg_id=i[0].assignmentId
            all_asg ={'date_of_assignment':i[0].dateOfAssignment.date(),
                      'state_of_prompt':i[0].stateOfPrompt,
                      'group_name':i[1].name}
            dict_to_return.append(all_asg)

        print(dict_to_return)
        print(json.dumps(dict_to_return))
        return dict_to_return


    else:
        date_asg = datetime.datetime.now()
        print("Assingment has NOT been created")
        print("creating assignment")
        # assign assignment to a new patient # generic assignment
        new_asg = create_asg(group_id=1, date_of_asg=date_asg,sop=0,expertN="General",expert_id=1,patient_id=get_patient_id())
        last_id= db.session.query(Assignment).order_by(Assignment.assignmentId.desc()).first()
        user_id_patient = db.session.query(Patient).filter(Patient.userId==patient).first()
        assignments_to_show = db.session.query(Assignment, GroupOfPrompt).join(GroupOfPrompt,GroupOfPrompt.groupOfPromptId == Assignment.groupOfPromptsId).filter(Assignment.patientId == user_id_patient.patientId).all()
        dict_to_return = []
        for i in assignments_to_show:
            print("test:", i[0].assignmentId)
            asg.asg_id = i[0].assignmentId
            all_asg = {'date_of_assignment': i[0].dateOfAssignment.date(),
                       'state_of_prompt': i[0].stateOfPrompt,
                       'group_name': i[1].name}
            dict_to_return.append(all_asg)

        print(dict_to_return)
        print(json.dumps(dict_to_return))
        return dict_to_return


# static for same expert. Assume expert one
def add_assignemnt_static(): # for time being, assume all assingments are of the group general
    patient = get_patient_id()
    expert_id=1
    date_now = datetime.datetime.now()
    group_of_prompt=2
    create_asg(group_id=group_of_prompt,date_of_asg=date_now,sop=0,expertN="General assignment",expert_id=expert_id,patient_id=patient)
    return


def get_patient_id():
    if current_user.is_authenticated:
        patient = current_user.get_id()
        print("Patient id: %s",patient)
        return patient
    return "user is not a patient"