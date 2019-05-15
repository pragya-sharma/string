'''
Aim: You are given a string and your task is to swap cases.
     In other words, convert all lowercase letters to uppercase
     letters and vice versa.
'''
import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase
S = input()      
for i in range(len(S)):
    if S[i] in lower:
        T = (S[i].upper())
        print(T,end="")
    elif S[i] in upper:
        u = (S[i].lower())
        print(u,end="")
    else:
        v = (S[i])
        print(v,end="")

