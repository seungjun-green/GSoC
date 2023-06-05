import helper

bodyParts = helper.file2List('bodyParts.txt')

prompts = []
for bodyPart in bodyParts:
    prompts.append(f"Write an expert-level document on {bodyPart.strip()}.\n")

helper.saveList2FIle('bodyPartsPrompts.txt', prompts)

