#! /usr/bin/python

import string
import random
import sys


class opt:
    length: int = 16
    lowercase: bool = True
    uppercase: bool = True
    numbers: bool = True
    special: bool = False

    def __str__(self):
        return f"Options: L{self.length} u{self.uppercase} l{self.lowercase} n{self.numbers} s{self.special}"


def craftPassword(options: opt):
    chars: str = ""
    chars += string.ascii_lowercase if options.lowercase else ""
    chars += string.ascii_uppercase if options.uppercase else ""
    chars += string.digits if options.numbers else ""
    chars += r",.<>/?:\";'|[]{}-=_+()&*%^#$!@~`" if options.special else ""

    return "".join(random.choice(chars) for i in range(options.length))


def main():
    options: opt = opt()

    for arg in sys.argv:
        if arg[0] == '-':
            if arg == "--help":
                print("""\
Password Generator Usage
./password [-ulns|+ulns] [length]
    -u      Disables uppercase letters
    -l      Disables lowecase letters
    -n      Disables digits
    -s      Disables special characters [Default]
    +u      Enables uppercase letters [Default]
    +l      Enables lowercase letters [Default]
    +n      Enables digits [Default]
    +s      Enables special characters

    -L int  Specify length
""")
                sys.exit(0)

            for a in arg[1:]:
                if a == "u":
                    options.uppercase = False
                if a == "l":
                    options.lowercase = False
                if a == "n":
                    options.numbers = False
                if a == "s":
                    options.special = False
                if a == "L":
                    options.length = int(arg[2:])

        elif arg[0] == '+':
            for a in arg[1:]:
                if a == "u":
                    options.uppercase = True
                if a == "l":
                    options.lowercase = True
                if a == "n":
                    options.numbers = True
                if a == "s":
                    options.special = True

    print(craftPassword(options))


main()
