import helper

talkingSubjects = helper.file2List('friends')

prompts = []
for subject in talkingSubjects:
    prompts.append(f"Write a conversation history between two friends talking on {subject.strip()}\nExample Output:\nName1: String1\nName2:String2\n")

helper.saveList2FIle('friendsPrompts.txt', prompts)



jobs = helper.file2List('otherJobs')

prompts = []
for job in jobs:
    for i in range(5):
        prompts.append(f"Write a conversation history between two {job.strip()}\nExample Output:\nName1: String1\nName2:String2\n")

helper.saveList2FIle('discussionPrompts.txt', prompts)


pilotConvs = helper.file2List('pilots')

prompts = []
for conv in pilotConvs:
    prompts.append(f"Write a conversation history between two pilots on {conv.strip()}\nExample Output:\nName1: String1\nName2:String2\n")

helper.saveList2FIle('pilotsConvPrompts.txt', prompts)
