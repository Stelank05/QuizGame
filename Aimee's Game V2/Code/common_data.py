import os

from audio import audio
from colour import colour
from file_handling import *
from question import question
from user import user

class common_data:
    # File Data
    root_folder: str
    setup_folder: str

    audio_file: str
    colour_file: str
    user_file: str
    window_design_file: str

    audio_folder: str
    user_folder: str

    usable_questions_file: str
    discarded_questions_file: str
    usable_questions_folder: str
    discarded_questions_folder: str

    quiz_setup_file: str


    # Lists
    audio_list: list[audio] = []
    colour_list: list[colour] = []
    user_list: list[user] = []

    usable_question_list: list[question] = []
    discarded_question_list: list[question] = []


    # File Controls

    def set_root_folder(new_root: str) -> None:
        common_data.root_folder = new_root
    
    def get_root_folder() -> str:
        return common_data.root_folder
    
    def set_setup_folder(new_setup: str) -> None:
        common_data.setup_folder = new_setup

    def get_setup_folder() -> str:
        return os.path.join(common_data.root_folder, common_data.setup_folder)

    def set_audio_file(new_audio: str) -> None:
        common_data.audio_file = new_audio

    def get_audio_file() -> str:
        return os.path.join(common_data.root_folder, common_data.setup_folder, common_data.audio_file)

    def set_audio_folder(new_audio: str) -> None:
        common_data.audio_folder = new_audio

    def get_audio_folder() -> str:
        return os.path.join(common_data.root_folder, common_data.setup_folder, common_data.audio_folder)
    
    def set_colour_file(new_colour: str) -> None:
        common_data.colour_file = new_colour

    def get_colour_file() -> str:
        return os.path.join(common_data.root_folder, common_data.setup_folder, common_data.colour_file)

    def set_user_file(new_user: str) -> None:
        common_data.user_file = new_user

    def get_user_file() -> None:
        return os.path.join(common_data.root_folder, common_data.setup_folder, common_data.user_file)

    def set_user_folder(new_user: str) -> None:
        common_data.user_folder = new_user

    def get_user_folder() -> str:
        return os.path.join(common_data.root_folder, common_data.setup_folder, common_data.user_folder)

    def set_window_design_file(new_window: str) -> None:
        common_data.window_design_file = new_window

    def get_window_design_file() -> str:
        return os.path.join(common_data.root_folder, common_data.setup_folder, common_data.window_design_file)

    def set_quiz_setup_file(new_file: str) -> None:
        common_data.quiz_setup_file = new_file

    def get_quiz_setup_file() -> str:
        return os.path.join(common_data.root_folder, common_data.setup_folder, common_data.quiz_setup_file)


    # Usable Question File Controls

    def set_usable_question_file(new_file: str) -> None:
        common_data.usable_questions_file = new_file

    def get_usable_question_file() -> str:
        return os.path.join(common_data.root_folder, common_data.setup_folder, common_data.usable_questions_file)
    
    def set_usable_question_folder(new_folder: str) -> None:
        common_data.usable_questions_folder = new_folder

    def get_usable_question_folder() -> str:
        return os.path.join(common_data.root_folder, common_data.setup_folder, common_data.usable_questions_folder)


    # Discarded Question File Controls

    def set_discarded_question_file(new_file: str) -> None:
        common_data.discarded_questions_file = new_file

    def get_discarded_question_file() -> str:
        return os.path.join(common_data.root_folder, common_data.setup_folder, common_data.discarded_questions_file)
    
    def set_discarded_question_folder(new_folder: str) -> None:
        common_data.discarded_questions_folder = new_folder

    def get_discarded_question_folder() -> str:
        return os.path.join(common_data.root_folder, common_data.setup_folder, common_data.discarded_questions_folder)
    

    # Audio Controls

    def add_audio(new_audio: audio) -> None:
        common_data.audio_list.append(new_audio)

    def delete_audio(delete_audio: audio) -> None:
        common_data.audio_list.remove(delete_audio)

    def get_audio(index: int) -> audio:
        return common_data.audio_list[index]
    
    def get_audio_list() -> list[audio]:
        return common_data.audio_list


    # Colour Controls

    def add_colour(new_colour: colour) -> None:
        common_data.colour_list.append(new_colour)
    
    def remove_colour(remove_colour: colour) -> None:
        common_data.colour_list.remove(remove_colour)
    
    def get_colour(index: int) -> colour:
        return common_data.colour_list[index]
    
    def get_colour_list() -> list[colour]:
        return common_data.colour_list
    
    def get_colour_index_from_name(colour_name: str) -> int:
        for i in range(len(common_data.colour_list)):
            if common_data.colour_list[i].colour_name == colour_name:
                return i
        
        return common_data.get_colour_index_from_name("White")

    def get_colour_from_name(colour_name: str) -> colour:
        for colour_option in common_data.colour_list:
            if colour_option.colour_name == colour_name:
                return colour_option

        print(f"NULL COLOUR - Name: {colour_name}")
        return colour("NULL COLOUR", "#FFFFFF")    

    def get_colour_from_code(colour_code: str) -> colour:
        for colour_option in common_data.colour_list:
            if colour_option.colour_code == colour_code:
                return colour_option

        print(f"NULL COLOUR - Code: {colour_code}")
        return colour("NULL COLOUR", "#FFFFFF")    


    # User Controls

    def add_user(new_user: user) -> None:
        common_data.user_list.append(new_user)
    
    def remove_user(remove_user: user) -> None:
        common_data.user_list.remove(remove_user)
    
    def get_user(index: int) -> user:
        return common_data.user_list[index]
    
    def get_user_list() -> list[user]:
        return common_data.user_list
    
    
    # Question Controls

    def add_usable_question(new_question: question) -> None:
        common_data.usable_question_list.append(new_question)

    def add_discarded_question(new_question: question) -> None:
        common_data.discarded_question_list.append(new_question)

    def discard_question(discard_question: question) -> None:
        common_data.usable_question_list.remove(discard_question)
        common_data.discarded_question_list.append(discard_question)

        common_data.sort_usable_questions()
        common_data.sort_discarded_questions()
        
    def reinstate_question(reinstate_question: question) -> None:
        common_data.discarded_question_list.remove(reinstate_question)
        common_data.usable_question_list.append(reinstate_question)

        common_data.sort_usable_questions()
        common_data.sort_discarded_questions()

    def sort_usable_questions() -> None:
        swap: bool

        for i in range(len(common_data.usable_question_list) - 1):
            swap = False

            for j in range(len(common_data.usable_question_list) - i - 1):
                key_a: int = int((common_data.usable_question_list[j].question_id).replace("Q", ""))
                key_b: int = int((common_data.usable_question_list[j + 1].question_id).replace("Q", ""))

                if key_a > key_b:
                    swap = True

                    temp: question = common_data.usable_question_list[j]

                    common_data.usable_question_list[j] = common_data.usable_question_list[j + 1]
                    common_data.usable_question_list[j + 1] = temp

            if not swap:
                break

        write_string: str = ""

        for question_option in common_data.usable_question_list:
            write_string += f"{question_option.question_id}.json\n"

        write_file(common_data.get_usable_question_file(), write_string)

    def sort_discarded_questions() -> None:
        swap: bool
        for i in range(len(common_data.discarded_question_list) - 1):
            swap = False

            for j in range(len(common_data.discarded_question_list) - i - 1):
                key_a: int = int((common_data.discarded_question_list[j].question_id).replace("Q", ""))
                key_b: int = int((common_data.discarded_question_list[j + 1].question_id).replace("Q", ""))

                if key_a > key_b:
                    swap = True
                    
                    temp: question = common_data.discarded_question_list[j]

                    common_data.discarded_question_list[j] = common_data.discarded_question_list[j + 1]
                    common_data.discarded_question_list[j + 1] = temp

            if not swap:
                break
            
        write_string: str = ""

        for question_option in common_data.discarded_question_list:
            write_string += f"{question_option.question_id}.json\n"

        write_file(common_data.get_discarded_question_file(), write_string)