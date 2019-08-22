import json


with open('Quiz\quiz.json') as f:
    data = json.loads(f.read())

# print(data['quiz']['maths']['q2']['options'])


print("Choose sport or maths")
userchoose = input()

data = data['quiz'][str(userchoose)]


score = 0
# print(len(data))
for i in range(len(data)):
    rowno = 'q'+str(i+1)
    question = data[rowno]['question']
    print(question)
    option = data[rowno]['options']
    for i in range(len(option)):
        print(str(i+1)+" "+str(option[i]))
    print('choose right option')
    ans = int(input())
    print('right ans is -> '+data[rowno]['answer'])
    if ((data[rowno]['answer'])==option[ans-1]):
        score = score+1
    # print(score)

print('Total score '+str(score))


# You need to write python code so that someone can take the quiz/MCQ from the attached quiz.json file. When the code is run on command line, it should print the two groups, sport and math. User can select any one group, then it should print the question, with its options and let user provide an answer.
# After answering all the questions, final result should be printed.
