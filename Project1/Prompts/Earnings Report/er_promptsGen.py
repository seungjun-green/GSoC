from Project1 import helper
import random

sp500 = helper.file2List('SP500')

prompts = []
Qs = ['Q1', 'Q2', 'Q3', 'Q4']
Ys = [2022, 2021, 2020, 2019]
for company in sp500:
    qs = random.sample(Qs, 2)
    ys = random.sample(Ys, 2)
    for q in qs:
        for y in ys:
            prompts.append(f"Write an earnings report for {company.strip()} for {q} of {y}.\n")

helper.saveList2FIle('../../Prompts_text_files/er_prompts.txt', prompts)
