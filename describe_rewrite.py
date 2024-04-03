import json

#调用模型优化
def rec_image(model, images_path, prompt):
    response = ollama.chat(model= model, messages=[
        {"role": "system", "content": "You are ."},
        {
            'role': 'user',
            'content': prompt
        },
    ])
    result = {
        'images':images_path,
        'result':response['message']['content']
    }
    #print(result)
    return result 

if __name__ == "__main__":
    with open('co_description.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    rec_image("gemma:7b", )
    