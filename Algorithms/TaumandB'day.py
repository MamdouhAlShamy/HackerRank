T = int(raw_input())
for i in xrange(T):
	BW = raw_input().rstrip().split()
	B = int(BW[0])
	W = int(BW[1])
	XYZ = raw_input().rstrip().split()
	X = int(XYZ[0])
	Y = int(XYZ[1])
	Z = int(XYZ[2])
	price = 0
	if X + Z < Y :
		price = X * B + (X + Z) * W 	
	elif Y + Z < X :
		price = (Y + Z) * B + Y* W  
	else:
		price = X * B + Y * W

	print price
