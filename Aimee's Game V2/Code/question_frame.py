from tkinter import *

from answer import answer
from question import question

class question_frame:
    def __init__(self, window: Tk, the_question: question) -> None:
        self.window: Tk = window
        self.question: question = the_question

    def generate_frame(display_mode: str) -> None:
        pass

    def set_answer_question_controls() -> None:
        pass

    def set_preview_question_controls() -> None:
        pass

    def set_review_question_controls() -> None:
        pass