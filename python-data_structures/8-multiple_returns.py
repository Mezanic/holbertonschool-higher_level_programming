#!/usr/bin/python3
def multiple_returns(sentence):
   
    if len(sentence) <= 0:
        last_char = "None"

    return (len(sentence), sentence[0])
