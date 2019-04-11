def reverse(text):
    rev_string = []
    for i in range(len(text)-1,-1,-1):
        rev_string.append(text[i])

    return "".join(rev_string)
print reverse("Python!")