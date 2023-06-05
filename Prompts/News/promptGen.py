import helper
def generatePrompts(input, output):
    terms = helper.file2List(input)

    prompts = []
    for term in terms:
        prompts.append(f"Write a news article about {term.strip()}.\n")

    helper.saveList2FIle(output, prompts)


generatePrompts('Arts and Culture', 'artPrompts')
generatePrompts('environment', 'envPrompts')
generatePrompts('Health', 'HealthPrompts')
generatePrompts('human', 'humanPrompts')
generatePrompts('investingTitles.txt', 'invPrompts')
generatePrompts('Politics', 'politicsPrompts')