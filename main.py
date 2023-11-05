import serpentfunctions as sf
import bitstring as bts

import time
import ctypes

sbox_lib = ctypes.CDLL('./sboxes.dll')
# cc -fPIC -shared -o sboxes.dll sboxes.c
# compile the sboxes.c to either sboxes.dll or sboxes.co

sbox_lib.sbox_function.argtypes = (ctypes.c_uint32, ctypes.c_int, ctypes.POINTER(ctypes.c_uint32))
sbox_lib.sbox_function.restype = ctypes.c_uint32

SBoxDecimalTable = [
    3, 8, 15, 1, 10, 6, 5, 11, 14, 13, 4, 2, 7, 0, 9, 12,
    15, 12, 2, 7, 9, 0, 5, 10, 1, 11, 14, 8, 6, 13, 3, 4,
    8, 6, 7, 9, 3, 12, 10, 15, 13, 1, 14, 4, 0, 11, 5, 2,
    0, 15, 11, 8, 12, 9, 6, 3, 13, 1, 2, 4, 10, 7, 5, 14,
    1, 15, 8, 3, 12, 0, 11, 6, 2, 5, 4, 10, 9, 14, 7, 13,
    15, 5, 2, 11, 4, 10, 9, 12, 0, 3, 14, 8, 13, 6, 7, 1,
    7, 2, 12, 5, 8, 4, 6, 11, 14, 9, 1, 15, 13, 3, 10, 0,
    1, 13, 15, 0, 14, 8, 2, 11, 7, 4, 12, 10, 9, 3, 5, 6,
]


sboxes_c = (ctypes.c_uint32 * 128)(*SBoxDecimalTable)

"""print("Please enter 128, 192, 256 for your keylength: ")
length = sf.input_val(2, int)
print("Please enter a numerical seed for the RNG: ")
rng = sf.input_val(16, int)
key = sf.generate_key(length, rng)"""
start = time.perf_counter()

sf.call_globals()
key = sf.generate_key()
subkeys = sf.subkey(key)
usable_keys = sf.key_132(subkeys)
full_keys = sf.output_key(usable_keys)

binary_data, filename = sf.binary_from_file()  # change
padded_info = bts.BitArray(sf.endian_and_padding(binary_data))
print(len(padded_info))

need_1000 = 0
fp_tabled_data = bts.BitArray()
word_ba = list()
sboxed_128 = bts.BitArray(uint=0, length=128)

with open(f"{filename}encoded.txt", "wb") as outputfile:
    while padded_info:
        data_bitarray = padded_info[0:128].copy()
        del padded_info[0:128]
        need_1000 += 16
        data_128_IPTabled = sf.IPTable_func(data_bitarray)

        for idx in range(32):
            data_128_IPTabled ^= full_keys[idx]
            for split_idx in range(4):
                word_ba = data_128_IPTabled[0 + (split_idx * 32):32 + (split_idx * 32)]
                result = sbox_lib.sbox_function(ctypes.c_uint32(word_ba.uint), idx, sboxes_c)
                sboxed_128[0 + (split_idx * 32):32 + (split_idx * 32)] = result
            data_128_IPTabled = sboxed_128
            if idx != 31:
                data_128_IPTabled = sf.lin_transform(sboxed_128)
        data_128_IPTabled = data_128_IPTabled ^ full_keys[32]
        data_128_IPTabled = sf.FPTable_func(data_128_IPTabled)
        fp_tabled_data.append(data_128_IPTabled)

        if need_1000 >= 1000:
            fp_tabled_data.tofile(outputfile)
            fp_tabled_data.clear()
            need_1000 = 0
    fp_tabled_data.tofile(outputfile)

elapsed = time.perf_counter() - start

print(f"elapsed time is {elapsed}")
