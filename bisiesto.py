# coding: utf-8
def esBisiesto(anyo):
	if anyo%4 == 0 or anyo%100 !=0 or anyo%400 == 0:
		print "Bisesto"
	else:
		print "No bisiesto"
esBisiesto (2100)
esBisiesto (2300)
esBisiesto (1995) 
