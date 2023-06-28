words = []
names = []
char = 'a'

def get_names() -> list:

    global names

    names_ = input('Enter the names of players, pls: ').split(sep=',')
    [names.append(name) for name in names_]


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

def is_cancelled(word) -> bool:
    if word == 'stop':
        return True
# Main method to run
def main():

    global char

    get_names()

    print(f'Start with symbol: {char}')

    while True:
        for name in names:

            print(f'Your turn, {name}')

            word = get_word()

            if is_word(word) and not is_cancelled(word):
                print(f'good word: {word}')
                words.append(word)
                char = word[len(word) - 1]
                continue
            elif not is_word(word) and not is_cancelled(word):
                print(f'bad word: {word}')
                continue
            else:
                print('Game over')
                exit(0)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
