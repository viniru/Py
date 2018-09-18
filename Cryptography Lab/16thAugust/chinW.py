import math


def gcd_extended_euclidean(a, b):
	global x, y, d
	if b == 0:
		x = 1
		y = 0
	else:
		gcd_extended_euclidean(b, a%b)
		t = x
		x = y
		y = t - math.floor(a/b)*y

def multiplicative_inverse(a, m):
	gcd_extended_euclidean(a, m)
	return int((x%m+m)%m)

def chinese_remainder(eqns):
	M = 1
	bi = []
	bi_dash = []
	x = 0

	for i in eqns:
		M *= i[1]

	for i in eqns:
		bi.append(M/i[1])
		bi_dash.append(multiplicative_inverse(bi[-1], i[1]))

	for i in range(len(eqns)):
		x += (eqns[i][0]*bi[i]*bi_dash[i])%M

	return x

def main():
	print chinese_remainder([(2,5), (3,7)])

main()
