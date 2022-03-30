# Gerrit van Rensburg
# Jan 29 2022

# Pseudo code from Wikipedia SHA-2: https://en.wikipedia.org/wiki/SHA-2

# L is original message (current 40x Fs)

import math


L = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF1
print("L: ", L)
print("0xL: ", hex(L))

hexCount = int(math.log(L,16)) #hexCount is to determine number of hexidecimals to add at end of preprocessing
#print("Number of hexidecimal digits:", hexCount) 


# Initial hash values h's are the first 32 bits of the fractional 
# parts of the square roots of first 8  primes 2 to 19.

h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a
h4 = 0x510e527f
h5 = 0x9b05688c
h6 = 0x1f83d9ab
h7 = 0x5be0cd19

# Initialize array of round constants:
# (first 32 bits of the fractional parts of the cube roots of the first 64 primes 2..311)

k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
   0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
   0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
   0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
   0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
   0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
   0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
   0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

# Preprocessing (padding)

pL = int(L+1) #pL is preprocessed message 
print("0xpL: ", hex(pL))

# create for loop to add pad zeros to 512 or (448) and then add in 64 at the very end
# 512 zeros = 128 zeros in hexidecimal (512/4) 
padding = int(128)
#print("padding: ", padding)
#padding is left shift which is based multiplication

#modulous variable to stop while when = 0 - multiple of 512 in binary or 128 in hex
xpL = math.log(pL,16)  #xpL variable to keep track of number of hexidecimal digits
mod = xpL % padding
# print("mod", mod)
while (mod!=0):
    pL = pL*16
    #print("Padding pL: ", hex(pL))
    xpL = math.log(pL,16)
    mod = xpL % padding


pLp = pL + hexCount #pLp is the post-processed message L which has been padded and initial digits added
print("Post-processed message:", hex(pLp))
 
 # ----------------- Preprocessing completed above ------------------------------

#32 bits is 8 hexidecimals
#post-processed message is 128 hexidecimals = 16* 8 hexidecimal words per address
message_schedule_array = [0x00000000]*64 #create empty message schedule array of 64* 32 bit words

split = int(128) #split variable to split the 512 bit - 128 hexidecimal message into 16* 8 hexidecimal words
temp = pLp #modifying temp to preserve pLp
hexWord = 0 #temp value to store and write 8 hexidecimal word to message_schedule_array
array_index = 0 #value to increment through message schedule array indices


# LOGIC CHECK - need to split the pLp into 8 hexidecimal words in hex would be pLp // 120..112..104..96..etc
# So 120..112..104..96.. are the positions, not the value that represent them - find those and then convert them to decimal and do decimal division for qoutient 
while (split!=0):
    split = split-8
    splitor = int(math.pow(16,split)) # determine the proper value for splitting the 8 bits
    hexWord = temp//splitor #taking qoutient of hexidecimal over split 
    # print("hexWord",array_index,":",hex(hexWord))
    array_index = array_index+1

    #LOGIC CHECK - need to determine to remove the 8 most significant hexidecimals hexWord from temp - so the next 8 significant hexidecimals can be removed
    temp = temp - (hexWord*(16*split))
    # print("Temp:", hex(temp))


INT_BITS = 32

# Function to left
# rotate n by d bits
def leftRotate(n, d):
 
    # In n<<d, last d bits are 0.
    # To put first 3 bits of n at
    # last, do bitwise or of n<<d
    # with n >>(INT_BITS - d)
    return (n << d)|(n >> (INT_BITS - d))
 
# Function to right
# rotate n by d bits
def rightRotate(n, d):
 
    # In n>>d, first d bits are 0.
    # To put last 3 bits of at
    # first, do bitwise or of n>>d
    # with n <<(INT_BITS - d)
    return (n >> d)|(n << (INT_BITS - d)) & 0xFFFFFFFF
 
