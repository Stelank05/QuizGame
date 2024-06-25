import functools
import math
import pygame
import random
import re

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from answer import answer
from audio import audio
from colour import colour
from common_data import common_data
from file_handling import *
from question import question
from quiz_handler import quiz_handler
from user import user
from window_design import window_design

from poland import *

class window_controls:
    # General Data

    window: Tk

    pygame.mixer.init()

    login_page: Toplevel = None
    logout_page: Toplevel = None

    create_account_page: Toplevel = None
    colour_selector_page: Toplevel = None

    user_account_page: Toplevel = None
    view_account_page: Toplevel = None

    setup_quiz_page: Toplevel = None
    set_length_window: Toplevel = None
    main_quiz_page: Toplevel = None
    finish_quiz_page: Toplevel = None

    question_main_page: Toplevel = None
    question_list_page: Toplevel = None
    create_question_page: Toplevel = None
    select_question_colours_page: Toplevel = None
    
    colour_editor_page: Toplevel = None
    audio_editor_page: Toplevel = None

    frame_list: list[str] = ["Login", "Create Account", "User Account", "Colour Editor", "Audio Editor"]#, ""]

    current_user: user


    # Login + Create Account Data

    enter_username: Entry
    enter_password: Entry

    username_label: Label
    password_label: Label

    choose_colours_button: Button
    create_account_button: Button
    clear_button: Button

    window_back: StringVar
    window_text: StringVar
    select_window_back: ttk.Combobox
    select_window_text: ttk.Combobox

    label_back: StringVar
    label_text: StringVar
    select_label_back: ttk.Combobox
    select_label_text: ttk.Combobox

    button_back: StringVar
    button_text: StringVar
    select_button_back: ttk.Combobox
    select_button_text: ttk.Combobox

    entry_back: StringVar
    entry_text: StringVar
    select_entry_back: ttk.Combobox
    select_entry_text: ttk.Combobox
    
    window_colours_contrast: Label
    button_colours_contrast: Label

    window_colour_label: Label
    window_text_label: Label
    label_colours_label: Label
    button_colours_label: Button
    entry_colours_label: Label


    # View Account Data

    high_score_label: Label
    average_score_label: Label
    previous_scores_listbox: Listbox

    
    # Colour Editor Data

    colour_listbox: Listbox

    colour_name: Entry
    colour_code: Entry
    colour_preview: Label

    selected_colour: colour


    # Audio Editor Data

    audio_listbox: Listbox

    audio_name: Entry
    audio_file: Entry

    selected_audio: audio


    # Question List Data

    current_question_list: list[question]
    selected_question_list: str

    question_listbox: Listbox
    selected_question: question = None

    delete_question: Button


    # Question Editor Data

    enter_question_text: Entry
    create_question_button: Button

    answer_details: list[tuple[Entry, Label]] = []
    answer_colours: list[list[StringVar]] = []

    question_difficulty: StringVar
    correct_answer: StringVar

    correct_audio: StringVar
    incorrect_audio: StringVar

    enter_fun_fact: Entry
    enter_hint: Entry

    quiz_length: DoubleVar

    
    # Setup Quiz Data

    difficulty_buttons: list[Button] = []
    quiz_length_buttons: list[Button] = []


    # Play Quiz Data

    question_frames: list[Toplevel] = []
    answer_buttons: list[Button] = []

    current_selected_answer: answer
    attempts_at_question: int = 0
    total_attempts: int = 0

    current_score_label: Label

    select_answer_button: Button
    quiz_back_button: Button
    quiz_exit_button: Button


    # Frame Sequence

    frame_sequence: list[str] = []

    last_frame: str
    current_frame: str = ""


    # Set Window Function

    def set_window(window: Tk) -> None:
        window_controls.window = window


    # Login Functions

    def login_controller() -> None:
        try:
            window_controls.frame_sequence.remove(window_controls.frame_sequence[0])
        except:
            pass
        
        window_controls.frame_sequence.append("Login")

        try:
            window_controls.withdraw_frame(window_controls.frame_sequence[0])
        except:
            pass

        if window_controls.login_page == None or not window_controls.login_page.winfo_exists():
            window_controls.make_login_page()
        else:
            window_controls.clear_login_page()
            window_controls.login_page.deiconify()

    def make_login_page() -> None:
        window_controls.login_page = Toplevel(window_controls.window)

        window_colours: list[colour] = window_design.get_window_colours()
        button_colours: list[colour] = window_design.get_button_colours()
        entry_colours: list[colour] = window_design.get_entry_colours()

        width: int = window_design.get_login_width()
        height: int = window_design.get_login_height()

        window_controls.login_page.geometry(window_controls.calculate_login_dimensions())
        window_controls.login_page.config(bg = window_colours[0].colour_code)

        username_label: Label = Label(window_controls.login_page, text = "Username:", bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, font = window_design.main_font)
        username_label.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer), width = width, height = height)

        window_controls.enter_username = Entry(window_controls.login_page, bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        window_controls.enter_username.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer) + (1 * (window_design.spacer + height)), width = width, height = height)

        password_label: Label = Label(window_controls.login_page, text = "Password:", bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, font = window_design.main_font)
        password_label.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer) + (2 * (window_design.spacer + height)), width = width, height = height)

        window_controls.enter_password = Entry(window_controls.login_page, bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        window_controls.enter_password.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer) + (3 * (window_design.spacer + height)), width = width, height = height)

        login_button: Button = Button(window_controls.login_page, text = "Login", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.login)
        login_button.place(x = (2 * window_design.spacer), y = (4 * window_design.spacer) + (4 * (window_design.spacer + height)), width = width, height = height)

        create_account_button: Button = Button(window_controls.login_page, text = "Create Account", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.create_account_controller, "Create Account"))
        create_account_button.place(x = (2 * window_design.spacer), y = (4 * window_design.spacer) + (5 * (window_design.spacer + height)), width = width, height = height)
    
        exit_button: Button = Button(window_controls.login_page, text = "Exit", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.kill_program)
        exit_button.place(x = (2 * window_design.spacer), y = (5 * window_design.spacer) + (6 * (window_design.spacer + height)), width = width, height = height)
    
        window_controls.window.mainloop()


    # Create / Edit Account Functions

    def create_account_controller(selector_type: str) -> None:
            if len(window_controls.frame_sequence) > 1:
                window_controls.frame_sequence.remove(window_controls.frame_sequence[0])

            window_controls.frame_sequence.append("Create Account")

            try:
                window_controls.withdraw_frame(window_controls.frame_sequence[0])
            except:
                pass

            if window_controls.create_account_page == None or not window_controls.create_account_page.winfo_exists():
                window_controls.make_new_create_account_page(selector_type)
            else:
                window_controls.clear_create_account_page()
                window_controls.create_account_page.update()
                window_controls.create_account_page.deiconify()

    def make_new_create_account_page(selector_type: str) -> None:
        window_controls.create_account_page = Toplevel(window_controls.window)

        window_colours: list[colour]
        label_colours: list[colour]
        button_colours: list[colour]
        entry_colours: list[colour]

        match selector_type:
            case "Create Account":
                window_colours = window_design.get_window_colours()
                label_colours = window_design.get_label_colours()
                button_colours = window_design.get_button_colours()
                entry_colours = window_design.get_entry_colours()
            case "Update User Colours":
                window_colours = window_controls.convert_to_colours(window_controls.current_user.window_colours)
                label_colours = window_controls.convert_to_colours(window_controls.current_user.label_colours)
                button_colours = window_controls.convert_to_colours(window_controls.current_user.button_colours)
                entry_colours = window_controls.convert_to_colours(window_controls.current_user.entry_colours)

        width: int = window_design.get_create_account_width()
        small_height: int = window_design.get_create_account_small_height()
        large_height: int = window_design.get_create_account_large_height()

        window_controls.create_account_page.geometry(window_controls.calculate_new_create_account_dimensions())
        window_controls.create_account_page.config(bg = window_colours[0].colour_code)

        x_value: int = (2 * window_design.spacer)


        # Enter Username

        window_controls.username_label = Label(window_controls.create_account_page, text = "Username:", bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, font = window_design.main_font)
        window_controls.username_label.place(x = x_value, y = (2 * window_design.spacer), width = width, height = small_height)

        window_controls.enter_username = Entry(window_controls.create_account_page, bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        window_controls.enter_username.place(x = x_value, y = (2 * window_design.spacer) + (1 * small_height), width = width, height = small_height)


        # Enter Password

        window_controls.password_label = Label(window_controls.create_account_page, text = "Password:", bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, font = window_design.main_font)
        window_controls.password_label.place(x = x_value, y = (3 * window_design.spacer) + (2 * small_height), width = width, height = small_height)

        window_controls.enter_password = Entry(window_controls.create_account_page, bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        window_controls.enter_password.place(x = x_value, y = (3 * window_design.spacer) + (3 * small_height), width = width, height = small_height)


        # Controls
        
        control_row: int = (6 * window_design.spacer) + (4 * small_height)

        window_controls.create_account_button = Button(window_controls.create_account_page, text = "Create Account", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.create_account)
        window_controls.create_account_button.place(x = x_value, y = control_row, width = width, height = small_height)

        control_row_2: int = control_row + ((1 * window_design.spacer) + small_height)

        window_controls.clear_button = Button(window_controls.create_account_page, text = "Clear", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.clear_create_account_page)
        window_controls.clear_button.place(x = x_value, y = control_row_2, width = width, height = small_height)

        back_button: Button = Button(window_controls.create_account_page, text = "Back", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.go_back)
        back_button.place(x = x_value, y = control_row_2 + ((1 * window_design.spacer) + small_height), width = width, height = small_height)

        exit_button: Button = Button(window_controls.create_account_page, text = "Exit", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.kill_program)
        exit_button.place(x = x_value, y = control_row_2 + (2 * ((1 * window_design.spacer) + small_height)), width = width, height = small_height)


        # Chosen Colour Labels

        colour_x_value: int = (6 * window_design.spacer) + width

        window_controls.choose_colours_button = Button(window_controls.create_account_page, text = "Choose Colours", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.colour_selector_controller, selector_type))
        window_controls.choose_colours_button.place(x = colour_x_value, y = control_row_2 + (2 * (window_design.spacer + small_height)), width = width, height = small_height)

        window_border: Label = Label(window_controls.create_account_page, bg = "#000000")
        window_border.place(x = colour_x_value, y = 2 * window_design.spacer, width = width, height = control_row_2 + (2 * (window_design.spacer + small_height)) - (5 * window_design.spacer))

        preview_width: int = width - (2 * window_design.spacer)

        window_controls.window_colour_label = Label(window_controls.create_account_page, bg = window_colours[0].colour_code)
        window_controls.window_colour_label.place(x = colour_x_value + window_design.spacer, y = 3 * window_design.spacer, width = preview_width, height = control_row_2 + (2 * (window_design.spacer + small_height)) - (7 * window_design.spacer))

        preview_width -= (2 * window_design.spacer)
        preview_window: int = 3 * window_design.spacer + (1 * window_design.spacer)

        window_controls.window_text_label = Label(window_controls.create_account_page, text = "Window Colours", bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, font = window_design.main_font)
        window_controls.window_text_label.place(x = colour_x_value + (2 * window_design.spacer), y = preview_window, width = preview_width, height = large_height)

        window_controls.label_colours_label = Label(window_controls.create_account_page, text = "Label Colours", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        window_controls.label_colours_label.place(x = colour_x_value + (2 * window_design.spacer), y = preview_window + (1 * (window_design.spacer + large_height)), width = preview_width, height = large_height)

        window_controls.button_colours_label = Button(window_controls.create_account_page, text = "Button Colours", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font)
        window_controls.button_colours_label.place(x = colour_x_value + (2 * window_design.spacer), y = preview_window + (2 * (window_design.spacer + large_height)), width = preview_width, height = large_height)

        window_controls.entry_colours_label = Label(window_controls.create_account_page, text = "Entry Colours", bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        window_controls.entry_colours_label.place(x = colour_x_value + (2 * window_design.spacer), y = preview_window + (3 * (window_design.spacer + large_height)), width = preview_width, height = large_height)

    def insert_user_data() -> None:
        if window_controls.colour_selector_page != None and window_controls.colour_selector_page.winfo_exists():
            window_controls.colour_selector_page.destroy()

        window_controls.enter_username.delete(0, len(window_controls.enter_username.get()))
        window_controls.enter_password.delete(0, len(window_controls.enter_password.get()))

        window_controls.enter_username.insert(0, window_controls.current_user.username)
        window_controls.enter_password.insert(0, window_controls.current_user.password)

        window_controls.choose_colours_button.configure(command = functools.partial(window_controls.colour_selector_controller, "Update User Colours"))
        window_controls.create_account_button.configure(text = "Update Account", command = window_controls.update_account)
        window_controls.clear_button.configure(text = "Reset User Data", command = window_controls.insert_user_data)

        window_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.window_colours)
        label_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.label_colours)
        button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)
        entry_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.entry_colours)

        window_controls.window_colour_label.configure(bg = window_colours[0].colour_code)
        window_controls.window_text_label.configure(bg = window_colours[0].colour_code, fg = window_colours[1].colour_code)
        window_controls.label_colours_label.configure(bg = label_colours[0].colour_code, fg = label_colours[1].colour_code)
        window_controls.button_colours_label.configure(bg = button_colours[0].colour_code, fg = button_colours[1].colour_code)
        window_controls.entry_colours_label.configure(bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code)

    def colour_selector_controller(selector_type: str) -> None:
        if window_controls.colour_selector_page == None or not window_controls.colour_selector_page.winfo_exists():
            window_controls.make_colour_selector_page(selector_type)
        else:
            window_controls.colour_selector_page.update()
            window_controls.colour_selector_page.deiconify()

    def make_colour_selector_page(selector_type: str) -> None:
        window_controls.colour_selector_page = Toplevel(window_controls.window)

        window_colours: list[colour] = window_design.get_window_colours()
        label_colours: list[colour] = window_design.get_label_colours()
        button_colours: list[colour] = window_design.get_button_colours()

        width: int = window_design.get_choose_colours_width()
        small_height: int = window_design.get_choose_colours_small_height()

        window_controls.colour_selector_page.geometry(window_controls.calculate_colour_selector_dimensions())
        window_controls.colour_selector_page.config(bg = window_colours[0].colour_code)

        header_label: Label = Label(window_controls.colour_selector_page, text = "Select Colours", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        header_label.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer), width = (2 * window_design.spacer) + (2 * (window_design.spacer + width)), height = small_height)

        window_controls.choose_colour_pair_v2(selector_type, "Window")
        window_controls.choose_colour_pair_v2(selector_type, "Label")
        window_controls.choose_colour_pair_v2(selector_type, "Button")
        window_controls.choose_colour_pair_v2(selector_type, "Entry")

        confirm_button_y: int = (6 * window_design.spacer) + (15 * (window_design.spacer + small_height)) + (2 * (window_design.spacer + window_design.get_choose_colours_large_height()))

        reset_colours_button: Button = Button(window_controls.colour_selector_page, text = "Reset Colours", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.reset_colours, selector_type, "All"))
        reset_colours_button.place(x = (2 * window_design.spacer), y = confirm_button_y, width = (2 * window_design.spacer) + (2 * (window_design.spacer + width)), height = small_height)

        confirm_button: Button = Button(window_controls.colour_selector_page, text = "Confirm Colours", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.select_colours)
        confirm_button.place(x = (2 * window_design.spacer), y = confirm_button_y + (window_design.spacer + small_height), width = (2 * window_design.spacer) + (2 * (window_design.spacer + width)), height = small_height)

    def choose_colour_pair_v2(selector_type: str, colour_pair: str) -> None:
        colour_name_list: list[str] = []

        for colour_option in common_data.get_colour_list():
            colour_name_list.append(colour_option.colour_name)

        window_colours: list[colour] = window_design.get_window_colours()
        label_colours: list[colour] = window_design.get_label_colours()
        button_colours: list[colour] = window_design.get_button_colours()

        width: int = window_design.get_choose_colours_width()
        small_height: int = window_design.get_choose_colours_small_height()
        large_height: int = window_design.get_choose_colours_large_height()

        x_value: int
        y_value: int

        small_height_spacer: int = window_design.spacer + small_height
        large_height_spacer: int = window_design.spacer + large_height

        set_back: str; set_text: str
        [set_back, set_text] = window_controls.get_set_colours(selector_type, colour_pair)

        column_1: int = (2 * window_design.spacer)
        column_2: int = (6 * window_design.spacer) + width

        row_1: int = (4 * window_design.spacer) + small_height
        row_2: int = (5 * window_design.spacer) + (8 * (window_design.spacer + small_height)) + (window_design.spacer + large_height)

        match colour_pair:
            case "Window":
                x_value = column_1
                y_value = row_1
            case "Label":
                x_value = column_2
                y_value = row_1
            case "Button":
                x_value = column_1
                y_value = row_2
            case "Entry":
                x_value = column_2
                y_value = row_2

        window_colours_header: Label = Label(window_controls.colour_selector_page, text = f"Select {colour_pair} Colours:", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        window_colours_header.place(x = x_value, y = y_value, width = width, height = small_height)

        window_back_label: Label = Label(window_controls.colour_selector_page, text = "Select Background Colour:", bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, font = window_design.main_font)
        window_back_label.place(x = x_value, y = y_value + (1 * small_height_spacer), width = width, height = small_height)

        select_back = ttk.Combobox(window_controls.colour_selector_page)
        select_back['values'] = colour_name_list
        select_back.place(x = x_value, y = y_value + (2 * small_height_spacer) - window_design.spacer, width = width, height = small_height)

        window_text_label: Label = Label(window_controls.colour_selector_page, text = "Select Text Colour:", bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, font = window_design.main_font)
        window_text_label.place(x = x_value, y = y_value + (3 * small_height_spacer) - window_design.spacer, width = width, height = small_height)

        select_text = ttk.Combobox(window_controls.colour_selector_page)
        select_text['values'] = colour_name_list
        select_text.place(x = x_value, y = y_value + (4 * small_height_spacer) - (2 * window_design.spacer), width = width, height = small_height)

        window_colour_contrast = Label(window_controls.colour_selector_page, text = "Colour Contrast Ratio:\nN/A", bg = window_colours[1].colour_code, fg = window_colours[0].colour_code, font = window_design.main_font)
        window_colour_contrast.place(x = x_value, y = y_value + (5 * small_height_spacer), width = width, height = large_height)

        calculate_window_ratio: Button = Button(window_controls.colour_selector_page, text = "Calculate Contrast Ratio", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.set_contrast_ratio, colour_pair, window_colour_contrast))
        calculate_window_ratio.place(x = x_value, y = y_value + (5 * small_height_spacer) + large_height_spacer, width = width, height = small_height)

        invert_window_colours: Button = Button(window_controls.colour_selector_page, text = "Invert Colours", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.invert_colours, colour_pair))
        invert_window_colours.place(x = x_value, y = y_value + (6 * small_height_spacer) + large_height_spacer, width = width, height = small_height)

        match colour_pair:
            case "Window":
                window_controls.window_back = StringVar()
                window_controls.window_text = StringVar()

                select_back.configure(textvariable = window_controls.window_back)
                select_text.configure(textvariable = window_controls.window_text)

                window_controls.window_back.set(set_back)
                window_controls.window_text.set(set_text)
            case "Label":
                window_controls.label_back = StringVar()
                window_controls.label_text = StringVar()
                
                select_back.configure(textvariable = window_controls.label_back)
                select_text.configure(textvariable = window_controls.label_text)

                window_controls.label_back.set(set_back)
                window_controls.label_text.set(set_text)
            case "Button":
                window_controls.button_back = StringVar()
                window_controls.button_text = StringVar()
                
                select_back.configure(textvariable = window_controls.button_back)
                select_text.configure(textvariable = window_controls.button_text)

                window_controls.button_back.set(set_back)
                window_controls.button_text.set(set_text)
            case "Entry":
                window_controls.entry_back = StringVar()
                window_controls.entry_text = StringVar()
                
                select_back.configure(textvariable = window_controls.entry_back)
                select_text.configure(textvariable = window_controls.entry_text)

                window_controls.entry_back.set(set_back)
                window_controls.entry_text.set(set_text)

    def select_colours() -> None:
        window_controls.colour_selector_page.withdraw()

        window_colours: list[colour] = [common_data.get_colour_from_name(window_controls.window_back.get()), common_data.get_colour_from_name(window_controls.window_text.get())]
        label_colours: list[colour] = [common_data.get_colour_from_name(window_controls.label_back.get()), common_data.get_colour_from_name(window_controls.label_text.get())]
        button_colours: list[colour] = [common_data.get_colour_from_name(window_controls.button_back.get()), common_data.get_colour_from_name(window_controls.button_text.get())]
        entry_colours: list[colour] = [common_data.get_colour_from_name(window_controls.entry_back.get()), common_data.get_colour_from_name(window_controls.entry_text.get())]

        winlab_ratio: float = window_controls.get_contrast_ratio(window_colours[0].luminance, label_colours[0].luminance)
        winbut_ratio: float = window_controls.get_contrast_ratio(window_colours[0].luminance, button_colours[0].luminance)
        winent_ratio: float = window_controls.get_contrast_ratio(window_colours[0].luminance, entry_colours[0].luminance)

        winlab_ratio_str: str = f"Label Colours\n{winlab_ratio}:1"
        winbut_ratio_str: str = f"Button Colours\n{winbut_ratio}:1"
        winent_ratio_str: str = f"Entry Colours\n{winent_ratio}:1"

        if winlab_ratio < window_design.minimum_contrast_ratio:
            winlab_ratio_str += " !!"
        if winbut_ratio < window_design.minimum_contrast_ratio:
            winbut_ratio_str += " !!"
        if winent_ratio < window_design.minimum_contrast_ratio:
            winent_ratio_str += " !!"

        window_controls.window_colour_label.configure(bg = window_colours[0].colour_code)
        window_controls.window_text_label.configure(bg = window_colours[0].colour_code, fg = window_colours[1].colour_code)
        window_controls.label_colours_label.configure(text = winlab_ratio_str, bg = label_colours[0].colour_code, fg = label_colours[1].colour_code)
        window_controls.button_colours_label.configure(text = winbut_ratio_str, bg = button_colours[0].colour_code, fg = button_colours[1].colour_code)
        window_controls.entry_colours_label.configure(text = winent_ratio_str, bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code)


    # Main Page Functions

    def user_account_controller(last_frame: str) -> None:
        if len(window_controls.frame_sequence) > 1:
            window_controls.frame_sequence.remove(window_controls.frame_sequence[0])

        window_controls.frame_sequence.append("User Account")

        try:
            window_controls.withdraw_frame(window_controls.frame_sequence[0])
        except:
            pass

        if window_controls.user_account_page == None or not window_controls.user_account_page.winfo_exists():
            window_controls.make_user_account_page()
        else:
            window_controls.user_account_page.update()
            window_controls.user_account_page.deiconify()

    def make_user_account_page() -> None:
        window_controls.user_account_page = Toplevel(window_controls.window)

        window_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.window_colours)
        label_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.label_colours)
        button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)

        width: int = window_design.get_user_account_width()
        height: int = window_design.get_user_account_small_height()

        window_controls.user_account_page.geometry(window_controls.calculate_user_account_dimensions())
        window_controls.user_account_page.config(bg = window_colours[0].colour_code)

        column_1: int = (2 * window_design.spacer)
        column_2: int = (4 * window_design.spacer) + width

        row_1: int = (2 * window_design.spacer)
        row_2: int = (2 * window_design.spacer) + (1 * ((2 * window_design.spacer) + height))
        row_3: int = (2 * window_design.spacer) + (2 * ((2 * window_design.spacer) + height))
        row_4: int = (2 * window_design.spacer) + (3 * ((2 * window_design.spacer) + height))
        row_5: int = (2 * window_design.spacer) + (4 * ((2 * window_design.spacer) + height))
        row_6: int = (2 * window_design.spacer) + (5 * ((2 * window_design.spacer) + height))
        row_7: int = (2 * window_design.spacer) + (6 * ((2 * window_design.spacer) + height))

        current_user_header: Label = Label(window_controls.user_account_page, text = "Current User", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        current_user_header.place(x = column_1, y = row_1, width = width, height = height)

        current_user_label: Label = Label(window_controls.user_account_page, text = window_controls.current_user.username, bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        current_user_label.place(x = column_2, y = row_1, width = width, height = height)

        user_high_score_header: Label = Label(window_controls.user_account_page, text = "High Score", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        user_high_score_header.place(x = column_1, y = row_2, width = width, height = height)

        user_high_score_label: Label = Label(window_controls.user_account_page, text = window_controls.current_user.high_score, bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        user_high_score_label.place(x = column_2, y = row_2, width = width, height = height)

        play_quiz_button: Button = Button(window_controls.user_account_page, text = "Play Quiz", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.setup_quiz_controller)
        play_quiz_button.place(x = column_1, y = row_3, width = 2 * (width + window_design.spacer), height = height)
        
        edit_quiz_button: Button = Button(window_controls.user_account_page, text = "Edit Quiz", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.select_question_controller, "User Account"))
        edit_quiz_button.place(x = column_1, y = row_4, width = 2 * (width + window_design.spacer), height = height)

        edit_colours_button: Button = Button(window_controls.user_account_page, text = "Edit Colours", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.colour_editor_controller)
        edit_colours_button.place(x = column_1, y = row_5, width = width, height = height)

        edit_audio_button: Button = Button(window_controls.user_account_page, text = "Edit Audio", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.audio_editor_controller)
        edit_audio_button.place(x = column_2, y = row_5, width = width, height = height)

        view_account_button: Button = Button(window_controls.user_account_page, text = "View Account", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.view_account_controller)
        view_account_button.place(x = column_1, y = row_6, width = width, height = height)

        edit_account_button: Button = Button(window_controls.user_account_page, text = "Edit Account", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.edit_account)
        edit_account_button.place(x = column_2, y = row_6, width = width, height = height)

        logout_button: Button = Button(window_controls.user_account_page, text = "Logout", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.logout)
        logout_button.place(x = column_1, y = row_7, width = width, height = height)

        exit_button: Button = Button(window_controls.user_account_page, text = "Exit", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.kill_program)
        exit_button.place(x = column_2, y = row_7, width = width, height = height)


    # View Account Functions

    def view_account_controller() -> None:
        window_controls.frame_sequence.remove(window_controls.frame_sequence[0])
        window_controls.frame_sequence.append("View Account")

        try:
            window_controls.withdraw_frame(window_controls.frame_sequence[0])
        except:
            pass

        if window_controls.view_account_page == None or not window_controls.view_account_page.winfo_exists():
            window_controls.make_view_account_page()
        else:
            window_controls.clear_colour_selector()
            window_controls.view_account_page.update()
            window_controls.view_account_page.deiconify()

    def make_view_account_page() -> None:
        window_controls.view_account_page = Toplevel(window_controls.window)

        window_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.window_colours)
        label_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.label_colours)
        button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)

        width: int = window_design.get_view_account_width()
        small_height: int = window_design.get_view_account_small_height()

        listbox_height: int = window_design.get_view_account_listbox_item_height()
        listbox_visible: int = window_design.get_view_account_listbox_visible_items()

        window_controls.view_account_page.geometry(window_controls.calculate_view_account_dimensions())
        window_controls.view_account_page.config(bg = window_colours[0].colour_code)

        window_controls.high_score_label = Label(window_controls.view_account_page, text = f"High Score: {window_controls.current_user.high_score}", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        window_controls.high_score_label.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer), width = width, height = small_height)

        window_controls.average_score_label = Label(window_controls.view_account_page, text = f"Average Score: {window_controls.current_user.average_score}", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        window_controls.average_score_label.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer) + (1 * (window_design.spacer + small_height)), width = width, height = small_height)

        scores_listbox_height: int = listbox_height * listbox_visible
        scores_listbox_height_stratified: int = scores_listbox_height + (5 - (scores_listbox_height % 5))

        window_controls.previous_scores_listbox = Listbox(window_controls.view_account_page, font = window_design.main_font)
        window_controls.previous_scores_listbox.place(x = 2 * window_design.spacer, y = (2 * window_design.spacer) + (2 * (window_design.spacer + small_height)), width = width, height = scores_listbox_height)

        for i in range(len(window_controls.current_user.previous_scores)):
            window_controls.previous_scores_listbox.insert('end', f"{(i + 1)}: {window_controls.current_user.previous_scores[i]}")

        back_button: Button = Button(window_controls.view_account_page, text = "Back", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.go_back)
        back_button.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer) + (2 * (window_design.spacer + small_height)) + (window_design.spacer + scores_listbox_height_stratified), width = width, height = small_height)

        exit_button: Button = Button(window_controls.view_account_page, text = "Exit", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.kill_program)
        exit_button.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer) + (3 * (window_design.spacer + small_height)) + (window_design.spacer + scores_listbox_height_stratified), width = width, height = small_height)

    def edit_account() -> None:
        if window_controls.create_account_page != None:
            window_controls.create_account_page.destroy()

        window_controls.create_account_controller("Update User Colours")
        window_controls.insert_user_data()

    
    # Colour Editor Function

    def colour_editor_controller() -> None:
        window_controls.frame_sequence.remove(window_controls.frame_sequence[0])
        window_controls.frame_sequence.append("Colour Editor")

        try:
            window_controls.withdraw_frame(window_controls.frame_sequence[0])
        except:
            pass

        if window_controls.colour_editor_page == None or not window_controls.colour_editor_page.winfo_exists():
            window_controls.make_colour_editor_page()
        else:
            window_controls.clear_colour_selector()
            window_controls.colour_editor_page.update()
            window_controls.colour_editor_page.deiconify()

    def make_colour_editor_page() -> None:
        window_controls.colour_editor_page = Toplevel(window_controls.window)

        window_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.window_colours)
        label_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.label_colours)
        button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)
        entry_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.entry_colours)

        width: int = window_design.get_colour_editor_width()
        small_height: int = window_design.get_colour_editor_small_height()
        large_height: int = window_design.get_colour_editor_large_height()

        listbox_height: int = window_design.get_colour_editor_listbox_item_height()
        listbox_visible: int = window_design.get_colour_editor_listbox_visible_items()

        window_controls.colour_editor_page.geometry(window_controls.calculate_colour_editor_dimensions())
        window_controls.colour_editor_page.config(bg = window_colours[0].colour_code)

        colour_listbox_height: int = listbox_height * listbox_visible
        colour_listbox_height_stratified: int = colour_listbox_height + (5 - (colour_listbox_height % 5))

        window_controls.colour_listbox = Listbox(window_controls.colour_editor_page, font = window_design.main_font)
        window_controls.colour_listbox.place(x = 2 * window_design.spacer, y = 2 * window_design.spacer, width = width, height = colour_listbox_height)

        for colour_option in common_data.colour_list:
            window_controls.colour_listbox.insert('end', colour_option.colour_name)

        colour_name_label: Label = Label(window_controls.colour_editor_page, text = "Colour Name:", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        colour_name_label.place(x = (6 * window_design.spacer) + width, y = (2 * window_design.spacer), width = width, height = small_height)

        window_controls.colour_name = Entry(window_controls.colour_editor_page, bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        window_controls.colour_name.place(x = (6 * window_design.spacer) + width, y = (2 * window_design.spacer) + (1 * (window_design.spacer + small_height)), width = width, height = small_height)

        colour_code_label: Label = Label(window_controls.colour_editor_page, text = "Colour Code:", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        colour_code_label.place(x = (6 * window_design.spacer) + width, y = (3 * window_design.spacer) + (2 * (window_design.spacer + small_height)), width = width, height = small_height)

        window_controls.colour_code = Entry(window_controls.colour_editor_page, bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        window_controls.colour_code.place(x = (6 * window_design.spacer) + width, y = (3 * window_design.spacer) + (3 * (window_design.spacer + small_height)), width = width, height = small_height)

        colour_preview_border: Label = Label(window_controls.colour_editor_page, bg = label_colours[0].colour_code)
        colour_preview_border.place(x = (6 * window_design.spacer) + width, y = (5 * window_design.spacer) + (4 * (window_design.spacer + small_height)), width = width, height = large_height)

        window_controls.colour_preview = Label(window_controls.colour_editor_page, bg = window_colours[0].colour_code)
        window_controls.colour_preview.place(x = (7 * window_design.spacer) + width, y = (6 * window_design.spacer) + (4 * (window_design.spacer + small_height)), width = width - (2 * window_design.spacer), height = large_height - (2 * window_design.spacer))

        # Right Hand Buttons
        create_colour_button: Button = Button(window_controls.colour_editor_page, text = "Create Colour", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.create_colour)
        create_colour_button.place(x = (6 * window_design.spacer) + width, y = (6 * window_design.spacer) + (4 * (window_design.spacer + small_height)) + (window_design.spacer + large_height), width = width, height = small_height)

        update_colour_button: Button = Button(window_controls.colour_editor_page, text = "Update Colour", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.update_colour)
        update_colour_button.place(x = (6 * window_design.spacer) + width, y = (6 * window_design.spacer) + (5 * (window_design.spacer + small_height)) + (window_design.spacer + large_height), width = width, height = small_height)

        clear_button: Button = Button(window_controls.colour_editor_page, text = "Clear Colour", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.clear_colour_selector)
        clear_button.place(x = (6 * window_design.spacer) + width, y = (6 * window_design.spacer) + (6 * (window_design.spacer + small_height)) + (window_design.spacer + large_height), width = width, height = small_height)

        # Left Hand Buttons
        select_colour_button: Button = Button(window_controls.colour_editor_page, text = "Select Colour", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.select_colour)
        select_colour_button.place(x = 2 * window_design.spacer, y = (4 * window_design.spacer) + (colour_listbox_height_stratified), width = width, height = small_height)

        delete_colour_button: Button = Button(window_controls.colour_editor_page, text = "Delete Colour", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.delete_colour)
        delete_colour_button.place(x = 2 * window_design.spacer, y = (4 * window_design.spacer) + (colour_listbox_height_stratified) + (1 * (window_design.spacer + small_height)), width = width, height = small_height)

        back_button: Button = Button(window_controls.colour_editor_page, text = "Back", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.go_back)
        back_button.place(x = 2 * window_design.spacer, y = (4 * window_design.spacer) + (colour_listbox_height_stratified) + (2 * (window_design.spacer + small_height)), width = width, height = small_height)

        exit_button: Button = Button(window_controls.colour_editor_page, text = "Exit", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.kill_program)
        exit_button.place(x = 2 * window_design.spacer, y = (4 * window_design.spacer) + (colour_listbox_height_stratified) + (3 * (window_design.spacer + small_height)), width = width, height = small_height)

    def select_colour() -> None:
        window_controls.selected_colour = common_data.colour_list[window_controls.colour_listbox.curselection()[0]]

        window_controls.clear_colour_selector()

        window_controls.colour_name.insert(0, window_controls.selected_colour.colour_name)
        window_controls.colour_code.insert(0, window_controls.selected_colour.colour_code)
        window_controls.colour_preview.configure(bg = window_controls.selected_colour.colour_code)


    # Audio Editor Functions

    def audio_editor_controller() -> None:
        window_controls.frame_sequence.remove(window_controls.frame_sequence[0])
        window_controls.frame_sequence.append("Audio Editor")

        try:
            window_controls.withdraw_frame(window_controls.frame_sequence[0])
        except:
            pass

        if window_controls.audio_editor_page == None or not window_controls.audio_editor_page.winfo_exists():
            window_controls.make_audio_editor_page()
        else:
            window_controls.clear_audio_selector()
            window_controls.audio_editor_page.update()
            window_controls.audio_editor_page.deiconify()

    def make_audio_editor_page() -> None:
        window_controls.audio_editor_page = Toplevel(window_controls.window)

        window_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.window_colours)
        label_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.label_colours)
        button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)
        entry_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.entry_colours)

        width: int = window_design.get_audio_editor_width()
        small_height: int = window_design.get_audio_editor_small_height()
