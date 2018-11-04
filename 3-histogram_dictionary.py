# config_file = '/Users/ruhsane/dev/courses/cs1.2/source.txt'
# import sys
# import os
#
# sys.path.append(os.path.dirname(config_file))

def histogram(source):
    dict_histogram = {}
    for word in source:
        # if the word is already in the dict, we increment its freqeuncy, else add 1 freq.
        if word in dict_histogram:
            dict_histogram[word] += 1
        else:
            dict_histogram[word] = 1

    return dict_histogram

def unique_words(histogram):
    return len(histogram)

def result():
    with open("/Users/ruhsane/dev/courses/cs1.2/tweet-generator/source.txt") as text_file:
         words = text_file.read().replace("\n", "").lower().split()
    created_histogram = histogram(words)
    print("{} There are {} unique words".format(created_histogram, unique_words(created_histogram)))

if __name__ == "__main__":
    result()
