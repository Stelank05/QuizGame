class answer:
    def __init__(self, present_data: dict) -> None:
        self.answer_text: str = present_data["Answer Text"]
        self.answer_colours: list[str] = [present_data["Answer Back Colour"], present_data["Answer Text Colour"]]

        self.correct_answer: bool = present_data["Correct Answer"] == True
    
        self.answer_index: int = int(present_data["Answer Index"])