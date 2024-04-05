# -*- coding:utf-8 -*-
import subprocess
import tkinter as tk
from tkinter import ttk
import json

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
    
    root.destroy()

    subprocess.run(["python", "sence_demo.py"])
    subprocess.run(["python", "img_describe.py"])
    subprocess.run(["python", "describe_rewrite.py"])
    subprocess.run(["python", "splicing.py"])

root = tk.Tk()
root.title("AIMC V0.2-040510")
root.geometry("450x750")
root.configure(bg="#f0f0f0")

# 创建上中下三个部分的框架
top_frame = tk.Frame(root, pady=10, bg="#f0f0f0")
top_frame.pack(fill="both", expand=True, padx=10)
middle_frame = tk.Frame(root, pady=10, bg="#f0f0f0")
middle_frame.pack(fill="both", expand=True, padx=10)
bottom_frame = tk.Frame(root, pady=10, bg="#f0f0f0")
bottom_frame.pack(fill="both", expand=True, padx=10)

# 上部分：图像描述
tk.Label(top_frame, text="图像描述", anchor="w", font=("Arial", 12), bg="#f0f0f0").pack(fill="x")

tk.Label(top_frame, text="背景设定", anchor="w", bg="#f0f0f0").pack(fill="x")
background_var_1 = tk.StringVar(top_frame)
background_var_1.set("You are an assistant who perfectly describes images.")
tk.Entry(top_frame, textvariable=background_var_1).pack(fill="x")

tk.Label(top_frame, text="提示语", anchor="w", bg="#f0f0f0").pack(fill="x")
prompt_var_1 = tk.StringVar(top_frame)
prompt_var_1.set("Describe the picture in terms of someone doing something in a place")
tk.Entry(top_frame, textvariable=prompt_var_1).pack(fill="x")

# 中部分：描述精简
ttk.Separator(middle_frame, orient="horizontal").pack(fill="x")
tk.Label(middle_frame, text="描述精简", anchor="w", font=("Arial", 12), bg="#f0f0f0").pack(fill="x")
tk.Label(middle_frame, text="使用模型", anchor="w", bg="#f0f0f0").pack(fill="x")
model_var_2 = tk.StringVar(middle_frame)
model_var_2.set("llava:latest")
tk.OptionMenu(middle_frame, model_var_2, "llava:latest", "gemma:7b").pack(fill="x")
filename_var_2 = tk.StringVar(middle_frame)
filename_var_2.set("co_description.json")  # 设置默认值
tk.Label(middle_frame, text="处理文件名", anchor="w", bg="#f0f0f0").pack(fill="x")
tk.Entry(middle_frame, textvariable=filename_var_2).pack(fill="x")

tk.Label(middle_frame, text="背景设定", anchor="w", bg="#f0f0f0").pack(fill="x")
background_var_2 = tk.StringVar(middle_frame)
background_var_2.set("You're a writer who's good at extracting information.")
tk.Entry(middle_frame, textvariable=background_var_2).pack(fill="x")

tk.Label(middle_frame, text="提示语", anchor="w", bg="#f0f0f0").pack(fill="x")
prompt_var_2 = tk.StringVar(middle_frame)
prompt_var_2.set("Summarize the narrative elements of the sentence into a sentence of 15 words or less, including characters, plot, environment, and historical context. Get rid of the non-narrative stuff.")
tk.Entry(middle_frame, textvariable=prompt_var_2).pack(fill="x")

# 下部分：描述整合
ttk.Separator(bottom_frame, orient="horizontal").pack(fill="x")
tk.Label(bottom_frame, text="描述整合", anchor="w", font=("Arial", 12), bg="#f0f0f0").pack(fill="x")
tk.Label(bottom_frame, text="使用模型", anchor="w", bg="#f0f0f0").pack(fill="x")
model_var_3 = tk.StringVar(bottom_frame)
model_var_3.set("llava:latest")
tk.OptionMenu(bottom_frame, model_var_3, "llava:latest", "gemma:7b").pack(fill="x")
filename_var_3 = tk.StringVar(bottom_frame)
filename_var_3.set("opt_description.json")  # 设置默认值
tk.Label(bottom_frame, text="处理文件名", anchor="w", bg="#f0f0f0").pack(fill="x")
tk.Entry(bottom_frame, textvariable=filename_var_3).pack(fill="x")

tk.Label(bottom_frame, text="背景设定", anchor="w", bg="#f0f0f0").pack(fill="x")
background_var_3 = tk.StringVar(bottom_frame)
background_var_3.set("You're a writer who's good at extracting information.")
tk.Entry(bottom_frame, textvariable=background_var_3).pack(fill="x")

tk.Label(bottom_frame, text="提示语", anchor="w", bg="#f0f0f0").pack(fill="x")
prompt_var_3 = tk.StringVar(bottom_frame)
prompt_var_3.set("These words are a shot script for a movie. Based on these contents, please speculate about the story of this movie.")
tk.Entry(bottom_frame, textvariable=prompt_var_3).pack(fill="x")

# 开始运行按钮
tk.Button(root, text="开始运行", command=start_processing, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)

root.mainloop()
