def histogram():
    histogram = []
    words = []
    with open("/Users/ruhsane/dev/courses/cs1.2/tweet-generator/histograms/source.txt") as f:
        for line in f:
            for word in line.split():
                words.append(word)

    for word in words:
        word_found = False
        if len(histogram):
            for sublist in histogram:
                if sublist[0] == word:
                    word_found = True
                    sublist[1] += 1
                    break
            if not word_found:
                histogram.append([word, 1])
        else:
            histogram.append([word, 1])
    return histogram

def unique_words(histogram):
    print("there are {} unique words.".format(len(histogram)))

def frequency(word, histogram):
    for sublist in histogram:
        if sublist[0] == word:
            time = sublist[1]
        else:
            continue
    print("{} appears {} times".format(word, time))

if __name__ == "__main__":
    print(histogram())
    unique_words(histogram())
    frequency("fish", histogram())
