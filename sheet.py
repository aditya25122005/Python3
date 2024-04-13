# print all duplicates
s="Geeksforgeeks"
freq={}
for i in range(len(s)):
    if s[i] in freq:
        freq[s[i]]+=1
    else:
        freq[s[i]]=1
for val in freq:
    if freq[val] >1:
        print(val)           