import os  # to save recording to disk
from flask import request
from flask_login import current_user
import pathlib

import prompt_helper_functions
from database import *
from flask import request
# import app
import boto3

dict_to_return = []
dict_to_return_expert = []
dic = []
name = ""
file_path = ""
prompt_counter = 0
language = ""
prompt_expert = ""

BUCKET_PREFIX = "ucm-cse120-330-"


def get_patient_id():
    if current_user.is_authenticated:
        patient = current_user.get_id()
        print("Patient id: %s", patient)
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

    current_query = db.session.query(Assignment,
                                     TypeOfPrompt.name,
                                     Language.prefix,
                                     Prompt.promptId,
                                     Patient.firstName,
                                     Patient.lastName,
                                     Patient.patientId)

    current_query.join(GroupOfPrompt,
                       GroupOfPrompt.groupOfPromptId == Assignment.groupOfPromptsId)
    current_query.join(ListGroup,
                       ListGroup.groupOfPromptId == GroupOfPrompt.groupOfPromptId)
    current_query.join(Prompt,
                       Prompt.promptId == ListGroup.promptId)
    current_query.join(TypeOfPrompt,
                       TypeOfPrompt.typeOfPromptId == Prompt.typeOfPromptId)
    current_query.join(Language,
                       Language.languageId == Prompt.languageId)
    current_query.join(Patient,
                       Patient.patientId == Assignment.patientId)
    current_query.join(User,
                       User.userId == Patient.userId)

    current_query.filter(User.userId == get_patient_id()).all()

    for i in current_query:
        dict_to_return.append(i)

    # print(type(dict_to_return))
    # print(len(dict_to_return))
    # print(dict_to_return)

    generate_file_name(prompt_counter)
    # prompt_counter += 1


def get_file_name_expert():
    global prompt_expert
    global dic
    control = 0

    prompt_expert = db.session.query(Assignment,
                                     TypeOfPrompt.name,
                                     Language.prefix,
                                     Prompt.promptId,
                                     Patient.firstName,
                                     Patient.lastName,
                                     Patient.patientId)

    prompt_expert.join(GroupOfPrompt,
                       GroupOfPrompt.groupOfPromptId == Assignment.groupOfPromptsId)
    prompt_expert.join(ListGroup,
                       ListGroup.groupOfPromptId == GroupOfPrompt.groupOfPromptId)
    prompt_expert.join(Prompt,
                       Prompt.promptId == ListGroup.promptId)
    prompt_expert.join(TypeOfPrompt,
                       TypeOfPrompt.typeOfPromptId == Prompt.typeOfPromptId)
    prompt_expert.join(Language,
                       Language.languageId == Prompt.languageId)
    prompt_expert.join(Patient,
                       Patient.patientId == Assignment.patientId)
    prompt_expert.join(Expert,
                       Expert.expertId == Assignment.expertId)
    prompt_expert.join(User,
                       User.userId == Expert.userId)

    prompt_expert.filter(User.userId == get_expert_id()).all()

    for i in prompt_expert:
        dict_to_return_expert.append(i)
    print(dict_to_return_expert)

    for i in dict_to_return_expert:
        name_file_download = "_".join([dict_to_return_expert[control][1],
                                       dict_to_return_expert[control][2],
                                       str(dict_to_return_expert[control][3]),
                                       dict_to_return_expert[control][4] + "-" + dict_to_return_expert[control][5],
                                       str(dict_to_return_expert[control][6]) + ".wav"])
        dic.append(name_file_download)
        control += 1
    print(type(dic))
    print(dic)
    return dic


