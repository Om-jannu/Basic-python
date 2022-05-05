
str = "hello@world123"
vowel = 0
numer = 0
special = 0
for i in str:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U' :
        vowel = vowel+1
    elif i.isnumeric():
        numer = numer +1
    elif i=='@' or i=='#' or i=='$' or i=='&':
        special = special +1

print(vowel)
print(numer)
print(special)

