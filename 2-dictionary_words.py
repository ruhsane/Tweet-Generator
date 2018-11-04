import sys
import random

def read_file(content):
    f = open(content, 'r') # open file at URL
    content = f.read().splitlines() # split file up lines and add each linne to an array named 'content'
    f.close()
    return content

def generate_random(content, number):
    random_index = random.randrange(0,len(content))
    print(content[random_index], end=" ")

if __name__ == "__main__":
    content = read_file("/usr/share/dict/words")
    number = int(sys.argv[1])
    for x in range(number):
        generate_random(content, number)
