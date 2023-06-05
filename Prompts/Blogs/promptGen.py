import helper
def generatePrompts(input, output, type):
    terms = helper.file2List(input)

    prompts = []
    for term in terms:
        prompts.append(f"Write an {type} blog post on {term.strip()}.\n")

    helper.saveList2FIle(output, prompts)


generatePrompts('TravelTerms', 'TravelPrompts', 'travel')
generatePrompts('FoodTerms', 'FoodPrompts', 'food')
generatePrompts('HealthTerms', 'HealthPrompts', 'health')
generatePrompts('FamilyTerms', 'FamilyPrompts', 'family')
generatePrompts('fashionTerms', 'FashionPrompts', 'fashion')








