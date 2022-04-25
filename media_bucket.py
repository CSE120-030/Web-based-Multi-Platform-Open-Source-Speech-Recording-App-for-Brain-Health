import os # to save recording to disk
from flask import request
from flask_login import current_user
import pathlib

import prompt_helper_functions
from database import *
from flask import request
#import app
import boto3
dict_to_return=[]
dict_to_return_expert = []
dic=[]
name =""
file_path=""
prompt_counter=0
languagee =""
prompt_expert = ""
#BUCKET_PREFIX = "330-personal-test-bucket"
BUCKET_PREFIX = "ucm-cse120-330"
# Replace above with "ucm-cse-120-330-" when credentials are given.
def get_patient_id():
    if current_user.is_authenticated:
        patient = current_user.get_id()
        print("Patient id: %s",patient)
        return patient
    return "user is not a patient"

def get_expert_id():
    if current_user.is_authenticated:
        expert = current_user.get_id()
        print("Expert id: %s", expert)
        return expert
    return "user is not a expert"


def get_file_name():
    global dict_to_return
    global prompt_counter
    name = db.session.query(Assignment,TypeOfPrompt.name,Language.prefix,Prompt.promptId,Patient.firstName,Patient.lastName,Patient.patientId).join(GroupOfPrompt,GroupOfPrompt.groupOfPromptId==Assignment.groupOfPromptsId).join(ListGroup,ListGroup.groupOfPromptId==GroupOfPrompt.groupOfPromptId).join(Prompt, Prompt.promptId==ListGroup.promptId).join(TypeOfPrompt, TypeOfPrompt.typeOfPromptId==Prompt.typeOfPromptId).join(Language,Language.languageId==Prompt.languageId).join(Patient,Patient.patientId==Assignment.patientId).join(User,User.userId==Patient.userId).filter(User.userId==get_patient_id()).all()

    for i in name:
        dict_to_return.append(i)
    print(type(dict_to_return))
    print(len(dict_to_return))
    print(dict_to_return)
    asg_specific_name(prompt_counter)
    prompt_counter+=1
    return ""

def get_file_name_expert():
    global prompt_expert
    global dic
    control=0
    prompt_expert = db.session.query(Assignment,TypeOfPrompt.name,Language.prefix,Prompt.promptId,Patient.firstName,Patient.lastName,Patient.patientId).join(GroupOfPrompt,GroupOfPrompt.groupOfPromptId==Assignment.groupOfPromptsId).join(ListGroup,ListGroup.groupOfPromptId==GroupOfPrompt.groupOfPromptId).join(Prompt,Prompt.promptId==ListGroup.promptId).join(TypeOfPrompt,TypeOfPrompt.typeOfPromptId==Prompt.typeOfPromptId).join(Language,Language.languageId==Prompt.languageId).join(Patient,Patient.patientId==Assignment.patientId).join(Expert,Expert.expertId==Assignment.expertId).join(User,User.userId==Expert.userId).filter(User.userId==get_expert_id()).all()
    for i in prompt_expert:
        dict_to_return_expert.append(i)
    print(dict_to_return_expert)
    for i in dict_to_return_expert:
        name_file_download = dict_to_return_expert[control][1] +"_"+ dict_to_return_expert[control][2] +"_"+ str(dict_to_return_expert[control][3]) +"_"+ dict_to_return_expert[control][4] +"_"+ dict_to_return_expert[control][5] +"_"+ str(dict_to_return_expert[control][6])+ ".wav"
        dic.append(name_file_download)
        control+=1
    print(type(dic))
    print(dic)
    return dic

def info_expert_portal():
    info_asg=[]
    control=0
    prompts = db.session.query(Assignment,TypeOfPrompt.name,Language.name,Patient.firstName,Patient.lastName,Assignment.assignmentId,Prompt.promptId).join(GroupOfPrompt, GroupOfPrompt.groupOfPromptId==Assignment.groupOfPromptsId).join(ListGroup,ListGroup.groupOfPromptId==GroupOfPrompt.groupOfPromptId).join(Prompt,Prompt.promptId==ListGroup.promptId).join(TypeOfPrompt,TypeOfPrompt.typeOfPromptId==Prompt.typeOfPromptId).join(Language,Language.languageId==Prompt.languageId).join(Patient,Patient.patientId==Assignment.patientId).join(Expert,Expert.expertId==Assignment.expertId).join(User,User.userId==Expert.userId).filter(User.userId==get_expert_id()).all()
    for i in prompts:
        info = {'type_of_prompt':i[1],
                'language':i[2],
                'first_name':i[3],
                'last_name':i[4],
                'asg_id':i[5],
                'prompt_id':i[6]}
        info_asg.append(info)
    print(info_asg)
    return info_asg

