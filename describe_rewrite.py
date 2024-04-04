import json
import ollama
from tqdm import tqdm

#调用模型优化
def rec_image(model, images_path, prompt):
    with tqdm(total=1) as pbar:
        response = ollama.chat(model= model, messages=[
        {"role": "system", "content": "You're a writer who's good at extracting information"},
        {
            'role': 'user',
            'content': prompt
        },
    ])
    result = {
        'images':images_path,
        'result':response['message']['content']
    }
    print(result)
    return result 

if __name__ == "__main__":
    with open('co_description.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    rec_image("gemma:7b",data, "Please summarize the information about the content of the picture in the sentence into a sentence of 15 words or less,including characters, plot, environment and historical background")
    