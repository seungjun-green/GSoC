import helper

titles = helper.file2List('gossip')

prompts = []
for title in titles:
    prompts.append(f"Write a conversational style article using slang words on {title}")

helper.saveList2FIle('gossipPrompts.txt', prompts)

