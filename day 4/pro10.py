#write a python program to print word,count of the vowels in the word,list of the vowels in the word of the sentence using functions.
def counting(s):
    print(s)
    s1,vc='',0
    for i in s:
        if i.lower() in "aeiou":
            vc+=1
            s1+=i
    print("vowel count:",vc)
    print(list(set(s1)))
l=input().split()
for i in l:
    counting(i)
        
