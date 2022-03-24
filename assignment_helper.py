from datetime import *
from flask_login import current_user
from helper_functions import *

def get_assignments():



    return 1

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
        return patient
    return "user is not a patient"