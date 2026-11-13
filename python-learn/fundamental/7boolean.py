# Operasi logika atau Booleam
# not, or, and ,xor

# Not
a = True
b = not a
print(a)

#  OR (Jika salah satu True maka hasilnya = True)
print("----OR----")

a = True
b = False
c = a or b
print('False + False =', b or b ) # False
print('False + True =', b or a )  # True
print('True + False =', a or b )  # True
print('True + True =', a or a )   #True


#  AND (Jika salah satu tetap False maka hasilnya = False, True jika true + true)
print("----AND----")

a = True
b = False
c = a and b
print('False + False =', b and b ) # False
print('False + True =', b and a )  # False
print('True + False =', a  and b ) # False
print('True + True =', a  and a )  #True

#  XOR (Jika True + True maka hasilnya = False)
print("----XOR----")

a = True
b = False
c = a ^ b
print('False + False =', b ^ b ) # False
print('False + True =', b ^ a )  # True
print('True + False =', a ^ b )  # True
print('True + True =', a ^ a )   #false

