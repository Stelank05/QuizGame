import random

from tkinter import *
from tkinter import messagebox

from common_data import common_data
from question import question

class quiz_handler:
    quiz_length: int = None
    quiz_difficulty: str = None
    
    question_list: list[question] = []

    current_question: question
    question_number: int = 0

    first_attempt_points: float
    second_attempt_points: float

    current_score: float = 0

    first_attempts: int = 0
    second_attempts: int = 0
    incorrect_questions: int = 0

    difficulty_range: list[str] = ["Easy", "Medium", "Hard"]
    correct_answers: list[int] = [1, 2, 3, 4]

    length_options: list[str] = ["Short", "Medium", "Long"]
    quiz_lengths: list[int] = []


    def setup_quiz(quiz_data):
        quiz_handler.first_attempt_points = float(quiz_data["First Attempt Points"])
        quiz_handler.second_attempt_points = float(quiz_data["Second Attempt Points"])

        quiz_handler.quiz_lengths.append(int(quiz_data["Short Quiz Length"]))
        quiz_handler.quiz_lengths.append(int(quiz_data["Medium Quiz Length"]))
        quiz_handler.quiz_lengths.append(int(quiz_data["Long Quiz Length"]))

    def valid_length(desired_length) -> bool:
        if quiz_handler.quiz_difficulty == None:
            messagebox.showwarning("No Difficulty Selected", "Please Select a Quiz Difficulty")
            return False
        
        if quiz_handler.quiz_difficulty != "Mixed":
            if quiz_handler.get_question_count() < desired_length:
                messagebox.showwarning("Insufficient Questions", "Insufficient Number of Appropriate Usable Questions")
                return False
            else:
                return True
        else:
            if len(common_data.usable_question_list) < desired_length:
                messagebox.showwarning("Insufficient Questions", "Insufficient Number of Usable Questions")
                return False
            else:
                return True
        
    def get_question_count() -> int:
        appropriate_question_count: int = 0

        for question in common_data.usable_question_list:
            if question.question_difficulty == quiz_handler.quiz_difficulty:
                appropriate_question_count += 1
        
        return appropriate_question_count
    
    def generate_quiz() -> None:
        quiz_handler.first_attempts = 0
        quiz_handler.second_attempts = 0
        quiz_handler.incorrect_questions = 0

        quiz_handler.current_score = 0

        quiz_handler.question_number = 1

        quiz_handler.question_list.clear()

        full_question_list: list[question] = quiz_handler.get_questions()

        for i in range(quiz_handler.quiz_length):
            full_question_list[i].randomise_answer_order()
            quiz_handler.question_list.append(full_question_list[i])
        
        #for quiz_question in quiz_handler.question_list:
        #    print(f"{quiz_question.question_index} - {quiz_question.question_text}")


    def get_questions() -> list[question]:
        for question_option in common_data.usable_question_list:
            question_option.question_answered = False
            question_option.selected_answers.clear()

        if quiz_handler.quiz_difficulty == "Mixed":
            return quiz_handler.randomise_questions(common_data.usable_question_list, 3)

        question_list: list[question] = []

        for this_question in common_data.usable_question_list:
            if this_question.question_difficulty == quiz_handler.quiz_difficulty:
                question_list.append(this_question)
        
        return quiz_handler.randomise_questions(question_list, 3)
    
    def randomise_questions(question_list, times) -> list[question]:
        full_question_list: list[question] = question_list
        
        for i in range(times):
            indexes: list[int] = list(range(len(full_question_list)))

            for this_question in full_question_list:
                index: int = random.randint(1, len(indexes)) - 1
                new_index: int = indexes[index]
                indexes.remove(new_index)

                this_question.question_index = new_index

            swap: bool

            for i in range(len(full_question_list) - 1):
                swap = False
                
                for j in range(len(full_question_list) - i - 1):
                    if full_question_list[j].question_index > full_question_list[j + 1].question_index:
                        swap = True

                        temp = full_question_list[j]
                        full_question_list[j] = full_question_list[j + 1]
                        full_question_list[j + 1] = temp

                if not swap:
                    break
        
        return full_question_list
