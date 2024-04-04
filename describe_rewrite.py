# -*- coding:utf-8 -*-
import json
import ollama
from tqdm import tqdm
import time

#调用模型优化
def rec_image(model, origin_text, images_path, prompt, background):
    response = ollama.chat(model= model, messages=[
    {
        "role": "system" ,
        "content": background
    },
    {
        'role': 'user',
        'content': prompt + origin_text
    },
    ])
    result = {
        'images': images_path,
        'origin_text': origin_text,
        'optimization': response['message']['content']
    }
    # print(result)
    return result 

def saveFile(filename,filecontent):
    json_data = json.dumps(filecontent, ensure_ascii=False,indent=3)
    with open(filename,"w",encoding="utf-8") as f: #设置文件对象
        f.write(json_data)

if __name__ == "__main__":
    start_time = int(round(time.time() * 1000))
    with open('data.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    model = config["describe_rewrite"]["model"]
    prompt = config["describe_rewrite"]["prompt"]
    background = config["describe_rewrite"]["background"]
    file = config["describe_rewrite"]["file"]
    optimis = []
    with open(file, 'r', encoding='utf-8') as f:
        datas = json.load(f)
    for data in tqdm(datas):
        optimi = rec_image(model, data["result"], data["images"], prompt, background)
        optimis.append(optimi)
    saveFile('opt_description.json', optimis)

    end_time = int(round(time.time() * 1000))
    print(f'本次处理时间为：{end_time - start_time}ms')