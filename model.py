y0 = 50
x0 = 50
#print(y0)
#print(x0)

import random

if random.random() < 0.5:
    y0=y0+1
else:
    y0=y0-1

if random.random() < 0.5:
    x0=x0+1
else:
    x0=x0-1
    
print(x0,y0)






y1 = 1 + random.randint(0,99)
x1 = 1 + random.randint(0,99)

if random.random() < 0.5:
    y1=y1+1
else:
    y1=y1-1

print(x1,y1)

answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print(answer)

echo "# Random-Agent" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/Airbornsock/Random-Agent.git
git push -u origin master
yo
