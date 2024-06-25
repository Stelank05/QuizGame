import random

from tkinter import *

from answer import answer

class question:
    def __init__(self, question_data: dict) -> None:
        self.question_id: str = question_data["Question ID"]
        self.question_difficulty: str = question_data["Question Difficulty"]

        self.question_text: str = question_data["Question"]
        self.answer_options: list[answer] = self.get_answer_list(question_data["Answers"])
        self.correct_answer: answer = self.get_correct_answer()

        self.fun_fact: str = question_data["Fun Fact"]
        self.hint: str = question_data["Hint"]

        self.correct_audio: str = question_data["Correct Audio"]
        self.incorrect_audio: str = question_data["Incorrect Audio"]

#        self.question_frame: Toplevel = None
        self.selected_answers: list[answer] = []

        self.question_index: int = 0

        self.question_answered: bool = False
    
    def get_answer_list(self, answer_dicts: list[dict]) -> list[answer]:
        return_list: list[question] = []

        for answer_option in answer_dicts:
            return_list.append(answer(answer_option))
        
        return return_list
    
    def get_correct_answer(self) -> answer:
        for answer_option in self.answer_options:
            if answer_option.correct_answer:
                return answer_option

    def make_dictionary(self) -> dict:
        answer_list: list[dict] = []

        for answer_option in self.answer_options:
            answer_dict: dict = {
                "Answer Text" : answer_option.answer_text,
                "Answer Back Colour" : answer_option.answer_colours[0],
                "Answer Text Colour" : answer_option.answer_colours[1],
                "Correct Answer" : answer_option.correct_answer,
                "Answer Index" : answer_option.answer_index
            }

            answer_list.append(answer_dict)

        return_dict: dict = {
            "Question ID" : self.question_id,
            "Question Difficulty" : self.question_difficulty,
            "Question" : self.question_text,
            "Answers" : answer_list,
            "Fun Fact" : self.fun_fact,
            "Hint" : self.hint,
            "Correct Audio" : self.correct_audio,
            "Incorrect Audio" : self.incorrect_audio
        }

        return return_dict

    def add_selected_answer(self, selected_answer: answer) -> None:
        self.selected_answers.append(selected_answer)

    def randomise_answer_order(self) -> None:
        indexes: list[int] = list(range(len(self.answer_options)))

        for this_answer in self.answer_options:
            index: int = random.randint(1, len(indexes)) - 1
            new_index: int = indexes[index]
            indexes.remove(new_index)

            #print(f"{index} -> {new_index}")

            this_answer.answer_index = new_index

        swap: bool

        for i in range(len(self.answer_options) - 1):
            swap = False
            
            for j in range(len(self.answer_options) - i - 1):
                if self.answer_options[j].answer_index > self.answer_options[j + 1].answer_index:
                    swap = True

                    temp = self.answer_options[j]
                    self.answer_options[j] = self.answer_options[j + 1]
                    self.answer_options[j + 1] = temp

            if not swap:
                break