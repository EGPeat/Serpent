import serpentfunctions as sf
from icecream import ic

# a,b = b, a
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
full_keys = sf.output_key(usable_keys)
quit()
binary_data = sf.binary_from_file()
padded_info = sf.endian_and_padding(binary_data)


# Eventually turn this into a loop, and then into a function to call
data_128 = padded_info[0:128]
ic(data_128)


data_128_IPTabled = sf.IPTable_func(data_128)
ic(data_128_IPTabled)

# data_128_FPTabled = sf.FPTable_func(data_128_IPTabled)
# ic(data_128_FPTabled)
