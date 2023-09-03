#!/usr/bin/python3

text = "my name is Gideon. I am a swe: What do you want to know about me? I am here to answer all your questions."
tokens = []
start = 0
delim = ".:?"

while start < len(text):
    end = len(text)  # Initialize end to the end of the text
    for ch in delim:
        char_index = text.find(ch, start)
        if char_index != -1 and char_index < end:
            end = char_index + 1
    
    tokens.append(text[start:end].strip())
    start = end + 1

for token in tokens:
    print(token)
