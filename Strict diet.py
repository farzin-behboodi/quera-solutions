ghaza=input()
g_count=ghaza.count("G")
y_count=ghaza.count("Y")
r_count=ghaza.count("R")
if r_count>=3 or r_count>=2 and y_count>=2 or g_count==0:
    print("nakhor lite")
else:
    print("rahat baash")