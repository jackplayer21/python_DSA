import string


def caeser_algo(input_text, input_int, action_cd):
    alphabet_lower = {v: k for (k, v) in zip(range(1, 27), string.ascii_lowercase)}
    alphabet_upper = {v: k for (k, v) in zip(range(1, 27), string.ascii_uppercase)}
    res_word = ''
    if action_cd.lower() == 'enc':
        for s in input_text:
            if s.isupper():
                alpha_pos = alphabet_upper[s]
                res_pos = (alpha_pos + input_int) % 26
                res_alpha = list(filter(lambda x: alphabet_upper[x] == res_pos, alphabet_upper))[0]
                res_word += res_alpha
            elif s.islower():
                alpha_pos = alphabet_lower[s]
                res_pos = (alpha_pos + input_int) % 26
                res_alpha = list(filter(lambda x: alphabet_lower[x] == res_pos, alphabet_lower))[0]
                res_word += res_alpha
            else:
                res_word += str(s)
    elif action_cd.lower() == 'dec':
        input_int = 26 - input_int
        for s in input_text:
            if s.isupper():
                alpha_pos = alphabet_upper[s]
                res_pos = (alpha_pos + input_int) % 26
                res_alpha = list(filter(lambda x: alphabet_upper[x] == res_pos, alphabet_upper))[0]
                res_word += res_alpha
            elif s.islower():
                alpha_pos = alphabet_lower[s]
                res_pos = (alpha_pos + input_int) % 26
                res_alpha = list(filter(lambda x: alphabet_lower[x] == res_pos, alphabet_lower))[0]
                res_word += res_alpha
            else:
                res_word += str(s)
    else:
        print("Enter Correct Value of enc/dec")
    return res_word
