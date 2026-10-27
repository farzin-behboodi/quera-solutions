d=input()
e=input()
f=input()
a=int(d)
b=int(e)
c=int(f)
if (c*c)+(a*a)==b*b and a>0 and b>0 and c>0 :
    print("YES")
elif (b*b)+(a*a)==c*c and a>0 and b>0 and c>0 :
    print("YES")
elif (c*c)+(b*b)==a*a and a>0 and b>0 and c>0 :
    print("YES")
else :
    print("NO")
