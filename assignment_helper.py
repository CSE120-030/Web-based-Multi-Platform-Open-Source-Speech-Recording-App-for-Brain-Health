from datetime import *
from flask_login import current_user
from helper_functions import *

def asg_to_do(asg_name):
    #print(asg_name["group_name"])
    group_id = db.session.query(GroupOfPrompt).filter(GroupOfPrompt.name==asg_name["group_name"]).first()
    #group_id.groupOfPromptId
    # get list of prompts
    list_prompt = db.session.query(ListGroup).filter(ListGroup.groupOfPromptId==group_id.groupOfPromptId).all() # this is the list of asg to be completed
    print(len(list_prompt))
    list_prompt_id=[]
    control=0
    for i in list_prompt:
        list_prompt_id.append(list_prompt[control].promptId)
        control+=1
    print(list_prompt_id)
    return group_id





def get_assignments():
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

            all_asg ={'date_of_assignment':i[0].dateOfAssignment.date(),
                      'state_of_prompt':i[0].stateOfPrompt,
                      'group_name':i[1].name}
            dict_to_return.append(all_asg)

        print(dict_to_return)
        print(json.dumps(dict_to_return))
        return dict_to_return


    else:

        print("Assingment has NOT been created")
        # assign assignment to a new patient # generic assignment
        return "TBD"






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