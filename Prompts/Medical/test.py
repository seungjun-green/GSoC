import helper

fileNames = ['./Prompts/bodyPartsPrompts.txt',
             './Prompts/diagnoseNotePrompts.txt',
             './Prompts/diseasesPrompts.txt',
             './Prompts/medicinesPrompts.txt',
             './Prompts/operativePrompts.txt',
             './Prompts/treatmentPrompts.txt'
             ]


helper.combine_text_files(fileNames, 'medicalPrompts2.txt')
