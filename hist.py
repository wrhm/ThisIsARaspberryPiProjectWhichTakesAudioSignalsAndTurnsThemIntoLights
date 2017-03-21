d = dict()
for i in xrange(10):
	d[i] = 0
while True:
	n = int(raw_input('>> '))
	d[n] += 1
	for i in xrange(10):
		print '%2d : %s'%(i,'*'*d[i])
	print ''
	print '='*50
	print ''