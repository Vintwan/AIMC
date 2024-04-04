import json
import ollama
# from tqdm import tqdm 

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
def rec_text(model, sen_1, sen_2, prompt):
    background = "You're a writer who's good at extracting information."
    with tqdm(total=1) as pbar:
        response = ollama.chat(model= model, messages=[
        {
            "role": "system" ,
            "content": background
        },
        {
            'role': 'user',
            'content': prompt + sen_1 + "(2)" + sen_2
        },
    ])
    return response['message']['content']


if __name__ == "__main__":
    folder_path = "sence_images_list/"

    with open('opt_description.json', 'r', encoding='utf-8') as f:
        optds = json.load(f)
    content = [None] * len(optds)
    #桶排序
    for optd in optds:
        content[find_number(optd["images"])] = cut(optd["optimization"])
    sentence_1 = content[0]
    i = 1
    while i < len(content):
        sentence_2 = content[i]
        sentence_1 = rec_text("gemma:7b", sentence_1, sentence_2, "Combine these two descriptions of the picture into one sentence:(1)")
        i = i + 1
    with open("splicing_text.txt", "w") as file:
        file.write(sentence_1)
    print("处理完成")