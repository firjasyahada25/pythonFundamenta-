# macam macam string

# cara mengubah ' agar  menjadi string
print('malam jum\'at')
print('g\'day. isn\'t it?')

# backlash
print("C:\\user\\ucup")

# tab
print("ucup\t\totong, semakin jauhan")

# backspace
print("ucup \botong, jadi dekat")

# Newline
print("baris pertama. \nbaris kedua") # LF ->> Line Feed ; macos, uni
print("baris pertama. \rbaris kedua") # CR ->> Carriage Reaturn
print("baris pertama. \r\nbaris kedua") # CRLF ->> Line Feed Carriage Reaturn

# Raw Sting " tidak mendeteksi string"

print(r'baris pertama. \r\n\\b baris kedua')


#  Multi-Line Literal Stiring 
print("""
 name = firja
 kegantengan= 10000%

 """)

#  Multi-Line Literal Stiring dan RAW
print(r"""
 name = firja\n ganteng
 kegantengan= 10000%
 website: porot.id.firja//988.com

 """)


