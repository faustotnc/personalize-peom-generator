
# Project-level modules
from ask_user_info import AskUserInfo
from models.model import Model

import time


class PoemGenerator:
    """
    The "motor" class for the application. From here, the different
    parts of the program get instantiated and executed.
    """

    def __init__(self):
        pass

    def run(self):
        """
        Runs all the different parts of the application with the
        end-goal of generating a poem conditioned on both user
        data and user preference.
        """

        print("\n=======================================================")
        print("✨ ✨  Welcome to the Personalized Poetry Generator ✨ ✨")
        print("=======================================================")
        print("\n:: Please answer the following questions to continue.\n")

        # Obtains the sentence used as input to the model
        # input_sentence = self.__get_input_sentence()

        # print("\n:: Great! We will use that information to personalize your poem.")
        # time.sleep(1)

        # print(":: We will now initialize our models.")
        # time.sleep(1)

        # Initializes the model
        m = Model()

    def __get_input_sentence(self):
        """
        Generates a sentence to be used as input for the
        model based on the obtained user information.
        """

        # Asks for the user information
        name, age, gender, fav_color = AskUserInfo()

        return f"{name} is a {age} year old {gender} whose favorite color is {fav_color}."
