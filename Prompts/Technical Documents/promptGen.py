import helper


def generatePrompts(input, output):
    terms = helper.file2List(input)

    prompts = []
    for term in terms:
        prompts.append(f"Write an expert-level document on {term.strip()}.\n")

    helper.saveList2FIle(output, prompts)

generatePrompts('./Terms/AeroSpaceTerms.txt', './Prompts/AeroSpacePrompts.txt')
generatePrompts('./Terms/CivilEngTerms.txt', './Prompts/CivilEngPrompts.txt')
generatePrompts('./Terms/chemicalEngTerms.txt', './Prompts/ChemicalEngTerms.txt')
generatePrompts('./Terms/NanoTechTerms.txt', './Prompts/NanoTechPrompts.txt')
generatePrompts('./Terms/BioTerms.txt', './Prompts/BioPrompts.txt')
generatePrompts('./Terms/csTerms.txt', './Prompts/CSPrompts.txt')


fileNames = ['./Prompts/AeroSpacePrompts.txt',
             './Prompts/CivilEngPrompts.txt',
             './Prompts/ChemicalEngTerms.txt',
             './Prompts/NanoTechPrompts.txt',
             './Prompts/BioPrompts.txt',
             './Prompts/CSPrompts.txt'
             ]


helper.combine_text_files(fileNames, 'techPrompts.txt')
