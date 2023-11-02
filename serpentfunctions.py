from icecream import ic
from random import randint, seed
import sys


def call_globals():
    global IPTable
    global FPTable
    global golden_ratio
    global sboxes
    IPTable = [
        0, 32, 64, 96, 1, 33, 65, 97, 2, 34, 66, 98, 3, 35, 67, 99,
        4, 36, 68, 100, 5, 37, 69, 101, 6, 38, 70, 102, 7, 39, 71, 103,
        8, 40, 72, 104, 9, 41, 73, 105, 10, 42, 74, 106, 11, 43, 75, 107,
        12, 44, 76, 108, 13, 45, 77, 109, 14, 46, 78, 110, 15, 47, 79, 111,
        16, 48, 80, 112, 17, 49, 81, 113, 18, 50, 82, 114, 19, 51, 83, 115,
        20, 52, 84, 116, 21, 53, 85, 117, 22, 54, 86, 118, 23, 55, 87, 119,
        24, 56, 88, 120, 25, 57, 89, 121, 26, 58, 90, 122, 27, 59, 91, 123,
        28, 60, 92, 124, 29, 61, 93, 125, 30, 62, 94, 126, 31, 63, 95, 127]
    FPTable = [
        0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60,
        64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108, 112, 116, 120, 124,
        1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61,
        65, 69, 73, 77, 81, 85, 89, 93, 97, 101, 105, 109, 113, 117, 121, 125,
        2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62,
        66, 70, 74, 78, 82, 86, 90, 94, 98, 102, 106, 110, 114, 118, 122, 126,
        3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63,
        67, 71, 75, 79, 83, 87, 91, 95, 99, 103, 107, 111, 115, 119, 123, 127]
    golden_ratio = 0x9e3779b9

    sboxes = ([[3], [8], [15], [1], [10], [6], [5], [11], [14], [13], [4], [2], [7], [0], [9], [12]],
              [[15], [12], [2], [7], [9], [0], [5], [10], [1], [11], [14], [8], [6], [13], [3], [4]],
              [[8], [6], [7], [9], [3], [12], [10], [15], [13], [1], [14], [4], [0], [11], [5], [2]],
              [[0], [15], [11], [8], [12], [9], [6], [3], [13], [1], [2], [4], [10], [7], [5], [14]],
              [[1], [15], [8], [3], [12], [0], [11], [6], [2], [5], [4], [10], [9], [14], [7], [13]],
              [[15], [5], [2], [11], [4], [10], [9], [12], [0], [3], [14], [8], [13], [6], [7], [1]],
              [[7], [2], [12], [5], [8], [4], [6], [11], [14], [9], [1], [15], [13], [3], [10], [0]],
              [[1], [13], [15], [0], [14], [8], [2], [11], [7], [4], [12], [10], [9], [3], [5], [6]])


def leftRotate(number, times_rotated):
    return ((number << times_rotated) % (1 << 32)) | (number >> (32 - times_rotated))


def rightRotate(number, times_rotated):
    return (number >> times_rotated) | (number << (32 - times_rotated)) & 0xFFFFFFFF


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
    return info


# changes endian as necessary, pads to nearest multiple of 128
def endian_and_padding(binary):
    binary = bytearray(binary)
    endian_value = sys.byteorder

    full_128 = 128 - (len(binary) % 128)
    binary += b'\x00' * (full_128)
    full_blocks = len(binary) // 16
    blocks128 = [None] * (full_blocks)

    if endian_value == "little":
        for idx in range(full_blocks):
            blocks128[idx] = binary[(0 + 16 * idx):(16 + 16 * idx)]
    else:  # need to add in endian swapping for bits as well as bytes. Not entirely sure this works
        for idx in range(full_blocks):
            blocks128[idx] = bytearray(binary[(3)::-1] + binary[(7):(3):-1] + binary[(11):(7):-1] + binary[(15):(11):-1])
            del binary[0:16]
            for idx2 in range(16):
                blocks128[idx][idx2] = int(('{:08b}'.format(blocks128[idx][idx2])[::-1]), 2)

    for idx in range(1, len(blocks128)):
        blocks128[0] = blocks128[0] + blocks128[idx]
    del blocks128[1:]
    blocks128 = blocks128[0]
    return blocks128


def IPTable_func(blocks128):
    IPTabled_blocks128 = bytearray([0] * 128)
    for idx in range(128):
        IPTabled_blocks128[idx] = blocks128[IPTable[idx]]
    return IPTabled_blocks128


def FPTable_func(blocks128):
    FPTabled_blocks128 = bytearray([0] * 128)
    for idx in range(128):
        FPTabled_blocks128[idx] = blocks128[FPTable[idx]]
    return FPTabled_blocks128


def subkey(key):
    subkeys = list()
    for idx in range(7, -1, -1):
        subkeys.append(key[(0 + (idx * 2)):(2 + (idx * 2))])
    ic(subkeys)
    return subkeys


def key_132(subkeys):
    key_output = list()
    for idx in range(132):  # range 132
        xor_variable = bytes(a ^ b for (a, b) in zip(subkeys[abs(idx - 7) % 8], subkeys[abs(idx - 5) % 8]))
        xor_variable2 = bytes(a ^ b for (a, b) in zip(xor_variable, subkeys[abs(idx - 3) % 8]))
        xor_variable3 = int.from_bytes(bytes(a ^ b for (a, b) in zip(xor_variable2, subkeys[abs(idx - 1) % 8])), 'little')
        xor_variable4 = xor_variable3 ^ golden_ratio  # I feel like this doesn't work correctly
        xor_variable5 = xor_variable4 ^ idx
        xor_variable5 = leftRotate(xor_variable5, 11)
        key_output.append(xor_variable5)
    return key_output


def output_key(key_132):
    key_output = list()
    full_output = list()

    for idx in range(33):
        outbox = ['0b', '0b', '0b', '0b']
        word0 = int.to_bytes(key_132[0 + (4 * idx)], 4, 'little')
        word1 = int.to_bytes(key_132[1 + (4 * idx)], 4, 'little')
        word2 = int.to_bytes(key_132[2 + (4 * idx)], 4, 'little')
        word3 = int.to_bytes(key_132[3 + (4 * idx)], 4, 'little')
        for idx2 in range(4):
            words = list()
            words.append('{:08b}'.format((word0[idx2])))
            words.append('{:08b}'.format((word1[idx2])))
            words.append('{:08b}'.format((word2[idx2])))
            words.append('{:08b}'.format((word3[idx2])))

            for idx3 in range(8):
                nibble = words[0][idx3] + words[1][idx3] + words[2][idx3] + words[3][idx3]
                numval = int(nibble, 2)
                outnum = int(sboxes[(3 - idx) % 8][numval][0])
                tempbin = '{:04b}'.format((outnum))
                outbox[0] += tempbin[0]
                outbox[1] += tempbin[1]
                outbox[2] += tempbin[2]
                outbox[3] += tempbin[3]

        for x in range(4):
            key_output.append(outbox[x][2:])

    ic(len(key_output))
    ic(len(key_output[-1]))
    ic(key_output[-1])
    for i in range(33):
        full_output.append(key_output[4 * i] + key_output[4 * i + 1] + key_output[4 * i + 2] + key_output[4 * i + 3])
    ic(full_output[-1])
    return full_output
