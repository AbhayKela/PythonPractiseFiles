n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result=""
    for i in range(len(words)):
        result=result+words[i]
    return result

print join_strings(n)

####################################################################
print "---------===================----------"

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results=[]
    for numbers in lists:
        for i in numbers:
            results.append(i)
    return results


print flatten(n)

####################################################################
