import helper


def starts_with_vowel(s):
    # List of vowels
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    # Check if the first character of the string is in vowels
    if s[0] in vowels:
        return True
    else:
        return False

def generatePrompts(input, output):
    terms = helper.file2List(input)

    prompts = []
    for term in terms:
        if starts_with_vowel(term.strip()):
            prompts.append(f"Write a job description for an {term.strip()}.\n")
        else:
            prompts.append(f"Write a job description for a {term.strip()}.\n")

    helper.saveList2FIle(output, prompts)

generatePrompts('jobsTerms', 'jobPrompts.txt')