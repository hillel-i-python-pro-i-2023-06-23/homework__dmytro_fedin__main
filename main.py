is_cancelled = False
words = []
char = 'a'

def get_word() -> str:

    global words

    def set_word():
        word = input('Enter a word:')
        return word

    word = set_word()

    if type(word) == str:
        return word
    else:
        print('not a word(')
        return None

def is_word(word) -> bool:

    global words
    global  char
    def in_words(word_):
        if word_ in words:
            return True
        else:
            return False
    def has_char(word):
        if word[0] == char:
            return True
        else:
            False

    if not in_words(word) and has_char(word):
        return True
    else:
        return False
        pass

def is_cancelled(word):
    if word == 'stop':
        return True
# Main method to run
def main():
    while True:

        global  char

        word = get_word()

        print(words)
        print(f'char: {char}')

        if is_word(word):
            print(f'good word: {word}')
            words.append(word)
            char = word[len(word) - 1]

            print(f'char: {char}')
            continue
        elif not is_word(word):
            print(f'bad word: {word}')
            continue
        elif is_cancelled(word):
            break



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
