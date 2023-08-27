import string


def caesar_encryption(input_String=None, shift_int=0):
    alphabet_lower = {v: k for (k, v) in zip(range(1, 27), string.ascii_lowercase)}
    alphabet_upper = {v: k for (k, v) in zip(range(1, 27), string.ascii_uppercase)}
    res_string = ''
    for s in input_String:
        if s.isupper():
            alpha_pos = alphabet_upper[s]
            res_pos = (alpha_pos + shift_int) % 26
            res_alpha = list(filter(lambda x: alphabet_upper[x] == res_pos, alphabet_upper))[0]
            res_string += res_alpha
        elif s.islower():
            alpha_pos = alphabet_lower[s]
            res_pos = (alpha_pos + shift_int) % 26
            res_alpha = list(filter(lambda x: alphabet_lower[x] == res_pos, alphabet_lower))[0]
            res_string += res_alpha
        else:
            res_string += str(s)
        return res_string


def caesar_algo(input_text, input_int, action_cd):
    if action_cd.lower() == 'enc':
        result = caesar_encryption(input_text, input_int)
    elif action_cd.lower() == 'dec':
        result = caesar_encryption(input_text, 26 - input_int)
    else:
        print("Enter Correct Value of enc/dec")
    return result


# run sample
print(caesar_algo('helley746HELLO', 3, 'enc'))
