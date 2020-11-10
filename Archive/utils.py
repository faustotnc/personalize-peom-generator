import readline
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import nltk


def questionLoop(question, message=None, condition=None):
    """
    This is a helper function to keep asking for user input
    given that a certain condition has not been met.

    :question (string) The question that will be displayed to the user
    :message (string) The message displayed to the user if the condition is not met
    :condition (lambda x) A lambda function that returns true if the condition is met
        given the answer x, and false if the condition is not met.
    """

    while True:
        answer = input(question + "\n>> ")

        if condition != None and not condition(answer):
            if message:
                print(message)
        else:
            break

    return answer


# Init the Wordnet Lemmatizer
Lemmatizer = WordNetLemmatizer()


def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""

    tag = nltk.pos_tag([word])[0][1][0].upper()

    tag_dict = {
        "J": wordnet.ADJ,
        "N": wordnet.NOUN,
        "V": wordnet.VERB,
        "R": wordnet.ADV
    }

    wn = wordnet.NOUN

    return tag_dict.get(tag, wn)


def Lemmatize(words):
    if type(words) == str:
        return Lemmatizer.lemmatize(words, get_wordnet_pos(words))
    else:
        return [Lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in words]


class textColors:
    """
    Helper class to show text with colors in the console.
    """

    HEADER_COLOR = '\033[95m'
    OKBLUE_COLOR = '\033[1;49;94m'
    OKGREEN_COLOR = '\033[92m'
    WARNING_COLOR = '\033[38;5;214m'
    FAIL_COLOR = '\033[91m'
    ENDC_COLOR = '\033[0m'
    BOLD_FORMAT = '\033[1m'
    UNDERLINE_FORMAT = '\033[4m'

    # Colors by name
    colornames = {
        "cyan": "\033[0;49;36m",
        "red": "\033[38;5;124m",
        "orange": "\033[38;5;166m",
        "yellow": "\033[38;5;184m",
        "green": "\033[38;5;70m",
        "blue": "\033[38;5;33m",
        "violet": "\033[38;5;134m",
        "brown": "\033[38;5;94m",
        "grey": "\033[38;5;244m",
    }

    def __init__(self):
        pass

    def colorize(self, color_name, string):
        return self.colornames.get(color_name) + string + self.ENDC_COLOR

    def header(self, string):
        return self.HEADER_COLOR + string + self.ENDC_COLOR

    def okBlue(self, string):
        return self.OKBLUE_COLOR + string + self.ENDC_COLOR

    def okGreen(self, string):
        return self.OKGREEN_COLOR + string + self.ENDC_COLOR

    def warning(self, string):
        return self.WARNING_COLOR + string + self.ENDC_COLOR

    def fail(self, string):
        return self.FAIL_COLOR + string + self.ENDC_COLOR

    def bold(self, string):
        return self.BOLD_FORMAT + string + self.ENDC_COLOR

    def underline(self, string):
        return self.UNDERLINE_FORMAT + string + self.ENDC_COLOR
