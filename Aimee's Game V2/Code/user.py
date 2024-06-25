class user:
    def __init__(self, user_data) -> None:
        self.user_id: str = user_data["User ID Code"]
        self.username: str = user_data["User Name"]
        self.password: str = user_data["User Password"]

        self.window_colours: list[str] = [user_data["User Colours"]["Window Background Colour"], user_data["User Colours"]["Window Foreground Colour"]]
        self.label_colours: list[str] = [user_data["User Colours"]["Label Background Colour"], user_data["User Colours"]["Label Foreground Colour"]]
        self.button_colours: list[str] = [user_data["User Colours"]["Button Background Colour"], user_data["User Colours"]["Button Foreground Colour"]]
        self.entry_colours: list[str] = [user_data["User Colours"]["Entry Background Colour"], user_data["User Colours"]["Entry Foreground Colour"]]

        self.high_score: float = user_data["High Score"]
        self.previous_scores: list[int] = self.load_previous_scores(user_data["Previous Scores"])

        self.average_score: float = self.calculate_average_score()

    def load_previous_scores(self, previous_scores: dict) -> list[int]:
        return_list: list[int] = []
        score_keys: list[str] = list(previous_scores.keys())

        for score in score_keys:
            return_list.append(int(previous_scores[score]))
        
        return return_list
    
    def calculate_average_score(self) -> float:
        average: float = 0.0

        if len(self.previous_scores) > 0:
            for score in self.previous_scores:
                average += score

            average /= len(self.previous_scores)

        return average

    def make_dictionary(self) -> dict:
        previous_scores_dictionary: dict = {}

        for i in range(len(self.previous_scores)):
            previous_scores_dictionary[f"Attempt {i + 1}"] = self.previous_scores[i]

        return_dictionary: dict = {
            "User ID Code" : self.user_id,
            "User Name" : self.username,
            "User Password" : self.password,
            "User Colours" : {
                "Window Background Colour" : self.window_colours[0],
                "Window Foreground Colour" : self.window_colours[1],
                "Label Background Colour" : self.label_colours[0],
                "Label Foreground Colour" : self.label_colours[1],
                "Button Background Colour" : self.button_colours[0],
                "Button Foreground Colour" : self.button_colours[1],
                "Entry Background Colour" : self.entry_colours[0],
                "Entry Foreground Colour" : self.entry_colours[1]
            },
            "High Score" : self.high_score,
            "Previous Scores" : previous_scores_dictionary
        }

        return return_dictionary

    def get_colour_dictionary(self) -> dict:
        return_dictionary: dict = {
            "Window Background Colour" : self.window_colours[0],
            "Window Foreground Colour" : self.window_colours[1],
            "Label Background Colour" : self.label_colours[0],
            "Label Foreground Colour" : self.label_colours[1],
            "Button Background Colour" : self.button_colours[0],
            "Button Foreground Colour" : self.button_colours[1],
            "Entry Background Colour" : self.entry_colours[0],
            "Entry Foreground Colour" : self.entry_colours[1]
        }

        return return_dictionary
    
    def update_colours(self, colour_dict: dict) -> None:
        dict_keys: list[str] = list(colour_dict.keys())

        self.window_colours[0] = colour_dict[dict_keys[0]]
        self.window_colours[1] = colour_dict[dict_keys[1]]
        self.label_colours[0] = colour_dict[dict_keys[2]]
        self.label_colours[1] = colour_dict[dict_keys[3]]
        self.button_colours[0] = colour_dict[dict_keys[4]]
        self.button_colours[1] = colour_dict[dict_keys[5]]
        self.entry_colours[0] = colour_dict[dict_keys[6]]
        self.entry_colours[1] = colour_dict[dict_keys[7]]