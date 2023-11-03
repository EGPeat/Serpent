from icecream import ic
from random import randint, seed
import sys
import bitstring as bts


def call_globals():
    global IPTable
    global FPTable
    global golden_ratio
    global sboxes
    global LTTable
    global SBoxDecimalTable

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
    LTTable = [
        [16, 52, 56, 70, 83, 94, 105], [72, 114, 125], [2, 9, 15, 30, 76, 84, 126], [36, 90, 103],
        [20, 56, 60, 74, 87, 98, 109], [1, 76, 118], [2, 6, 13, 19, 34, 80, 88], [40, 94, 107],
        [24, 60, 64, 78, 91, 102, 113], [5, 80, 122], [6, 10, 17, 23, 38, 84, 92], [44, 98, 111],
        [28, 64, 68, 82, 95, 106, 117], [9, 84, 126], [10, 14, 21, 27, 42, 88, 96], [48, 102, 115],
        [32, 68, 72, 86, 99, 110, 121], [2, 13, 88], [14, 18, 25, 31, 46, 92, 100], [52, 106, 119],
        [36, 72, 76, 90, 103, 114, 125], [6, 17, 92], [18, 22, 29, 35, 50, 96, 104], [56, 110, 123],
        [1, 40, 76, 80, 94, 107, 118], [10, 21, 96], [22, 26, 33, 39, 54, 100, 108], [60, 114, 127],
        [5, 44, 80, 84, 98, 111, 122], [14, 25, 100], [26, 30, 37, 43, 58, 104, 112], [3, 118],
        [9, 48, 84, 88, 102, 115, 126], [18, 29, 104], [30, 34, 41, 47, 62, 108, 116], [7, 122],
        [2, 13, 52, 88, 92, 106, 119], [22, 33, 108], [34, 38, 45, 51, 66, 112, 120], [11, 126],
        [6, 17, 56, 92, 96, 110, 123], [26, 37, 112], [38, 42, 49, 55, 70, 116, 124], [2, 15, 76],
        [10, 21, 60, 96, 100, 114, 127], [30, 41, 116], [0, 42, 46, 53, 59, 74, 120], [6, 19, 80],
        [3, 14, 25, 100, 104, 118], [34, 45, 120], [4, 46, 50, 57, 63, 78, 124], [10, 23, 84],
        [7, 18, 29, 104, 108, 122], [38, 49, 124], [0, 8, 50, 54, 61, 67, 82], [14, 27, 88],
        [11, 22, 33, 108, 112, 126], [0, 42, 53], [4, 12, 54, 58, 65, 71, 86], [18, 31, 92],
        [2, 15, 26, 37, 76, 112, 116], [4, 46, 57], [8, 16, 58, 62, 69, 75, 90], [22, 35, 96],
        [6, 19, 30, 41, 80, 116, 120], [8, 50, 61], [12, 20, 62, 66, 73, 79, 94], [26, 39, 100],
        [10, 23, 34, 45, 84, 120, 124], [12, 54, 65], [16, 24, 66, 70, 77, 83, 98], [30, 43, 104],
        [0, 14, 27, 38, 49, 88, 124], [16, 58, 69], [20, 28, 70, 74, 81, 87, 102], [34, 47, 108],
        [0, 4, 18, 31, 42, 53, 92], [20, 62, 73], [24, 32, 74, 78, 85, 91, 106], [38, 51, 112],
        [4, 8, 22, 35, 46, 57, 96], [24, 66, 77], [28, 36, 78, 82, 89, 95, 110], [42, 55, 116],
        [8, 12, 26, 39, 50, 61, 100], [28, 70, 81], [32, 40, 82, 86, 93, 99, 114], [46, 59, 120],
        [12, 16, 30, 43, 54, 65, 104], [32, 74, 85], [36, 90, 103, 118], [50, 63, 124], [16, 20, 34, 47, 58, 69, 108],
        [36, 78, 89], [40, 94, 107, 122], [0, 54, 67], [20, 24, 38, 51, 62, 73, 112],
        [40, 82, 93], [44, 98, 111, 126], [4, 58, 71], [24, 28, 42, 55, 66, 77, 116],
        [44, 86, 97], [2, 48, 102, 115], [8, 62, 75], [28, 32, 46, 59, 70, 81, 120],
        [48, 90, 101], [6, 52, 106, 119], [12, 66, 79], [32, 36, 50, 63, 74, 85, 124],
        [52, 94, 105], [10, 56, 110, 123], [16, 70, 83], [0, 36, 40, 54, 67, 78, 89],
        [56, 98, 109], [14, 60, 114, 127], [20, 74, 87], [4, 40, 44, 58, 71, 82, 93],
        [60, 102, 113], [3, 18, 72, 114, 118, 125], [24, 78, 91], [8, 44, 48, 62, 75, 86, 97],
        [64, 106, 117], [1, 7, 22, 76, 118, 122], [28, 82, 95], [12, 48, 52, 66, 79, 90, 101],
        [68, 110, 121], [5, 11, 26, 80, 122, 126], [32, 86, 99]]
    golden_ratio = bts.BitArray(bin='10011101100111101110110001111001', length=32)

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


