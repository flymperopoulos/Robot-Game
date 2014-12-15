import serial
import time

STEPS_PER_INCH = 3200

def send_tuple(tup):
	print "Decidign Up or Down..."
	# x = tup[0]
	# y = tup[1]
	with serial.Serial('/dev/ttyACM0',9600) as ser:
            time.sleep(2)
            if ser.isOpen():
                ser.write(str(tup))
                print "Serial is Open"
	print "Done Sending"


def main():
	#1.25 inches per cell
	dest = raw_input("Go UP or DOWN? ") 
	# coor = dest.split()
	# cor = (int(coor[0]),int(coor[1]))
	send_tuple(dest)

if __name__ == '__main__':
	main()
