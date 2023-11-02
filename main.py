import serpentfunctions as sf
from icecream import ic

# a,b = b, a
"""print("Please enter 128, 192, 256 for your keylength: ")
length = sf.input_val(2, int)
print("Please enter a numerical seed for the RNG: ")
rng = sf.input_val(16, int)
key = sf.generate_key(length, rng)"""
key = sf.generate_key()

test = sf.binary_from_file()
ic(len(test))
ic(test)

split_into_128 = sf.turn_into_128(test)
ic(split_into_128)
