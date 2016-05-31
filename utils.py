import math

def shift_left(number, shift_pos, word_size, modulo):
    return (number >> (word_size - shift_pos)) | ((number << shift_pos) % modulo)

def shift_right(number, shift_pos, word_size, modulo):
    return (number >> shift_pos) | ((number << (word_size - shift_pos)) % modulo)

def str2bin(ss):
    """
        Transform a string (e.g. 'Hello') into a string of bits
    """
    bs = ''
    for c in ss:
        bs = bs + bin(ord(c))[2:].zfill(8)
    return bs

def str2int(ss):
    """
        Transform a string (e.g. 'Hello') into a (long) integer by converting
        first to a bistream
    """
    bs = str2bin(ss)
    li = int(bs, 2)
    return li

def hex2bin(hs):
    """
        Transform a hex string (e.g. 'a2') into a string of bits (e.g.10100010)
    """
    bs = ''
    for c in hs:
        bs = bs + bin(int(c,16))[2:].zfill(4)
    return bs

def int2hexstring(bval):
    """
        Transform an int value into a hexstring (even number of characters)
    """
    hs = hex(bval)[2:]
    lh = len(hs)
    return hs.zfill(lh + lh%2)

def string2number(i):
    return int(i.encode('hex'),16)

def number2string(i):
    s = '%0*x' % (16, i)
    return s.decode('hex')

def monobit_test(rstr):
	n = len(rstr)
	s = 0
	for b in rstr:
		if b == '0':
			s = s - 1
		else:
			s = s + 1
	S = abs(s) / math.sqrt(n)
	P = math.erfc(S / math.sqrt(2))
	return P

def str2bytestr(s):
    "".join(["\\x%02x" % ord(c) for c in s])

