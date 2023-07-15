from Project1 import helper


def generatePrompts(input, output, type):
    terms = helper.file2List(input)

    prompts = []
    for term in terms:
        prompts.append(f"Write an {type} blog post on {term.strip()}.\n")

    helper.saveList2FIle(output, prompts)


generatePrompts('./Terms/TravelTerms', './Prompts/TravelPrompts.txt', 'travel')
generatePrompts('./Terms/FoodTerms', './Prompts/FoodPrompts.txt', 'food')
generatePrompts('./Terms/HealthTerms', './Prompts/HealthPrompts.txt', 'health')
generatePrompts('./Terms/FamilyTerms', './Prompts/FamilyPrompts.txt', 'family')
generatePrompts('./Terms/fashionTerms', './Prompts/FashionPrompts.txt', 'fashion')

fileNames = ['./Prompts/TravelPrompts.txt',
             './Prompts/FoodPrompts.txt',
             './Prompts/HealthPrompts.txt',
             './Prompts/FamilyPrompts.txt',
             './Prompts/FashionPrompts.txt'
             ]


helper.combine_text_files(fileNames, 'blogPrompts.txt')









