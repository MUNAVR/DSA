# def palindrom(string):
#     return string == string[::-1]

def palindrom(string):
    n=len(string)
    l=[]
    for i in range(n-1,-1,-1):
        l.append(string[i])
    s=''.join(l)
    if s==string:
        return True
    else:
        return False



string="malayalam"
result=palindrom(string)
print(result)