def generate_key(key_len=256, sneed=2023):
    seed(sneed)
    key_bin = bts.BitArray(uint=0, length=key_len)
    for idx in range(key_len):
        key_bin[idx] = (randint(0, 1))
    return key_bin


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
    return info, filename


# changes endian as necessary, pads to nearest multiple of 128
def endian_and_padding(binary):  # rewrite using bitarray? Or leave be
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
    IPTabled_blocks128 = bts.BitArray(blocks128)
    for idx in range(128):
        IPTabled_blocks128[idx] = blocks128[IPTable[idx]]
    return IPTabled_blocks128


def FPTable_func(blocks128):
    FPTabled_blocks128 = bts.BitArray(blocks128)
    for idx in range(128):
        FPTabled_blocks128[idx] = blocks128[FPTable[idx]]
    return FPTabled_blocks128


def subkey(key):  # rewritten, verified.
    subkeys = list()
    for idx in range(0, 8):
        subkeys.append(key[(0 + (idx * 32)):(32 + (idx * 32))])
    return subkeys


def key_132(subkeys):  # rewritten, verified.
    key_output = list()
    for idx in range(132):
        xor_variable = subkeys[(- 8)] ^ subkeys[(- 5)]
        xor_variable ^= subkeys[(- 3)]
        xor_variable ^= subkeys[(- 1)]
        xor_variable ^= golden_ratio  # I feel like this doesn't work correctly
        intcheck = bts.BitArray(uint=idx, length=32)
        intcheck.reverse()
        xor_variable ^= intcheck
        xor_variable.ror(11)
        subkeys.append(xor_variable)
        key_output.append(xor_variable)
    return key_output


def output_key(key_132):  # rewrite using bitarray
    full_output = list()

    for idx in range(33):
        outbox = [bts.BitArray(), bts.BitArray(), bts.BitArray(), bts.BitArray()]
        word0 = (key_132[0 + (4 * idx)])
        word1 = (key_132[1 + (4 * idx)])
        word2 = (key_132[2 + (4 * idx)])
        word3 = (key_132[3 + (4 * idx)])

        for idx3 in range(32):  # 32
            nibble = bts.BitArray(bool=word3[idx3])
            nibble.append(bts.BitArray(bool=word2[idx3]))
            nibble.append(bts.BitArray(bool=word1[idx3]))
            nibble.append(bts.BitArray(bool=word0[idx3]))  # jank, fix later
            outnum_ba = bts.BitArray(uint=int(sboxes[(3 - idx) % 8][nibble.uint][0]), length=4)
            outbox[0].append(bts.BitArray(bool=outnum_ba[3]))
            outbox[1].append(bts.BitArray(bool=outnum_ba[2]))
            outbox[2].append(bts.BitArray(bool=outnum_ba[1]))
            outbox[3].append(bts.BitArray(bool=outnum_ba[0]))
        full_output.append(outbox[0] + outbox[1] + outbox[2] + outbox[3])
    return full_output


def ic_testing(variable):
    ic(variable)
    ic(type(variable))
    ic(len(variable))


def print_ba(data, length=128):
    length = len(data)

    bin_nums = ''
    for idx in range(length):
        if (data[idx]):
            bin_nums += "1"
        else:
            bin_nums += "0"
    print(bin_nums)


def sbox_function(word, round_num):
    output = bts.BitArray(uint=0, length=32)
    for idx in range(8):
        temp = sboxes[round_num][word[0 + (idx * 4):4 + (idx * 4)].uint][0]
        output[0 + (idx * 4):4 + (idx * 4)] = bts.BitArray(uint=temp, length=4)
    return output


def lin_transform(input):
    result = bts.BitArray(uint=0, length=128)
    for idx in range(len(LTTable)):
        outputBit = False
        for yidx in LTTable[idx]:
            outputBit = (outputBit ^ input[yidx])
        result[idx] = outputBit
    return result
