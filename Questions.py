from MCQ import question
question_asks = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Red\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries\n(a) Green\n(b) Purple\n(c) Red\n\n"
]

questions = [
  question(question_asks[0], "a"),
  question(question_asks[1], "c"),
  question(question_asks[2], "c")
  ]

def run_test(Quiz):
    score = 0
    for MCQ in Quiz:
        answer = input(MCQ.prompt)
        if answer == MCQ.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) +  "correct")
run_test(questions)
