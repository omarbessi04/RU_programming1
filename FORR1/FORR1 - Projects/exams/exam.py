class Exam:
    def __init__(self):
        """Initialize Exam class"""
        self.questions = []
        self.points = 0

    def add_question(self, question: str):
        self.questions.append(question)

    def take(self):
        for question in self.questions:
            print(question.get_question())
            response = input()
            if question.check_answer(response):
                self.points += 1
            print(question.check_answer(response))
            print()

    def get_points(self) -> int:
        return self.points

    def get_num_questions(self) -> int:
        return len(self.questions)

    def __repr__(self) -> str:
        return "\n".join([str(question) for question in self.questions])