#        large_height: int = window_design.get_audio_editor_large_height()

        listbox_height: int = window_design.get_audio_editor_listbox_item_height()
        listbox_visible: int = window_design.get_audio_editor_listbox_visible_items()

        window_controls.audio_editor_page.geometry(window_controls.calculate_audio_editor_dimensions())
        window_controls.audio_editor_page.config(bg = window_colours[0].colour_code)

        audio_listbox_height: int = listbox_height * listbox_visible
        audio_listbox_height_stratified: int = audio_listbox_height + (5 - (audio_listbox_height % 5))

        window_controls.audio_listbox = Listbox(window_controls.audio_editor_page, font = window_design.main_font)
        window_controls.audio_listbox.place(x = 2 * window_design.spacer, y = 2 * window_design.spacer, width = width, height = audio_listbox_height_stratified)

        for audio_option in common_data.audio_list:
            window_controls.audio_listbox.insert('end', audio_option.audio_name)

        audio_name_label: Label = Label(window_controls.audio_editor_page, text = "Audio Name:", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        audio_name_label.place(x = (6 * window_design.spacer) + width, y = (2 * window_design.spacer), width = width, height = small_height)

        window_controls.audio_name = Entry(window_controls.audio_editor_page, bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        window_controls.audio_name.place(x = (6 * window_design.spacer) + width, y = (2 * window_design.spacer) + (1 * (window_design.spacer + small_height)), width = width, height = small_height)

        audio_file_label: Label = Label(window_controls.audio_editor_page, text = "Audio File:", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        audio_file_label.place(x = (6 * window_design.spacer) + width, y = (3 * window_design.spacer) + (2 * (window_design.spacer + small_height)), width = width, height = small_height)

        window_controls.audio_file = Entry(window_controls.audio_editor_page, bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        window_controls.audio_file.place(x = (6 * window_design.spacer) + width, y = (3 * window_design.spacer) + (3 * (window_design.spacer + small_height)), width = width, height = small_height)

        # Preview Audio Button
        preview_audio: Button = Button(window_controls.audio_editor_page, text = "Preview Audio", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.play_audio)
        preview_audio.place(x = (6 * window_design.spacer) + width, y = (4 * window_design.spacer) + (audio_listbox_height_stratified), width = width, height = small_height)

        # Right Hand Buttons
        create_audio_button: Button = Button(window_controls.audio_editor_page, text = "Create Audio", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.create_audio)
        create_audio_button.place(x = (6 * window_design.spacer) + width, y = (4 * window_design.spacer) + (audio_listbox_height_stratified) + (1 * (window_design.spacer + small_height)), width = width, height = small_height)

        update_audio_button: Button = Button(window_controls.audio_editor_page, text = "Update Audio", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.update_audio)
        update_audio_button.place(x = (6 * window_design.spacer) + width, y = (4 * window_design.spacer) + (audio_listbox_height_stratified) + (2 * (window_design.spacer + small_height)), width = width, height = small_height)

        clear_button: Button = Button(window_controls.audio_editor_page, text = "Clear Audio", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.clear_audio_selector)
        clear_button.place(x = (6 * window_design.spacer) + width, y = (4 * window_design.spacer) + (audio_listbox_height_stratified) + (3 * (window_design.spacer + small_height)), width = width, height = small_height)

        # Left Hand Buttons
        select_audio_button: Button = Button(window_controls.audio_editor_page, text = "Select Audio", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.select_audio)
        select_audio_button.place(x = 2 * window_design.spacer, y = (4 * window_design.spacer) + (audio_listbox_height_stratified), width = width, height = small_height)

        delete_audio_button: Button = Button(window_controls.audio_editor_page, text = "Delete Audio", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.delete_audio)
        delete_audio_button.place(x = 2 * window_design.spacer, y = (4 * window_design.spacer) + (audio_listbox_height_stratified) + (1 * (window_design.spacer + small_height)), width = width, height = small_height)

        back_button: Button = Button(window_controls.audio_editor_page, text = "Back", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.go_back)
        back_button.place(x = 2 * window_design.spacer, y = (4 * window_design.spacer) + (audio_listbox_height_stratified) + (2 * (window_design.spacer + small_height)), width = width, height = small_height)

        exit_button: Button = Button(window_controls.audio_editor_page, text = "Exit", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.kill_program)
        exit_button.place(x = 2 * window_design.spacer, y = (4 * window_design.spacer) + (audio_listbox_height_stratified) + (3 * (window_design.spacer + small_height)), width = width, height = small_height)

    def select_audio() -> None:
        window_controls.selected_audio = common_data.audio_list[window_controls.audio_listbox.curselection()[0]]

        window_controls.clear_audio_selector()

        window_controls.audio_name.insert(0, window_controls.selected_audio.audio_name)
        window_controls.audio_file.insert(0, window_controls.selected_audio.audio_file)


    # Question Editor Functions

    def select_question_controller(last_frame: str) -> None:
        if last_frame != "Edit Question":
            window_controls.frame_sequence.remove(window_controls.frame_sequence[0])
            window_controls.frame_sequence.append("Question Editor")

        try:
            window_controls.withdraw_frame(window_controls.frame_sequence[0])
        except:
            pass

        if window_controls.question_list_page == None or not window_controls.question_list_page.winfo_exists():
            window_controls.make_select_question_page()
        else:
            window_controls.clear_question_selector()
            window_controls.question_list_page.update()
            window_controls.question_list_page.deiconify()

    def make_select_question_page() -> None:
        window_controls.question_list_page = Toplevel(window_controls.window)

        window_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.window_colours)
        button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)
        
        width: int = window_design.get_question_list_width()
        button_width: int = window_design.get_question_list_button_width()
        small_height: int = window_design.get_question_list_small_height()

        window_controls.question_list_page.geometry(window_controls.calculate_select_question_dimensions())
        window_controls.question_list_page.config(bg = window_colours[0].colour_code)

        unit: int = (window_design.spacer + small_height)

        window_controls.question_listbox = Listbox(window_controls.question_list_page, font = window_design.main_font)
        window_controls.question_listbox.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer), width = width, height = (5 * unit) - window_design.spacer)

        load_usable_questions: Button = Button(window_controls.question_list_page, text = "Load Usable Questions", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.load_question_list, "Usable"))
        load_usable_questions.place(x = (6 * window_design.spacer) + width, y = (2 * window_design.spacer), width = button_width, height = small_height)

        load_discarded_questions: Button = Button(window_controls.question_list_page, text = "Load Discarded Questions", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.load_question_list, "Discarded"))
        load_discarded_questions.place(x = (6 * window_design.spacer) + width, y = (2 * window_design.spacer) + (1 * unit), width = button_width, height = small_height)

        create_question: Button = Button(window_controls.question_list_page, text = "Create Question", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.edit_question_controller, "Question Editor"))
        create_question.place(x = (6 * window_design.spacer) + width, y = (2 * window_design.spacer) + (2 * unit), width = button_width, height = small_height)

        select_question: Button = Button(window_controls.question_list_page, text = "Edit Question", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.edit_question)
        select_question.place(x = (6 * window_design.spacer) + width, y = (2 * window_design.spacer) + (3 * unit), width = button_width, height = small_height)

        window_controls.delete_question = Button(window_controls.question_list_page, text = "Discard Question", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font)
        window_controls.delete_question.place(x = (6 * window_design.spacer) + width, y = (2 * window_design.spacer) + (4 * unit), width = button_width, height = small_height)

        back_button: Button = Button(window_controls.question_list_page, text = "Back", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.go_back)
        back_button.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer) + (5 * unit), width = width, height = small_height)

        exit_button: Button = Button(window_controls.question_list_page, text = "Exit", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.kill_program)
        exit_button.place(x = (6 * window_design.spacer) + width, y = (2 * window_design.spacer) + (5 * unit), width = button_width, height = small_height)

    def load_question_list(list_option: str) -> None:
        match list_option:
            case "Usable":
                window_controls.current_question_list = common_data.usable_question_list
                window_controls.delete_question.configure(text = "Discard Question", command = window_controls.discard_question)
            case "Discarded":
                window_controls.current_question_list = common_data.discarded_question_list
                window_controls.delete_question.configure(text = "Restore Question", command = window_controls.reinstate_question)
                
        window_controls.selected_question_list = list_option

        window_controls.question_listbox.delete(0, END)

        for question_option in window_controls.current_question_list:
            window_controls.question_listbox.insert('end', f"QD{question_option.question_difficulty} - {question_option.question_id}")

    def edit_question() -> None:
        window_controls.edit_question_controller("Question Editor")
        window_controls.insert_question_data()

    def edit_question_controller(last_frame: str) -> None:
        match last_frame:
            case "Question Editor":
                try:
                    window_controls.withdraw_frame(window_controls.frame_sequence[1])
                except:
                    pass

                if window_controls.create_question_page == None or not window_controls.create_question_page.winfo_exists():
                    window_controls.make_create_question_page()
                else:
                    window_controls.clear_question_editor()
                    window_controls.create_question_page.update()
                    window_controls.create_question_page.deiconify()

            case "Edit Question":
                window_controls.create_question_page.withdraw()
                window_controls.select_question_controller(last_frame)

    def make_create_question_page() -> None:
        window_controls.create_question_page = Toplevel(window_controls.window)

        window_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.window_colours)
        label_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.label_colours)
        button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)
        entry_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.entry_colours)
        
        width: int = window_design.get_question_editor_width()
        small_height: int = window_design.get_question_editor_small_height()
        large_height: int = window_design.get_question_editor_large_height()

        window_controls.create_question_page.geometry(window_controls.calculate_edit_question_dimensions())
        window_controls.create_question_page.config(bg = window_colours[0].colour_code)

        unit: int = (window_design.spacer) + small_height

        question_text_label: Label = Label(window_controls.create_question_page, text = "Enter Question", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        question_text_label.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer), width = (4 * window_design.spacer) + (2 * width), height = small_height)
        
        window_controls.enter_question_text = Entry(window_controls.create_question_page, bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        window_controls.enter_question_text.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer) + (1 * unit), width = (4 * window_design.spacer) + (2 * width), height = small_height)


        # Question Difficulty + Points Entry

        window_controls.question_difficulty = StringVar()
        window_controls.correct_answer = StringVar()

        question_difficulty_header: Label = Label(window_controls.create_question_page, text = "Question Difficulty", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        question_difficulty_header.place(x = (2 * window_design.spacer), y = (3 * window_design.spacer) + (2 * unit), width = width, height = small_height)

        question_difficulty_entry: ttk.Combobox = ttk.Combobox(window_controls.create_question_page, textvariable = window_controls.question_difficulty)
        question_difficulty_entry['values'] = quiz_handler.difficulty_range
        question_difficulty_entry.place(x = (2 * window_design.spacer), y = (3 * window_design.spacer) + (3 * unit), width = width, height = small_height)

        correct_answer_header: Label = Label(window_controls.create_question_page, text = "Correct Answer", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        correct_answer_header.place(x = (6 * window_design.spacer) + width, y = (3 * window_design.spacer) + (2 * unit), width = width, height = small_height)

        correct_answer_entry: ttk.Combobox = ttk.Combobox(window_controls.create_question_page, textvariable = window_controls.correct_answer)
        correct_answer_entry['values'] = quiz_handler.correct_answers
        correct_answer_entry.place(x = (6 * window_design.spacer) + width, y = (3 * window_design.spacer) + (3 * unit), width = width, height = small_height)

        for i in range(4):
            window_controls.place_answer_input(i)
            window_controls.answer_colours.append([StringVar(), StringVar()])


        # Hint and Fun Fact Entry (Single Width because this is quite tall)

        hint_y_value: int = (6 * window_design.spacer) + (10 * unit) + (2 * (window_design.spacer + large_height))

        fun_fact_header: Label = Label(window_controls.create_question_page, text = "Enter Fun Fact", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        fun_fact_header.place(x = (2 * window_design.spacer), y = hint_y_value, width = width, height = small_height)

        window_controls.enter_fun_fact = Entry(window_controls.create_question_page, bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        window_controls.enter_fun_fact.place(x = (2 * window_design.spacer), y = hint_y_value + unit, width = width, height = small_height)

        hint_header: Label = Label(window_controls.create_question_page, text = "Enter Question Hint", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        hint_header.place(x = (6 * window_design.spacer) + width, y = hint_y_value, width = width, height = small_height)

        window_controls.enter_hint = Entry(window_controls.create_question_page, bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        window_controls.enter_hint.place(x = (6 * window_design.spacer) + width, y = hint_y_value + unit, width = width, height = small_height)


        # Question Correct / Incorrect Audio Selection

        audio_y_value: int = hint_y_value + window_design.spacer + (2 * unit)

        window_controls.correct_audio = StringVar()
        window_controls.incorrect_audio = StringVar()

        audio_name_list: list[str] = []

        for audio_option in common_data.audio_list:
            audio_name_list.append(audio_option.audio_name)

        correct_audio_header: Label = Label(window_controls.create_question_page, text = "Correct Answer Audio", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        correct_audio_header.place(x = (2 * window_design.spacer), y = audio_y_value, width = width, height = small_height)

        correct_audio_entry: ttk.Combobox = ttk.Combobox(window_controls.create_question_page, textvariable = window_controls.correct_audio)
        correct_audio_entry['values'] = audio_name_list
        correct_audio_entry.place(x = (2 * window_design.spacer), y = audio_y_value + unit, width = width, height = small_height)

        incorrect_audio_header: Label = Label(window_controls.create_question_page, text = "Incorrect Answer Audio", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        incorrect_audio_header.place(x = (6 * window_design.spacer) + width, y = audio_y_value, width = width, height = small_height)

        incorrect_audio_entry: ttk.Combobox = ttk.Combobox(window_controls.create_question_page, textvariable = window_controls.incorrect_audio)
        incorrect_audio_entry['values'] = audio_name_list
        incorrect_audio_entry.place(x = (6 * window_design.spacer) + width, y = audio_y_value + unit, width = width, height = small_height)


        # Control Buttons

        control_y_value: int = audio_y_value + window_design.spacer + (2 * unit)

        window_controls.create_question_button = Button(window_controls.create_question_page, text = "Create Question", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.create_question)
        window_controls.create_question_button.place(x = (2 * window_design.spacer), y = control_y_value, width = (4 * window_design.spacer) + (2 * width), height = small_height)

        preview_question_button = Button(window_controls.create_question_page, text = "Preview Question", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font)#, command = window_controls.preview_question)
        preview_question_button.place(x = (2 * window_design.spacer), y = control_y_value + unit, width = (4 * window_design.spacer) + (2 * width), height = small_height)

        back_button: Button = Button(window_controls.create_question_page, text = "Back", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.edit_question_controller, "Edit Question"))
        back_button.place(x = (2 * window_design.spacer), y = control_y_value + (window_design.spacer + (2 * unit)), width = width, height = small_height)

        exit_button: Button = Button(window_controls.create_question_page, text = "Exit", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.kill_program)
        exit_button.place(x = (6 * window_design.spacer) + width, y = control_y_value + (window_design.spacer + (2 * unit)), width = width, height = small_height)

    def place_answer_input(answer_number: int) -> None:
        window_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.window_colours)
        label_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.label_colours)
        button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)
        entry_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.entry_colours)
        
        width: int = window_design.get_question_editor_width()
        small_height: int = window_design.get_question_editor_small_height()
        large_height: int = window_design.get_question_editor_large_height()

        row: int
        column: int

        unit: int = (window_design.spacer + small_height)

        r1: int = (4 * window_design.spacer) + (4 * unit)
        r2: int = (5 * window_design.spacer) + (7 * unit) + (window_design.spacer + large_height)

        c1: int = (2 * window_design.spacer)
        c2: int = (6 * window_design.spacer) + width

        match answer_number + 1:
            case 1:
                row = r1
                column = c1
            case 2:
                row = r1
                column = c2
            case 3:
                row = r2
                column = c1
            case 4:
                row = r2
                column = c2

        enter_answer_label: Label = Label(window_controls.create_question_page, text = f"Enter Answer {answer_number + 1}", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        enter_answer_label.place(x = column, y = row, width = width, height = small_height)

        placed_entry: Entry = Entry(window_controls.create_question_page, bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        placed_entry.place(x = column, y = row + (1 * unit), width = width, height = small_height)

        placed_contrast: Label = Label(window_controls.create_question_page, text = "Colour Preview", bg = window_colours[1].colour_code, fg = window_colours[0].colour_code, font = window_design.main_font)
        placed_contrast.place(x = column, y = row + (2 * unit), width = width, height = large_height)

        select_colours_button: Button = Button(window_controls.create_question_page, text = "Choose Colours", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.select_answer_colours, answer_number))
        select_colours_button.place(x = column, y = row + (2 * unit) + (window_design.spacer + large_height), width = width, height = small_height)

        window_controls.answer_details.append([placed_entry, placed_contrast])

    def select_question() -> None:
        if len(window_controls.question_listbox.curselection()) > 0:
            window_controls.selected_question = window_controls.current_question_list[window_controls.question_listbox.curselection()[0]]
        else:
            messagebox.showwarning("No Question Selected", "Please Select a Question")

    def insert_question_data() -> None:
        window_controls.clear_question_editor()

        print(len(window_controls.question_listbox.curselection()))

        if len(window_controls.question_listbox.curselection()) == 0:
            messagebox.showwarning("No Question Selected", "Please Select a Question")
        else:
            window_controls.selected_question = window_controls.current_question_list[window_controls.question_listbox.curselection()[0]]

            window_controls.enter_question_text.insert(0, window_controls.selected_question.question_text)

            window_controls.question_difficulty.set(window_controls.selected_question.question_difficulty)

            for i in range(4):
                answer_colours: list[colour] = window_controls.convert_to_colours(window_controls.selected_question.answer_options[i].answer_colours)
                window_back: colour = common_data.get_colour_from_name(window_controls.current_user.window_colours[0])

                window_controls.answer_details[i][0].insert(0, window_controls.selected_question.answer_options[i].answer_text)
                window_controls.answer_details[i][1].configure(text = f"Win-Ans Contrast Ratio:\n{window_controls.get_contrast_ratio(window_back.luminance, answer_colours[0].luminance)}", bg = answer_colours[0].colour_code, fg = answer_colours[1].colour_code)

                for j in range(2):
                    window_controls.answer_colours[i][j].set(answer_colours[j].colour_name)

                if bool(window_controls.selected_question.answer_options[i].correct_answer):
                    window_controls.correct_answer.set(str(i + 1))

            window_controls.enter_fun_fact.insert(0, window_controls.selected_question.fun_fact)
            window_controls.enter_hint.insert(0, window_controls.selected_question.hint)

            window_controls.correct_audio.set(window_controls.selected_question.correct_audio)
            window_controls.incorrect_audio.set(window_controls.selected_question.incorrect_audio)

            window_controls.create_question_button.configure(text = "Update Question", command = window_controls.update_question)


    # Question Editor Colour Handling

    def select_answer_colours(answer_index: int) -> None:
        window_controls.select_question_colours_page = Toplevel(window_controls.window)

        colour_name_list: list[str] = []

        for colour_option in common_data.get_colour_list():
            colour_name_list.append(colour_option.colour_name)

        colour_name_list.remove(window_design.correct_answer_colours[0].colour_name)
        colour_name_list.remove(window_design.incorrect_answer_colours[0].colour_name)
        #colour_name_list.remove(window_design.double_wrong_answer_colours[0].colour_name)

        window_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.window_colours)
        label_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.label_colours)
        button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)

        window_controls.select_question_colours_page.geometry(window_controls.calculate_select_answer_colour_dimensions())
        window_controls.select_question_colours_page.configure(bg = window_colours[0].colour_code)

        width: int = window_design.get_choose_colours_width()
        small_height: int = window_design.get_choose_colours_small_height()
        large_height: int = window_design.get_choose_colours_large_height()

        x_value: int = (2 * window_design.spacer)
        y_value: int = (2 * window_design.spacer)

        small_height_spacer: int = window_design.spacer + small_height
        large_height_spacer: int = window_design.spacer + large_height

        window_colours_header: Label = Label(window_controls.select_question_colours_page, text = f"Select Question {answer_index + 1} Colours:", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        window_colours_header.place(x = x_value, y = y_value, width = width, height = small_height)

        window_back_label: Label = Label(window_controls.select_question_colours_page, text = "Select Background Colour:", bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, font = window_design.main_font)
        window_back_label.place(x = x_value, y = y_value + (1 * small_height_spacer), width = width, height = small_height)

        select_back = ttk.Combobox(window_controls.select_question_colours_page, textvariable = window_controls.answer_colours[answer_index][0])
        select_back['values'] = colour_name_list
        select_back.place(x = x_value, y = y_value + (2 * small_height_spacer) - window_design.spacer, width = width, height = small_height)

        window_text_label: Label = Label(window_controls.select_question_colours_page, text = "Select Text Colour:", bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, font = window_design.main_font)
        window_text_label.place(x = x_value, y = y_value + (3 * small_height_spacer) - window_design.spacer, width = width, height = small_height)

        select_text = ttk.Combobox(window_controls.select_question_colours_page, textvariable = window_controls.answer_colours[answer_index][1])
        select_text['values'] = colour_name_list
        select_text.place(x = x_value, y = y_value + (4 * small_height_spacer) - (2 * window_design.spacer), width = width, height = small_height)

        window_colour_contrast = Label(window_controls.select_question_colours_page, text = "Colour Contrast Ratio:\nN/A", bg = window_colours[1].colour_code, fg = window_colours[0].colour_code, font = window_design.main_font)
        window_colour_contrast.place(x = x_value, y = y_value + (5 * small_height_spacer), width = width, height = large_height)

        calculate_window_ratio: Button = Button(window_controls.select_question_colours_page, text = "Calculate Contrast Ratio", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.set_answer_contrast_ratio, answer_index, window_colour_contrast))
        calculate_window_ratio.place(x = x_value, y = y_value + (5 * small_height_spacer) + large_height_spacer, width = width, height = small_height)

        invert_window_colours: Button = Button(window_controls.select_question_colours_page, text = "Invert Colours", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.invert_answer_colours, answer_index))
        invert_window_colours.place(x = x_value, y = y_value + (6 * small_height_spacer) + large_height_spacer, width = width, height = small_height)

        select_colours: Button = Button(window_controls.select_question_colours_page, text = "Select Colours", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.set_answer_colours, answer_index))
        select_colours.place(x = x_value, y = y_value + (7 * small_height_spacer) + large_height_spacer, width = width, height = small_height)

    def set_answer_contrast_ratio(answer_index: int, ratio_label: Label) -> None:
        back_colour: colour = common_data.get_colour_from_name(window_controls.answer_colours[answer_index][0].get())
        text_colour: colour = common_data.get_colour_from_name(window_controls.answer_colours[answer_index][1].get())

        ratio_label.configure(text = f"Colour Contrast Ratio:\n{window_controls.get_contrast_ratio(back_colour.luminance, text_colour.luminance)}", bg = back_colour.colour_code, fg = text_colour.colour_code)

    def invert_answer_colours(answer_index: int) -> None:
        temp: str = window_controls.answer_colours[answer_index][0].get()
        window_controls.answer_colours[answer_index][0].set(window_controls.answer_colours[answer_index][1].get())
        window_controls.answer_colours[answer_index][1].set(temp)

    def set_answer_colours(answer_index: int) -> None:
        window_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.window_colours)

        back_colour: colour = common_data.get_colour_from_name(window_controls.answer_colours[answer_index][0].get())
        text_colour: colour = common_data.get_colour_from_name(window_controls.answer_colours[answer_index][1].get())

        if back_colour.colour_name == "NULL COLOUR" or text_colour.colour_name == "NULL COLOUR":
            messagebox.showwarning("No Colours Selected", "Please Select a Colour Pairing")
        else:
            window_controls.answer_details[answer_index][1].configure(text = f"Win-Ans Contrast Ratio:\n{window_controls.get_contrast_ratio(window_colours[0].luminance, back_colour.luminance)}", bg = back_colour.colour_code, fg = text_colour.colour_code)
            window_controls.select_question_colours_page.destroy()


    # Quiz Setup Functions

    def setup_quiz_controller() -> None:
        window_controls.frame_sequence.remove(window_controls.frame_sequence[0])
        window_controls.frame_sequence.append("Setup Quiz")

        try:
            window_controls.withdraw_frame(window_controls.frame_sequence[0])
        except:
            pass

        if window_controls.setup_quiz_page == None or not window_controls.setup_quiz_page.winfo_exists():
            window_controls.make_setup_quiz_page()
        else:
            #window_controls.clear_setup_quiz_page()
            window_controls.setup_quiz_page.update()
            window_controls.setup_quiz_page.deiconify()

    def make_setup_quiz_page() -> None:
        window_controls.setup_quiz_page = Toplevel(window_controls.window)

        window_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.window_colours)
        label_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.label_colours)
        button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)
        
        width: int = window_design.get_setup_quiz_width()
        small_height: int = window_design.get_setup_quiz_small_height()

        window_controls.setup_quiz_page.geometry(window_controls.calculate_setup_quiz_dimensions())
        window_controls.setup_quiz_page.config(bg = window_colours[0].colour_code)

        select_difficulty_label: Label = Label(window_controls.setup_quiz_page, text = "Select Difficulty", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        select_difficulty_label.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer), width = width, height = small_height)

        for i in range(len(quiz_handler.difficulty_range)):
            difficulty_button: Button = Button(window_controls.setup_quiz_page, text = quiz_handler.difficulty_range[i], bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font)
            difficulty_button.configure(command = functools.partial(window_controls.select_difficulty, difficulty_button))
            difficulty_button.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer) + ((i + 1) * (window_design.spacer + small_height)), width = width, height = small_height)

            window_controls.difficulty_buttons.append(difficulty_button)

        difficulty_button: Button = Button(window_controls.setup_quiz_page, text = "Mixed", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font)
        difficulty_button.configure(command = functools.partial(window_controls.select_difficulty, difficulty_button))
        difficulty_button.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer) + ((len(quiz_handler.difficulty_range) + 1) * (window_design.spacer + small_height)), width = width, height = small_height)
        window_controls.difficulty_buttons.append(difficulty_button)

        select_length_label: Label = Label(window_controls.setup_quiz_page, text = "Select Quiz Length", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        select_length_label.place(x = (6 * window_design.spacer) + width, y = (2 * window_design.spacer), width = width, height = small_height)

        for i in range(len(quiz_handler.quiz_lengths)):
            length_button: Button = Button(window_controls.setup_quiz_page, text = f"{quiz_handler.length_options[i]} - {quiz_handler.quiz_lengths[i]} Questions", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font)
            length_button.configure(command = functools.partial(window_controls.select_quiz_length, quiz_handler.length_options[i], length_button))
            length_button.place(x = (6 * window_design.spacer) + width, y = (2 * window_design.spacer) + ((i + 1) * (window_design.spacer + small_height)), width = width, height = small_height)

            window_controls.quiz_length_buttons.append(length_button)

        length_button: Button = Button(window_controls.setup_quiz_page, text = "Custom", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font)
        length_button.configure(command = functools.partial(window_controls.select_quiz_length, "Custom", length_button))
        length_button.place(x = (6 * window_design.spacer) + width, y = (2 * window_design.spacer) + ((len(quiz_handler.quiz_lengths) + 1) * (window_design.spacer + small_height)), width = width, height = small_height)
        window_controls.quiz_length_buttons.append(length_button)

        start_quiz_button: Button = Button(window_controls.setup_quiz_page, text = "Start Quiz", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.start_quiz)
        start_quiz_button.place(x = (2 * window_design.spacer), y = (3 * window_design.spacer) + ((len(quiz_handler.quiz_lengths) + 2) * (window_design.spacer + small_height)), width = (4 * window_design.spacer) + (2 * width), height = small_height)

        back_button: Button = Button(window_controls.setup_quiz_page, text = "Back", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.go_back)
        back_button.place(x = (2 * window_design.spacer), y = (3 * window_design.spacer) + ((len(quiz_handler.quiz_lengths) + 3) * (window_design.spacer + small_height)), width = width, height = small_height)

        exit_button: Button = Button(window_controls.setup_quiz_page, text = "Exit", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.kill_program)
        exit_button.place(x = (6 * window_design.spacer) + width, y = (3 * window_design.spacer) + ((len(quiz_handler.quiz_lengths) + 3) * (window_design.spacer + small_height)), width = width, height = small_height)

    def select_difficulty(selected_button: Button) -> None:
        quiz_handler.quiz_difficulty = selected_button.cget('text')

        button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)

        window_controls.reset_buttons(window_controls.difficulty_buttons)
        selected_button.configure(bg = button_colours[1].colour_code, fg = button_colours[0].colour_code)
    
    def select_quiz_length(chosen_length: str, selected_button: Button) -> None:
        if chosen_length == "Custom":
            button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)

            window_controls.reset_buttons(window_controls.quiz_length_buttons)
            selected_button.configure(bg = button_colours[1].colour_code, fg = button_colours[0].colour_code)

            window_controls.get_custom_quiz_length()
        else:
            desired_length: int

            match chosen_length:
                case "Short":
                    desired_length = quiz_handler.quiz_lengths[0]
                case "Medium":
                    desired_length = quiz_handler.quiz_lengths[1]
                case "Long":
                    desired_length = quiz_handler.quiz_lengths[2]
            
            if quiz_handler.valid_length(desired_length):
                quiz_handler.quiz_length = desired_length

                button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)

                window_controls.reset_buttons(window_controls.quiz_length_buttons)
                selected_button.configure(bg = button_colours[1].colour_code, fg = button_colours[0].colour_code)

    def reset_buttons(button_list: list[Button]) -> None:
        button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)

        for button in button_list:
            button.configure(bg = button_colours[0].colour_code, fg = button_colours[1].colour_code)

    def get_custom_quiz_length() -> int:
        if window_controls.set_length_window == None or not window_controls.set_length_window.winfo_exists():
            window_controls.set_length_window = Toplevel(window_controls.window)
        else:
            window_controls.set_length_window.destroy()
            window_controls.set_length_window = Toplevel(window_controls.window)

        window_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.window_colours)
        label_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.label_colours)
        button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)
        
        width: int = window_design.get_setup_quiz_width()
        small_height: int = window_design.get_setup_quiz_small_height()

        window_controls.set_length_window.geometry(window_controls.calculate_select_length_dimensions())
        window_controls.set_length_window.config(bg = window_colours[0].colour_code)

        header_label: Label = Label(window_controls.set_length_window, text = "Select Quiz Length", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        header_label.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer), width = width, height = small_height)

        window_controls.quiz_length = DoubleVar()
        length_selector: Scale = Scale(window_controls.set_length_window, variable = window_controls.quiz_length, from_ = 1, to = len(quiz_handler.get_questions()), orient = HORIZONTAL, bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, borderwidth = 0, highlightthickness = 0)
        length_selector.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer) + (1 * (window_design.spacer + small_height)), width = width, height = (2 * small_height) - window_design.spacer)

        set_length_button: Button = Button(window_controls.set_length_window, text = "Set Quiz Length", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.set_custom_length)
        set_length_button.place(x = (2 * window_design.spacer), y = (0 * window_design.spacer) + (3 * (window_design.spacer + small_height)), width = width, height = small_height)


    def set_custom_length() -> None:
        quiz_handler.quiz_length = int(window_controls.quiz_length.get())
        window_controls.quiz_length_buttons[3].configure(text = f"Custom - {int(window_controls.quiz_length.get())} Questions")
        window_controls.set_length_window.destroy()

    def start_quiz() -> None:
        if not (quiz_handler.quiz_length == None and quiz_handler.quiz_difficulty == None):
            quiz_handler.generate_quiz()
            window_controls.display_question_controller(1)
        else:
            messagebox.showwarning("Items not Selected", "Please Select a Quiz Difficulty and/or Quiz Length to Continue")
            invasion_frame: Toplevel = Toplevel(window_controls.window)
            invasion_frame.withdraw()
            invade_poland(invasion_frame)


    # Complete Quiz Functions

    def display_question_controller(question_number: int) -> None:
        #print(f"{question_number} - {quiz_handler.question_number}")
        #window_controls.setup_quiz_page.deiconify()

        window_controls.attempts_at_question = 0
        window_controls.current_selected_answer = None

        if window_controls.main_quiz_page != None and window_controls.main_quiz_page.winfo_exists():
            window_controls.main_quiz_page.destroy()

        if question_number == quiz_handler.question_number:
            window_controls.make_view_question_page(question_number)
        elif question_number < quiz_handler.question_number:
            window_controls.make_review_question_page(question_number)

    def make_view_question_page(question_number: int) -> None:
        window_controls.main_quiz_page = window_controls.make_question_page_template(question_number)
        window_controls.main_quiz_page.geometry(window_controls.calculate_view_question_dimensions())
        
        window_controls.main_quiz_page.update()
        window_controls.main_quiz_page.deiconify()
        
        button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)
        
        width: int = window_design.get_question_page_width()
        small_height: int = window_design.get_question_page_small_height()
        large_height: int = window_design.get_question_page_large_height()

        start_height: int = (4 * window_design.spacer) + (1 * (window_design.spacer + small_height)) + ((window_design.spacer + (2 * small_height))) + (2 * (window_design.spacer + large_height))

        window_controls.select_answer_button = Button(window_controls.main_quiz_page, text = "Check Answer", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.check_answer, question_number))
        window_controls.select_answer_button.place(x = (2 * window_design.spacer), y = start_height, width = (2 * (window_design.spacer + width)), height = small_height)

        # Back + Exit Button Layout (Probably Send to Function so Review Page can also use)
        window_controls.bottom_row_buttons(question_number, start_height + (window_design.spacer + small_height))

    def make_review_question_page(question_number: int) -> None:
        window_controls.main_quiz_page = window_controls.make_question_page_template(question_number)
        window_controls.main_quiz_page.geometry(window_controls.calculate_review_question_dimensions())

        window_controls.main_quiz_page.update()
        window_controls.main_quiz_page.deiconify()
        
        button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)
        
        width: int = window_design.get_question_page_width()
        small_height: int = window_design.get_question_page_small_height()
        large_height: int = window_design.get_question_page_large_height()

        start_height: int = (4 * window_design.spacer) + (1 * (window_design.spacer + small_height)) + ((window_design.spacer + (2 * small_height))) + (2 * (window_design.spacer + large_height))

        window_controls.select_answer_button = Button(window_controls.main_quiz_page, text = "Next Question", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.display_question_controller, question_number + 1))
        window_controls.select_answer_button.place(x = (2 * window_design.spacer), y = start_height, width = (2 * (window_design.spacer + width)), height = small_height)

        start_height += (window_design.spacer + small_height)

        if question_number != quiz_handler.question_number - 1:
            pass

        # Back + Exit Button Layout (Probably Send to Function so Review Page can also use)
        window_controls.bottom_row_buttons(question_number, start_height)

    def bottom_row_buttons(question_number, start_height) -> None:
        button_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.button_colours)
        
        width: int = window_design.get_question_page_width()
        height: int = window_design.get_question_page_small_height()

        if question_number == 1:
            window_controls.quiz_exit_button = Button(window_controls.main_quiz_page, text = "Exit", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.kill_program)
            window_controls.quiz_exit_button.place(x = (2 * window_design.spacer), y = start_height, width = (2 * (window_design.spacer + width)), height = height)
        else:
            window_controls.quiz_back_button = Button(window_controls.main_quiz_page, text = "Review Last Question", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.display_question_controller, question_number - 1))
            window_controls.quiz_back_button.place(x = (2 * window_design.spacer), y = start_height, width = width, height = height)

            window_controls.quiz_exit_button = Button(window_controls.main_quiz_page, text = "Exit", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.kill_program)
            window_controls.quiz_exit_button.place(x = (4 * window_design.spacer) + width, y = start_height, width = width, height = height)


    def make_question_page_template(question_number: int) -> Toplevel:
        template_frame: Toplevel = Toplevel(window_controls.window)
        template_frame.withdraw()

        window_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.window_colours)
        label_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.label_colours)
        
        width: int = window_design.get_question_page_width()
        difficulty_width: int = window_design.get_question_page_difficulty_width()
        small_height: int = window_design.get_question_page_small_height()
        large_height: int = window_design.get_question_page_large_height()

        template_frame.geometry(window_controls.calculate_setup_quiz_dimensions())
        template_frame.config(bg = window_colours[0].colour_code)

        current_question: question = quiz_handler.question_list[question_number - 1]

        question_number_label: Label = Label(template_frame, text = f"Question Number: {question_number}/{quiz_handler.quiz_length}", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        question_number_label.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer), width = width, height = small_height)

        window_controls.current_score_label = Label(template_frame, text = f"Current Score: {quiz_handler.current_score}", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        window_controls.current_score_label.place(x = (4 * window_design.spacer) + width, y = (2 * window_design.spacer), width = width, height = small_height)

        question_text_label: Label = Label(template_frame, text = f"Question:\n{current_question.question_text}", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        question_text_label.place(x = (2 * window_design.spacer), y = (3 * window_design.spacer) + (1 * (window_design.spacer + small_height)), width = (2 * (window_design.spacer + width)), height = (2 * small_height))

        question_difficulty_label: Label = Label(template_frame, text = current_question.question_difficulty, bg = label_colours[0].colour_code, fg = label_colours[1].colour_code, font = window_design.main_font)
        question_difficulty_label.place(x = (2 * window_design.spacer), y = (3 * window_design.spacer) + (1 * (window_design.spacer + small_height)), width = difficulty_width, height = small_height)

        window_controls.answer_buttons.clear()

        row_1: int = (3 * window_design.spacer) + (1 * (window_design.spacer + small_height)) + ((window_design.spacer + (2 * small_height)))
        row_2: int = (3 * window_design.spacer) + (1 * (window_design.spacer + small_height)) + ((window_design.spacer + (2 * small_height))) + (window_design.spacer + large_height)

        col_1: int = (2 * window_design.spacer)
        col_2: int = (4 * window_design.spacer) + width

        x: int
        y: int

        for i in range(len(quiz_handler.question_list[question_number - 1].answer_options)):
            answer_option: answer = quiz_handler.question_list[question_number - 1].answer_options[i]
            answer_colours: list[colour] = window_controls.convert_to_colours(answer_option.answer_colours)

            match i:
                case 0:
                    x = col_1
                    y = row_1
                case 1:
                    x = col_2
                    y = row_1
                case 2:
                    x = col_1
                    y = row_2
                case 3:
                    x = col_2
                    y = row_2
            
            answer_button: Button = Button(template_frame, text = answer_option.answer_text, bg = answer_colours[0].colour_code, fg = answer_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.select_answer, question_number, i))
            answer_button.place(x = x, y = y, width = width, height = large_height)

            window_controls.answer_buttons.append(answer_button)

        return template_frame

    def select_answer(question_number: int, answer_index: int) -> None:
        current_question: question = quiz_handler.question_list[question_number - 1]

        if not current_question.question_answered:
            if window_controls.can_select_answer(question_number, answer_index):
                window_controls.reset_question_buttons(question_number)

                button_colours: list[colour] = window_controls.convert_to_colours(current_question.answer_options[answer_index].answer_colours)
                window_controls.answer_buttons[answer_index].configure(bg = button_colours[1].colour_code, fg = button_colours[0].colour_code)

                window_controls.current_selected_answer = current_question.answer_options[answer_index]

    def can_select_answer(question_number: int, answer_index: int) -> bool:
        current_question: question = quiz_handler.question_list[question_number - 1]
        potential_answer: answer = current_question.answer_options[answer_index]

        if potential_answer == window_controls.current_selected_answer:
            #print("Returned False - Answer Already Selected")
            return False
        
        for selected_answer in current_question.selected_answers:
            if potential_answer == selected_answer:
                #print("Returned False - Answer Already Chosen")
                return False

        #print("Returned True - No Issues")
        return True        

    def reset_question_buttons(question_number: int) -> None:
        button_colours: list[colour]

        for i in range(len(window_controls.answer_buttons)):
            button_colours = window_controls.convert_to_colours(quiz_handler.question_list[question_number - 1].answer_options[i].answer_colours)
            window_controls.answer_buttons[i].configure(bg = button_colours[0].colour_code, fg = button_colours[1].colour_code)

    def check_answer(question_number: int) -> None:
        if window_controls.current_selected_answer == None:
            messagebox.showwarning("No Answer Selected", "Please Select an Answer")
            return 0
        
        quiz_handler.question_list[question_number - 1].add_selected_answer(window_controls.current_selected_answer)

        window_controls.attempts_at_question += 1
        window_controls.total_attempts += 1

        points_awarded: int = 0

        match window_controls.attempts_at_question:
            case 1:
                points_awarded = quiz_handler.first_attempt_points
            case 2:
                points_awarded = quiz_handler.second_attempt_points

        if window_controls.current_selected_answer == quiz_handler.question_list[question_number - 1].correct_answer:
            window_controls.answer_buttons[window_controls.current_selected_answer.answer_index].configure(bg = window_design.correct_answer_colours[0].colour_code, fg = window_design.correct_answer_colours[1].colour_code)

            the_question: question = quiz_handler.question_list[question_number - 1]
            the_answer: answer = the_question.answer_options[window_controls.current_selected_answer.answer_index]
            the_answer.answer_colours = [window_design.correct_answer_colours[0].colour_name,
                                         window_design.correct_answer_colours[1].colour_name]

            the_question.question_answered = True
            quiz_handler.current_score += points_awarded
            window_controls.current_score_label.configure(text = f"Current Score: {quiz_handler.current_score}")

            quiz_handler.question_number += 1
            window_controls.next_question(question_number, "Fun Fact")
        else:
            window_controls.answer_buttons[window_controls.current_selected_answer.answer_index].configure(bg = window_design.incorrect_answer_colours[0].colour_code,fg = window_design.incorrect_answer_colours[1].colour_code)

            the_question: question = quiz_handler.question_list[question_number - 1]
            the_answer: answer = the_question.answer_options[window_controls.current_selected_answer.answer_index]
            the_answer.answer_colours = [window_design.incorrect_answer_colours[0].colour_name,
                                         window_design.incorrect_answer_colours[1].colour_name]

            if window_controls.attempts_at_question == 2:
                the_question.question_answered = True
                window_controls.next_question(question_number, "Hint")

    def next_question(question_number: int, popup_option: str) -> None:
        popup_string: str

        match popup_option:
            case "Fun Fact":
                popup_string = quiz_handler.question_list[question_number - 1].fun_fact
            case "Hint":
                popup_string = quiz_handler.question_list[question_number - 1].hint
        
        print(popup_string)

        # Display Hint or Fact
        # Go To Next Question or End Quiz and Go To Score Page

        if question_number + 1 > quiz_handler.quiz_length:
            window_controls.select_answer_button.configure(text = "End Quiz", command = window_controls.main_quiz_page.destroy)
        else:
            window_controls.select_answer_button.configure(text = "Next Question", command = functools.partial(window_controls.display_question_controller, question_number + 1))


    # Clear Pages

    def clear_login_page() -> None:
        window_controls.enter_username.delete(0, len(window_controls.enter_username.get()))
        window_controls.enter_password.delete(0, len(window_controls.enter_password.get()))

    def clear_create_account_page() -> None:
        window_controls.enter_username.delete(0, len(window_controls.enter_username.get()))
        window_controls.enter_password.delete(0, len(window_controls.enter_password.get()))

        window_colours: list[colour] = window_design.get_window_colours()
        label_colours: list[colour] = window_design.get_label_colours()
        button_colours: list[colour] = window_design.get_button_colours()
        entry_colours: list[colour] = window_design.get_entry_colours()

        window_controls.window_colour_label.configure(bg = window_colours[0].colour_code)
        window_controls.window_text_label.configure(bg = window_colours[0].colour_code, fg = window_colours[1].colour_code)
        window_controls.label_colours_label.configure(text = "Label Colours", bg = label_colours[0].colour_code, fg = label_colours[1].colour_code)
        window_controls.button_colours_label.configure(text = "Button Colours", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code)
        window_controls.entry_colours_label.configure(text = "Entry Colours", bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code)

        if window_controls.colour_selector_page != None:
            window_controls.colour_selector_page.destroy()

    def clear_colour_selector() -> None:
        window_controls.colour_name.delete(0, len(window_controls.colour_name.get()))
        window_controls.colour_code.delete(0, len(window_controls.colour_code.get()))
        window_controls.colour_preview.configure(bg = window_controls.convert_to_colours(window_controls.current_user.window_colours)[0].colour_code)
        window_controls.colour_listbox.selection_clear(0, 'end')

    def clear_audio_selector() -> None:
        window_controls.audio_name.delete(0, len(window_controls.audio_name.get()))
        window_controls.audio_file.delete(0, len(window_controls.audio_file.get()))
        window_controls.audio_listbox.selection_clear(0, 'end')

    def clear_question_selector() -> None:
        window_controls.question_listbox.delete(0, END)
        window_controls.delete_question.configure(text = "Discard Question")

    def clear_question_editor() -> None:
        window_colours: list[colour] = window_controls.convert_to_colours(window_controls.current_user.window_colours)

        window_controls.enter_question_text.delete(0, len(window_controls.enter_question_text.get()))

        for answer_details_pair in window_controls.answer_details:
            answer_details_pair[0].delete(0, len(answer_details_pair[0].get()))
            answer_details_pair[1].configure(bg = window_colours[1].colour_code, fg = window_colours[0].colour_code)

        window_controls.create_question_button.configure(text = "Create Question")#, command = window_controls.create_question)


    # Dimension Calculations

    def calculate_login_dimensions() -> str:
        page_width: int = (4 * window_design.spacer) + window_design.get_login_width()
        page_height: int = (6 * window_design.spacer) + (7 * (window_design.spacer + window_design.get_login_height()))

        return f"{page_width}x{page_height}"

    def calculate_new_create_account_dimensions() -> str:
        small_height: int = window_design.get_create_account_small_height()
        page_width: int = (8 * window_design.spacer) + (2 * window_design.get_create_account_width())
        page_height: int = (7 * window_design.spacer) + (4 * small_height) + (4 * ((window_design.spacer) + small_height))
        return f"{page_width}x{page_height}"
    
    def calculate_colour_selector_dimensions() -> str:
        page_width: int = (8 * window_design.spacer) + (2 * window_design.get_choose_colours_width())
        page_height: int = (7 * window_design.spacer) + (17 * (window_design.spacer + window_design.get_choose_colours_small_height())) + (2 * (window_design.spacer + window_design.get_choose_colours_large_height()))
        return f"{page_width}x{page_height}"

    def calculate_user_account_dimensions() -> str:
        page_width: int = (6 * window_design.spacer) + (2 * window_design.user_account_small_width)
        page_height: int = (2 * window_design.spacer) + (7 * ((2 * window_design.spacer) + window_design.user_account_small_height))
        return f"{page_width}x{page_height}"

    def calculate_view_account_dimensions() -> str:
        page_width: int = (4 * window_design.spacer) + window_design.view_account_small_width
        scores_listbox_height: int = int(window_design.view_account_listbox_item_height * window_design.view_account_listbox_visible_items)
        page_height: int = (3 * window_design.spacer) + (4 * (window_design.spacer + window_design.view_account_small_height)) + (window_design.spacer + (scores_listbox_height + (5 - (scores_listbox_height % 5))))

        return f"{page_width}x{page_height}"

    def calculate_colour_editor_dimensions() -> str:
        page_width: int = (8 * window_design.spacer) + (2 * window_design.get_colour_editor_width())
        listbox_height: int = int(window_design.colour_editor_listbox_item_height * window_design.colour_editor_listbox_visible_items)
        page_height: int = (5 * window_design.spacer) + (listbox_height) + (5 - (listbox_height % 5)) + (4 * (window_design.spacer + window_design.get_colour_editor_small_height()))

        return f"{page_width}x{page_height}"

    def calculate_audio_editor_dimensions() -> str:
        page_width: int = (8 * window_design.spacer) + (2 * window_design.get_audio_editor_width())
        listbox_height: int = int(window_design.audio_editor_listbox_item_height * window_design.audio_editor_listbox_visible_items)
        page_height: int = (5 * window_design.spacer) + (listbox_height) + (5 - (listbox_height % 5)) + (4 * (window_design.spacer + window_design.get_audio_editor_small_height()))

        return f"{page_width}x{page_height}"

    def calculate_select_question_dimensions() -> str:
        page_width: int = (8 * window_design.spacer) + window_design.get_question_list_width() + window_design.get_question_list_button_width()
        page_height: int = (3 * window_design.spacer) + (6 * (window_design.spacer + window_design.get_question_list_small_height()))
        return f"{page_width}x{page_height}"

    def calculate_edit_question_dimensions() -> str:
        page_width: int = (8 * window_design.spacer) + (2 * window_design.question_editor_small_width)
        page_height: int = (10 * window_design.spacer) + (17 * (window_design.spacer + window_design.question_editor_small_height)) + (2 * (window_design.spacer + window_design.question_editor_large_height))
        return f"{page_width}x{page_height}"

    def calculate_select_answer_colour_dimensions() -> str:
        page_width: int = (4 * window_design.spacer) + window_design.get_choose_answer_colours_width()
        page_height: int = (3 * window_design.spacer) + (8 * (window_design.spacer + window_design.get_choose_colours_small_height())) + (window_design.spacer + window_design.get_choose_colours_large_height())
        return f"{page_width}x{page_height}"

    def calculate_setup_quiz_dimensions() -> str:
        page_width: int = (8 * window_design.spacer) + (2 * window_design.get_setup_quiz_width())
        page_height: int = (4 * window_design.spacer) + ((len(quiz_handler.quiz_lengths) + 4) * (window_design.spacer + window_design.get_setup_quiz_small_height()))
        return f"{page_width}x{page_height}"
    
    def calculate_select_length_dimensions() -> str:
        page_width: int = (4 * window_design.spacer) + (window_design.get_setup_quiz_width())
        page_height: int = (1 * window_design.spacer) + (4 * (window_design.spacer + window_design.get_setup_quiz_small_height()))
        return f"{page_width}x{page_height}"

    def calculate_view_question_dimensions() -> str:
        page_width: int = (6 * window_design.spacer) + (2 * window_design.get_question_page_width())
        page_height: int = 500
        return f"{page_width}x{page_height}"
    
    def calculate_review_question_dimensions() -> str:
        page_width: int = (6 * window_design.spacer) + (2 * window_design.get_question_page_width())
        page_height: int = 500
        return f"{page_width}x{page_height}"


    # Colour Handling

    def set_contrast_ratio(colour_set: str, contrast_label: Label) -> None:
        back_colour: colour
        text_colour: colour

        back_luminance: float
        text_luminance: float
        
        match colour_set:
            case "Window":
                back_colour = common_data.get_colour_from_name(window_controls.window_back.get())
                text_colour = common_data.get_colour_from_name(window_controls.window_text.get())
                back_luminance = back_colour.luminance
                text_luminance = text_colour.luminance
            case "Label":
                back_colour = common_data.get_colour_from_name(window_controls.label_back.get())
                text_colour = common_data.get_colour_from_name(window_controls.label_text.get())
                back_luminance = back_colour.luminance
                text_luminance = text_colour.luminance
            case "Button":
                back_colour = common_data.get_colour_from_name(window_controls.button_back.get())
                text_colour = common_data.get_colour_from_name(window_controls.button_text.get())
                back_luminance = back_colour.luminance
                text_luminance = text_colour.luminance
            case "Entry":
                back_colour = common_data.get_colour_from_name(window_controls.entry_back.get())
                text_colour = common_data.get_colour_from_name(window_controls.entry_text.get())
                back_luminance = back_colour.luminance
                text_luminance = text_colour.luminance

        contrast_label.configure(text = f"Colour Contrast Ratio:\n{window_controls.get_contrast_ratio(back_luminance, text_luminance)}", bg = back_colour.colour_code, fg = text_colour.colour_code)

    def get_contrast_ratio(back_luminance: float, text_luminance: float) -> float:
        if back_luminance > text_luminance:
            return round(back_luminance / text_luminance, 2)
        else:
            return round(text_luminance / back_luminance, 2)

    def check_contrast_ratio(back_luminance: float, text_luminance: float) -> bool:
        ratio: float = window_controls.get_contrast_ratio(back_luminance, text_luminance)

        if ratio < window_design.get_minimum_contrast_ratio():
            return False
        else:
            return True

    def invert_colours(colour_set: str) -> None:
        match colour_set:
            case "Window":
                temp_colour: str = window_controls.window_back.get()

                window_controls.window_back.set(window_controls.window_text.get())
                window_controls.window_text.set(temp_colour)
            case "Label":
                temp_colour: str = window_controls.label_back.get()

                window_controls.label_back.set(window_controls.label_text.get())
                window_controls.label_text.set(temp_colour)
            case "Button":
                temp_colour: str = window_controls.button_back.get()

                window_controls.button_back.set(window_controls.button_text.get())
                window_controls.button_text.set(temp_colour)
            case "Label":
                temp_colour: str = window_controls.entry_back.get()

                window_controls.entry_back.set(window_controls.entry_text.get())
                window_controls.entry_text.set(temp_colour)

    def get_set_colours(selector_type: str, colour_pair: str) -> tuple[str, str]:
        return_back: str
        return_text: str

        match selector_type:
            case "Create Account":
                match colour_pair:
                    case "Window":
                        return_back = window_design.get_window_colours()[0].colour_name
                        return_text = window_design.get_window_colours()[1].colour_name
                    case "Label":
                        return_back = window_design.get_label_colours()[0].colour_name
                        return_text = window_design.get_label_colours()[1].colour_name
                    case "Button":
                        return_back = window_design.get_button_colours()[0].colour_name
                        return_text = window_design.get_button_colours()[1].colour_name
                    case "Entry":
                        return_back = window_design.get_entry_colours()[0].colour_name
                        return_text = window_design.get_entry_colours()[1].colour_name
            case "Update User Colours":
                match colour_pair:
                    case "Window":
                        return_back = window_controls.current_user.window_colours[0]
                        return_text = window_controls.current_user.window_colours[1]
                    case "Label":
                        return_back = window_controls.current_user.label_colours[0]
                        return_text = window_controls.current_user.label_colours[1]
                    case "Button":
                        return_back = window_controls.current_user.button_colours[0]
                        return_text = window_controls.current_user.button_colours[1]
                    case "Entry":
                        return_back = window_controls.current_user.entry_colours[0]
                        return_text = window_controls.current_user.entry_colours[1]

        return [return_back, return_text]

    def reset_colours(selector_type: str, colour_pair: str) -> None:
        if colour_pair == "All":
            window_controls.reset_colours(selector_type, "Window")
            window_controls.reset_colours(selector_type, "Label")
            window_controls.reset_colours(selector_type, "Button")
            window_controls.reset_colours(selector_type, "Entry")
        else:
            match selector_type:
                case "Create Account":
                    match colour_pair:
                        case "Window":
                            window_controls.window_back.set(window_design.get_window_colours()[0].colour_name)
                            window_controls.window_text.set(window_design.get_window_colours()[1].colour_name)
                        case "Label":
                            window_controls.label_back.set(window_design.get_label_colours()[0].colour_name)
                            window_controls.label_text.set(window_design.get_label_colours()[1].colour_name)
                        case "Button":
                            window_controls.button_back.set(window_design.get_button_colours()[0].colour_name)
                            window_controls.button_text.set(window_design.get_button_colours()[1].colour_name)
                        case "Entry":
                            window_controls.entry_back.set(window_design.get_entry_colours()[0].colour_name)
                            window_controls.entry_text.set(window_design.get_entry_colours()[1].colour_name)
                case "Update User Colours":
                    match colour_pair:
                        case "Window":
                            window_controls.window_back.set(window_controls.current_user.window_colours[0])
                            window_controls.window_text.set(window_controls.current_user.window_colours[1])
                        case "Label":
                            window_controls.label_back.set(window_controls.current_user.label_colours[0])
                            window_controls.label_text.set(window_controls.current_user.label_colours[1])
                        case "Button":
                            window_controls.button_back.set(window_controls.current_user.button_colours[0])
                            window_controls.button_text.set(window_controls.current_user.button_colours[1])
                        case "Entry":
                            window_controls.entry_back.set(window_controls.current_user.entry_colours[0])
                            window_controls.entry_text.set(window_controls.current_user.entry_colours[1])


    # Colour Editor Functions

    def create_colour() -> None:
        if window_controls.valid_colour_details(colour("", "#FFFFFF")):
            common_data.add_colour(colour(window_controls.colour_name.get(), window_controls.colour_code.get()))
            append_file(common_data.get_colour_file(), f"{window_controls.colour_name.get()},{window_controls.colour_code.get()}")
            window_controls.update_colour_list()

    def update_colour() -> None:
        if window_controls.valid_colour_details(window_controls.selected_colour):
            window_controls.update_user_colours()
            window_controls.update_question_colours()
            
            window_controls.selected_colour.colour_name = window_controls.colour_name.get()
            window_controls.selected_colour.colour_code = window_controls.colour_code.get()

            window_controls.update_colour_file()
            window_controls.update_colour_list()

    def delete_colour() -> None:
        common_data.colour_list.remove(window_controls.selected_colour)
        window_controls.update_colour_file()
        window_controls.update_colour_list()

    def update_colour_file() -> None:
        write_string: str = ""

        for colour_option in common_data.colour_list:
            write_string += f"{colour_option.colour_name},{colour_option.colour_code}\n"

        write_file(common_data.get_colour_file(), write_string)

    def valid_colour_details(exempt_colour: colour) -> None:
        colour_name: str = window_controls.colour_name.get()
        colour_code: str = window_controls.colour_code.get()

        valid_colour_name_pt1: bool = window_controls.check_field(colour_name, 3, 30, False)
        valid_colour_name_pt2: bool = window_controls.unique_colour_name(colour_name, exempt_colour.colour_name)
        valid_colour_name: bool = valid_colour_name_pt1 and valid_colour_name_pt2

        valid_colour_code: bool = window_controls.valid_hex_code(colour_code)

        unique_colour_code: bool
        matched_colour: colour

        unique_colour_code, matched_colour = window_controls.unique_colour_code(colour_code, exempt_colour.colour_code)

        if valid_colour_name and valid_colour_code and unique_colour_code:
            return True
        else:
            messagebox.showerror("Invalid Colour Details", f"Colour Details are Invalid\n\nBreakdown:\nValid Name: {valid_colour_name}\nValid Code: {valid_colour_code}\nUnique Colour Code: {unique_colour_code} ({matched_colour.colour_name})")
            return False

    def unique_colour_name(check_string: str, exempt_name: str) -> bool:
        for check_colour in common_data.colour_list:
            if check_colour.colour_name == check_string and check_colour.colour_name != exempt_name:
                return False
            
        return True

    def unique_colour_code(check_string: str, exempt_code: str) -> tuple[bool, colour]:
        for check_colour in common_data.colour_list:
            if check_colour.colour_code == check_string and check_colour.colour_code != exempt_code:
                return [False, check_colour]
            
        return [True, colour("Unique Colour", "#FFFFFF")]

    def valid_hex_code(test_code: str) -> bool:
        hex_string = re.compile(r'^#([a-fA-F0-9]{6})$')
        return bool(re.match(hex_string, test_code))

    def update_colour_list() -> None:
        window_controls.colour_listbox.delete(0, END)

        for colour_option in common_data.colour_list:
            window_controls.colour_listbox.insert('end', colour_option.colour_name)


    # Audio Handling

    def play_audio() -> None:
        audio_path: str = os.path.join(common_data.get_audio_folder(), window_controls.audio_file.get())
        
        if not os.path.exists(audio_path):
            messagebox.showerror("Invalid File Path", "Audio File doesn't Exist")
        elif not audio_path.lower().endswith((".wav", ".mp3", ".midi")):
            messagebox.showerror("Invalid File Format", "Audio File Format is Invalid")
        else:
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play(loops = 0)

    def create_audio() -> None:
        if window_controls.valid_audio_details(audio("", "")):
            common_data.add_audio(audio(window_controls.audio_name.get(), window_controls.audio_file.get()))
            append_file(common_data.get_audio_file(), f"{window_controls.audio_name.get()},{window_controls.audio_file.get()}")
            window_controls.update_audio_list()

            window_controls.selected_audio = None

    def update_audio() -> None:
        if window_controls.valid_audio_details(window_controls.selected_audio):
            
            window_controls.selected_audio.audio_name = window_controls.audio_name.get()
            window_controls.selected_audio.audio_file = window_controls.audio_file.get()

            window_controls.update_audio_file()
            window_controls.update_audio_list()

            window_controls.update_question_audios()

            window_controls.selected_audio = None

    def delete_audio() -> None:
        common_data.audio_list.remove(window_controls.selected_audio)

        window_controls.update_audio_file()
        window_controls.update_audio_list()

        window_controls.selected_audio = None

    def valid_audio_details(exempt_audio: audio) -> bool:
        audio_name: str = window_controls.audio_name.get()
        audio_file: str = window_controls.audio_file.get()

        valid_audio_name: bool = window_controls.check_field(audio_name, 3, 30, False) and window_controls.unique_audio_name(audio_name, exempt_audio.audio_name)
        valid_audio_file: bool = window_controls.valid_audio_file(audio_file) and file_exists(os.path.join(common_data.get_audio_folder(), audio_file))

        print(f"{window_controls.check_field(audio_file, 3, 30, False)}\n{window_controls.valid_audio_file(audio_file)}\n{file_exists(os.path.join(common_data.get_audio_folder(), audio_file))}")
        
        unique_audio_file: bool
        duplicate_audio: audio

        unique_audio_file, duplicate_audio = window_controls.unique_audio_file(audio_file, exempt_audio.audio_file)

        if valid_audio_name and valid_audio_file and unique_audio_file:
            return True
        else:
            messagebox.showerror("Invalid Audio Details", f"Audio Details are Invalid\n\nBreakdown:\nValid Name: {valid_audio_name}\nValid Code: {valid_audio_file}\nUnique Colour Code: {unique_audio_file} ({duplicate_audio.audio_name})")
            return False

    def unique_audio_name(check_string: str, exempt_name: str) -> bool:
        for check_colour in common_data.colour_list:
            if check_colour.colour_name == check_string and check_colour.colour_name != exempt_name:
                return False
            
        return True

    def unique_audio_file(check_string: str, exempt_file: str) -> tuple[bool, audio]:
        for check_colour in common_data.colour_list:
            if check_colour.colour_code == check_string and check_colour.colour_code != exempt_file:
                return [False, check_colour]
            
        return [True, audio("Unique Audio", "audio.mp4")]

    def valid_audio_file(audio_file: str) -> bool:
        valid_file_name: bool = not re.findall("[/*-+<>:;'#@~,`¬!£$%^&*()=]", audio_file)
        valid_file_type: bool = audio_file.lower().endswith((".wav", ".mp3", ".midi"))

        return valid_file_name and valid_file_type

    def update_audio_list() -> None:
        window_controls.audio_listbox.delete(0, END)

        for audio_option in common_data.audio_list:
            window_controls.audio_listbox.insert('end', audio_option.audio_name)

    def update_audio_file() -> None:
        write_string: str = ""

        for audio_option in common_data.audio_list:
            write_string += f"{audio_option.audio_name},{audio_option.audio_file}\n"

        write_file(common_data.get_audio_file(), write_string)


    # Question Handling

    def create_question() -> None:
        if window_controls.valid_question_details(""):
            print("Tits")

            answer_list: list[dict] = []

            for i in range(4):
                answer_dict: dict = {
                    "Answer Text" : window_controls.answer_details[i][0].get(),
                    "Answer Back Colour" : window_controls.answer_colours[i][0].get(),
                    "Answer Text Colour" : window_controls.answer_colours[i][1].get(),
                    "Correct Answer" : window_controls.get_is_correct(i),
                    "Answer Index" : (i + 1)
                }

                answer_list.append(answer_dict)

            question_id: str = window_controls.get_next_question_id()

            question_dictionary: dict = {
                "Question ID" : question_id,
                "Question Difficulty" : window_controls.question_difficulty.get(),
                "Question" : window_controls.enter_question_text.get(),
                "Answers" : answer_list,
                "Fun Fact" : window_controls.enter_fun_fact.get(),
                "Hint" : window_controls.enter_hint.get(),
                "Correct Audio" : window_controls.correct_audio.get(),
                "Incorrect Audio" : window_controls.incorrect_audio.get()
            }

            common_data.add_usable_question(question(question_dictionary))
            append_file(common_data.get_usable_question_file(), (question_id + ".json"))
            write_json_file(os.path.join(common_data.get_usable_question_folder(), (question_id + ".json")), question_dictionary)
        else:
            print("No Tits")

    def update_question() -> None:
        if window_controls.valid_question_details(window_controls.selected_question.question_text):
            print("Boobs")

            window_controls.selected_question.question_text = window_controls.enter_question_text.get()
            window_controls.selected_question.question_difficulty = window_controls.question_difficulty.get()

            window_controls.selected_question.fun_fact = window_controls.enter_fun_fact.get()
            window_controls.selected_question.hint = window_controls.enter_hint.get()

            window_controls.correct_audio = window_controls.correct_audio.get()
            window_controls.incorrect_audio = window_controls.incorrect_audio.get()

            for i in range(4):
                window_controls.selected_question.answer_options[i].answer_text = window_controls.answer_details[i][0].get()
                window_controls.selected_question.answer_options[i].answer_colours[0] = window_controls.answer_colours[i][0].get()
                window_controls.selected_question.answer_options[i].answer_colours[1] = window_controls.answer_colours[i][1].get()
                window_controls.selected_question.answer_options[i].correct_answer = window_controls.get_is_correct(i)

            question_folder: str

            match window_controls.selected_question_list:
                case "Usable":
                    question_folder = common_data.get_usable_question_folder()
                case "Discarded":
                    question_folder = common_data.get_discarded_question_folder()

            write_json_file(os.path.join(question_folder, f"{window_controls.selected_question.question_id}.json"), window_controls.selected_question.make_dictionary())
        else:
            print("No Boobs")

    def valid_question_details(exempt_question_text: str) -> bool:
        valid_question: bool = window_controls.check_field(window_controls.enter_question_text.get(), 3, 80, False) and window_controls.unique_question_text(window_controls.enter_question_text.get(), exempt_question_text)
        valid_difficulty: bool = window_controls.question_difficulty.get() in quiz_handler.difficulty_range
        valid_correct_answer: bool = int(window_controls.correct_answer.get()) in quiz_handler.correct_answers
        valid_answers: bool = window_controls.valid_answers(3)
        valid_audios: bool = window_controls.incorrect_audio.get() != window_controls.correct_audio.get()

        return valid_question and valid_difficulty and valid_correct_answer and valid_answers and valid_audios

    def unique_question_text(check_string: str, ignore_string: str) -> bool:
        for check_question in common_data.usable_question_list:
            if check_question.question_text == check_string and check_question.question_text != ignore_string:
                return False
            
        for check_question in common_data.discarded_question_list:
            if check_question.question_text == check_string and check_question.question_text != ignore_string:
                return False
            
        return True
    
    def valid_answers(current_index: int) -> bool:
        return_bool: bool
        if current_index > 0:
            return_bool = window_controls.valid_answer(current_index) and window_controls.valid_answers(current_index - 1)
        else:
            return_bool = window_controls.valid_answer(current_index)
        
        return return_bool

    def valid_answer(answer_index: int) -> bool:
        answer_text: str = window_controls.answer_details[answer_index][0].get()

        window_back_colour: colour = common_data.get_colour_from_name(window_controls.current_user.window_colours[0])

        back_colour: colour = common_data.get_colour_from_name(window_controls.answer_colours[answer_index][0].get())
        text_colour: colour = common_data.get_colour_from_name(window_controls.answer_colours[answer_index][1].get())

        print(answer_index)
        print(f"Back Colour: {back_colour.colour_name}")
        print(f"Text Colour: {text_colour.colour_name}\n")

        answer_ratio: float = window_controls.get_contrast_ratio(back_colour.luminance, text_colour.luminance)
        winans_ratio: float = window_controls.get_contrast_ratio(window_back_colour.luminance, back_colour.luminance)

        valid_answer_text: bool = window_controls.check_field(answer_text, 1, 50, False)

        valid_answer_ratio: bool = answer_ratio >= window_design.minimum_contrast_ratio
        valid_winans_ratio: bool = winans_ratio >= window_design.minimum_contrast_ratio

        if valid_answer_text and valid_answer_ratio and valid_winans_ratio:
            return True
        else:
            messagebox.showerror("Invalid Answer Data", f"Answer {answer_index + 1} Details:\nAnswer Text: {valid_answer_text}\nAnswer Colour Ratio: {valid_answer_ratio}\n Valid Window Ratio: {valid_winans_ratio}")
            return False

    def get_next_question_id() -> str:
        common_data.sort_usable_questions()
        common_data.sort_discarded_questions()

        usable_id: int
        discarded_id: int

        if len(common_data.usable_question_list) > 0 and len(common_data.discarded_question_list) > 0:
            usable_id = int(common_data.usable_question_list[len(common_data.usable_question_list) - 1].question_id.replace("Q", ""))
            discarded_id = int(common_data.discarded_question_list[len(common_data.discarded_question_list) - 1].question_id.replace("Q", ""))
        elif len(common_data.usable_question_list) == 0 and len(common_data.discarded_question_list) == 0:
            usable_id = 0
            discarded_id = 0
        elif len(common_data.usable_question_list) == 0:
            usable_id = 0
            discarded_id = int(common_data.discarded_question_list[len(common_data.discarded_question_list) - 1].question_id.replace("Q", ""))  
        else:
            usable_id = int(common_data.usable_question_list[len(common_data.usable_question_list) - 1].question_id.replace("Q", ""))
            discarded_id = 0

        new_id: int = 0

        if usable_id > discarded_id:
            new_id = usable_id + 1
        else:
            new_id = discarded_id + 1

        print(f"Q{str(new_id).rjust(3, "0")}")
        return f"Q{str(new_id).rjust(3, "0")}"

    def get_is_correct(answer_index: int) -> bool:
        print(f"{answer_index}\n{answer_index + 1}\n{int(window_controls.correct_answer.get())}")
        if answer_index + 1 == int(window_controls.correct_answer.get()):
            print("true")
            return True
        else:
            print("false")
            return False

    def discard_question() -> None:
        window_controls.select_question()

        delete_file(os.path.join(common_data.get_usable_question_folder(), f"{window_controls.selected_question.question_id}.json"))
        write_json_file(os.path.join(common_data.get_discarded_question_folder(), f"{window_controls.selected_question.question_id}.json"), window_controls.selected_question.make_dictionary())

        common_data.discard_question(window_controls.selected_question)
        window_controls.load_question_list(window_controls.selected_question_list)

        window_controls.selected_question = None

    def reinstate_question() -> None:
        window_controls.select_question()

        delete_file(os.path.join(common_data.get_discarded_question_folder(), f"{window_controls.selected_question.question_id}.json"))
        write_json_file(os.path.join(common_data.get_usable_question_folder(), f"{window_controls.selected_question.question_id}.json"), window_controls.selected_question.make_dictionary())

        common_data.reinstate_question(window_controls.selected_question)
        window_controls.load_question_list(window_controls.selected_question_list)

        window_controls.selected_question = None


    # Update Functions

    def update_user_colours() -> None:
        for update_user in common_data.user_list:
            colour_dict: dict = update_user.get_colour_dictionary()

            key_list: list[str] = list(colour_dict.keys())

            for key in key_list:
                if colour_dict[key] == window_controls.selected_colour.colour_name:
                    colour_dict[key] = window_controls.colour_name.get()
            
            update_user.update_colours(colour_dict)
        
            write_json_file(os.path.join(common_data.get_user_folder(), f"{update_user.user_id}.json"), update_user.make_dictionary())

    def remove_user_colour() -> None:
        for update_user in common_data.user_list:
            colour_dict: dict = update_user.get_colour_dictionary()

            key_list: list[str] = list(colour_dict.keys())

            for key in key_list:
                if colour_dict[key] == window_controls.selected_colour.colour_name:
                    colour_dict[key] = common_data.colour_list[0].colour_name
            
            update_user.update_colours(colour_dict)
        
            write_json_file(os.path.join(common_data.get_user_folder(), f"{update_user.user_id}.json"), update_user.make_dictionary())

    def update_question_colours() -> None:
        for update_question in common_data.usable_question_list:
            answer_list: list[answer] = update_question.answer_options

            for answer_option in answer_list:
                for answer_colour in answer_option.answer_colours:
                    if answer_colour == window_controls.selected_colour.colour_name:
                        answer_colour = window_controls.colour_name.get()
            
            write_json_file(os.path.join(common_data.get_usable_questions_folder(), f"{update_question.question_id}.json", update_question.make_dictionary()))

    def remove_question_colour() -> None:
        for update_question in common_data.usable_question_list:
            answer_list: list[answer] = update_question.answer_options

            for answer_option in answer_list:
                for answer_colour in answer_option.answer_colours:
                    if answer_colour == window_controls.selected_colour.colour_name:
                        answer_colour = common_data.colour_list[0].colour_name
            
            write_json_file(os.path.join(common_data.get_usable_questions_folder(), f"{update_question.question_id}.json", update_question.make_dictionary()))

    def update_question_audios() -> None:
        for update_question in common_data.usable_question_list:
            if update_question.correct_audio == window_controls.selected_audio.audio_name:
                update_question.correct_audio = window_controls.audio_name.get()
                
            if update_question.incorrect_audio == window_controls.selected_audio.audio_name:
                update_question.incorrect_audio = window_controls.audio_name.get()
            
            write_json_file(os.path.join(common_data.get_usable_questions_folder(), f"{update_question.question_id}.json", update_question.make_dictionary()))

        for update_question in common_data.discarded_question_list:
            if update_question.correct_audio == window_controls.selected_audio.audio_name:
                update_question.correct_audio = window_controls.audio_name.get()
                
            if update_question.incorrect_audio == window_controls.selected_audio.audio_name:
                update_question.incorrect_audio = window_controls.audio_name.get()
            
            write_json_file(os.path.join(common_data.get_discarded_questions_folder(), f"{update_question.question_id}.json", update_question.make_dictionary()))

    def remove_question_colours() -> None:
        for update_question in common_data.usable_question_list:
            if update_question.correct_audio == window_controls.selected_audio.audio_name:
                update_question.correct_audio = window_controls.audio_name.get()
                
            if update_question.incorrect_audio == window_controls.selected_audio.audio_name:
                update_question.incorrect_audio = common_data.audio_list[0].audio_name
            
            write_json_file(os.path.join(common_data.get_usable_questions_folder(), f"{update_question.question_id}.json", update_question.make_dictionary()))

        for update_question in common_data.discarded_question_list:
            if update_question.correct_audio == window_controls.selected_audio.audio_name:
                update_question.correct_audio = window_controls.audio_name.get()
                
            if update_question.incorrect_audio == window_controls.selected_audio.audio_name:
                update_question.incorrect_audio = common_data.audio_list[0].audio_name
            
            write_json_file(os.path.join(common_data.get_discarded_questions_folder(), f"{update_question.question_id}.json", update_question.make_dictionary()))


    # Go Back

    def go_back() -> None:
        current_frame: str = window_controls.frame_sequence[len(window_controls.frame_sequence) - 1]
        last_frame: str = window_controls.frame_sequence[len(window_controls.frame_sequence) - 2]

        window_controls.withdraw_frame(current_frame)
        window_controls.deiconify_frame(last_frame)

        window_controls.frame_sequence[len(window_controls.frame_sequence) - 1] = last_frame

    def withdraw_frame(frame: str) -> None:
        match frame:
            case "Login":
                window_controls.login_page.withdraw()
                window_controls.clear_login_page()
            case "Create Account":
                if window_controls.colour_selector_page != None and window_controls.colour_selector_page.winfo_exists():
                    window_controls.colour_selector_page.withdraw()
                window_controls.create_account_page.withdraw()
            case "User Account":
                window_controls.user_account_page.withdraw()
            case "View Account":
                window_controls.view_account_page.withdraw()
            case "Colour Editor":
                window_controls.colour_editor_page.withdraw()
            case "Audio Editor":
                window_controls.audio_editor_page.withdraw()
            case "Question Editor":
                window_controls.question_list_page.withdraw()
            case "Setup Quiz":
                window_controls.setup_quiz_page.withdraw()
            case _:
                pass

    def destroy_all_frames() -> None:
        for frame in window_controls.frame_list:
            window_controls.destroy_frame(frame)

    def destroy_frame(frame: str) -> None:
        match frame:
            case "User Account":
                window_controls.user_account_page.destroy()
            case "View Account":
                window_controls.view_account_page.destroy()
            case "Colour Editor":
                window_controls.colour_editor_page.destroy()
            case "Audio Editor":
                window_controls.audio_editor_page.destroy()
            case "Question Editor":
                window_controls.question_list_page.destroy()
            case "Setup Quiz":
                window_controls.setup_quiz_page.destroy()
            case _:
                pass

    def deiconify_frame(frame: str) -> None:
        match frame:
            case "Login":
                window_controls.login_page.destroy()
                window_controls.login_controller()
            case "Create Account":
                window_controls.create_account_page.deiconify()
            case "User Account":
                window_controls.update_frame(window_controls.user_account_page)
                window_controls.user_account_page.deiconify()
            case "Colour Editor":
                window_controls.clear_colour_selector()
                window_controls.colour_editor_page.update()
                window_controls.colour_editor_page.deiconify()
            case "View Account":
                window_controls.view_account_page.update()
                window_controls.view_account_page.deiconify()
            case "Audio Editor":
                window_controls.clear_audio_selector()
                window_controls.audio_editor_page.update()
                window_controls.audio_editor_page.deiconify()
            case "Question Editor":
                window_controls.clear_question_editor()
                window_controls.question_list_page.update()
                window_controls.question_list_page.deiconify()
            case "Setup Quiz":
#                window_controls.clear_setup_quiz()
                window_controls.setup_quiz_page.update()
                window_controls.setup_quiz_page.deiconify()
            case _:
                pass

    def update_frame(frame: Toplevel) -> None:
        window_colours: list[colour]
        label_colours: list[colour]
        button_colours: list[colour]
        entry_colours: list[colour]

        if window_controls.current_user == None:
            window_colours = window_design.window_colours
            label_colours = window_design.label_colours
            button_colours = window_design.button_colours
            entry_colours = window_design.entry_colours
        else:
            window_colours = window_controls.convert_to_colours(window_controls.current_user.window_colours)
            label_colours = window_controls.convert_to_colours(window_controls.current_user.label_colours)
            button_colours = window_controls.convert_to_colours(window_controls.current_user.button_colours)
            entry_colours = window_controls.convert_to_colours(window_controls.current_user.entry_colours)
        
        frame.configure(bg = window_colours[0].colour_code)

        for widget in frame.winfo_children():
            match type(widget):
                case "Label":
                    widget.configure(bg = label_colours[0].colour_code, fg = label_colours[1].colour_code)
                case "Button":
                    widget.configure(bg = button_colours[0].colour_code, fg = button_colours[1].colour_code)
                case "Entry":
                    widget.configure(bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code)


    # User Handling

    def login() -> None:
        valid_details: bool = False

        for check_user in common_data.get_user_list():
            if check_user.username == window_controls.enter_username.get() and check_user.password == window_controls.enter_password.get():
                window_controls.current_user = check_user
                valid_details = True
                break
        
        if valid_details:
            window_controls.user_account_controller("Login")
        else:
            window_controls.enter_password.delete(0, len(window_controls.enter_password.get()))
            messagebox.showinfo("Login Unsuccessful", "Your Login Details were Incorrect, please try again")

    def logout() -> None:
        window_controls.destroy_all_frames()
        window_controls.current_frame = "Login"

        window_controls.current_user = None

        window_controls.login_controller()
        window_controls.clear_login_page()

    def valid_account_details(exempt_name: str) -> bool:
        new_username: str = window_controls.enter_username.get()
        new_password: str = window_controls.enter_password.get()

        window_back: colour = common_data.get_colour_from_name(window_controls.window_back.get())
        window_text: colour = common_data.get_colour_from_name(window_controls.window_text.get())
        label_back: colour = common_data.get_colour_from_name(window_controls.label_back.get())
        label_text: colour = common_data.get_colour_from_name(window_controls.label_text.get())
        button_back: colour = common_data.get_colour_from_name(window_controls.button_back.get())
        button_text: colour = common_data.get_colour_from_name(window_controls.button_text.get())
        entry_back: colour = common_data.get_colour_from_name(window_controls.entry_back.get())
        entry_text: colour = common_data.get_colour_from_name(window_controls.entry_text.get())

        valid_username: bool = window_controls.check_field(new_username, 5, 20, True) and window_controls.unique_username(new_username, exempt_name)
        valid_password: bool = window_controls.check_field(new_password, 5, 20, True)
        valid_details: bool = valid_username and valid_password

        valid_window_contrast: bool = window_controls.check_contrast_ratio(window_back.luminance, window_text.luminance)
        valid_label_contrast: bool = window_controls.check_contrast_ratio(label_back.luminance, label_text.luminance)
        valid_button_contrast: bool = window_controls.check_contrast_ratio(button_back.luminance, button_text.luminance)
        valid_entry_contrast: bool = window_controls.check_contrast_ratio(entry_back.luminance, entry_text.luminance)

        valid_winlab_contrast: bool = window_controls.check_contrast_ratio(window_back.luminance, label_back.luminance)
        valid_winbut_contrast: bool = window_controls.check_contrast_ratio(window_back.luminance, button_back.luminance)
        valid_winent_contrast: bool = window_controls.check_contrast_ratio(window_back.luminance, entry_back.luminance)

        valid_widget_contrasts: bool = valid_window_contrast and valid_label_contrast and valid_button_contrast and valid_entry_contrast
        valid_winwid_contrasts: bool = valid_winlab_contrast and valid_winbut_contrast and valid_winent_contrast

        if valid_details and valid_widget_contrasts and valid_winwid_contrasts:
            return True
        else:
            messagebox.showerror("Invalid Account Details", f"Account Details are Invalid\n\nBreakdown:\nValid Username: {valid_username}\nValid Password: {valid_password}\nValid Window Contrast: {valid_window_contrast}\nValid Button Contrast: {valid_button_contrast}\nValid Window-Button Contrast: {valid_winbut_contrast}")
            return False

    def create_account() -> None:
        new_user_id: str = window_controls.generate_user_id()
        
        if window_controls.valid_account_details(""):
            new_user_dict: dict = window_controls.make_dictionary(new_user_id, window_controls.enter_username.get(), window_controls.enter_password.get(), [[window_controls.window_back.get(), window_controls.window_text.get()], [window_controls.label_back.get(), window_controls.label_text.get()], [window_controls.button_back.get(), window_controls.button_text.get()], [window_controls.entry_back.get(), window_controls.entry_text.get()]], [0, []])

            new_user: user = user(new_user_dict)
            common_data.add_user(new_user)
            write_json_file(os.path.join(common_data.get_user_folder(), f"{new_user.user_id}.json"), new_user_dict)
            append_file(common_data.get_user_file(), f"{new_user.user_id}.json")

            window_controls.current_user = new_user

            window_controls.user_account_controller("Create Account")

    def update_account() -> None:
        if window_controls.valid_account_details(window_controls.current_user.username):
            window_controls.current_user.username = window_controls.enter_username.get()
            window_controls.current_user.password = window_controls.enter_password.get()

            window_controls.current_user.window_colours = [window_controls.window_back.get(), window_controls.window_text.get()]
            window_controls.current_user.label_colours = [window_controls.label_back.get(), window_controls.label_text.get()]
            window_controls.current_user.button_colours = [window_controls.button_back.get(), window_controls.button_text.get()]
            window_controls.current_user.entry_colours = [window_controls.entry_back.get(), window_controls.entry_text.get()]

            write_json_file(os.path.join(common_data.get_user_folder(), f"{window_controls.current_user.user_id}.json"), window_controls.current_user.make_dictionary())

            window_controls.create_account_page.configure(bg = common_data.get_colour_from_name(window_controls.window_back.get()).colour_code)
            window_controls.username_label.configure(bg = common_data.get_colour_from_name(window_controls.window_back.get()).colour_code)
            window_controls.password_label.configure(bg = common_data.get_colour_from_name(window_controls.window_back.get()).colour_code)

            messagebox.showinfo("Account Updated", "User Details Successfully Updated")

    def generate_user_id() -> str:
        user_list: list[user] = common_data.get_user_list()
        last_id: str = user_list[len(user_list) - 1].user_id

        return f"U{str(int(last_id.replace("U", "")) + 1).rjust(3, "0")}"

    def check_field(check_string: str, min_length: int, max_length: int, check_space: bool) -> bool:
        string_length: int = len(check_string)

        if string_length < min_length or string_length > max_length:
            return False
        
        if check_space and " " in check_string:
            return False
        
        if re.findall("[/*-+<>:;'#@~,.`¬!£$%^&*()=]", check_string):
            return False
        
        return True

    def unique_username(check_string: str, exempt_name: str) -> bool:
        for check_user in common_data.user_list:
            if check_user.username == check_string and check_user.username != exempt_name:
                return False
            
        return True

    def make_dictionary(id: str, name: str, password: str, colours: list[list[str]], scores: tuple[float, list[int]]) -> dict:
        previous_scores_dictionary: dict = {}

        for i in range(len(scores[1])):
            previous_scores_dictionary[f"Attempt {i + 1}"] = scores[1][i]

        return_dictionary = {
            "User ID Code" : id,
            "User Name" : name,
            "User Password" : password,
            "User Colours" : {
                "Window Background Colour" : colours[0][0],
                "Window Foreground Colour" : colours[0][1],
                "Label Background Colour" : colours[1][0],
                "Label Foreground Colour" : colours[1][1],
                "Button Background Colour" : colours[2][0],
                "Button Foreground Colour" : colours[2][1],
                "Entry Background Colour" : colours[3][0],
                "Entry Foreground Colour" : colours[3][1]
            },
            "High Score" : scores[0],
            "Previous Scores" : previous_scores_dictionary
        }

        return return_dictionary


    # Misc Functions

    def convert_to_colours(colours: list[str]) -> list[colour]:
        colour_a: colour = common_data.get_colour_from_name(colours[0])
        colour_b: colour = common_data.get_colour_from_name(colours[1])

        return [colour_a, colour_b]

    def kill_program() -> None:
        window_controls.window.destroy()


    # Old Create Account Functions
    
    def calculate_old_create_account_dimensions() -> str:
        page_width: int = (6 * window_design.spacer) + (2 * window_design.get_create_account_width())
        page_height: int = (6 * window_design.spacer) + (13 * (window_design.spacer + window_design.get_create_account_small_height())) + (window_design.spacer + window_design.get_create_account_large_height())

        return f"{page_width}x{page_height}"

    def make_old_create_account_page() -> None:
        window_controls.create_account_page = Toplevel(window_controls.window)

        window_colours: list[colour] = window_design.get_window_colours()
        button_colours: list[colour] = window_design.get_button_colours()
        entry_colours: list[colour] = window_design.get_entry_colours()

        width: int = window_design.get_create_account_width()
        small_height: int = window_design.get_create_account_small_height()
        large_height: int = window_design.get_create_account_large_height()

        window_controls.create_account_page.geometry(window_controls.calculate_old_create_account_dimensions())
        window_controls.create_account_page.config(bg = window_colours[0].colour_code)

        # Enter Username
        username_label: Label = Label(window_controls.create_account_page, text = "Username:", bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, font = window_design.main_font)
        username_label.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer), width = width, height = small_height)

        window_controls.enter_username = Entry(window_controls.create_account_page, bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        window_controls.enter_username.place(x = (2 * window_design.spacer), y = (2 * window_design.spacer) + (1 * (window_design.spacer + small_height)), width = width, height = small_height)

        # Enter Password
        password_label: Label = Label(window_controls.create_account_page, text = "Password:", bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, font = window_design.main_font)
        password_label.place(x = (4 * window_design.spacer) + width, y = (2 * window_design.spacer), width = width, height = small_height)

        window_controls.enter_password = Entry(window_controls.create_account_page, bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        window_controls.enter_password.place(x = (4 * window_design.spacer) + width, y = (2 * window_design.spacer) + (1 * (window_design.spacer + small_height)), width = width, height = small_height)

        colour_name_list: list[str] = []

        for colour_option in common_data.get_colour_list():
            colour_name_list.append(colour_option.colour_name)

        # Choose Window Colours
        window_colours_x_value: int = (2 * window_design.spacer)
        window_colours_header: Label = Label(window_controls.create_account_page, text = "Select Window Colours:", bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        window_colours_header.place(x = window_colours_x_value, y = (4 * window_design.spacer) + (2 * (window_design.spacer + small_height)), width = width, height = small_height)

        window_back_label: Label = Label(window_controls.create_account_page, text = "Select Background Colour:", bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, font = window_design.main_font)
        window_back_label.place(x = window_colours_x_value, y = (4 * window_design.spacer) + (3 * (window_design.spacer + small_height)), width = width, height = small_height)

        window_controls.window_back = StringVar()
        window_controls.select_window_back = ttk.Combobox(window_controls.create_account_page, textvariable = window_controls.window_back)
        window_controls.select_window_back['values'] = colour_name_list
        window_controls.select_window_back.current(common_data.get_colour_index_from_name(window_colours[0].colour_name))
        window_controls.select_window_back.place(x = window_colours_x_value, y = (3 * window_design.spacer) + (4 * (window_design.spacer + small_height)), width = width, height = small_height)

        window_text_label: Label = Label(window_controls.create_account_page, text = "Select Text Colour:", bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, font = window_design.main_font)
        window_text_label.place(x = window_colours_x_value, y = (3 * window_design.spacer) + (5 * (window_design.spacer + small_height)), width = width, height = small_height)

        window_controls.window_text = StringVar()
        window_controls.select_window_text = ttk.Combobox(window_controls.create_account_page, textvariable = window_controls.window_text)
        window_controls.select_window_text['values'] = colour_name_list
        window_controls.select_window_text.current(common_data.get_colour_index_from_name(window_colours[1].colour_name))
        window_controls.select_window_text.place(x = window_colours_x_value, y = (2 * window_design.spacer) + (6 * (window_design.spacer + small_height)), width = width, height = small_height)

        window_controls.window_colours_contrast = Label(window_controls.create_account_page, text = "Colour Contrast Ratio:\nN/A", bg = window_colours[1].colour_code, fg = window_colours[0].colour_code, font = window_design.main_font)
        window_controls.window_colours_contrast.place(x = window_colours_x_value, y = (4 * window_design.spacer) + (7 * (window_design.spacer + small_height)), width = width, height = large_height)

        calculate_window_ratio: Button = Button(window_controls.create_account_page, text = "Calculate Contrast Ratio", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.set_contrast_ratio, "Window"))
        calculate_window_ratio.place(x = window_colours_x_value, y = (4 * window_design.spacer) + (7 * (window_design.spacer + small_height)) + (window_design.spacer + large_height), width = width, height = small_height)

        invert_window_colours: Button = Button(window_controls.create_account_page, text = "Invert Colours", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.invert_colours, "Window"))
        invert_window_colours.place(x = window_colours_x_value, y = (4 * window_design.spacer) + (8 * (window_design.spacer + small_height)) + (window_design.spacer + large_height), width = width, height = small_height)

        # Choose Button Colours
        button_colours_x_value: int = (4 * window_design.spacer) + width
        window_colours_header: Label = Label(window_controls.create_account_page, text = "Select Window Colours:", bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        window_colours_header.place(x = button_colours_x_value, y = (4 * window_design.spacer) + (2 * (window_design.spacer + small_height)), width = width, height = small_height)

        window_back_label: Label = Label(window_controls.create_account_page, text = "Select Background Colour:", bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, font = window_design.main_font)
        window_back_label.place(x = button_colours_x_value, y = (4 * window_design.spacer) + (3 * (window_design.spacer + small_height)), width = width, height = small_height)

        window_controls.button_back = StringVar()
        window_controls.select_button_back = ttk.Combobox(window_controls.create_account_page, textvariable = window_controls.button_back)
        window_controls.select_button_back['values'] = colour_name_list
        window_controls.select_button_back.current(common_data.get_colour_index_from_name(button_colours[0].colour_name))
        window_controls.select_button_back.place(x = button_colours_x_value, y = (3 * window_design.spacer) + (4 * (window_design.spacer + small_height)), width = width, height = small_height)

        window_text_label: Label = Label(window_controls.create_account_page, text = "Select Text Colour:", bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, font = window_design.main_font)
        window_text_label.place(x = button_colours_x_value, y = (3 * window_design.spacer) + (5 * (window_design.spacer + small_height)), width = width, height = small_height)

        window_controls.button_text = StringVar()
        window_controls.select_button_text = ttk.Combobox(window_controls.create_account_page, textvariable = window_controls.button_text)
        window_controls.select_button_text['values'] = colour_name_list
        window_controls.select_button_text.current(common_data.get_colour_index_from_name(button_colours[1].colour_name))
        window_controls.select_button_text.place(x = button_colours_x_value, y = (2 * window_design.spacer) + (6 * (window_design.spacer + small_height)), width = width, height = small_height)

        window_controls.button_colours_contrast = Label(window_controls.create_account_page, text = "Colour Contrast Ratio:\nN/A", bg = window_colours[1].colour_code, fg = window_colours[0].colour_code, font = window_design.main_font)
        window_controls.button_colours_contrast.place(x = button_colours_x_value, y = (4 * window_design.spacer) + (7 * (window_design.spacer + small_height)), width = width, height = large_height)

        calculate_window_ratio: Button = Button(window_controls.create_account_page, text = "Calculate Contrast Ratio", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.old_set_contrast_ratio, "Button"))
        calculate_window_ratio.place(x = button_colours_x_value, y = (4 * window_design.spacer) + (7 * (window_design.spacer + small_height)) + (window_design.spacer + large_height), width = width, height = small_height)

        invert_window_colours: Button = Button(window_controls.create_account_page, text = "Invert Colours", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.old_invert_colours, "Button"))
        invert_window_colours.place(x = button_colours_x_value, y = (4 * window_design.spacer) + (8 * (window_design.spacer + small_height)) + (window_design.spacer + large_height), width = width, height = small_height)

        randomise_colours_button: Button = Button(window_controls.create_account_page, text = "Randomise Colours", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.old_randomise_colours)
        randomise_colours_button.place(x = window_colours_x_value, y = (4 * window_design.spacer) + (9 * (window_design.spacer + small_height)) + (window_design.spacer + large_height), width = 2 * (window_design.spacer + width), height = small_height)

        # Controls
        control_row: int = (5 * window_design.spacer) + (10 * (window_design.spacer + small_height)) + (window_design.spacer + large_height)

        create_account_button: Button = Button(window_controls.create_account_page, text = "Create Account", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.create_account)
        create_account_button.place(x = (2 * window_design.spacer), y = control_row, width = 2 * (window_design.spacer + width), height = small_height)

        control_row_2: int = control_row + (window_design.spacer + small_height)

        clear_button: Button = Button(window_controls.create_account_page, text = "Clear", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.clear_create_account_page)
        clear_button.place(x = (2 * window_design.spacer), y = control_row_2, width = 2 * (window_design.spacer + width), height = small_height)

        back_button: Button = Button(window_controls.create_account_page, text = "Back", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.go_back)
        back_button.place(x = (2 * window_design.spacer), y = control_row_2 + (window_design.spacer + small_height), width = width, height = small_height)

        exit_button: Button = Button(window_controls.create_account_page, text = "Exit", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = window_controls.kill_program)
        exit_button.place(x = (4 * window_design.spacer) + width, y = control_row_2 + (window_design.spacer + small_height), width = width, height = small_height)



