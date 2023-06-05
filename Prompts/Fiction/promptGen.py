import helper
def generatePrompts(input, output, type):
    terms = helper.file2List(input)

    prompts = []
    for term in terms:
        prompts.append(f"Write a short {type} fictional short where the title is {term.strip()}.\n")

    helper.saveList2FIle(output, prompts)



generatePrompts('AdventureTerms', 'AdventurePrompts', 'adventure')
generatePrompts('fantasyTerms', 'fantasyPrompts', 'fantasy')
generatePrompts('kidsTerms', 'kidsPrompts', 'kid')
generatePrompts('mysteryTerms', 'mysteryPrompts', 'mystery')
generatePrompts('spaceTerms', 'spaePrompts', 'space')
generatePrompts('thrillerTerms', 'thrillerPrompts', 'thriller')



