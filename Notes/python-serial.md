import serial

# bind ser to /dev/ttyACM0 115200 
ser=serial.Serial('/dev/ttyACM0',115200,timeout=1)

# ser read.. 
ser.readline()



## ser write

ser.write(b'h')

> b'h'  是将指定编码为byte 的 'h' 而不是unicode

#...


# help
help(ser)
dir(ser)
