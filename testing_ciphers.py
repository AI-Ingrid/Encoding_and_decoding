from person import *
from cipher import *


def main_1():
    # Test for Caesar
    message = "CODE"

    sender = Sender(Caesar(3))
    receiver = Receiver(Caesar(3))

    encrypted_text = sender.operate_cipher(message)
    receiver.operate_cipher(encrypted_text)


def main_2():
    # Test for Multiplicative
    message = "FOOTBALL"

    sender = Sender(Multiplicative(3))
    receiver = Receiver(Multiplicative(3))

    encrypted_text = sender.operate_cipher(message)
    receiver.operate_cipher(encrypted_text)


def main_3():
    # Test for Affine
    message = "ARSENAL"

    sender = Sender(Affine(3, 2))
    receiver = Receiver(Affine(3, 2))

    encrypted_text = sender.operate_cipher(message)
    receiver.operate_cipher(encrypted_text)


def main_4():
    # Test for Unbreakable
    message = "HEMMELIGHET"
    sender = Sender(Unbreakable("PIZZA"))
    receiver = Receiver(Unbreakable("PIZZA"))

    encrypted_text = sender.operate_cipher(message)
    receiver.operate_cipher(encrypted_text)


def main_5():
    # Test for RSA
    bits = 8
    text_message = "CODE"

    sender = Sender(RSA())
    receiver = Receiver(RSA())

    encryption_key = receiver.set_key(bits)
    sender.set_key(encryption_key)

    encrypted_text = sender.operate_cipher(text_message)
    receiver.operate_cipher(encrypted_text)


#main_1()
#main_2()
#main_3()
#main_4()
#main_5()