"""
    def choose_colour_pair(colour_pair: str) -> list[StringVar]:
        colour_name_list: list[str] = []

        for colour_option in common_data.get_colour_list():
            colour_name_list.append(colour_option.colour_name)

        window_colours: list[colour] = window_design.get_window_colours()
        label_colours: list[colour] = window_design.get_label_colours()
        button_colours: list[colour] = window_design.get_button_colours()
        entry_colours: list[colour] = window_design.get_entry_colours()

        width: int = window_design.get_choose_colours_width()
        small_height: int = window_design.get_choose_colours_small_height()
        large_height: int = window_design.get_choose_colours_large_height()

        x_value: int
        y_value: int

        set_back: str
        set_text: str

        column_1: int = (2 * window_design.spacer)
        column_2: int = (6 * window_design.spacer) + width

        row_1: int = (4 * window_design.spacer) + small_height
        row_2: int = (5 * window_design.spacer) + (8 * (window_design.spacer + small_height)) + (window_design.spacer + large_height)

        match colour_pair:
            case "Window":
                x_value = column_1
                y_value = row_1

#                set_back = common_data.get_colour_index_from_name(window_colours[0].colour_name); set_text = common_data.get_colour_index_from_name(window_colours[1].colour_name)
                set_back = window_colours[0].colour_name; set_text = window_colours[1].colour_name
            case "Label":
                x_value = column_2
                y_value = row_1

#                set_back = common_data.get_colour_index_from_name(label_colours[0].colour_name); set_text = common_data.get_colour_index_from_name(label_colours[1].colour_name)
                set_back = label_colours[0].colour_name; set_text = label_colours[1].colour_name
            case "Button":
                x_value = column_1
                y_value = row_2

#                set_back = common_data.get_colour_index_from_name(button_colours[0].colour_name); set_text = common_data.get_colour_index_from_name(button_colours[1].colour_name)
                set_back = button_colours[0].colour_name; set_text = button_colours[1].colour_name
            case "Entry":
                x_value = column_2
                y_value = row_2

#                set_back = common_data.get_colour_index_from_name(entry_colours[0].colour_name); set_text = common_data.get_colour_index_from_name(entry_colours[1].colour_name)
                set_back = entry_colours[0].colour_name; set_text = entry_colours[1].colour_name

        back_colour = StringVar()
        text_colour = StringVar()

        # Choose Colours
        window_colours_header: Label = Label(window_controls.colour_selector_page, text = f"Select {colour_pair} Colours:", bg = entry_colours[0].colour_code, fg = entry_colours[1].colour_code, font = window_design.main_font)
        window_colours_header.place(x = x_value, y = y_value, width = width, height = small_height)

        window_back_label: Label = Label(window_controls.colour_selector_page, text = "Select Background Colour:", bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, font = window_design.main_font)
        window_back_label.place(x = x_value, y = y_value + (1 * (window_design.spacer + small_height)), width = width, height = small_height)

        #window_controls.window_back = StringVar()
        select_back = ttk.Combobox(window_controls.colour_selector_page, textvariable = back_colour)
        select_back['values'] = colour_name_list
        #back_colour.set(set_back)
        #select_back.current(common_data.get_colour_index_from_name(set_back))
        select_back.place(x = x_value, y = y_value + (2 * (window_design.spacer + small_height)) - window_design.spacer, width = width, height = small_height)

        window_text_label: Label = Label(window_controls.colour_selector_page, text = "Select Text Colour:", bg = window_colours[0].colour_code, fg = window_colours[1].colour_code, font = window_design.main_font)
        window_text_label.place(x = x_value, y = y_value + (3 * (window_design.spacer + small_height)) - window_design.spacer, width = width, height = small_height)

        #window_controls.window_text = StringVar()
        select_text = ttk.Combobox(window_controls.colour_selector_page, textvariable = text_colour)
        select_text['values'] = colour_name_list
        #text_colour.set(set_text)
        #select_text.current(common_data.get_colour_index_from_name(set_text))
        select_text.place(x = x_value, y = y_value + (4 * (window_design.spacer + small_height)) - (2 * window_design.spacer), width = width, height = small_height)

        window_colour_contrast = Label(window_controls.colour_selector_page, text = "Colour Contrast Ratio:\nN/A", bg = window_colours[1].colour_code, fg = window_colours[0].colour_code, font = window_design.main_font)
        window_colour_contrast.place(x = x_value, y = y_value + (5 * (window_design.spacer + small_height)), width = width, height = large_height)

        calculate_window_ratio: Button = Button(window_controls.colour_selector_page, text = "Calculate Contrast Ratio", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.set_contrast_ratio, window_colour_contrast, back_colour.get(), text_colour.get()))
        calculate_window_ratio.place(x = x_value, y = y_value + (5 * (window_design.spacer + small_height)) + (window_design.spacer + large_height), width = width, height = small_height)

        invert_window_colours: Button = Button(window_controls.colour_selector_page, text = "Invert Colours", bg = button_colours[0].colour_code, fg = button_colours[1].colour_code, font = window_design.main_font, command = functools.partial(window_controls.invert_colours, back_colour, text_colour))
        invert_window_colours.place(x = x_value, y = y_value + (6 * (window_design.spacer + small_height)) + (window_design.spacer + large_height), width = width, height = small_height)

        #return [back_colour, text_colour]

    def old_randomise_colours() -> None:
        colour_list: list[colour] = common_data.get_colour_list()
        window_controls.window_back.set(colour_list[random.randint(1, len(colour_list)) - 1].colour_name)
        window_controls.window_text.set(colour_list[random.randint(1, len(colour_list)) - 1].colour_name)
        window_controls.button_back.set(colour_list[random.randint(1, len(colour_list)) - 1].colour_name)
        window_controls.button_text.set(colour_list[random.randint(1, len(colour_list)) - 1].colour_name)

    def old_clear_create_account_page() -> None:
        window_controls.clear_login_page()

        window_controls.window_back.set(window_design.get_default_window_colours()[0].colour_name)
        window_controls.window_text.set(window_design.get_default_window_colours()[1].colour_name)
        window_controls.button_back.set(window_design.get_default_button_colours()[0].colour_name)
        window_controls.button_text.set(window_design.get_default_button_colours()[1].colour_name)

        window_controls.window_colours_contrast.configure(text = f"Colour Contrast Ratio:\nN/A", bg = window_design.get_default_window_colours()[1].colour_code, fg = window_design.get_default_window_colours()[0].colour_code)
        window_controls.button_colours_contrast.configure(text = f"Colour Contrast Ratio:\nN/A", bg = window_design.get_default_window_colours()[1].colour_code, fg = window_design.get_default_window_colours()[0].colour_code)
"""