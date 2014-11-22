import serial


STEPS_PER_INCH = 3200

def send_tuple(tup):
	print "Sending Tuple"
	x = tup[0]
	y = tup[1]
	with serial.Serial('/dev/tty.usbmodemfa131',9600) as ser:
	    if ser.isOpen():
                ser.write('X'+str(x)+'Y'+str(y))
                print "Serial is Open"
	print "Done Sending"


def main():
	#1.25 inches per cell
	dest = raw_input("Coordinates of destination(X Y). ") 
	coor = dest.split()
	cor = (int(coor[0]),int(coor[1]))
	send_tuple(cor)

if __name__ == '__main__':
	main()
