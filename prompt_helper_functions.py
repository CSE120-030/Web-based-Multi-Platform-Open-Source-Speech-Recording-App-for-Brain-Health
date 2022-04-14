from database import *
from flask_login import current_user


def get_all_prompts():
    control = 0
    prompts_to_return = []
    prompts = db.session.query(TypeOfPrompt).all()
    for i in prompts:
        prompt_data = {'type_of_prompt': prompts[control].typeOfPromptId,
                       'prompt_name': prompts[control].name}
        control += 1
        prompts_to_return.append(prompt_data)

    get_prompt = json.dumps(prompts_to_return)
    print(get_prompt)
    print(prompts_to_return)
    return prompts_to_return


def get_expert():
    expert = 0
    if current_user.is_authenticated:
        expert = current_user.get_id()
        return expert
    return


def get_languages():
    control = 0
    languages_to_return = []
    languages = db.session.query(Language).all()
    for i in languages:
        languages_data = {'language_id': languages[control].languageId,
                          'name': languages[control].name,
                          'prefix': languages[control].prefix}
        control += 1
        languages_to_return.append(languages_data)
    # print(languages_to_return)

    return languages_to_return


def add_prompt_to_database(description, given_language_id, given_expert_id, given_image_id, prompt_type_id):
    """Creates new prompt and saves it to the database. Returns newly created Prompt object.

    Arguments:
        description: Prompt text. Make it pretty! *Will be displayed to the patient!*
        given_language_id: Language ID associated with prompt.
        given_expert_id: Expert ID associated with prompt.
        given_image_id: Image ID associated with prompt.
        prompt_type_id: ID of the prompt type. Corresponds to either Spontaneous, Semi-Spon, or Non-Spon.
    """

    # Get prompt type
    type_of_prompt_id = db.session.query(TypeOfPrompt).filter(TypeOfPrompt.typeOfPromptId == prompt_type_id).first()
    # Get language
    language_id = db.session.query(Language).filter(Language.languageId == given_language_id).first()
    # Get expert
    expert_id = db.session.query(Expert).filter(Expert.expertId == given_expert_id).first()
    # Get image
    image_id = db.session.query(Image).filter(Image.imageId == given_image_id).first()

    new_prompt_entry = Prompt(descriptionPrompt=description,
                              languageId=language_id.languageId,
                              expertId=expert_id.expertId,
                              imageId=image_id.imageId,
                              typeOfPromptId=type_of_prompt_id.typeOfPromptId)

    db.session.add(new_prompt_entry)
    db.session.commit()

    return new_prompt_entry


def get_image_id(image_name):
    if type(image_name) == int:
        image_id = db.session.query(Image).filter(Image.imageId == image_name).first()
    elif type(image_name) == str:
        image_id = db.session.query(Image).filter(Image.name == image_name).first()

    return image_id.imageId


def get_language_id(given_id):
    language_id = db.session.query(Language).filter(Language.languageId == given_id).first()
    return language_id.languageId


def get_type_prompt_id(given_id):
    type_prompt = db.session.query(TypeOfPrompt).filter(TypeOfPrompt.typeOfPromptId == given_id).first()
    return type_prompt.typeOfPromptId


def generate_prompt_from_request(prompt_request):
    """Parses data from arg: prompt_request (a .json file) and uses parsed data to call the final
    prompt generation function, add_prompt_to_database. Once added, it returns the newly generated
    Prompt object.

    Arguments:
        prompt_request: A .json file consisting of user-submitted prompt data.
    """
    image_id = get_image_id(prompt_request["image_name"])
    expert = get_expert()
    language = get_language_id(prompt_request["type_of_language"])
    type_of_prompt = get_type_prompt_id(prompt_request["type_of_prompt"])
    prompt_created = add_prompt_to_database(description=prompt_request["prompt_description"],
                                            given_language_id=language,
                                            given_expert_id=expert,
                                            given_image_id=image_id,
                                            prompt_type_id=type_of_prompt)
    print(prompt_created)
    return prompt_created
