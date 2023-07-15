from Project1 import helper

talkingSubjects = helper.file2List('Terms/friends.txt')

prompts = []
for subject in talkingSubjects:
    prompts.append(f"Write a conversation history between two friends talking on {subject.strip()}\nExample Output:\nFriend1: String1\nFriend2: String2\n")

helper.saveList2FIle('./Prompts/friendsPrompts.txt', prompts)



jobs = helper.file2List2('Terms/otherJobs.txt')
jobs2 = helper.file2List2('Terms/otherJobs2.txt')

prompts = []
for idx in range(len(jobs)):
    for i in range(3):
        prompts.append(f"Write a conversation history between {jobs[idx].strip()} and {jobs2[idx].strip()}\nExample Output:\n{jobs[idx].strip()}: String1\n{jobs2[idx].strip()}: String2\n")

helper.saveList2FIle('./Prompts/discussionPrompts.txt', prompts)


pilotConvs = helper.file2List('Terms/pilots')

prompts = []
for conv in pilotConvs:
    prompts.append(f"Write a conversation history between pilot and control tower on {conv.strip()}\nExample Output:\nPilot: String1\ncontrol tower: String2\n")

helper.saveList2FIle('./Prompts/pilotsConvPrompts.txt', prompts)


fileNames = [
'./Prompts/pilotsConvPrompts.txt',
'./Prompts/discussionPrompts.txt',
'./Prompts/friendsPrompts.txt'
]

helper.combine_text_files(fileNames, 'chatPrompts.txt')