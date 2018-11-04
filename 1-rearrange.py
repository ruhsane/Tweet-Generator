import random

words = ["how","now","brown","cow"]


def random_python_word():
    new_words = []

    while len(new_words) != len(words):
        rand_index = random.randrange(0, len(words))

        if words[rand_index] not in new_words:
            new_words.append(words[rand_index])
        else:
            continue
    return new_words

if __name__ == '__main__':
    result = random_python_word()
    print(result)
