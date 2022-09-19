from random import randint
from crypto_utils import modular_inverse, generate_random_prime, blocks_from_text, text_from_blocks


class Cipher:

    def __init__(self, key):
        self.key = key
        self.alphabet = [chr(i) for i in range(32, 127)]

    def encode(self, clear_text, key):
        pass

    def decode(self, encoded_text, key):
        pass

    def verify(self, clear_text):

        encrypted_text = self.encode(clear_text, self.key)
        decrypted_text = self.decode(encrypted_text, self.key)

        if decrypted_text == clear_text:
            return True

        return False

    def generate_encryption_key(self, bits):
        pass

    def generate_decryption_key(self, bits):
        pass

    @staticmethod
    def get_english_words():
        a_file = open("english_words.txt", "r")
        words = []

        for line in a_file:
            words.append(line.strip())

        a_file.close()
        return words


class Caesar(Cipher):

    def __init__(self, key):
        self.key = key
        self.possible_keys = []
        super().__init__(self.key)

    def encode(self, clear_text, key):
        encoded_text = ""
        print("Clear text: " + clear_text)

        for i in enumerate(clear_text):
            numeric_val = self.alphabet.index(i[1])
            coded_value = (numeric_val + key) % 95
            encoded_text += self.alphabet[coded_value]

        print("Encoded text: " + encoded_text)

        return encoded_text

    def decode(self, encoded_text, key):
        decoded_text = self.encode(encoded_text, 95 - key)

        return decoded_text

    def get_possible_keys(self):
        self.possible_keys = list(range(95))

        return self.possible_keys


class Multiplicative(Cipher):
    def __init__(self, key):
        self.key = key
        self.possible_keys = []
        super().__init__(self.key)

    def encode(self, clear_text, key):
        encoded_text = ""
        print("Clear text: " + clear_text)

        for i in enumerate(clear_text):
            numeric_val = self.alphabet.index(i[1])
            coded_value = (numeric_val * key) % 95
            encoded_text += self.alphabet[coded_value]

        print("Encoded text: " + encoded_text)

        return encoded_text

    def decode(self, encoded_text, key):
        inverse_of_key = modular_inverse(key, 95)

        print("Decoding ..")

        return self.encode(encoded_text, inverse_of_key)

    def get_possible_keys(self):
        self.possible_keys = self.possible_keys = list(range(95))

        return self.possible_keys


class Affine(Cipher):
    def __init__(self, n_1, n_2):
        self.key = (n_1, n_2)
        self.possible_keys = []

        super().__init__(self.key)

    def encode(self, clear_text, key):
        print("Encoding ...")

        mp_object = Multiplicative(key[0])
        caesar_object = Caesar(key[1])

        print(" --> First the Multiplicative..")
        encoded_mp_object = mp_object.encode(clear_text, key[0])

        print(" --> Then the Caesar..")
        encoded_caesar_object = caesar_object.encode(encoded_mp_object, key[1])

        return encoded_caesar_object

    def decode(self, encoded_text, key):
        print("Decoding ...")

        mp_object = Multiplicative(key[0])
        caesar_object = Caesar(key[1])

        print(" --> First the Caesar..")
        decoded_caesar_object = caesar_object.decode(encoded_text, key[1])

        print(" --> Then the Multiplicative..")
        decoded_mp_object = mp_object.decode(decoded_caesar_object, key[0])

        return decoded_mp_object

    def get_possible_keys(self):
        self.possible_keys = [(i, j) for i in range(
            0, len(self.alphabet)) for j in range(0, len(self.alphabet))]

        return self.possible_keys


class Unbreakable(Cipher):
    def __init__(self, key):
        self.key = key
        self.possible_keys = []

        super().__init__(self.key)

    def encode(self, clear_text, keyword):
        print("The clear text is: " + clear_text)

        encoded_text = ""
        i = 0

        while True:
            for j in enumerate(keyword):

                numeric_val_ct = self.alphabet.index(clear_text[i])
                numeric_val_keyword = self.alphabet.index(j[1])
                new_numeric_val = (numeric_val_keyword + numeric_val_ct) % 95
                encoded_text += self.alphabet[new_numeric_val]

                i += 1
                if i == len(clear_text):
                    print(encoded_text)

                    return encoded_text

    def decode(self, encoded_text, keyword):
        print("Decoding ..")
        decryption_key = ""

        for i in enumerate(keyword):
            e_i = self.alphabet.index(i[1])
            d_i = (len(self.alphabet) - e_i) % len(self.alphabet)

            decryption_key += self.alphabet[d_i]

        print(decryption_key)

        return self.encode(encoded_text, decryption_key)

    def get_possible_keys(self):
        self.possible_keys = self.get_english_words()

        return self.possible_keys


class RSA(Cipher):
    def __init__(self):
        self.decryption_key = 0

        super(RSA, self).__init__(self.decryption_key)

    def generate_encryption_key(self, bits):
        num_d = False
        num_n = 0
        num_e = 0

        while not num_d:
            p_prime = generate_random_prime(bits)
            q_prime = generate_random_prime(bits)

            while p_prime == q_prime:
                p_prime = generate_random_prime(bits)

            num_n = p_prime * q_prime
            phi = (p_prime - 1) * (q_prime - 1)

            num_e = randint(3, phi - 1)
            num_d = modular_inverse(num_e, phi)

        encryption_key = (num_n, num_e)
        self.decryption_key = (num_n, num_d)

        print("Encryption key: " + str(encryption_key))
        print("Decryption key: " + str(self.decryption_key))

        return encryption_key

    def encode(self, message, key):
        print("Encoding the message: " + message)

        num_n = key[0]
        num_e = key[1]

        integers = blocks_from_text(message, 1)
        print("The message is now converted into block "
              "of integers: " + str(integers))

        encoded_integers = []

        for integer in integers:
            encoded_integers.append(pow(integer, num_e) % num_n)

        print("The encoded integers are: " + str(encoded_integers))

        return encoded_integers

    def decode(self, encoded_integers, key):
        print("Decoding: " + str(encoded_integers))

        num_n = key[0]
        num_d = key[1]

        decrypted_integers = []

        for i in enumerate(encoded_integers):
            decrypted_int = (pow(i[1], num_d) % num_n)
            decrypted_integers.append(decrypted_int)

        print("The encoded integers are now decrypted to"
              " " + str(decrypted_integers))

        decrypted_text = text_from_blocks(decrypted_integers, 8)
        print("Decrypted_text: " + decrypted_text)

        return decrypted_text
