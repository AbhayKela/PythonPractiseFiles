def anti_vowel(text):
    text1= ''
    for letter in text:
        if not (letter in 'aeiouAEIOU'):
            text1 +=letter
    return text1
print anti_vowel("Hey You!")