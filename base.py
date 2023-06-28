
def get_last_letter(string_):
    return string_[len(string_)-1]

def get_first_letter(string_):
    return string_[0]

def check_match(input_char, stored_char):
    if input_char == stored_char:
        return True
    else:
        return False