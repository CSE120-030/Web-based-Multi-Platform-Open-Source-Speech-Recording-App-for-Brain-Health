from database import *
from flask_login import current_user

def get_all_prompts():
    control=0
    prompts_to_return=[]
    prompts = db.session.query(TypeOfPrompt).all()
    for i in prompts:
        promt_data = {'type_of_prompt':prompts[control].typeOfPromptId,
                      'prompt_name':prompts[control].name}
        control += 1
        prompts_to_return.append(promt_data)

    get_prompt = json.dumps(prompts_to_return)
    print(get_prompt)
    print(prompts_to_return)
    return prompts_to_return

def getExpert():
    expert=0
    if current_user.is_authenticated:
        expert = current_user.get_id()
        return expert
    return

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

def create_prompt(description, languageId, expertId, imageId, topId):
    # create object of group_of_prompt

    # get the type pf prompt id
    type_of_prompt_id = db.session.query(TypeOfPrompt).filter(TypeOfPrompt.typeOfPromptId == topId).first()
    # get the language
    language_id = db.session.query(Language).filter(Language.languageId == languageId).first()
    # get the expert
    expert_id = db.session.query(Expert).filter(Expert.expertId == expertId).first()
    # get the image
    image_id = db.session.query(Image).filter(Image.imageId == imageId).first()

    prompt_entry = Prompt(descriptionPrompt=description, languageId=language_id.languageId, expertId=expert_id.expertId,
                          imageId=image_id.imageId, typeOfPromptId=type_of_prompt_id.typeOfPromptId)
    db.session.add(prompt_entry)
    db.session.commit()
    return prompt_entry

def get_image_id(imageName):
    if type(imageName)== int:
        image_id = db.session.query(Image).filter(Image.imageId==imageName).first()


    if type(imageName)==str:
        image_id = db.session.query(Image).filter(Image.name==imageName).first()

    return image_id.imageId

def get_language_id(languageId):
    language_id = db.session.query(Language).filter(Language.languageId==languageId).first()
    return language_id.languageId

def get_type_prompt_id(typeId):
    type_prompt = db.session.query(TypeOfPrompt).filter(TypeOfPrompt.typeOfPromptId==typeId).first()
    return type_prompt.typeOfPromptId

def prompt_creation(prompt_request):
    image_id = get_image_id(prompt_request["image_name"])
    expert= getExpert()
    language = get_language_id(prompt_request["type_of_language"])
    type_of_prompt = get_type_prompt_id(prompt_request["type_of_prompt"])
    prompt_created = create_prompt(description=prompt_request["prompt_description"],languageId=language,expertId=expert,imageId=image_id,topId=type_of_prompt)
    print(prompt_created)
    return prompt_created
