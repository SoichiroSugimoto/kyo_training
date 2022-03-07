import random
import datetime

V1 = 1
V2 = 2
V3 = 3

# グローバル変数をうyhnランダムな値に書き換える

def print_time():
	# time = datetime.datetime.now()
	time = datetime.date.today()
	print('time' + ' = ' + str(time))
	print(int(time.day) * int(time.month))


def simple_print():
	time = datetime.date.today()
	random.seed(int(time.day) + 1)
	a = random.randint(0, 59)
	b = random.randint(0, 59)
	c = random.randint(0, 59)
	d = random.randint(0, 59)
	e = random.randint(0, 59)
	f = random.randint(0, 59)
	g = random.randint(0, 59)
	h = random.randint(0, 59)
	i = random.randint(0, 59)
	print('a' + ' = ' + str(a))
	print('b' + ' = ' + str(b))
	print('c' + ' = ' + str(c))
	print('d' + ' = ' + str(d))
	print('e' + ' = ' + str(e))
	print('f' + ' = ' + str(f))
	print('g' + ' = ' + str(g))
	print('h' + ' = ' + str(h))
	print('i' + ' = ' + str(i))


def print_test():
	time = datetime.date.today()
	random.seed(int(time.day) + 1)
	qz0 = 'q' + str(random.randint(0, 9))
	qz1 = 'q' + str(random.randint(10, 14))
	qz2 = 'q' + str(random.randint(15, 19))
	qz3 = 'q' + str(random.randint(20, 24))
	qz4 = 'q' + str(random.randint(25, 29))
	qz5 = 'q' + str(random.randint(30, 34))
	qz6 = 'q' + str(random.randint(35, 39))
	qz7 = 'q' + str(random.randint(40, 45))
	qz8 = 'q' + str(random.randint(46, 50))
	qz9 = 'q' + str(random.randint(51, 59))
	print('qz0' + ' = ' + qz0)
	print('qz1' + ' = ' + qz1)
	print('qz2' + ' = ' + qz2)
	print('qz3' + ' = ' + qz3)
	print('qz4' + ' = ' + qz4)
	print('qz5' + ' = ' + qz5)
	print('qz6' + ' = ' + qz6)
	print('qz7' + ' = ' + qz7)
	print('qz8' + ' = ' + qz8)
	print('qz9' + ' = ' + qz9)

# print_time()
# simple_print()
print_test()