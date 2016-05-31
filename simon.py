#!/usr/bin/env python

import utils

class Simon:

    def __init__(self, block_size, key_size, key):
        self.block_size = block_size
        self.key_size = key_size
        self.num_rounds, self.seq_id = self.get_num_rounds_and_seq_id()
        self.word_size = block_size / 2
        self.modulo = 1 << self.word_size
        self.key_seq = self.get_key_seq()
        self.key = key
        self.generate_round_keys()

    def get_num_rounds_and_seq_id(self):
        if self.block_size == 32 and self.key_size == 64:
            return 32, 0
        elif self.block_size == 48 and self.key_size == 72:
            return 36, 0
        elif self.block_size == 48 and self.key_size == 96:
            return 36, 1
        elif self.block_size == 64 and self.key_size == 96:
            return 42, 2
        elif self.block_size == 64 and self.key_size == 128:
            return 44, 3
        elif self.block_size == 96 and self.key_size == 96:
            return 52, 2
        elif self.block_size == 96 and self.key_size == 144:
            return 54, 3
        elif self.block_size == 128 and self.key_size == 128:
            return 68, 2
        elif self.block_size == 128 and self.key_size == 192:
            return 69, 3
        elif self.block_size == 128 and self.key_size == 256:
            return 72, 4

    def get_key_seq(self):
        seq = []

        shift_reg = [0, 0, 0, 0, 1]
        for i in range(62):
            f = shift_reg[2] ^ shift_reg[4]
            if self.seq_id in (0, 2):
                shift_reg[3] ^= shift_reg[4]
            elif self.seq_id in (1, 3):
                shift_reg[1] ^= shift_reg[0]
            res = shift_reg.pop()
            shift_reg.insert(0, f)
            if self.seq_id >= 2:
                res ^= i % 2
            seq.append(res)

        return tuple(seq)


    def generate_round_keys(self):
        c = (1 << self.word_size) - 4
        m = self.key_size / self.word_size
        self.round_key = []

        for i in range(m):
            self.round_key.append(self.key % self.modulo)
            self.key >>= self.word_size

        for i in range(m, self.num_rounds):
            k = utils.shift_right(self.round_key[-1], 3, self.word_size, self.modulo)

            if m == 4:
                k ^= self.round_key[-3]

            k ^= utils.shift_right(k, 1, self.word_size, self.modulo) ^ self.round_key[-m]
            k ^= c ^ self.key_seq[(i - m) % 62]
            self.round_key.append(k)

    def feistel_round(self, left, right, key):
        function = (utils.shift_left(left, 1, self.word_size, self.modulo) \
            & utils.shift_left(left, 8, self.word_size, self.modulo)) \
            ^ utils.shift_left(left, 2, self.word_size, self.modulo)
        return right ^ function ^ key, left

    def encrypt(self, plaintext):    
        left = plaintext >> self.word_size
        right = plaintext % self.modulo

        for i in range(self.num_rounds):
            left, right = self.feistel_round(left, right, self.round_key[i])

        ciphertext = (left << self.word_size) | right

        return ciphertext

    def decrypt(self, ciphertext):
        left = ciphertext >> self.word_size
        right = ciphertext % self.modulo

        for i in range(self.num_rounds):
            right, left = self.feistel_round(right, left, self.round_key[self.num_rounds - i - 1])

        plaintext = (left << self.word_size) | right

        return plaintext

