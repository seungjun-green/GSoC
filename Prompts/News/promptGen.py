import helper
def generatePrompts(input, output):
    terms = helper.file2List(input)

    prompts = []
    for term in terms:
        prompts.append(f"Write a news article about {term.strip()}.\n")

    helper.saveList2FIle(output, prompts)


generatePrompts('./Terms/Arts and Culture.txt', './Prompts/artPrompts.txt')
generatePrompts('./Terms/environment.txt', './Prompts/envPrompts.txt')
generatePrompts('./Terms/Health.txt', './Prompts/HealthPrompts.txt')
generatePrompts('./Terms/human.txt', './Prompts/humanPrompts.txt')
generatePrompts('./Terms/investingTerms.txt', './Prompts/invPrompts.txt')
generatePrompts('./Terms/Politics.txt', './Prompts/politicsPrompts.txt')


fileNames = [
'./Prompts/artPrompts.txt',
'./Prompts/envPrompts.txt',
'./Prompts/HealthPrompts.txt',
'./Prompts/humanPrompts.txt',
'./Prompts/invPrompts.txt',
'./Prompts/politicsPrompts.txt'
]

helper.combine_text_files(fileNames, 'newsPrompts.txt')