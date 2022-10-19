# document distance algorithm - the fastest version implemented with dictionaries.

# Program consern word "Hello" and "hello" as different words.
# Parsing methods as "str.maketrans" is not used, so words in a file append to a list in a default view.


import math
import string
import sys


# Operation 1: read a text file ##
def read_file(filename):
    try:
        f = open(filename, 'r')
        return f.read()
    except IOError:
        print ("Error opening or reading input file")
        sys.exit()

#Operation 2: split the text lines into words
def get_words_from_line_list(text):
    """
    Parse the given text into words.
    Return list of all words found.
    """
    word_list = text.split()
    return word_list

# Operation 3: count frequency of each word ##
def count_frequency(word_list):
    D = {}
    for new_word in word_list:
        if new_word in D:
            D[new_word] = D[new_word] + 1
        else:
            D[new_word] = 1
    return D

# Compute word frequencies for input file
def word_frequencies_for_file(filename):
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)

    print("File", filename, ":", )
    print(len(line_list), "lines,")
    print(len(word_list), "words,")
    print(len(freq_mapping), "distinct words")

    return freq_mapping # return a Dictionary

def inner_product(D1, D2):
    sum = 0.0

    for key in D1:
        if key in D2:
            sum += D1[key] * D2[key]
    return sum

def vector_angle(D1,D2):
    numerator = inner_product(D1, D2)
    denominator = math.sqrt(inner_product(D1, D1) * inner_product(D2, D2))
    return math.acos(numerator / denominator)

def main():
    print(len(sys.argv))

    filename_1 = "file1.txt"
    filename_2 = "file2.txt"
    sorted_word_list_1 = word_frequencies_for_file(filename_1)
    sorted_word_list_2 = word_frequencies_for_file(filename_2)
    distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
    print(f"The distance between the documents is: %{distance} (radians)")


if __name__ == "__main__":
    import profile
    profile.run("main()")
