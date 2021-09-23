# Python-Quiz
# importing json package to handle josn data
import json

# opening json file
fp = open('quiz.json')

# creating json data object
data = json.load(fp)

# extracting competion name(i.e. quiz) in a variable, in case of multiple set of quizes
compitionName = list(data.keys())

# extracting keys(i.e. topics(maths, sports, etc)) from json data
topics = list(data[compitionName[0]].keys())


# taking input from user
print("\nEnter your choice: \n")
for j in range(len(topics)):
    print(j, ".", topics[j])
choice = int(input("Choice: "))

# method to play game on corresponding topic
def play(topic):

    # setting initial score
    score = 0

    # taking quetions in que
    que = data[compitionName[0]][topic]
    
    # creating a list of quetion numbers(i.e. keys of que ) in queNo
    queNo = []
    for key in dict.keys(que):
        queNo.append(key)
    # displaying quetion, taking answer from user & calculating score
    for i in range(len(queNo)):

        # displaying quetion
        print(que[queNo[i]]['question'])
        
        #displaying options 
        options = que[queNo[i]]['options']
        for j in range(len(options)):
            print(j, ".", options[j])
        
        # aceepting answer from user
        answer = int(input("Your answer option: "))
        
        # Validating user's answer & manipulating score
        if(answer < len(options) and answer >= 0):
            if(options[answer] == que[queNo[i]]['answer']):
                score += 1
                print("Right answer\n")
            else:
                print("Wrong anser\n")
        else:
            print("Wrong anser\n")

    # printing user's score & terminating game
    print("\nYou Score: ", score,"\nThanks for playing!!!\n")

# validating choice
if(choice < len(topics) and choice >= 0):
    play(topics[choice])
else:
    print("please enter valid choice!!!\n")
