from Project1 import helper


def generatePrompts(input, output, type):
    terms = helper.file2List(input)

    prompts = []
    for term in terms:
        prompts.append(f"Write a{'n' if type.startswith('a') else ''} {type} fictional story where the title is {term.strip()}.\n")

    helper.saveList2FIle(output, prompts)



generatePrompts('./Terms/AdventureTerms', './Prompts/adventurePrompts.txt', 'adventure')
generatePrompts('./Terms/fantasyTerms', './Prompts/fantasyPrompts.txt', 'fantasy')
generatePrompts('./Terms/kidsTerms', './Prompts/kidsPrompts.txt', 'kid')
generatePrompts('./Terms/mysteryTerms', './Prompts/mysteryPrompts.txt', 'mystery')
generatePrompts('./Terms/spaceTerms', './Prompts/spaePrompts.txt', 'science')
generatePrompts('./Terms/thrillerTerms', './Prompts/thrillerPrompts.txt', 'thriller')

fileNames = ['./Prompts/adventurePrompts.txt',
             './Prompts/fantasyPrompts.txt',
             './Prompts/kidsPrompts.txt',
             './Prompts/mysteryPrompts.txt',
             './Prompts/spaePrompts.txt',
             './Prompts/thrillerPrompts.txt'
             ]


helper.combine_text_files(fileNames, '../../Prompts_text_files/fiction_prompts.txt')




