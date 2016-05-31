#!/usr/bin/env python

import time

class Present:

    sbox = [0xc, 0x5, 0x6, 0xb, 0x9, 0x0, 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 0x2]
    inv_sbox = [sbox.index(x) for x in range(len(sbox))]

    pbox = [0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3,
            19, 35, 51, 4, 20, 36, 52, 5, 21, 37, 53, 6, 22,
            38, 54, 7, 23, 39, 55, 8, 24, 40, 56, 9, 25, 41,
            57, 10, 26, 42, 58, 11, 27, 43, 59, 12, 28, 44,
            60, 13, 29, 45, 61, 14, 30, 46, 62, 15, 31, 47, 63]
    inv_pbox = [pbox.index(x) for x in range(len(pbox))]

    def __init__(self, key_size, key, rounds=32):
        self.block_size = 64
        self.key_size = key_size
        self.key = key
        self.rounds = rounds
        self.round_keys = []
        self.time = 0
        self.pbox_time = 0

        if self.key_size == 80:
            self.generate_80bit_round_keys(self.key)

        elif self.key_size == 128:
            self.generate_128bit_round_keys(self.key)

    def generate_80bit_round_keys(self, key_register):
        for i in range(1, self.rounds + 1):
            self.round_keys.append(key_register >> 16)
            key_register = (key_register >> 19) + ((key_register & (2**19 - 1)) << 61)
            key_register = (key_register & (2**76 - 1)) + (self.sbox[key_register >> 76] << 76)
            key_register = (i << 15) ^ key_register

    def generate_128bit_round_keys(self, key_register):
        for i in range(1, self.rounds + 1):
            self.round_keys.append(key_register >> 64)
            key_register = (key_register >> 67) + ((key_register & (2**67 - 1)) << 61)
            key_register = (key_register & (2**120 - 1)) + (self.sbox[key_register >> 124] << 124) + (self.sbox[(key_register >> 120) & 0xF] << 120)
            key_register = (i << 62) ^ key_register

    def encrypt(self, block):
        state = block
        for i in range(self.rounds - 1):
            state = state ^ self.round_keys[i]
            sbox_layer = 0
            pbox_layer = 0

            start_time = time.time()
            for j in range(16):
                sbox_layer += self.sbox[( state >> (j * 4)) & 0xF] << (j * 4)

            self.time += time.time() - start_time

            state = sbox_layer

            start_time = time.time()
            for j in range(64):
                pbox_layer += ((state >> j) & 0x01) << self.pbox[j]
            self.pbox_time += time.time() - start_time

            state = pbox_layer

        return state ^ self.round_keys[-1]

    def decrypt(self, block):
        state = block
        for i in range(self.rounds - 1):
            state = state ^ self.round_keys[self.rounds - i - 1]
            sbox_layer = 0
            pbox_layer = 0

            for j in range(64):
                pbox_layer += ((state >> j) & 0x01) << self.inv_pbox[j]

            state = pbox_layer

            for j in range(16):
                sbox_layer += self.inv_sbox[( state >> (j * 4)) & 0xF] << (j * 4)

            state = sbox_layer

        return state ^ self.round_keys[0]
