from colour import colour

class window_design:
    # Default Colours

    window_colours: list[colour]
    label_colours: list[colour]
    button_colours: list[colour]
    entry_colours: list[colour]

    minimum_contrast_ratio: float = 4.5


    # Fonts

    main_font: tuple[str, int]


    # Answer Colours

    correct_answer_colours: list[colour]
    incorrect_answer_colours: list[colour]
    double_wrong_answer_colours: list[colour]


    # Generic Sizes

    spacer: int


    # Login Page Sizes

    login_widget_width: int
    login_widget_height: int


    # Create Account Page Sizes

    create_account_small_width: int
    create_account_small_height: int
    create_account_large_height: int


    # Choose Colours Page Sizes

    choose_colours_small_width: int
    choose_colours_small_height: int
    choose_colours_large_height: int


    # User Account Page Sizes

    user_account_small_width: int
    user_account_small_height: int
    user_account_large_height: int


    # Colour Editor Page Sizes

    colour_editor_small_width: int
    colour_editor_small_height: int
    colour_editor_large_height: int
    colour_editor_listbox_item_height: int
    colour_editor_listbox_visible_items: int


    # View Account Page Sizes

    view_account_small_width: int
    view_account_small_height: int
    view_account_listbox_item_height: int
    view_account_listbox_visible_items: int


    # Audio Editor Page Sizes

    audio_editor_small_width: int
    audio_editor_small_height: int
    audio_editor_large_height: int
    audio_editor_listbox_item_height: int
    audio_editor_listbox_visible_items: int


    # Question List Page Sizes

    question_list_small_width: int
    question_list_button_width: int
    question_list_small_height: int


    # Question List Page Sizes

    question_editor_small_width: int
    question_editor_small_height: int
    question_editor_large_height: int


    # Choose Answer Colours Page Sizes

    choose_answer_colours_small_width: int
    choose_answer_colours_small_height: int
    choose_answer_colours_large_height: int


    # Setup Quiz Page Sizes

    setup_quiz_width: int
    setup_quiz_small_height: int
    setup_quiz_large_height: int

    
    # Question Page Sizes

    question_page_width: int
    question_page_difficulty_width: int
    question_page_small_height: int
    question_page_large_height: int


    # Default Window Design Controls

    def set_window_colours(new_window_colours: list[colour]) -> None:
        window_design.window_colours = new_window_colours
    
    def get_window_colours() -> list[colour]:
        return window_design.window_colours
    
    def set_label_colours(new_label_colours: list[colour]) -> None:
        window_design.label_colours = new_label_colours
    
    def get_label_colours() -> list[colour]:
        return window_design.label_colours
    
    def set_button_colours(new_button_colours: list[colour]) -> None:
        window_design.button_colours = new_button_colours
    
    def get_button_colours() -> list[colour]:
        return window_design.button_colours
    
    def set_entry_colours(new_entry_colours: list[colour]) -> None:
        window_design.entry_colours = new_entry_colours
    
    def get_entry_colours() -> list[colour]:
        return window_design.entry_colours
    
    def set_minimum_contrast_ratio(new_ratio: float) -> None:
        window_design.minimum_contrast_ratio = new_ratio

    def get_minimum_contrast_ratio() -> float:
        return window_design.minimum_contrast_ratio


    # Font Controls
    
    def set_main_font(new_font: tuple[str, int]) -> None:
        window_design.main_font = new_font

    def get_main_font() -> tuple[str, int]:
        return window_design.main_font
    

    # Answer Colour Controls

    def set_correct_answer_colours(new_back: colour, new_text: colour) -> None:
        window_design.correct_answer_colours = [new_back, new_text]

    def set_incorrect_answer_colours(new_back: colour, new_text: colour) -> None:
        window_design.incorrect_answer_colours = [new_back, new_text]

    def set_double_wrong_answer_colours(new_back: colour, new_text: colour) -> None:
        window_design.double_wrong_answer_colours = [new_back, new_text]


    # Generic Size Controls

    def set_spacer(new_spacer: int) -> None:
        window_design.spacer = new_spacer


    # Login Page Size Controls

    def set_login_width(new_width: int) -> None:
        window_design.login_widget_width = new_width

    def get_login_width() -> int:
        return window_design.login_widget_width
    
    def set_login_height(new_height: int) -> None:
        window_design.login_widget_height = new_height

    def get_login_height() -> int:
        return window_design.login_widget_height


    # Create Account Size Controls

    def set_create_account_width(new_width: int) -> None:
        window_design.create_account_small_width = new_width

    def get_create_account_width() -> int:
        return window_design.create_account_small_width
    
    def set_create_account_small_height(new_height: int) -> None:
        window_design.create_account_small_height = new_height

    def get_create_account_small_height() -> int:
        return window_design.create_account_small_height
    
    def set_create_account_large_height(new_height: int) -> None:
        window_design.create_account_large_height = new_height

    def get_create_account_large_height() -> int:
        return window_design.create_account_large_height
    

    # Choose Colours Size Controls

    def set_choose_colours_width(new_width: int) -> None:
        window_design.choose_colours_small_width = new_width

    def get_choose_colours_width() -> int:
        return window_design.choose_colours_small_width
    
    def set_choose_colours_small_height(new_height: int) -> None:
        window_design.choose_colours_small_height = new_height

    def get_choose_colours_small_height() -> int:
        return window_design.choose_colours_small_height
    
    def set_choose_colours_large_height(new_height: int) -> None:
        window_design.choose_colours_large_height = new_height

    def get_choose_colours_large_height() -> int:
        return window_design.choose_colours_large_height


    # User Account Size Controls

    def set_user_account_width(new_width: int) -> None:
        window_design.user_account_small_width = new_width

    def get_user_account_width() -> int:
        return window_design.user_account_small_width
    
    def set_user_account_small_height(new_height: int) -> None:
        window_design.user_account_small_height = new_height

    def get_user_account_small_height() -> int:
        return window_design.user_account_small_height
    
    def set_user_account_large_height(new_height: int) -> None:
        window_design.user_account_large_height = new_height

    def get_user_account_large_height() -> int:
        return window_design.user_account_large_height
    

    # Colour Editor Size Controls

    def set_colour_editor_width(new_width: int) -> None:
        window_design.colour_editor_small_width = new_width

    def get_colour_editor_width() -> int:
        return window_design.colour_editor_small_width
    
    def set_colour_editor_small_height(new_height: int) -> None:
        window_design.colour_editor_small_height = new_height

    def get_colour_editor_small_height() -> int:
        return window_design.colour_editor_small_height
    
    def set_colour_editor_large_height(new_height: int) -> None:
        window_design.colour_editor_large_height = new_height

    def get_colour_editor_large_height() -> int:
        return window_design.colour_editor_large_height
    
    def set_colour_editor_listbox_item_height(new_height: int) -> None:
        window_design.colour_editor_listbox_item_height = new_height

    def get_colour_editor_listbox_item_height() -> int:
        return window_design.colour_editor_listbox_item_height
    
    def set_colour_editor_listbox_visible_items(new_height: int) -> None:
        window_design.colour_editor_listbox_visible_items = new_height

    def get_colour_editor_listbox_visible_items() -> int:
        return window_design.colour_editor_listbox_visible_items
    

    # View Account Size Controls

    def set_view_account_width(new_width: int) -> None:
        window_design.view_account_small_width = new_width

    def get_view_account_width() -> int:
        return window_design.view_account_small_width
    
    def set_view_account_small_height(new_height: int) -> None:
        window_design.view_account_small_height = new_height

    def get_view_account_small_height() -> int:
        return window_design.view_account_small_height
    
    def set_view_account_listbox_item_height(new_height: int) -> None:
        window_design.view_account_listbox_item_height = new_height

    def get_view_account_listbox_item_height() -> int:
        return window_design.view_account_listbox_item_height
    
    def set_view_account_listbox_visible_items(new_height: int) -> None:
        window_design.view_account_listbox_visible_items = new_height

    def get_view_account_listbox_visible_items() -> int:
        return window_design.view_account_listbox_visible_items
    

    # Audio Editor Size Controls

    def set_audio_editor_width(new_width: int) -> None:
        window_design.audio_editor_small_width = new_width

    def get_audio_editor_width() -> int:
        return window_design.audio_editor_small_width
    
    def set_audio_editor_small_height(new_height: int) -> None:
        window_design.audio_editor_small_height = new_height

    def get_audio_editor_small_height() -> int:
        return window_design.audio_editor_small_height
    
    def set_audio_editor_large_height(new_height: int) -> None:
        window_design.audio_editor_large_height = new_height

    def get_audio_editor_large_height() -> int:
        return window_design.audio_editor_large_height
    
    def set_audio_editor_listbox_item_height(new_height: int) -> None:
        window_design.audio_editor_listbox_item_height = new_height

    def get_audio_editor_listbox_item_height() -> int:
        return window_design.audio_editor_listbox_item_height
    
    def set_audio_editor_listbox_visible_items(new_height: int) -> None:
        window_design.audio_editor_listbox_visible_items = new_height

    def get_audio_editor_listbox_visible_items() -> int:
        return window_design.audio_editor_listbox_visible_items
    

    # Question List Size Controls

    def set_question_list_width(new_width: int) -> None:
        window_design.question_list_small_width = new_width

    def get_question_list_width() -> int:
        return window_design.question_list_small_width

    def set_question_list_button_width(new_width: int) -> None:
        window_design.question_list_button_width = new_width

    def get_question_list_button_width() -> int:
        return window_design.question_list_button_width
    
    def set_question_list_small_height(new_height: int) -> None:
        window_design.question_list_small_height = new_height

    def get_question_list_small_height() -> int:
        return window_design.question_list_small_height
    

    # Question Editor Size Controls

    def set_question_editor_width(new_width: int) -> None:
        window_design.question_editor_small_width = new_width

    def get_question_editor_width() -> int:
        return window_design.question_editor_small_width
    
    def set_question_editor_small_height(new_height: int) -> None:
        window_design.question_editor_small_height = new_height

    def get_question_editor_small_height() -> int:
        return window_design.question_editor_small_height
    
    def set_question_editor_large_height(new_height: int) -> None:
        window_design.question_editor_large_height = new_height

    def get_question_editor_large_height() -> int:
        return window_design.question_editor_large_height


    # Choose Answer Colours Size Controls

    def set_choose_answer_colours_width(new_width: int) -> None:
        window_design.choose_answer_colours_small_width = new_width

    def get_choose_answer_colours_width() -> int:
        return window_design.choose_answer_colours_small_width
    
    def set_choose_answer_colours_small_height(new_height: int) -> None:
        window_design.choose_answer_colours_small_height = new_height

    def get_choose_answer_colours_small_height() -> int:
        return window_design.choose_answer_colours_small_height
    
    def set_choose_answer_colours_large_height(new_height: int) -> None:
        window_design.choose_answer_colours_large_height = new_height

    def get_choose_answer_colours_large_height() -> int:
        return window_design.choose_answer_colours_large_height


    # Setup Quiz Size Controls

    def set_setup_quiz_width(new_width: int) -> None:
        window_design.setup_quiz_width = new_width

    def get_setup_quiz_width() -> int:
        return window_design.setup_quiz_width
    
    def set_setup_quiz_small_height(new_height: int) -> None:
        window_design.setup_quiz_small_height = new_height

    def get_setup_quiz_small_height() -> int:
        return window_design.setup_quiz_small_height
    
    def set_setup_quiz_large_height(new_height: int) -> None:
        window_design.setup_quiz_large_height = new_height

    def get_setup_quiz_large_height() -> int:
        return window_design.setup_quiz_large_height


    # Question Page Size Controls

    def set_question_page_width(new_width: int) -> None:
        window_design.question_page_width = new_width

    def get_question_page_width() -> int:
        return window_design.question_page_width

    def set_question_page_difficulty_width(new_width: int) -> None:
        window_design.question_page_difficulty_width = new_width

    def get_question_page_difficulty_width() -> int:
        return window_design.question_page_difficulty_width
    
    def set_question_page_small_height(new_height: int) -> None:
        window_design.question_page_small_height = new_height

    def get_question_page_small_height() -> int:
        return window_design.question_page_small_height
    
    def set_question_page_large_height(new_height: int) -> None:
        window_design.question_page_large_height = new_height

    def get_question_page_large_height() -> int:
        return window_design.question_page_large_height
