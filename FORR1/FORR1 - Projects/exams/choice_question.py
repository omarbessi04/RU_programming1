from question import Question

class ChoiceQuestion(Question):
    """Creates a multiple-choice question"""
    def __init__(self, question_str: str):
        """Initialize ChoiceQuestion class with it's parent class, Question"""
        super().__init__(question_str, "")
        self.choices = []
        self.correct_answer = 0
    
    def add_choice(self, choice: str, is_correct: bool):
        """Add option to the multiple-choice question"""
        self.choices.append((choice, is_correct))
        # Save the correct answer
        if is_correct == True:
            self.correct_answer = len(self.choices)
    
    def check_answer(self, response: str) -> int or bool:
        """Check if the answer is correct"""
        try:
            response = int(response)
            # Check if the answer is within the range
            if 1 <= response <= len(self.choices):
                # Return the second value of the chosen answer
                return self.choices[response - 1][1]
            else:
                return False
            
        # If the answer isn't an integer, it's incorrect
        except ValueError:
            return False

    def get_question(self) -> str:
        """Return question with specific format"""
        question_text = super().get_question()
        for i, (choice, _) in enumerate(self.choices, start=1):
            
            question_text += f"\n{i}. {choice}"
        return question_text

    def __repr__(self) -> str:
        return f"Q: {super().get_question()} A: {self.correct_answer}"