import sys,getopt
import code
import gbops

filename = None
blocksize = 1024

opts,args = getopt.getopt(sys.argv[1:],'f:b:')
for o,a in opts:
	if o == '-f':
		filename = a
	if o == '-b':
		blocksize = a

# operations dict

# load the file
offset = 0
with open(filename,"rb") as f:
	block = f.read(blocksize)
	current = 0
	while current < len(block):
		sys.stdout.write(hex(current) + "\t\t")
		sys.stdout.flush
		instruction = ord(block[current])
		instlen = gbops.oplen[instruction]
		if instlen == 1:
			print(gbops.opcode[instruction]())
			current += 1
		elif instlen == 2:
			param = ord(block[current + 1])
			print(gbops.opcode[instruction](param))
			current += 2
		elif instlen == 3:
			param = ord(block[current + 1]) + ord(block[current + 2])*256
			#code.interact(local=locals())
			print(gbops.opcode[instruction](param))
			current += 3
		else:
			current += 1
		