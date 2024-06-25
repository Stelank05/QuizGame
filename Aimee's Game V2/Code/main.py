"""
Made by Stephen Lankshear in about a Month because he was bored after University Year 1 Finished
And also because he thought it'd be funny to make a V2 because V1 was so bad, and also go "surprise" to Aimee when I'm done
"""

import os

from tkinter import *
from tkinter import messagebox

from audio import audio
from colour import colour
from common_data import common_data
from file_handling import *
from question import question
from quiz_handler import quiz_handler
from user import user
from window_controls import window_controls
from window_design import window_design

def setup() -> None:
    setup_data = read_file(os.path.join(os.getcwd(), "Code", "Setup File.csv"))

    common_data.set_root_folder(os.getcwd())
    common_data.set_setup_folder(setup_data[0])
    common_data.set_audio_folder(setup_data[1])
    common_data.set_usable_question_folder(setup_data[2])
    common_data.set_discarded_question_folder(setup_data[3])
    common_data.set_user_folder(setup_data[4])
    common_data.set_usable_question_file(setup_data[5])
    common_data.set_discarded_question_file(setup_data[6])
    common_data.set_audio_file(setup_data[7])
    common_data.set_colour_file(setup_data[8])
    common_data.set_user_file(setup_data[9])
    common_data.set_window_design_file(setup_data[10])
    common_data.set_quiz_setup_file(setup_data[11])

def load_quiz_data() -> None:
    quiz_handler.setup_quiz(read_json_file(common_data.get_quiz_setup_file()))

def load_colours() -> None:
    colour_data: list[str] = read_file(common_data.get_colour_file())

    for colour_option in colour_data:
        common_data.add_colour(colour(colour_option.split(',')[0], colour_option.split(',')[1]))

def load_window_data() -> None:
    window_data: dict = read_json_file(common_data.get_window_design_file())

    window_design.set_window_colours([common_data.get_colour_from_name(window_data["Default Window Background"]), common_data.get_colour_from_name(window_data["Default Window Foreground"])])
    window_design.set_label_colours([common_data.get_colour_from_name(window_data["Default Label Background"]), common_data.get_colour_from_name(window_data["Default Label Foreground"])])
    window_design.set_button_colours([common_data.get_colour_from_name(window_data["Default Button Background"]), common_data.get_colour_from_name(window_data["Default Button Foreground"])])
    window_design.set_entry_colours([common_data.get_colour_from_name(window_data["Default Entry Background"]), common_data.get_colour_from_name(window_data["Default Entry Foreground"])])

    window_design.set_main_font(window_data["Main Font"])

    window_design.set_correct_answer_colours(common_data.get_colour_from_name(window_data["Correct Answer Back Colour"]), common_data.get_colour_from_name(window_data["Correct Answer Text Colour"]))
    window_design.set_incorrect_answer_colours(common_data.get_colour_from_name(window_data["Incorrect Answer Back Colour"]), common_data.get_colour_from_name(window_data["Incorrect Answer Text Colour"]))
    #window_design.set_double_wrong_answer_colours(common_data.get_colour_from_name(window_data["Double Wrong Answer Back Colour"]), common_data.get_colour_from_name(window_data["Double Wrong Answer Text Colour"]))

    window_design.set_spacer(window_data["Spacer Size"])

    # Login Window Details
    window_design.set_login_width(window_data["Login Page Sizes"][0]["Widget Width"])
    window_design.set_login_height(window_data["Login Page Sizes"][0]["Widget Height"])

    # Create Account Window Details
    window_design.set_create_account_width(window_data["Create Account Page Sizes"][0]["Small Widget Width"])
    window_design.set_create_account_small_height(window_data["Create Account Page Sizes"][0]["Small Widget Height"])
    window_design.set_create_account_large_height(window_data["Create Account Page Sizes"][0]["Large Widget Height"])

    # Create Account Window Details
    window_design.set_choose_colours_width(window_data["Choose Colours Page Sizes"][0]["Small Widget Width"])
    window_design.set_choose_colours_small_height(window_data["Choose Colours Page Sizes"][0]["Small Widget Height"])
    window_design.set_choose_colours_large_height(window_data["Choose Colours Page Sizes"][0]["Large Widget Height"])

    # User Account Window Details
    window_design.set_user_account_width(window_data["User Home Page Sizes"][0]["Small Widget Width"])
    window_design.set_user_account_small_height(window_data["User Home Page Sizes"][0]["Small Widget Height"])
    window_design.set_user_account_large_height(window_data["User Home Page Sizes"][0]["Large Widget Height"])

    # Load Colour Editor Window Details
    window_design.set_colour_editor_width(window_data["Colour Editor Page Sizes"][0]["Small Widget Width"])
    window_design.set_colour_editor_small_height(window_data["Colour Editor Page Sizes"][0]["Small Widget Height"])
    window_design.set_colour_editor_large_height(window_data["Colour Editor Page Sizes"][0]["Large Widget Height"])
    window_design.set_colour_editor_listbox_item_height(window_data["Colour Editor Page Sizes"][0]["Listbox Item Height"])
    window_design.set_colour_editor_listbox_visible_items(window_data["Colour Editor Page Sizes"][0]["Listbox Visible Items"])

    # Load View Account Window Details
    window_design.set_view_account_width(window_data["View Account Page Sizes"][0]["Small Widget Width"])
    window_design.set_view_account_small_height(window_data["View Account Page Sizes"][0]["Small Widget Height"])
    window_design.set_view_account_listbox_item_height(window_data["View Account Page Sizes"][0]["Listbox Item Height"])
    window_design.set_view_account_listbox_visible_items(window_data["View Account Page Sizes"][0]["Listbox Visible Items"])

    # Load Audio Editor Window Details
    window_design.set_audio_editor_width(window_data["Audio Editor Page Sizes"][0]["Small Widget Width"])
    window_design.set_audio_editor_small_height(window_data["Audio Editor Page Sizes"][0]["Small Widget Height"])
    window_design.set_audio_editor_listbox_item_height(window_data["Audio Editor Page Sizes"][0]["Listbox Item Height"])
    window_design.set_audio_editor_listbox_visible_items(window_data["Audio Editor Page Sizes"][0]["Listbox Visible Items"])

    # Load Question List Window Details
    window_design.set_question_list_width(window_data["Question List Page Sizes"][0]["Small Widget Width"])
    window_design.set_question_list_button_width(window_data["Question List Page Sizes"][0]["Button Widget Width"])
    window_design.set_question_list_small_height(window_data["Question List Page Sizes"][0]["Small Widget Height"])

    # Load Question Editor Window Details
    window_design.set_question_editor_width(window_data["Question Editor Page Sizes"][0]["Small Widget Width"])
    window_design.set_question_editor_large_height(window_data["Question Editor Page Sizes"][0]["Large Widget Height"])
    window_design.set_question_editor_small_height(window_data["Question Editor Page Sizes"][0]["Small Widget Height"])

    # Answer Colours Window Details
    window_design.set_choose_answer_colours_width(window_data["Choose Answer Colours Page Sizes"][0]["Small Widget Width"])
    window_design.set_choose_answer_colours_small_height(window_data["Choose Answer Colours Page Sizes"][0]["Small Widget Height"])
    window_design.set_choose_answer_colours_large_height(window_data["Choose Answer Colours Page Sizes"][0]["Large Widget Height"])

    # Setup Quiz Window Details
    window_design.set_setup_quiz_width(window_data["Setup Quiz Page Sizes"][0]["Small Widget Width"])
    window_design.set_setup_quiz_small_height(window_data["Setup Quiz Page Sizes"][0]["Small Widget Height"])
    window_design.set_setup_quiz_large_height(window_data["Setup Quiz Page Sizes"][0]["Large Widget Height"])

    # Setup Quiz Window Details
    window_design.set_question_page_width(window_data["Question Page Sizes"][0]["Widget Width"])
    window_design.set_question_page_difficulty_width(window_data["Question Page Sizes"][0]["Widget Difficulty Width"])
    window_design.set_question_page_small_height(window_data["Question Page Sizes"][0]["Small Widget Height"])
    window_design.set_question_page_large_height(window_data["Question Page Sizes"][0]["Large Widget Height"])

def load_audio_files() -> None:
    audio_data: list[str] = read_file(common_data.get_audio_file())

    for audio_file in audio_data:
        common_data.add_audio(audio(audio_file.split(',')[0], audio_file.split(',')[1]))

def load_questions() -> None:
    load_usable_questions()
    load_discarded_questions()

def load_usable_questions() -> None:
    usable_question_files: list[str] = read_file(common_data.get_usable_question_file())

    for new_usable_question in usable_question_files:
        file_path: str = os.path.join(common_data.get_usable_question_folder(), new_usable_question)

        if os.path.exists(file_path) and os.path.isfile(file_path):
            usable_question_json: dict = read_json_file(file_path)

            common_data.add_usable_question(question(usable_question_json))

def load_discarded_questions() -> None:
    discarded_question_files: list[str] = read_file(common_data.get_discarded_question_file())

    for new_discarded_question in discarded_question_files:
        file_path: str = os.path.join(common_data.get_discarded_question_folder(), new_discarded_question)

        if os.path.exists(file_path) and os.path.isfile(file_path):
            discarded_question_json: dict = read_json_file(file_path)

            common_data.add_discarded_question(question(discarded_question_json))

def load_users() -> None:
    user_files: list[str] = read_file(common_data.get_user_file())

    for new_user in user_files:
        user_json: dict = read_json_file(os.path.join(common_data.get_user_folder(), new_user))

        common_data.add_user(user(user_json))


setup()
load_quiz_data()
load_colours()
load_window_data()
load_audio_files()
load_questions()
load_users()

window: Tk = Tk()
window.withdraw()
window.title("Aimee Played Me - The Remix V2")

window_controls.set_window(window)

window_controls.login_controller()