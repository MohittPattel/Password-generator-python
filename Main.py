import random

lower="qwertyuioplkjhgfdsazxcvbnm"
upper="QWERTYUIOPLKJHGFDSAZXCVBNM"
number="0123456789"
symbol="()!@#$%^&*,./"

all=lower+upper+number+symbol
length=16
password="".join(random.sample(all,length))
print(password)