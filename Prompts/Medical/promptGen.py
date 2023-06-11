import random

import helper

def generatePrompts_1(termsfile, output):
    terms = helper.file2List(termsfile)
    prompts = []
    for term in terms:
        prompts.append(f"Write an expert-level document on {term.strip()}.\n")

    helper.saveList2FIle(output, prompts)

generatePrompts_1('./Terms/bodyParts.txt', './Prompts/bodyPartsPrompts.txt') #1
generatePrompts_1('./Terms/diseases.txt', './Prompts/diseasesPrompts.txt') #2
generatePrompts_1('./Terms/medicines.txt', './Prompts/medicinesPrompts.txt') #3

ageGroups = ['young adult', 'middle-aged adult', 'senior']
def generatePrompts_2(termsfile, output):
    terms = helper.file2List(termsfile)
    prompts = []
    for term in terms:
        for patientAge in ageGroups:
            prompts.append(f"Write a treatment plan for a {patientAge} patient who have {term.strip()}. Write the document as if you are a doctor.\n")

    helper.saveList2FIle(output, prompts)

generatePrompts_2('./Terms/diseases.txt', './Prompts/treatmentPrompts.txt') #4


def generatePrompts_3(termsfile, output):
    terms = helper.file2List(termsfile)
    prompts = []
    for term in terms:
        for patientAge in ageGroups:
            prompts.append(f"Write a diagnosis note for a {patientAge} patient who have {term.strip()}. Write the document as if you are a doctor.\n")

    helper.saveList2FIle(output, prompts)

generatePrompts_3('./Terms/diseases.txt', './Prompts/diagnoseNotePrompts.txt') #5

def generatePrompts_4(termsfile, output):
    terms = helper.file2List(termsfile)
    prompts = []
    for term in terms:
        for patientAge in ageGroups:
            prompts.append(f"Write an operative note for a {patientAge} patient who had a {term.strip()}.\n")

    helper.saveList2FIle(output, prompts)

generatePrompts_4('./Terms/surgeryNames.txt', './Prompts/operativePrompts.txt') #5


