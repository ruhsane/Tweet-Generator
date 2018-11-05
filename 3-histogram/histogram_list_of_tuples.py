def histogram():
    histogram = []
    words = []
    with open("/Users/ruhsane/dev/courses/cs1.2/tweet-generator/3-histogram/source.txt") as f:
        for line in f:
            for word in line.split():
                words.append(word)

    for word in words:

        word_found = False
        if len(histogram):
            # if histogram is NOT emoty
            for i in range(len(histogram)):
                current_tup = histogram[i]
                if current_tup[0] == word:
                    # found the word:
                    word_found = True
                    freq_count = current_tup[1]
                    histogram[i] = (word, freq_count + 1)
                    break
            if not word_found:
                # word not found:
                histogram.append((word, 1))
        else:
            # if histogram is empty:
            histogram.append((word, 1))

    return histogram

def unique_words(histogram):
    print("there are {} unique words".format(len(histogram)))

def frequency(word, histogram):
    for i in range(len(histogram)):
        current_tup = histogram[i]
        if current_tup[0] == word:
            print("{} appears {} times.".format(word, current_tup[1]))

if __name__ == "__main__":
    print(histogram())
    unique_words(histogram())
    frequency("fish", histogram())
