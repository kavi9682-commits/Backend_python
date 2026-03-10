text= input("Enter the text ")
word_list=[]
word=""

for i in text:
    if i==" ":
        word_list.append(word)
        word=""
    else:
        word+=i
        
word_list.append(word)

removed_words=[]
for word in word_list:
    if word not in removed_words:
        removed_words.append(word)
        
result=""

for j in removed_words:
    result=result+j+" "
print(result)
