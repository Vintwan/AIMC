# -*- coding:utf-8 -*-
import subprocess
import tkinter as tk
from tkinter import ttk
import json
import shutil
import os

def start_processing():
    data = {
        "img_describe": {
            "model": "llava:latest",
            "background": background_var_1.get(),
            "prompt": prompt_var_1.get()
        },
        "describe_rewrite": {
            "model": model_var_2.get(),
            "file": filename_var_2.get(),
            "background": background_var_2.get(),
            "prompt": prompt_var_2.get()
        },
        "splicing": {
            "model": model_var_3.get(),
            "file": filename_var_3.get(),
            "background": background_var_3.get(),
            "prompt": prompt_var_3.get()
        }
    }
    
    with open('data.json', 'w') as f:
        json.dump(data, f)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if os.path.exists("sence_images_list"):
        shutil.rmtree("sence_images_list")
    root.destroy()
    print("Cutting the Video\n")
    subprocess.run(["python", "sence_demo.py"])
    print("Finished cutting. Describing the images\n")
    subprocess.run(["python", "img_describe.py"])
    print("Finished describing. Rewriting\n")
    subprocess.run(["python", "describe_rewrite.py"])
    print("Finished rewriting. Splicing. It takes just a few seconds.\n")
    subprocess.run(["python", "splicing.py"])

root = tk.Tk()
root.title("AIMC V0.3 开发者模式")
root.geometry("450x680")
root.configure(bg="#f0f0f0")

# 创建上中下三个部分的框架
top_frame = tk.Frame(root, pady=10)
top_frame.pack(fill="both", expand=True, padx=10)
middle_frame = tk.Frame(root, pady=10)
middle_frame.pack(fill="both", expand=True, padx=10)
bottom_frame = tk.Frame(root, pady=10)
bottom_frame.pack(fill="both", expand=True, padx=10)

# 上部分：图像描述
tk.Label(top_frame, text="图像描述微调", anchor="w", font=("Arial", 12)).pack(fill="x")

tk.Label(top_frame, text="背景设定", anchor="w").pack(fill="x")
background_var_1 = tk.StringVar(top_frame)
background_var_1.set("You are an assistant who perfectly describes images.")
background_text_1 = tk.Text(top_frame, height=3, wrap=tk.WORD)
background_text_1.insert("1.0", background_var_1.get())
background_text_1.pack(fill="x")

tk.Label(top_frame, text="提示语", anchor="w").pack(fill="x")
prompt_var_1 = tk.StringVar(top_frame)
prompt_var_1.set("Describe the picture in terms of someone doing something in a place")
prompt_text_1 = tk.Text(top_frame, height=3, wrap=tk.WORD)
prompt_text_1.insert("1.0", prompt_var_1.get())
prompt_text_1.pack(fill="x")

# 中部分：描述精简
ttk.Separator(middle_frame, orient="horizontal").pack(fill="x")
tk.Label(middle_frame, text="描述精简微调", anchor="w", font=("Arial", 12)).pack(fill="x")

# 使用一个新的框架来包含模型下拉框和文件名文本框
model_filename_frame_2 = tk.Frame(middle_frame)
model_filename_frame_2.pack(fill="x", pady=(5, 0))

# 模型下拉框
tk.Label(model_filename_frame_2, text="使用模型", anchor="w").pack(side="left")
model_var_2 = tk.StringVar(model_filename_frame_2)
model_var_2.set("llava:latest")
tk.OptionMenu(model_filename_frame_2, model_var_2, "llava:latest", "gemma:7b").pack(side="left", padx=(0, 5))

# 文件名文本框
filename_var_2 = tk.StringVar(model_filename_frame_2)
filename_var_2.set("co_description.json")  # 设置默认值
tk.Label(model_filename_frame_2, text="处理文件名", anchor="w").pack(side="left")
tk.Entry(model_filename_frame_2, textvariable=filename_var_2).pack(side="left")

tk.Label(middle_frame, text="背景设定", anchor="w").pack(fill="x")
background_var_2 = tk.StringVar(middle_frame)
background_var_2.set("You're a writer who's good at extracting information.")
background_text_2 = tk.Text(middle_frame, height=3, wrap=tk.WORD)
background_text_2.insert("1.0", background_var_2.get())
background_text_2.pack(fill="x")

tk.Label(middle_frame, text="提示语", anchor="w").pack(fill="x")
prompt_var_2 = tk.StringVar(middle_frame)
prompt_var_2.set("Summarize the narrative elements of the sentence into a sentence of 15 words or less, including characters, plot, environment, and historical context. Get rid of the non-narrative stuff.")
prompt_text_2 = tk.Text(middle_frame, height=3, wrap=tk.WORD)
prompt_text_2.insert("1.0", prompt_var_2.get())
prompt_text_2.pack(fill="x")

# 下部分：描述整合
ttk.Separator(bottom_frame, orient="horizontal").pack(fill="x")
tk.Label(bottom_frame, text="描述整合微调", anchor="w", font=("Arial", 12)).pack(fill="x")

# 使用一个新的框架来包含模型下拉框和文件名文本框
model_filename_frame_3 = tk.Frame(bottom_frame)
model_filename_frame_3.pack(fill="x", pady=(5, 0))

# 模型下拉框
tk.Label(model_filename_frame_3, text="使用模型", anchor="w").pack(side="left")
model_var_3 = tk.StringVar(model_filename_frame_3)
model_var_3.set("llava:latest")
tk.OptionMenu(model_filename_frame_3, model_var_3, "llava:latest", "gemma:7b").pack(side="left", padx=(0, 5))

# 文件名文本框
filename_var_3 = tk.StringVar(model_filename_frame_3)
filename_var_3.set("opt_description.json")  # 设置默认值
tk.Label(model_filename_frame_3, text="处理文件名", anchor="w").pack(side="left")
tk.Entry(model_filename_frame_3, textvariable=filename_var_3).pack(side="left")

tk.Label(bottom_frame, text="背景设定", anchor="w").pack(fill="x")
background_var_3 = tk.StringVar(bottom_frame)
background_var_3.set("You're a writer who's good at extracting information.")
background_text_3 = tk.Text(bottom_frame, height=3, wrap=tk.WORD)
background_text_3.insert("1.0", background_var_3.get())
background_text_3.pack(fill="x")

tk.Label(bottom_frame, text="提示语", anchor="w").pack(fill="x")
prompt_var_3 = tk.StringVar(bottom_frame)
prompt_var_3.set("These words are a shot script for a movie. Based on these contents, please speculate about the story of this movie.")
prompt_text_3 = tk.Text(bottom_frame, height=3, wrap=tk.WORD)
prompt_text_3.insert("1.0", prompt_var_3.get())
prompt_text_3.pack(fill="x")

# 开始运行按钮
tk.Button(root, text="开始运行", command=start_processing,  font=("Arial", 12)).pack(pady=10)

root.mainloop()
