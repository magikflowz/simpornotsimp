import random

simp_or_not_simp = ["simp", "not simp"]
x = 0
while x < 100:
    print(random.choice(simp_or_not_simp))
    x+=1