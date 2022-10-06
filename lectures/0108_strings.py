# strings
# Строки, срезы

text = 'the quick brown fox jumps over the lazy dog'

# help(text.istitle) 

print(text[0]) # t
print(text[0]) # h
# print(text[len(text)]) #IndexError
print(text[len(text)-1]) # g
print(text[-5]) # y
print(text[0:2]) # th
print(text[:2])
print(text[len(text)-2:]) # og
print(text[4:9]) # quick
print(text[4:-18]) # quick brown fox jumps
print()
print(text[::6]) # every 6th symbol

