from utils import questionLoop, textColors

# Creates a new text colors instance
text = textColors()


class AskUserInfo:
    """
    Asks for the basic user info needed to personalize the generated poem.
    """

    def __init__(self):
        self.data_iterator = []

        self.data_iterator.append(self.ask_name())
        self.data_iterator.append(self.ask_age())
        self.data_iterator.append(self.ask_gender())
        self.data_iterator.append(self.ask_fav_color())

    def __iter__(self):
        return iter(self.data_iterator)

    def ask_name(self):
        """
        Asks for the user's name.
        """

        return questionLoop(
            question=text.okBlue("\nWhat is your name?"),
            message=text.fail("\nPlease provide a valid name"),
            condition=lambda answer: answer.isalpha()
        )

    def ask_age(self):
        """
        Asks for the user's age.
        """

        age = questionLoop(
            question=text.okBlue("\nWhat is your age?"),
            message=text.fail("\nPlease enter a valid age"),
            condition=lambda answer: answer.isdigit()
        )
        return age

    def ask_gender(self):
        """
        Asks for the user's gender.
        """

        gender = questionLoop(
            question=text.okBlue(
                "\nWhat is your gender?\n" +
                text.colorize("grey", "\n1) Male") +
                text.colorize("grey", "\n2) Female\n")
            ),
            message=text.warning("\nPlease select the gender that most closely describes you."),
            condition=lambda g: self.__gender_condition(g)
        )

        if gender == "male" or gender == 1:
            return "male"
        else:
            return "female"

    def __gender_condition(self, gender):
        if (gender.isalpha() and (gender.lower() == "male" or gender.lower() == "female")):
            return True
        elif (gender.isdigit() and (int(gender) == 1 or int(gender) == 2)):
            return True

        return False

    def ask_fav_color(self):
        """
        Asks for the user's favorite color.
        """

        color = questionLoop(
            question=text.okBlue(
                "\nSelect the color that best approximates your favorite color:\n" +
                text.colorize("grey", "\n1) Red\n" +
                              "2) Orange\n" +
                              "3) Yellow\n" +
                              "4) Green\n" +
                              "5) Blue\n" +
                              "6) Violet\n" +
                              "7) Brown\n")
            ),
            message=text.fail("\nPlease select a color from the options."),
            condition=lambda c: self.__fav_colo_condition(c)
        )

        if color.isdigit():
            colors = ["red", "orange", "yellow", "green", "blue", "violet", "brown"]
            return colors[int(color) - 1]
        else:
            return color

    def __fav_colo_condition(self, color):
        colors = ["red", "orange", "yellow", "green", "blue", "violet", "brown"]

        if (color.isdigit() and int(color) >= 1 and int(color) <= len(colors)):
            return True
        elif (color.isalpha() and color.lower() in colors):
            return True

        return False
