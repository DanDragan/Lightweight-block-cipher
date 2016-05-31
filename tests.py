#!/usr/bin/env python

import time
import cbc
import utils

if __name__ == '__main__':

    f1 = open("text1", "r")
    plaintext1 = f1.read()

    f2 = open("text2", "r")
    plaintext2 = f2.read()

    f3 = open("text3", "r")
    plaintext3 = f3.read()

    c = cbc.CBC(128, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Aes")

    start_time = time.time()
    encrypted = c.encrypt(plaintext1)
    elapsed_time = time.time() - start_time

    print "Elapsed time for AES 128/128 encrypt in 313.5KB file was: " + str(elapsed_time)

    c = cbc.CBC(128, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Simon")

    start_time = time.time()
    encrypted = c.encrypt(plaintext1)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Simon 128/128 encrypt in 313.5KB file was: " + str(elapsed_time)

    c = cbc.CBC(128, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Speck")

    start_time = time.time()
    encrypted = c.encrypt(plaintext1)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Speck 128/128 encrypt in 313.5KB file was: " + str(elapsed_time)

    c = cbc.CBC(128, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Aes")

    start_time = time.time()
    encrypted = c.encrypt(plaintext2)
    elapsed_time = time.time() - start_time

    print "Elapsed time for AES 128/128 encrypt in 627KB file was: " + str(elapsed_time)

    c = cbc.CBC(128, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Simon")

    start_time = time.time()
    encrypted = c.encrypt(plaintext2)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Simon 128/128 encrypt in 627KB file was: " + str(elapsed_time)

    c = cbc.CBC(128, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Speck")

    start_time = time.time()
    encrypted = c.encrypt(plaintext2)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Speck 128/128 encrypt in 627KB file was: " + str(elapsed_time)

    c = cbc.CBC(128, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Aes")

    start_time = time.time()
    encrypted = c.encrypt(plaintext3)
    elapsed_time = time.time() - start_time

    print "Elapsed time for AES 128/128 encrypt in 1.3MB file was: " + str(elapsed_time)

    c = cbc.CBC(128, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Simon")

    start_time = time.time()
    encrypted = c.encrypt(plaintext3)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Simon 128/128 encrypt in 1.3MB file was: " + str(elapsed_time)

    c = cbc.CBC(128, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Speck")

    start_time = time.time()
    encrypted = c.encrypt(plaintext3)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Speck 128/128 encrypt in 1.3MB file was: " + str(elapsed_time)

    c = cbc.CBC(64, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Present")

    start_time = time.time()
    encrypted = c.encrypt(plaintext1)
    elapsed_time = time.time() - start_time - (c.sbox_time / 16) - (c.pbox_time / 64)

    print c.sbox_time
    print c.pbox_time

    print "Elapsed time for Present 64/128 in 313.5KB file was: " + str(elapsed_time)

    c = cbc.CBC(64, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Simon")

    start_time = time.time()
    encrypted = c.encrypt(plaintext1)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Simon 64/128 in 313.5KB  file was: " + str(elapsed_time)


    c = cbc.CBC(64, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Speck")

    start_time = time.time()
    encrypted = c.encrypt(plaintext1)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Speck 64/128 in 313.5KB file was: " + str(elapsed_time)

    c = cbc.CBC(64, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Present")

    start_time = time.time()
    encrypted = c.encrypt(plaintext2)
    elapsed_time = time.time() - start_time - (c.sbox_time / 16) - (c.pbox_time / 64)

    print c.sbox_time
    print c.pbox_time

    print "Elapsed time for Present 64/128 in 627KB file was: " + str(elapsed_time)

    c = cbc.CBC(64, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Simon")

    start_time = time.time()
    encrypted = c.encrypt(plaintext2)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Simon 64/128 in 627KB  file was: " + str(elapsed_time)


    c = cbc.CBC(64, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Speck")

    start_time = time.time()
    encrypted = c.encrypt(plaintext2)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Speck 64/128 in 627KB file was: " + str(elapsed_time)

    c = cbc.CBC(64, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Present")

    start_time = time.time()
    encrypted = c.encrypt(plaintext3)
    elapsed_time = time.time() - start_time - (c.sbox_time / 16) - (c.pbox_time / 64)

    print c.sbox_time
    print c.pbox_time

    print "Elapsed time for Present 64/128 in 1.3MB file was: " + str(elapsed_time)

    c = cbc.CBC(64, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Simon")

    start_time = time.time()
    encrypted = c.encrypt(plaintext3)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Simon 64/128 in 1.3MB  file was: " + str(elapsed_time)


    c = cbc.CBC(64, 128, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Speck")

    start_time = time.time()
    encrypted = c.encrypt(plaintext3)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Speck 64/128 in 1.3MB file was: " + str(elapsed_time)

    c = cbc.CBC(64, 96, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Simon")

    start_time = time.time()
    encrypted = c.encrypt(plaintext1)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Simon 64/96 in 313.5KB  file was: " + str(elapsed_time)

    c = cbc.CBC(64, 96, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Speck")

    start_time = time.time()
    encrypted = c.encrypt(plaintext1)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Speck  64/96 in 313.5KB file was: " + str(elapsed_time)

    c = cbc.CBC(64, 96, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Simon")

    start_time = time.time()
    encrypted = c.encrypt(plaintext2)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Simon 64/96 in 627KB  file was: " + str(elapsed_time)

    c = cbc.CBC(64, 96, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Speck")

    start_time = time.time()
    encrypted = c.encrypt(plaintext2)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Speck  64/96 in 627KB file was: " + str(elapsed_time)

    c = cbc.CBC(64, 96, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Simon")

    start_time = time.time()
    encrypted = c.encrypt(plaintext3)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Simon 64/96 in 1.3MB  file was: " + str(elapsed_time)

    c = cbc.CBC(64, 96, utils.string2number('Cheia este secre'), utils.string2number('precizie'), "Speck")

    start_time = time.time()
    encrypted = c.encrypt(plaintext3)
    elapsed_time = time.time() - start_time

    print "Elapsed time for Speck  64/96 in 1.3MB file was: " + str(elapsed_time)

    f1.close()
    f2.close()
    f3.close()
