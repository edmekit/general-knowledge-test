import random 

matching_quiz = {
    1: ("CPU", "Central Processing Unit"),
    2: ("RAM", "Random Access Memory"),
    3: ("SSD", "Solid State Drive"),
    4: ("GPU", "Graphics Processing Unit"),
    5: ("URL", "Uniform Resource Locator"),
    6: ("HTML", "HyperText Markup Language"),
    7: ("IP", "Internet Protocol"),
    8: ("DNS", "Domain Name System"),
    9: ("HTTP", "HyperText Transfer Protocol"),
    10: ("IDE", "Integrated Development Environment"),
    11: ("OS", "Operating System"),
    12: ("API", "Application Programming Interface"),
    13: ("CLI", "Command Line Interface"),
    14: ("GUI", "Graphical User Interface"),
    15: ("SQL", "Structured Query Language"),
    16: ("JSON", "JavaScript Object Notation"),
    17: ("FTP", "File Transfer Protocol"),
    18: ("LAN", "Local Area Network"),
    19: ("WAN", "Wide Area Network"),
    20: ("DNS", "Domain Name System"),
}

for i in range(20):
    questions = open(f"quiz{i+1}.txt", "w")
    answers = open(f"answers{i+1}.txt", "w")
    questions.write('Name: \n')
    questions.write((' ' * 20) + f'IT Quiz (Form{i + 1})')
    questions.write('\n\n')
    abbv = list(matching_quiz.keys())
    random.shuffle(abbv)
    for j in range(20):
        correct = matching_quiz[abbv[j]]
        wrong = list(matching_quiz.values())
        del wrong[wrong.index(correct)]
        wrong = random.sample(wrong, 3)
        choices = wrong + [correct]
        random.shuffle(choices)
        questions.write(f'{j + 1}. Meaning of {abbv[j]}: \n')
        for choice in choices:
            questions.write(f'{"ABCD"[choices.index(choice)]}. {choice}\n')
        answers.write(f'{j + 1}. {"ABCD"[choices.index(correct)]}\n')
    questions.close()
    answers.close()
