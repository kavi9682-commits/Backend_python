word=input("Enter a word ")
result=""

for i in word:
    if i not in result:
        result+=i
print("The word after removing duplicate is",result)
