from person import *
from cipher import *


def main_1():
    # Testing hacking on Caesar
    sender = Sender(Caesar(7))
    receiver = Receiver(Caesar(7))
    message = "HATERS"

    encrypted_text = sender.operate_cipher(message)
    decrypted_text = receiver.operate_cipher(encrypted_text)

    hacker = Hacker(Caesar(7))
    hacker.do_some_hacking(encrypted_text)


def main_2():
    # Testing hacking Multiplicative
    sender = Sender(Multiplicative(23))
    receiver = Receiver(Multiplicative(23))
    message = "STREET"

    encrypted_text = sender.operate_cipher(message)
    receiver.operate_cipher(encrypted_text)

    hacker = Hacker(Multiplicative(23))
    hacker.do_some_hacking(encrypted_text)


def main_3():
    # Testing hacking Affine
    sender = Sender(Affine(3, 2))
    receiver = Receiver(Affine(3, 2))
    message = "HEAD"

    encrypted_text = sender.operate_cipher(message)
    receiver.operate_cipher(encrypted_text)

    hacker = Hacker(Affine(3, 2))
    hacker.do_some_hacking(encrypted_text)


def main_4():
    # Testing hacking Unbreakable
    sender = Sender(Unbreakable("PIZZA"))
    receiver = Receiver(Unbreakable("PIZZA"))
    message = "HEAD"

    encrypted_text = sender.operate_cipher(message)
    receiver.operate_cipher(encrypted_text)

    hacker = Hacker(Unbreakable("PIZZA"))
    hacker.do_some_hacking(encrypted_text)


#main_1()
#main_2()
#main_3()
#main_4()
