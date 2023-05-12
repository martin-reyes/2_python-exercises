
def is_two(x):
    if int(x) == 2:
        return True
    else: 
        return False


def is_vowel(letter):
    if letter.lower() in ["a", "e", "i", "o", "u"]:
        return True
    else: 
        return False
    

def is_consonant(letter):
    return not is_vowel(letter)


def cap_first_letter(word):
    if is_consonant(word[0]):
        return word.capitalize()
    else:
        return word
    

def calculate_tip(tip_perc, bill):
    ## if we dont assume the right input throw this error
    # assert tip_perc >= 0 and bill>= 0: "numbers must be positive"
    # assert 0 <= tip_perc <= 1: "tip not between 0 and 1"
    return round(bill * tip_perc, 2)


def apply_discount(orig_price, disc_perc):
    return round(orig_price * (1 - disc_perc), 2)


def handle_commas(str_num):
    str_w_o_commas = "".join(str_num.split(','))
    return int(str_w_o_commas)


def get_letter_grade(grade):
    
    # could add asserts or check to make sure there is valid input
    
    letter_grade = ''
    
    if grade >= 90:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 75:
        letter_grade = 'C'
    elif grade >= 70:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    
    return letter_grade


def remove_vowels(word):
    vowels = "aeiouAEIOU"
    for letter in word:
        if letter in vowels:
            word = word.replace(letter, "")
    return word


import re

def normalize_name(name):
    # remove non-alphabet characters
    normalized = re.sub(r'\W+', ' ', name)
    
    # normalize whitespace and convert to lowercase
    normalized = normalized.strip().lower().replace(' ', '_')

    # remove numbers at the beginning
    if normalized[0].isdigit():  # remove numbers at the beginning
        normalized = re.sub(r'^\d+', '', normalized)
    return normalized


def cumulative_sum(numbers):
    return [sum(numbers[:i+1]) for i in range(len(numbers))]

