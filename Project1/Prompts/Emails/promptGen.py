from Project1 import helper

jobs1 = helper.file2List2('jobs1.txt')
jobs2 = helper.file2List2('jobs2.txt')

prompts = []
for idx in range(len(jobs1)):
    prompts.append(f"Write an email {jobs1[idx].strip()} sending to {jobs2[idx].strip()}.\n")
    prompts.append(f"Write an email {jobs2[idx].strip()} sending to {jobs1[idx].strip()}.\n")

helper.saveList2FIle('../../Prompts_text_files/emailPrompts.txt', prompts)