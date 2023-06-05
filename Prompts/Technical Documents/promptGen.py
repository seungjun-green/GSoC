import helper


def generatePrompts(input, output):
    terms = helper.file2List(input)

    prompts = []
    for term in terms:
        prompts.append(f"Write an expert-level document on {term.strip()}.\n")

    helper.saveList2FIle(output, prompts)

generatePrompts('AeroSpaceTerms.txt', 'AeroSpacePrompts.txt')
generatePrompts('CivilEngTemts.txt', 'CivilEngPrompts.txt')
generatePrompts('chemicalEngTerms.txt', 'ChemicalEngTerms.txt')
generatePrompts('NanotechTerms.txt', 'NanoTechPrompts.txt')
generatePrompts('BioTerms.txt', 'BioPrompts.txt')
generatePrompts('computerScienceTerms.txt', 'CSPrompts.txt')
