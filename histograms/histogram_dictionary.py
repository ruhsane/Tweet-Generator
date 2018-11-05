def histogram():
    histogram_dict = {}
    with open('/Users/ruhsane/dev/courses/cs1.2/tweet-generator/histograms/source.txt','r') as f:
        for line in f:
            for word in line.split():
                if word in histogram_dict:
                    histogram_dict[word] += 1
                else:
                    histogram_dict[word]=1
    return histogram_dict

def unique_words(histogram):
    unique = len(histogram.keys())
    print("there are {} unique words".format(unique))

def frequency(word, histogram):
    print("{} appears {} times".format(word, histogram.get(word)))

if __name__ == "__main__":
    print(histogram())
    unique_words(histogram())
    frequency("fish", histogram())
