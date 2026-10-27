# Quera Python Solutions

## introduction
This project is my python codes for 5 questions from (quera.org) website in the Terminal.
the main goal of this project is to solve algorithmic problems in python without need for install any extra library in cmd.
in this folder we have 5 main files: Strict diet.py, Freedom of Speech Day in Barareh.py, Pythagorean triples.py, Diamond print.py and Star diamonds.py.

---

## 1. Strict diet
* **question link** : [Strict diet on Quera](https://quera.org/problemset/20256)

When we run this code with (python "Strict diet.py") in the Terminal, the system gets a 5 letter string for the food label and checks if it is safe to eat:

```python
ghaza=input()
g_count=ghaza.count("G")
y_count=ghaza.count("Y")
r_count=ghaza.count("R")
if r_count>=3 or r_count>=2 and y_count>=2 or g_count==0:
    print("nakhor lite")
else:
    print("rahat baash")
```

in this code the program checks the input letters in the Terminal:
* **ghaza=input()** :for give the 5 letters of food health label (G, Y, R) to the program you must write the string in the Terminal.
* **count("G"), count("Y"), count("R")** :the code counts green, yellow and red letters and saves them in (g_count), (y_count) and (r_count).
* **print("nakhor lite")** :if red is 3 or more, or at least 2 red and 2 yellow, or no green at all (g_count==0), the code shows (nakhor lite), and if not it shows (rahat baash).

---

## 2. Freedom of Speech Day in Barareh
* **question link** : [Freedom of Speech Day in Barareh on Quera](https://quera.org/problemset/10162)

when you run (python "Freedom of Speech Day in Barareh.py") in the Terminal, the code gets number (k) and checks which side of Barareh starts talking:

```python
d=input()
k=int(d)
if k%2==0 :
        print("Bala Barare")
else :
        print("Payin Barare")
```

in this file the code works with these steps in the Terminal:
* **k=int(d)** :for enter the number you must write it in Terminal so (d=input()) gets it and changes it to integer in (k).
* **if k%2==0** :the code checks if (k) is even, and prints (Bala Barare) in the Terminal.
* **else** :if the number is odd, the code goes to else and prints (Payin Barare) in the Terminal.

---

## 3. Pythagorean triples
* **question link** : [Pythagorean triples on Quera](https://quera.org/problemset/280)

when we run (python "Pythagorean triples.py") in the Terminal, the system gets 3 numbers and checks if they make a right triangle:

```python
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
```

in this code you must enter 3 numbers one by one in the Terminal:
* **a, b, c** :first you must write 3 numbers in (d), (e) and (f) and the code changes them to integer in (a), (b) and (c).
* **if / elif checks** :the code checks ((c*c)+(a*a)==b*b) in all 3 states and checks (a>0 and b>0 and c>0), and if it is right it shows (YES) in Terminal, or shows (NO) in else.

---

## 4. Diamond print
* **question link** : [Diamond print on Quera](https://quera.org/problemset/618)

when you run (python "Diamond print.py") in the Terminal, the code gets (n) and prints a star diamond with size (2*n+1):

```python
n=input()
n=int(n)
n=2*n+1
a=n//2
for i in range (a*-a,n//2+1,1):
     if i<0 :
         i=-i
     s=" "*(i)+"*"*(-2*i+n)
     print(s)
```

in this file the loop makes each line of the diamond in the Terminal:
* **n=2*n+1** :first you must write a number in Terminal and the code calculates the full width in (n) and the middle in (a=n//2).
* **for i in range** :in the loop if (i<0) it changes to positive with (i=-i), and then prints spaces and stars with (s=" "*(i)+"*"*(-2*i+n)) in the Terminal.

---

## 5. Star diamonds
* **question link** : [Star diamonds on Quera](https://quera.org/problemset/9773)

when we run (python "Star diamonds.py") in the Terminal, the code prints two diamonds next to each other on the same lines:

```python
n=input()
n=int(n)
a=n//2
for i in range (a*-a,n//2+1,1):
     if i<0 :
         i=-i
     s=" "*(i)+"*"*(-2*i+n)+" "*(2*i)+"*"*(-2*i+n)
     print(s)
```

this code works just like the previous diamond code in the Terminal:
* **a=n//2** :for start the loop you must write the odd size (n) in the Terminal so the code sets the middle in (a).
* **s=" "*(i)+...** :in each line of the loop, the code puts (2*i) spaces between two star parts (`"*"*(-2*i+n)`) and prints both diamonds together in the Terminal.