def asg_specific_name(promptId):
    print("in specific name")
    print(dict_to_return[promptId])
    global name
    global language
    name = dict_to_return[promptId][1] +"_"+ dict_to_return[promptId][2] +"_"+ str(dict_to_return[promptId][3]) +"_"+ dict_to_return[promptId][4] +"_"+ dict_to_return[promptId][5] +"_"+ str(dict_to_return[promptId][6])
    language = dict_to_return[promptId][2] # get the language prefix
    languagee=get_language(language)
    print(languagee)
    print(name)
    print(type(name))

    return name

def get_media(media_got):
    print("Media bucket script")
    print(media_got)
    global file_path
    global name
    get_file_name()
    audio_to_write=media_got.read()

    #write to server folder
    #f = open('./Audios/test.wav', 'wb')
    name = name+'.wav'
    f=open('./Audios/'+name+'.wav','wb')
    #f.write(request.get_data("audio_data"))
    f.write(audio_to_write)
    f.close()
    file_path = './Audios/'+name+'.wav'
    aws_upload(name,file_path,get_language(language))
    os.remove(file_path) # remove audio from Audio folder. To keep server light
    print(file_path)
    return 1

def get_language(key: str):
    """Finds language using given key. Used to select bucket when downloading."""
    lang = key
    if lang == "eng":
        return "english"
    elif lang == "can":
        return "cantonese"
    elif lang == "man":
        return "mandarin"
    elif lang == "spa":
        return "spanish"
    else:
        return "tagalog"

def aws_upload(file_key: str, file_to_upload: str, language: str):
    """Uploads a file to an AWS bucket.
    Arguments:
        file_key: This should be the name you want the file saved under on AWS.
        AWS doesn't just use the given file name. PLEASE MAKE SURE IT ENDS IN .WAV!
        file_to_upload: Actual (local) path of the file to be uploaded.
        language: Bucket to shove it in. Buckets follow the same naming convention, so all you need to input is the
        language of the file.
    """

    aws_client = boto3.client('s3')
    print("bucket is:"+BUCKET_PREFIX+"-"+language)
    aws_client.upload_file(file_to_upload, BUCKET_PREFIX+"-"+language, file_key)
    #aws_client.upload_file(file_to_upload, BUCKET_PREFIX+'-'+get_language(language), file_key)
    # aws_client.upload_file(file_to_upload, "ucm-cse-120-330-" + language, file_key) <<UNCOMMENT WHEN AWS SHIT HITS

def aws_download(file_key: str):
    """Returns an AWS url that allows file downloads for an hour.
    Arguments:
        file_key: Name of the file on AWS. Also known as the key used when you called aws_upload.
    """
    print("the file key is:"+file_key)
    lang = file_key.split('_')
    print(lang[1])
    languagee = lang[1]
    print("bucket is:" + BUCKET_PREFIX + "-" + get_language(languagee))
    url = boto3.client('s3').generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': BUCKET_PREFIX+'-'+get_language(languagee), 'Key': file_key},
        ExpiresIn=3600)
    # url = boto3.client('s3').generate_presigned_url(
    #     ClientMethod='get_object',
    #     Params={'Bucket': BUCKET_PREFIX + language, 'Key': file_key},
    #     ExpiresIn=3600) << Replace above with this when school account is active!
    s3 = boto3.resource('s3')
    print(file_key)
    #aws_client = boto3.client('s3')
    #aws_client.download_file(BUCKET_PREFIX + "-"+get_language(languagee), file_key, "/downloads/" + file_key)
    B= BUCKET_PREFIX+'-'+get_language(languagee)
    s3.Bucket(B).download_file(file_key, './Downloads')
    print(url)
    return url

def aws_batch_download(file_keys):
    """Generates a zip file containing requested files. Uploads to AWS.
    Returns the AWS url of the generated zip file.
    Arguments:
        file_keys: List/Set/Whatever of file keys.
    """
    aws_client = boto3.client('s3')
    for key in file_keys:  # Downloads all selected files to local directory.
        aws_client.download_file(BUCKET_PREFIX, key, "temp_download/batch/" + key)
        # lang = get_language(key)
        # aws_client.download_file(BUCKET_PREFIX + lang, key, "temp_download/batch/" + key) << see above comments
    import shutil, os
    zip_file_name = "testarchive"
    shutil.make_archive(zip_file_name, 'zip', "temp_download/")  # Zip 'em up.
    aws_client.upload_file(zip_file_name + ".zip", BUCKET_PREFIX, zip_file_name + ".zip")  # Upload it.
    url = aws_client.generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': BUCKET_PREFIX, 'Key': zip_file_name},
        ExpiresIn=3600)
    for file in os.scandir("temp_download/batch/"):
        os.remove(file.path)
    return url