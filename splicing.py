# -*- coding:utf-8 -*-
import json
import ollama
from tqdm import tqdm 

# 识别文件名中的数字方便排序
def find_number(filename):
    index_start = filename.find("Scene-")
    if index_start != -1:
        index_start += len("Scene-")
        index_end = filename.find("-", index_start)
        if index_end != -1:
            scene_number = filename[index_start:index_end]
            return int(scene_number) - 1  # 修正索引从0开始
        else:
            return 0
    else:
        return 0
#从\n\n切断
def cut(text):
    return text[text.find("\n\n") + 2:]

#调用模型优化

def rec_solve(model, content, prompt, background):
    response = ollama.chat(model= model, messages=[
    {
        "role": "system" ,
        "content": background
    },
    {
        'role': 'user',
        'content': prompt + content
    },
    ])
    return response['message']['content']


if __name__ == "__main__":

    with open('data.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    model = config["splicing"]["model"]
    prompt = config["splicing"]["prompt"]
    background = config["splicing"]["background"]
    file = config["splicing"]["file"]

    with open(file, 'r', encoding='utf-8') as f:
        optds = json.load(f)
    content = [None] * len(optds)
    #桶排序
    for optd in optds:
        content[find_number(optd["images"])] = cut(optd["optimization"])
    text = ""
    for i in range(len(content)):
        text = text + f"({i})" + content[i]
    result = rec_solve(model, text, prompt, background)
    with open("splicing_text.txt", "w") as file:
        file.write(result)
    print("处理完成")
