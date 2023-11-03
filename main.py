import serpentfunctions as sf
from icecream import ic
import bitstring as bts
# a,b = b, a

# this is not a bitslice form of anything
"""print("Please enter 128, 192, 256 for your keylength: ")
length = sf.input_val(2, int)
print("Please enter a numerical seed for the RNG: ")
rng = sf.input_val(16, int)
key = sf.generate_key(length, rng)"""

sf.call_globals()
key = sf.generate_key()
key = bytearray(key.to_bytes(16, 'little'))
subkeys = sf.subkey(key)

usable_keys = sf.key_132(subkeys)
full_keys_not_ba = sf.output_key(usable_keys)

full_keys = list()
for idx in range(len(full_keys_not_ba)):
    full_keys.append(bts.BitArray(uint=(int(full_keys_not_ba[idx], 2)), length=128))


binary_data, filename = sf.binary_from_file()
padded_info = sf.endian_and_padding(binary_data)

with open(f"{filename}encoded.txt", "wb") as outputfile:
    while padded_info:
        data_bitarray = bts.BitArray(padded_info[0:16])
        del padded_info[0:16]
        data_bitarray2 = bts.BitArray(data_bitarray)
        data_128_IPTabled = sf.IPTable_func(data_bitarray)

        for idx in range(32):
            xored_ba = full_keys[idx] ^ data_128_IPTabled
            word_ba = list()
            sboxed_128 = bts.BitArray(uint=0, length=128)
            for split_idx in range(4):
                word_ba = xored_ba[0 + (split_idx * 32):32 + (split_idx * 32)]
                sboxed_128[0 + (split_idx * 32):32 + (split_idx * 32)] = sf.sbox_function(word_ba, 0)
            data_128_IPTabled = sf.lin_transform(sboxed_128)
        fp_tabled_data = sf.IPTable_func(data_128_IPTabled)
        fp_tabled_data.tofile(outputfile)


# data_128_FPTabled = sf.FPTable_func(data_128_IPTabled)
# ic(data_128_FPTabled)
