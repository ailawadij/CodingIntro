from MCQ2 import TV
Channel_is = [
    "Cartoon Network?\n(a) 369\n(b) 3\n(c) 385\n\n",
    "Disney?\n(a) 385\n(b) 3\n(c) 369\n\n",
    "ABC?\n(a) 385\n(b) 3\n(c) 369\n\n"
]

Channels = [
    TV(Channel_is[0], "a"),
    TV(Channel_is[1], "a"),
    TV(Channel_is[2], "b")
]

def TV_test(Number):
    grade = 0
    for Channel in Channels:
        Channel_answer = input(Channel.TV_Show)
        if Channel_answer == Channel.Channel_number:
            grade += 1
    print("Your grade is " + str(grade) + "/" + str(len(Channels)))
TV_test(Channels)

