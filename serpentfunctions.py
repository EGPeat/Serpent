from icecream import ic
from random import randint, seed
import sys


def p(info):
    print(info)


def pt(info):
    print(type(info))


def generate_key(key_len=128, sneed=2023):
    seed(sneed)
    key_bin = '0b'
    for idx in range(key_len):
        key_bin += str(randint(0, 1))

    return int(key_bin, 2)


def input_val(maxSize=16, valType=int, options=False):  # unused

    while True:
        try:
            if not options:
                info = valType(input())
                if isinstance(info, str) and (len(info) > maxSize):
                    raise IndexError
                elif isinstance(info, int) and (info > maxSize):
                    raise IndexError
                return info
            else:
                info = input()
                if info.isnumeric():
                    info = int(info)
                    if info > maxSize:
                        raise IndexError
                    return info
                elif isinstance(info, str) and (len(info) > maxSize):
                    raise IndexError
                return info

        except ValueError:
            info = f"It seems you entered something that isn't a {valType}. Please try again"
        except IndexError:
            info = "you put in something that is a larger int than is allowed, or a longer string than is allowed"


def binary_from_file(default_choice=True):
    if default_choice is False:
        print("Please enter the filename you wish to encrypt, excluding the .txt: ")
        filename = input_val(32, str)
    else:
        filename = "sampletext"
    with open(f"{filename}.txt", 'rb') as file:
        info = file.read()
        ic(type(info))
    return info


def turn_into_128(binary):
    binary = bytearray(binary)
    endian_value = sys.byteorder
    full_blocks = len(binary) // 16
    partial_blocks = len(binary) % 16
    blocks128 = [None] * (full_blocks + 1)
    binary += b'\x00' * (16 - partial_blocks)

    if endian_value == "little":
        for idx in range(full_blocks + 1):
            blocks128[idx] = binary[(0 + 16 * idx):(16 + 16 * idx)]
    else:  # need to add in endian swapping for bits as well as bytes. Not entirely sure this works
        for idx in range(full_blocks + 1):
            blocks128[idx] = bytearray(binary[(3)::-1] + binary[(7):(3):-1] + binary[(11):(7):-1] + binary[(15):(11):-1])
            del binary[0:16]
            for idx2 in range(16):
                blocks128[idx][idx2] = int(('{:08b}'.format(blocks128[idx][idx2])[::-1]), 2)

    return blocks128
