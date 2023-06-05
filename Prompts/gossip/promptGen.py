import helper

titles = helper.file2List('gossip')

prompts = []
for title in titles:
    prompts.append(f"Write an gossip magazine article on {title}")

helper.saveList2FIle('gossipPrompts.txt', prompts)

