import string
import time
x="Hello World"
yazi=""
y=" "+string.ascii_letters
for a in range(len(x)):
    for i in range(len(y)):
        print(yazi+y[i])
        time.sleep(0.01)
        if y[i]==x[a]:
            yazi=yazi+y[i]
            if yazi==x:
                break
            else:
                continue


input()
