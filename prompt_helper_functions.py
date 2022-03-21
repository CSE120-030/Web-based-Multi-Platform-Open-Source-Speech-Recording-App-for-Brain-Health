from database import *

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

