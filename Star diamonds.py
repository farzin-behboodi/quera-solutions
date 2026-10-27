n=input()
n=int(n)
a=n//2
for i in range (a*-a,n//2+1,1):
     if i<0 :
         i=-i
     s=" "*(i)+"*"*(-2*i+n)+" "*(2*i)+"*"*(-2*i+n)
     print(s)