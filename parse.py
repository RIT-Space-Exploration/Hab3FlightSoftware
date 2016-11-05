"""Quick script to parse binary data into a csv file."""
import struct

byte_string = open("TESTER.BIN", "rb").read()

write_s = ('time_since_init,tempC,pressurePa,altM,humidity,'
           'gX,gY,gZ,aX,aY,aZ,mX,mY,mZ\n'
           )

for i in range(0, len(byte_string) - 1, 60):
    x = byte_string[i:i+60]
    for j in range(0, 15):
        y = x[(j * 4):(j*4)+4]
        write_s += '{:.9f}'.format(struct.unpack('f', y)[0])
        write_s += ','

    write_s += '\n'

f = open('test.csv', 'w')
f.write(write_s)
f.close()
