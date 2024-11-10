import openai
from config import sentence

BE = sentence
print(BE)

def gptgen(BE = BE,epoch = 1,model= "gpt-4o"):
    prompt=f'''You will be provided with a piece of text containing conversational English that may include multiple word repetitions and sequences of broken letters.
    There might be names or proper nouns within the text.
    Your task is to produce a refined version of the text by correcting errors, eliminating repetitions, and properly formatting any proper nouns.

    Text provided: {BE}

    Please return only the refined version of the provided text.'''
    role ='''
    You are an expert in English language processing.
    Your task is to convert any unclean or broken English sentences into coherent, grammatically correct, and natural-sounding conversational English. 
    This includes correcting grammatical errors, removing unnecessary word repetitions, and combining sequences of broken letters to form proper nouns, such as names.
    '''
    print(f"#####{BE}######")
    print("Computing")
    api_key = "xxx"
    openai.api_key = api_key

    params = {
        'model': model, 
        'temperature': 0,
        'max_tokens': 2000,
        'top_p': 0.3,
    }

    response = openai.chat.completions.create(
        model=params['model'],
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": prompt}
        ],
        temperature=params['temperature'],
        max_tokens=params['max_tokens'],

        top_p=params['top_p']
    )
    hyperparameters={
    "n_epochs":epoch
  }
    generated_text = str(response.choices[0].message.content).strip()
    
    ret=generated_text.replace("```",'').replace('mermaid','')
    
    with open('output.txt', 'w') as file:
        file.write(ret)
    # ts.clear() 
    sentence.clear()
    return ret