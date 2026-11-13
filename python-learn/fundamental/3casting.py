#apa itu casting?
#casting adalah merubah dari satu tipe ke tipe lain

##integer
print("""DATA INTEGER""")
data_integer = 8
print("type =", data_integer, type(data_integer) )

data_float = float(data_integer)
data_string = str(data_integer)
data_bool = bool(data_integer)

print(data_float)
print(data_string)
print(data_bool)

## FLOAT
print("""DATA FLOAT""") 
data_float = 8.0
print("type =", data_float, type(data_float) )

data_integer = int(data_float)
data_string = str(data_float)
data_bool = bool(data_float)

print(data_integer)
print(data_string)
print(data_bool)

## BOOLEAN
print("""DATA BOOLEAN""") 
data_bool = True
print("type =", data_bool, type(data_bool) )

data_integer = int(data_bool)
data_string = str(data_bool)
data_float = float(data_bool)

print(data_integer)
print(data_string)
print(data_float)

## string
print("""DATA STRING""") 
data_string = "6" 
print("type =", data_string, type(data_string) )

data_integer = int(data_string)
data_float = float(data_string)
data_bool = bool(data_string)

print(data_integer)
print(data_float)
print(data_bool)