def info_expert_portal():
    info_asg = []

    prompts = db.session.query(Assignment,
                               TypeOfPrompt.name,
                               Language.name,
                               Patient.firstName,
                               Patient.lastName,
                               Assignment.assignmentId,
                               Prompt.promptId)

    prompts.join(GroupOfPrompt,
                 GroupOfPrompt.groupOfPromptId == Assignment.groupOfPromptsId)
    prompts.join(ListGroup,
                 ListGroup.groupOfPromptId == GroupOfPrompt.groupOfPromptId)
    prompts.join(Prompt,
                 Prompt.promptId == ListGroup.promptId)
    prompts.join(TypeOfPrompt,
                 TypeOfPrompt.typeOfPromptId == Prompt.typeOfPromptId)
    prompts.join(Language,
                 Language.languageId == Prompt.languageId)
    prompts.join(Patient,
                 Patient.patientId == Assignment.patientId)
    prompts.join(Expert,
                 Expert.expertId == Assignment.expertId)
    prompts.join(User,
                 User.userId == Expert.userId)

    prompts.filter(User.userId == get_expert_id()).all()

    for i in prompts:
        info = {'type_of_prompt': i[1],
                'language': i[2],
                'first_name': i[3],
                'last_name': i[4],
                'asg_id': i[5],
                'prompt_id': i[6]}
        info_asg.append(info)
    print(info_asg)

    return info_asg


def generate_file_name(prompt_id):
    # print("in specific name")
    # print(dict_to_return[prompt_id])
    global name
    global language
    name = "_".join([dict_to_return[prompt_id][1],
                     dict_to_return[prompt_id][2],
                     str(dict_to_return[prompt_id][3]),
                     dict_to_return[prompt_id][4] + "-" + dict_to_return[prompt_id][5],
                     str(dict_to_return[prompt_id][6])])
    language = dict_to_return[prompt_id][2]  # get the language prefix
    # print(name)
    # print(type(name))


def get_media(media_got):
    # print("Media bucket script")
    # print(media_got)
    global file_path
    global name
    get_file_name()
    audio_to_write = media_got.read()

    # write to server folder
    # f = open('./Audios/test.wav', 'wb')
    name = name + '.wav'
    f = open('./Audios/' + name + '.wav', 'wb')
    # f.write(request.get_data("audio_data"))
    f.write(audio_to_write)
    f.close()
    file_path = './Audios/' + name + '.wav'
    aws_upload(name, file_path)
    os.remove(file_path)  # remove audio from Audio folder. To keep server light
    print(file_path)
    return 1


# AWS SPECIFIC METHODS #


def get_language_from_prefix(key: str):
    lang = key.split("_")[1]
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


def aws_upload(file_key: str, current_file_path: str):
    """Uploads a file to an AWS bucket.

    Arguments:

        file_key: This should be the name you want the file saved under on AWS.
        AWS doesn't just use the given file name. PLEASE MAKE SURE IT ENDS IN .WAV!

        current_file_path: Actual (local) path of the file to be uploaded.
    """

    aws_client = boto3.client('s3')
    aws_client.upload_file(current_file_path, BUCKET_PREFIX + language, file_key)


def aws_download(file_key: str):
    """Make sure to include .wav in the file key."""
    lang_from_file_key = get_language_from_prefix(file_key)
    aws_client = boto3.client('s3')

    aws_client.download_file(BUCKET_PREFIX + lang_from_file_key, file_key, "/downloads/" + file_key)


def aws_batch_download(file_keys):
    """Creates a working directory to save files. Downloads files.
    Zips up directory. Deletes directory. Returns zip file.

    Arguments:

        file_keys: List/Set/Whatever of file keys.
    """
    aws_client = boto3.client('s3')

    from datetime import datetime
    current_time = str(int(datetime.now().timestamp()))  # Unix timestamp used to name working_directory.
    working_directory = "downloads/" + current_time + "/"

    for key in file_keys:  # Downloads all selected files to local directory.
        lang = get_language_from_prefix(key)
        aws_client.download_file(BUCKET_PREFIX + lang, key, working_directory + key)

    import shutil
    zip_file_name = "archive_" + current_time
    shutil.make_archive(zip_file_name, 'zip', working_directory)  # Zip 'em up. (Timestamp also used here.)
    shutil.rmtree(working_directory)  # Delete directory.

    return zip_file_name + ".zip"
