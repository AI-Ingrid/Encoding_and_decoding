class Person:
    def __init__(self, cipher_algorithm):
        self.cipher_algorithm = cipher_algorithm
        self.key = self.cipher_algorithm.key

    def set_key(self, bits):
        pass

    def get_key(self):
        return self.key

    def operate_cipher(self, message):
        pass


class Sender(Person):
    def operate_cipher(self, message):
        return self.cipher_algorithm.encode(message, self.key)

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key


class Receiver(Person):
    def operate_cipher(self, message):
        return self.cipher_algorithm.decode(message, self.key)

    def set_key(self, bits):
        encryption_key = self.cipher_algorithm.generate_encryption_key(bits)
        self.key = self.cipher_algorithm.decryption_key
        return encryption_key

    def get_key(self):
        return self.key


class Hacker(Receiver):

    def do_some_hacking(self, encrypted_text):
        possible_keys = self.cipher_algorithm.get_possible_keys()
        english_words = self.cipher_algorithm.get_english_words()

        for i in enumerate(possible_keys):
            decoded_text = self.cipher_algorithm.decode(encrypted_text, i[1])

            if decoded_text.lower() in english_words:
                print("--> First english word found: " + decoded_text)
                print("--> Index used: " + str(i))
                print(decoded_text)

                return decoded_text
        return False

    def hack_unbreakable(self, encrypted_text):
        possible_keys = self.cipher_algorithm.get_possible_keys()
        english_words = self.cipher_algorithm.get_english_words()
        list_of_decoded_text = []

        for i in enumerate(possible_keys):
            decoded_text = self.cipher_algorithm.decode(encrypted_text, i[1].upper())

            if decoded_text.lower() in english_words:

                if decoded_text not in list_of_decoded_text:
                    list_of_decoded_text.append(decoded_text)

        print(str(list_of_decoded_text))
        return list_of_decoded_text
