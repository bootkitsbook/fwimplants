import array
import base64
import sys
import zlib
import codecs

def main(f_name, f_save):
	f = open(f_name, "rb")
	data =  array.array("B",f.read())
	f.close()

	item_data = array.array("B",[])

	i = 0
	v4 = 0

	while True:
		v4 = data[i]
		i = i + 1
		
		if v4 & 1 == 1:
			v4 = v4 | (data[i] << 8)
			i = i + 1

		is_flag = v4 & 2
		leng = v4 >> 2

		if leng == 0:
			break

		while leng != 0:
			j = 0
			if is_flag == 0:
				j = data[i]
				i = i + 1
			item_data.append(j)

			leng = leng - 1


	f = open(f_save, "wb")
	f.write(item_data)
	f.close()


if (len(sys.argv) == 3):
    main(sys.argv[1], sys.argv[2])
else:
    print "Usage:"
    print "  %s <file> <dir_to_save>" % (sys.argv[0])
