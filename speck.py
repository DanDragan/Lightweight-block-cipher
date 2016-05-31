#!/usr/bin/env python

import utils

class Speck:

    def __init__(self, block_size, key_size, key):
        self.block_size = block_size
        self.key_size = key_size
        self.key = key
        self.num_rounds = self.get_num_rounds()
        self.alpha, self.beta = self.get_alpha_beta()
        self.word_size = self.block_size / 2
        self.modulo = 1 << self.word_size
        self.generate_round_keys()

    def get_num_rounds(self):
        if self.block_size == 32 and self.key_size == 64:
            return 22
        elif self.block_size == 48 and self.key_size == 72:
            return 22
        elif self.block_size == 48 and self.key_size == 96:
            return 23
        elif self.block_size == 64 and self.key_size == 96:
            return 26
        elif self.block_size == 64 and self.key_size == 128:
            return 27
        elif self.block_size == 96 and self.key_size == 96:
            return 28
        elif self.block_size == 96 and self.key_size == 144:
            return 29
        elif self.block_size == 128 and self.key_size == 128:
            return 32
        elif self.block_size == 128 and self.key_size == 192:
            return 33
        elif self.block_size == 128 and self.key_size == 256:
            return 34

    def get_alpha_beta(self):
        if self.block_size == 32 and self.key_size == 64:
            return 7, 2
        else:
            return 8, 3

    def th_feistel(self, left, right):
        return right, (utils.shift_right(left, self.alpha, self.word_size, self.modulo) + right) % self.modulo

    def bh_feistel(self, left, right):
        return right, utils.shift_left(left, self.beta, self.word_size, self.modulo) ^ right

    def inv_th_feistel(self, left, right):
        return utils.shift_left((right - left) % self.modulo, self.alpha, self.word_size, self.modulo), left

    def inv_bh_feistel(self, left, right):
        return utils.shift_right(left ^ right, self.beta, self.word_size, self.modulo), left

    def generate_round_keys(self):
        self.round_key = [self.key % self.modulo]
        self.key >>= self.word_size
        llist = []

        for i in range(self.key_size / self.word_size - 1):
            llist.append(self.key % self.modulo)
            self.key >>= self.word_size

        for i in range(self.num_rounds - 1):
            left, right = self.th_feistel(llist[i], self.round_key[i])
            right ^= i
            left, right = self.bh_feistel(left, right)
            llist.append(left)
            self.round_key.append(right)

    def encrypt(self, plaintext):
        left = plaintext >> self.word_size
        right = plaintext % self.modulo

        for i in range(self.num_rounds):
            left, right = self.th_feistel(left, right)
            right ^= self.round_key[i]
            left, right = self.bh_feistel(left, right)

        ciphertext = (left << self.word_size) | right

        return ciphertext

    def decrypt(self, ciphertext):
        left = ciphertext >> self.word_size
        right = ciphertext % self.modulo

        for i in range(self.num_rounds):
            left, right = self.inv_bh_feistel(left, right)
            right ^= self.round_key[self.num_rounds - i - 1]
            left, right = self.inv_th_feistel(left, right)

        plaintext = (left << self.word_size) | right

        return plaintext

