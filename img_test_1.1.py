import os
import ollama
import time
import json
from tqdm import tqdm

# 获取文件列表中的图片列表
def get_all_images(files):
  images = []
  try:
    for name in files:
      suffix = name.split('.').pop()
      if suffix in ['jpg', 'png', 'jpeg', 'bmp']:
        images.append(name)
  except Exception as e:
    print(e)
  else:
    return images

# 获取文件夹下所有的文件
def get_all_file(path):
  names = None
  try:
    names = os.listdir(path)
  except Exception as e:
    print(e)
  else:
    return names

# 读出指定文件夹下的所有图片，并返回图片路径数组
def get_img_file(path):
    imagelist = []
    for parent, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.lower().endswith(('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
                imagelist.append(os.path.join(parent, filename))
        return imagelist

# 识别指定图片的内容，并返回
def rec_image(model, images_path, prompt):
    response = ollama.chat(model= model, messages=[
        {"role": "system", "content": "You are an assistant who perfectly describes images."},
        {
            'role': 'user',
            'content': prompt,
            'images': [images_path]
        },
    ])
    result = {
        'images':images_path,
        'result':response['message']['content']
    }
    #print(result)
    return result 

#将内容以JSON格式保存为文件
def saveFile(filename,filecontent):
    json_data = json.dumps(filecontent, ensure_ascii=False,indent=3)
    with open(filename,"w") as f: #设置文件对象
        f.write(json_data)

if __name__ == "__main__":
    start_time = int(round(time.time() * 1000))

    folder_path = "sence_images_list/"
    model = "llava:latest"
    prompt = "Describe the picture in terms of someone doing something in a place"
    results = []

    # 读取指定目录下的所有图片，形成数组
    images = get_img_file(folder_path)

    for image in tqdm(images):
        res = rec_image(model=model,images_path=image,prompt=prompt)
        results.append(res)

    print(results)
    saveFile('wh.json',results)
    

    end_time = int(round(time.time() * 1000))
    print(f'本次图片处理时间为：{end_time - start_time}ms')