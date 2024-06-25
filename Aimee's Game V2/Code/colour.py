class colour:
    def __init__(self, name: str, code: str) -> None:
        self.colour_name: str = name
        self.colour_code: str = code

        self.luminance: float
        self.rgb_values: list[float]
        self.calculate_relative_luminance()
         
    def calculate_rgb_values(self) -> None:
        colour_code = self.colour_code.replace("#", "")
        r_value = colour_code[0] + colour_code[1]
        g_value = colour_code[2] + colour_code[3]
        b_value = colour_code[4] + colour_code[5]

        r_value = int(r_value, 16) / 255
        g_value = int(g_value, 16) / 255
        b_value = int(b_value, 16) / 255

        self.rgb_values = [r_value, g_value, b_value]

    def calculate_relative_luminance(self) -> None:
        self.calculate_rgb_values()

        r_value = self.calculate_luminance(self.rgb_values[0])
        g_value = self.calculate_luminance(self.rgb_values[1])
        b_value = self.calculate_luminance(self.rgb_values[2])

        r_value = r_value * 0.2126
        g_value = g_value * 0.7152
        b_value = b_value * 0.0722

        self.luminance = r_value + g_value + b_value + 0.05

    def calculate_luminance(self, c_value) -> float:
        if c_value <= 0.03928:
            c_value = c_value / 12.92
        else:
            c_value = ((c_value + 0.055) / 1.055) ** 2.4

        return c_value

"""
def get_contrast_ratio(back_colour, text_colour):
  background_colour_code = get_colour(back_colour).get_colour_code()
  text_colour_code = get_colour(text_colour).get_colour_code()

  background_values = get_rgb_values(background_colour_code)
  text_values = get_rgb_values(text_colour_code)

  background_luminance = get_relative_luminance(background_values) + 0.05
  text_luminance = get_relative_luminance(text_values) + 0.05

  luminance_ratio = 0

  if text_luminance > background_luminance:
    luminance_ratio = round((text_luminance) / (background_luminance), 2)
  else:
    luminance_ratio = round(background_luminance / text_luminance, 2)

  return luminance_ratio


def get_rgb_values(colour_code):
  colour_code = colour_code.replace("#", "")
  r_value = colour_code[0] + colour_code[1]
  g_value = colour_code[2] + colour_code[3]
  b_value = colour_code[4] + colour_code[5]

  r_value = int(r_value, 16) / 255
  g_value = int(g_value, 16) / 255
  b_value = int(b_value, 16) / 255

  return [r_value, g_value, b_value]

def get_relative_luminance(rgb_values):
  r_value = get_luminance(rgb_values[0])
  g_value = get_luminance(rgb_values[1])
  b_value = get_luminance(rgb_values[2])

  r_value = r_value * 0.2126
  g_value = g_value * 0.7152
  b_value = b_value * 0.0722

  total_value = r_value + g_value + b_value

  return total_value

def get_luminance(c_value):
  if c_value <= 0.03928:
    c_value = c_value / 12.92
  else:
    c_value = ((c_value + 0.055) / 1.055) ** 2.4

  return c_value
"""