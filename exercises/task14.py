def str_words(input_string):
    words = input_string.split(' ')
    word_count = len(words)
    unique_count = len(set(words))
    return [word_count, unique_count]

def main():
    input_string = input()
    [word_count, unique_count] = str_words(input_string)
    print(word_count, unique_count)


if __name__ == '__main__':
    main()
