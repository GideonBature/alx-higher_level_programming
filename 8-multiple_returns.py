#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    if str_len == 0:
        return 0, None
    else:
        return str_len, sentence[0]
