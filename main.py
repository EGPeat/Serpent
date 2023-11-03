import serpentfunctions as sf
import bitstring as bts


"""print("Please enter 128, 192, 256 for your keylength: ")
length = sf.input_val(2, int)
print("Please enter a numerical seed for the RNG: ")
rng = sf.input_val(16, int)
key = sf.generate_key(length, rng)"""

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
                sboxed_128[0 + (split_idx * 32):32 + (split_idx * 32)] = sf.sbox_function(word_ba, idx)
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
