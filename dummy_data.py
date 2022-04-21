import datetime

from helper_functions import *
from prompt_helper_functions import *
from datetime import date
language=1
expert=1
d = date(2000,9,15)
#print(d)
#create_expert("expert1","1234","fName","lName","00000","123@asd.com")
#create_language(name="English",prefix="eng")
#create_patient(username="patient2",password="1234",firstName="fName",lastName="lName",languageId=language,e="1234@asd.com",expertId=expert,dob=d,sex="M")


# create image
#create_image("image1","//images//some_path")
#create_image("number_one",'./Images/one.png')
#create_image("number_two",'./Images/two.png')
#create_image("number_three",'./Images/three.png')
#create_image("number_four",'./Images/four.png')
#create_image("number_five",'./Images/five.png')
#create_image("number_six",'./Images/six.png')
#create_image("number_seven",'./Images/seven.png')
#create_image("blank",'./Images/blank.jpg')
#create_image("test",'./Images/test.jpg')

#create type_prompt() # the description can be changed later
#create_type_of_prompt("Spontaneous","Spontaneous prompt")
#create_type_of_prompt("Semi-spontaneous","Semi-spontaneous prompt")
#create_type_of_prompt("Non-spontaneous","Non spontaneous")

# creaate type of media
#create_type_of_media("Audio",".wav")
#create_type_of_media("Video",".mp4")

#create group of Prompts
#create_group_of_prompt("Group1")

#create list of groups
#create_list_group()

  #create prompt
#create_prompt(description="Prompt2",languageId=1,imageId=1,expertId=1,topId=1)
#create_prompt(description="Semi spontaneous Prompt",languageId=1,imageId=9,expertId=1,topId=2)
#create_prompt(description="Non- spontaneous Prompt",languageId=1,imageId=9,expertId=1,topId=3)
#assign group to prompt
#add_prompt_to_group("Group1",1)
#get_list_group_id()

#create assignment
#date_asg = datetime.datetime.now()
#state_of_prompt =0 #0 for unfinished, 1 for finished
#expert_asg=1
#patient_asg=1
#group_of_prompt=1

#print(date_asg)
#create_asg(group_id=group_of_prompt,date_of_asg=date_asg,sop=state_of_prompt,expertN="Test",expert_id=expert_asg,patient_id=patient_asg)

#create media
#asg_id=1
#prompt_id=1
#type_media_id=1
#create_media(media_note="Audio good",file_path="../amazon/bucket",asg=asg_id,prompt=prompt_id,type_media=type_media_id)

# get expert id
#user_name="expert1"
#get_expert(username=user_name)

#get all media files for a given patient
#patient="patient1" #username
#get_media_file(username=patient)

#get_all_prompts()

#########################################################################################################################

#create_group_of_prompt(name="General")
#create_list_group(promptId=7,groupId=2) # semi spontaneous prompt to general list of prompts
#create_list_group(promptId=8,groupId=2) # Non-spontaneous prompt to general list of prompts

add_prompt_to_group(groupName="General",prompt=7)
add_prompt_to_group(groupName="General",prompt=8)