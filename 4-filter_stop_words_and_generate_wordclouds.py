import string
from shutil import copyfile
import os
import operator
from nltk.corpus import stopwords
import multidict as multidict

import numpy as np

import os
import re
from PIL import Image
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

my_path = os.path.abspath(os.path.dirname(__file__))


def get_all_stopwords(character_names=True):
    stopwords = []
    for file in os.listdir("resources"):
        with open(os.path.join(my_path, "resources", file)) as infile:
            if file == "char_stopwords.txt":
                if character_names == False:
                    pass
                else:
                    words = []
                    w = [line.strip() for line in infile.readlines()]
                    stopwords.extend(words)
            else:
                words = []
                w = [line.strip() for line in infile.readlines()]
                stopwords.extend(words)
            return list(set(stopwords))


stopwords_mine = get_all_stopwords()


def add_nltk_stopwords_to_set(stopwords_mine):
    stopwords_nltk = set(stopwords.words("english"))
    stopwords_all_inclusive = stopwords_mine + list(stopwords_nltk)
    return stopwords_all_inclusive


stopwords_all_inclusive = add_nltk_stopwords_to_set(stopwords_mine)

root_keep = os.path.join(my_path, "data_char_lines_top_100")
os.chdir(root_keep)


def filter_words(wordlist):
    filteredwords = []
    for w in wordlist:
        w = w.lower()
        if not w.isalpha():
            w = "".join([char for char in w if char not in string.punctuation])
        ##    if w[-1:] in string.punctuation:
        ##      w = w[:-1]
        ##    elif w[0] in string.punctuation:
        ##      w = w[1:]
        filteredwords.append(w)
    return filteredwords


def remove_stopwords(words):
    stopwords_count = 0
    filteredwords = []
    for w in words:
        if w not in stopwords_all_inclusive:
            ##      if w not in stopwords_mine:
            filteredwords.append(w)
        elif w in stopwords_all_inclusive:
            stopwords_count += 1
    print(stopwords_count)
    return filteredwords


def count_words(words):
    d = {}
    for w in set(words):
        d[w] = words.count(w)
    return d


picard_words = {}
words = []
fname = ""
with open("PICARD.txt") as infile:
    w = infile.readlines()
    for line in w:
        lexs = line.split(" ")
        words.extend(lexs)
    fname, ext = "PICARD.txt".split(".")

print("now processing")

words = filter_words(words)
words = remove_stopwords(words)
w_dict = count_words(words)

sd = sorted(w_dict.items(), key=lambda x: x[1], reverse=True)


def makeImage(w_dict, fname):
    ##    alice_mask = np.array(Image.open("alice_mask.png"))
    trek_mask = np.array(Image.open(os.path.join(my_path, "trek_mask.png")))

    wc = WordCloud(
        background_color="white", max_words=1000, mask=trek_mask
    )  # mask=alice_mask)
    # generate word cloud
    wc.generate_from_frequencies(w_dict)
    ##    fname, _, ext = fname.split(".")
    fname = fname.capitalize()
    wc.to_file(os.path.join(my_path, ("{}.png".format(fname))))

    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.imshow(trek_mask, cmap=plt.cm.gray, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    # show


##    plt.imshow(wc, interpolation="bilinear")
##    plt.axis("off")
##    plt.show()
##    plt.savefig('{}.png'.format(fname), bbox_inches='tight')


# makeImage(w_dict, fname)
print(fname)

##main


def process_files():
    for file in os.listdir(root_keep):  # data_char_lines_top_100
        with open(os.path.join(root_keep, file), encoding="utf-8") as infile:
            words = []
            w = infile.readlines()
            for line in w:
                lexs = line.split(" ")
                words.extend(lexs)

                words = filter_words(words)
                words = remove_stopwords(words)
                words_dict = count_words(words)

                makeImage(words_dict, file)


##        print(len(words_dict.keys()))
##        for k, v in words_dict.items():
##          if v>10:
##            print(k, v)


process_files()
