from utils import textColors, Lemmatize
import matplotlib.pyplot as plt
import pandas as pd
import nltk
import time


# Creates a new text colors instance
text = textColors()


class EmotionLabelingModel:
    def __init__(self):
        # Loads the EmoLex Dataset
        self.rawData = pd.read_csv("./datasets/NRC-Emotion-Intensity-Lexicon-v1/NRC-Emotion-Intensity-Lexicon-v1.txt", sep="\t")
        self.rawData = self.rawData.sample(frac=1)  # Randomizes the data

        print(text.header("\n\n:: Training Labeling Model..."))

        # # Extracts the words and the labels from the raw data
        self.words = Lemmatize(self.rawData["word"])
        self.labels = self.rawData["emotion"]
        self.scores = self.rawData["emotion-intensity-score"]

        self.emotion_map = dict()

        for w, l, s in zip(self.words, self.labels, self.scores):
            if (w not in self.emotion_map):
                self.emotion_map[w] = (l, s)
            else:
                # If the word is already present in the dictionary,
                # but now there is an emotion with a higher score
                # associated with that word, then we assign the new
                # emotion to the word.
                if (self.emotion_map[w][1] < s):
                    self.emotion_map[w] = (l, s)

        # Prints a success message after training this model
        time.sleep(0.2)
        print(text.okGreen(":: Labeling Model Trained!"))
        time.sleep(1)

    def guess_poem_emotion(self, poem):
        """
        Guesses the emotion of the passed poem string.
        """

        scores = dict()
        for word in nltk.word_tokenize(poem):
            if word.isalnum():
                word = Lemmatize(word.lower())

                if word in self.emotion_map:
                    emotion, score = self.emotion_map[word]

                    if emotion not in scores:
                        scores[emotion] = score
                    else:
                        scores[emotion] += score

        scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        return scores[0] if len(scores) > 0 else ("**UNKNOWN**", 1)

    def show_labels_freq(self):
        """
        Displays a plot with the 8 different emotions in the
        x-axis, and the frequency of each emotion in the training
        dataset in the y-axis.
        """

        freq = nltk.FreqDist(self.labels)

        plt.rcParams["figure.figsize"] = (10, 5)

        x, y = ([], [])
        for f in freq:
            x.append(f)
            y.append(freq[f])

        x_pos = [i for i, _ in enumerate(x)]

        plt.bar(x_pos, y, color='#2E8B57')
        plt.xlabel("Label")
        plt.ylabel("Frequency")
        plt.title("Frequency of Labels in EmoLex Data")

        plt.xticks(x_pos, x)

        plt.show()

    def show_word_freq(self):
        """
        Displays a plot with each unique word in the x-axis,
        and the frequency of each word in the training dataset
        in the y-axis.
        """

        freq = nltk.FreqDist(self.words).most_common(100)

        plt.rcParams["figure.figsize"] = (10, 5)

        x, y = ([], [])
        for w, f in freq:
            x.append("")
            y.append(f)

        x_pos = [i for i, _ in enumerate(x)]

        plt.bar(x_pos, y, color='#2E8B57')
        plt.xlabel("Label")
        plt.ylabel("Frequency")
        plt.title("Frequency of Labels in EmoLex Data")

        plt.xticks(x_pos, x)

        plt.show()
