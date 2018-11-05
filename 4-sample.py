import random
from histograms.histogram_dictionary import histogram

def sample_pure_random(histogram):
    return random.choice(list(histogram.keys()))

def sample_by_frequency(histogram):
    words=[]
    for word in histogram:
        for i in range(histogram[word]):
            words.append(word)
    return random.choice(words)

def test_pure(histogram):
    #prints how many times each word was chosen when we randomly pick from the words for 1000 times
    #result shows that each word was randomized around 200 times which proves it is purely randomized
    result = {}
    for i in range(1000):
        randomized_word = sample_pure_random(histogram)
        if randomized_word in result:
            result[randomized_word] += 1
        else:
            result[randomized_word] = 1
    return result

def test_weighted(histogram):
    result = {}
    for i in range(10000):
        randomized_word = sample_by_frequency(histogram)
        if randomized_word in result:
            result[randomized_word] += 1
        else:
            result[randomized_word] = 1
    return result

if __name__ == "__main__":
    histogram = histogram()
    print("Pure Randomized:")
    print(test_pure(histogram))
    print("Weighted Randomized:")
    print(test_weighted(histogram))
