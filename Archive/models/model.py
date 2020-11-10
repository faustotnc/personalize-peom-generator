import matplotlib.pyplot as plt
import pandas as pd
import nltk
import random
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

# Project-level modules
from models.EmotionLabelingModel import EmotionLabelingModel
from utils import textColors


# Creates a new text colors instance
text = textColors()


class Model:
    """
    This class will contain the model used for generating the poems.
    """

    def __init__(self):
        self.create_labeled_poems_dataset()

    def create_labeled_poems_dataset(self):
        # self.data = pd.read_csv("./datasets/PoetryFoundationData.csv")

        # # Creates a model for labeling poems based their emotion
        # self.LabelingModel = EmotionLabelingModel()

        # # Assigns an emotions to each poem in the dataset
        # print(text.header("\n\n:: Labeling Poems..."))
        # poemLabels = []
        # for poem in self.data["Poem"]:
        #     poemLabels.append(self.LabelingModel.guess_poem_emotion(poem)[0])

        #     # Prints a progress bar :)
        #     barLength = 50
        #     progress = round(len(poemLabels) / len(self.data) * 100)
        #     p = int((progress * barLength) / 100)
        #     bar = ("=" * p) + (" " * (barLength - p))
        #     print(f":: [{bar}] {str(progress)}% Done.", end="\r")

        # # Prints a success message after labeling the poems
        # print(text.okGreen(f":: [{bar}] {str(progress)}% Done."))

        # # Generates a new dataset file with the poems and their label
        # new_data = pd.DataFrame(data={
        #     "poem": self.data["Poem"],
        #     "emotion": poemLabels
        # })

        # new_data.to_csv("./datasets/LabeledPoetryFoundationPoems.csv")

        self.show_emotion_freq()

    def print_random_poem(self):
        index = random.randint(0, len(self.data))
        shown_poems = []

        while True:
            shown_poems.append(index)
            poem = self.data.iloc[index]

            print(poem["Poem"])
            print(poem["Emotion"])

            doNext = input("\n>>> Print next? Y/N")

            if (doNext.lower() == "n"):
                break

            # Clears the console
            print(chr(27)+'[2j')
            print('\033c')
            print('\x1bc')

            # Choose next poem, without repetition
            while True:
                newIndex = random.randint(0, len(self.data))
                if (newIndex in shown_poems):
                    continue
                else:
                    index = newIndex
                    break

    def show_emotion_freq(self):
        data = pd.read_csv("./datasets/LabeledPoetryFoundationPoems.csv")
        freq = nltk.FreqDist(data["emotion"])

        plt.rcParams["figure.figsize"] = (10, 5)

        x, y = ([], [])
        for f in freq:
            x.append(f)
            y.append(freq[f])

        x_pos = [i for i, _ in enumerate(x)]

        plt.bar(x_pos, y, color='#2E8B57')
        plt.xlabel("Emotion")
        plt.ylabel("Frequency")
        plt.title("Frequency of Emotions in Poem Data")

        plt.xticks(x_pos, x)

        plt.show()
