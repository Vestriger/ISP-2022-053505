import customstatistic

f = open("text.txt", "r")
text = f.read()
f.close()
print(customstatistic.medi(text))
print(customstatistic.average(text))
print(customstatistic.repetition(text))
customstatistic.topk_ngram(text)
