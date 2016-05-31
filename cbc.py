#!/usr/bin/env python

import present
import simon
import speck
import utils
import time
import aes

class CBC:

    def __init__(self, block_size, key_size, key, iv, cipher="Present"):
        self.block_size = block_size
        self.key_size = key_size
        self.key = key
        self.iv = iv
        self.cipher = cipher
        self.sbox_time = 0
        self.pbox_time = 0

    def encrypt(self, plaintext):
        cipher = ""
        l = len(plaintext)

        if self.cipher == "Present":
            bc = present.Present(self.key_size, self.key)

        elif self.cipher == "Simon":
            bc = simon.Simon(self.block_size, self.key_size, self.key)

        elif self.cipher == "Speck":
            bc = speck.Speck(self.block_size, self.key_size, self.key)

        elif self.cipher == "Aes":
            bc = aes.AES(self.key)

        for i in range(l * 8 / self.block_size):
            if i == 0:
                state = self.iv
            
            state ^= utils.string2number(plaintext[(self.block_size / 8) * i : (self.block_size / 8) * (i + 1)])

            state = bc.encrypt(state)

            #cipher += utils.number2string(state)

        if self.cipher == "Present":
            self.sbox_time = bc.time
            self.pbox_time = bc.pbox_time

        return cipher

    def decrypt(self, ciphertext):
        plaintext = ""
        l = len(ciphertext)

        if self.cipher == "Present":
            bc = present.Present(self.key_size, self.key)

        elif self.cipher == "Simon":
            bc = simon.Simon(self.block_size, self.key_size, self.key)

        elif self.cipher == "Speck":
            bc = speck.Speck(self.block_size, self.key_size, self.key)

        for i in range(l * 8 / self.block_size):

            state = bc.decrypt(utils.string2number(ciphertext[(self.block_size / 8) * i : (self.block_size / 8) * (i + 1)]))

            if i == 0:
                iv = self.iv
            else:
                iv = utils.string2number(ciphertext[(self.block_size / 8) * (i - 1) : (self.block_size / 8) * i])

            state ^= iv

            plaintext += utils.number2string(state)

        return plaintext

