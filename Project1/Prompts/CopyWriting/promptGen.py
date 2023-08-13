from Project1 import helper

terms  = helper.file2List('copywritingTerms.txt')

with open('../../Prompts_text_files/copywriting_prompts.txt', 'w') as f:
    for term in terms:
        f.write(f"Write a copywriting campaign for {term.strip()}.\n")