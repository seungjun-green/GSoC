from Project1 import helper

# helper.process_file('historyEvents.txt', 'historyEvents.txt')
bodyParts = helper.file2List('historyEvents.txt')

prompts = []
for bodyPart in bodyParts:
    prompts.append(f"Write a historical document on {bodyPart.strip()}.\n")

helper.saveList2FIle('historyPrompts.txt', prompts)