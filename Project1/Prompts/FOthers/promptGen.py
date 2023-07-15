from Project1 import helper

# combine two text files into one
files = [
    './Terms/buildings.txt',
    './Terms/celebrity.txt',
    './Terms/books.txt',
    './Terms/animals.txt',
    './Terms/movies.txt',
    './Terms/militaryAircrafts.txt',
]
helper.combine_text_files(files, 'fOthersTerms.txt')
# create a prompt txt file

terms = helper.file2List('fOthersTerms.txt')

with open('fOthersPrompts.txt', 'w') as f:
    for term in terms:
        f.write(f"Write a document explaining about {term.strip()}.\n")









