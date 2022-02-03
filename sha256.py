# Gerrit van Rensburg
# Jan 29 2022

# Pseudo code from Wikipedia SHA-2: https://en.wikipedia.org/wiki/SHA-2

# L is oritignal message (current 40x Fs)

L = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF1
print("L: ", L)
print("0xL: ", hex(L))

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

pL = int(L+1)
print("0xpL: ", hex(pL))
# create for loop to add pad zeros to 512 or (448) and then add in 64 at the very end
# 512 zeros = 128 zeros in hexidecimal (512/4) 
padding = int(128)
print("padding: ", padding)
#padding is left shift which is based multiplication

#modulous variable to stop while when = 0 - multiple of 512 in binary or 128 in hex
#LOGIC CHECK: padding with checing for multiple of 128 or 512 doesn't work
#Next Steps: Looks at converting hex to a string, count the string characters and then continue to pad until string is 128 characters long (excluding 0x)
#Once 128 characters long (excluding 0x) finish padding and add 64 to end.
mod = pL%padding
print("mod", mod)
while (mod!=0):
    pL = pL*16
    print("Padding pL: ", hex(pL))
    mod = pL%padding





#to convert pL to string 0x to pad
#pLchar = chr(pL)
#print(pLchar)

#to pad a string with zeros and print it as a hex value
#pLp = f"{pL:#0{padding}X}"
#print(pLp)


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
 
# Driver program to
# test above functions
# n = 16
# d = 2
 
# print("Left Rotation of",n,"by"
#       ,d,"is",end=" ")
# print(leftRotate(n, d))
 
# print("Right Rotation of",n,"by"
#      ,d,"is",end=" ")
# print(rightRotate(n, d))