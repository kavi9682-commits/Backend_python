word=input("Enter the word ")

word_list=list(word)
current=0

while current<len(word_list):
    nextpos=current+1
    while nextpos<len(word_list):
        temp=""
        if word_list[current]>word_list[nextpos]:
            temp=word_list[current]
            word_list[current]=word_list[nextpos]
            word_list[nextpos]=temp
        nextpos+=1
    current+=1

result=""

for i in word_list:
    result+=i
    
print("The sorted word is",result)