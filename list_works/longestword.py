# text="hello good goodmorning"

# words=text.split(" ")

# longest_word=max(words,key=lambda w:len(w))

# min_word=min(words,key=lambda w:len(w))


# print(min_word)

# get_len=lambda w:len(w)


text="hi is am hello good googmorning razal"

words=text.split(" ")

srt_words=sorted(words,key=lambda w:len(w),reverse=True)
print(srt_words)

