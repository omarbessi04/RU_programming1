class Question:
    """Creates a question with a single answer"""
    def __init__(self, question_str: str, answer_str: str) -> None:
        """Initialize Question class"""
        self.__question_str = question_str
        self.__answer_str = answer_str

    def get_question(self) -> str:
        """Get the question string"""
        return self.__question_str

    def check_answer(self, response:str) -> bool:
        """Check if the answer is correct"""
        return response.lower() == self.__answer_str.lower()

    def __repr__(self) -> str:
        """String representation of a Question"""
        return f"Q: {self.__question_str} A: {self.__answer_str}"