"""
contoh:
budi -> udibeuy
kereta -> eretakeuy
kram -> amkreuy
astronot -> tronotaseuy
"""

def bahaneh(x='Budi'):
    import string
    voc = ['a','i','u','e','o','A','I','U','E','O']
    con = set(list(string.ascii_letters)) - set(voc)
    if x[0] in con and x[1] in con:
        return x[2:] + x[:2] + 'euy'
    elif x[0] in voc and x[1] in con:
        return x[2:] + x[:2] + 'euy'
    else:  
        return x[1:] + x[:1] + 'euy'

"""
if __name__ == "__main__":
    x = input("Masukkan string di sini: ")
    bahaneh(x)
"""

stc = "yuk kita main layangan di rumah ini"
stc_bahaneh = map(bahaneh, stc.split())

print " ".join(stc_bahaneh)

"""
stc_bahaneh = ""
for i in stc.split():
    stc_bahaneh += bahaneh(i) + " "
"""

"""
i = 0
while i < len(stc.split()):
    if i == len(stc.split()) - 1:
        stc_bahaneh += bahaneh(stc.split()[i])
    stc_bahaneh += bahaneh(stc.split()[i]) + " "
    i += i

print stc_bahaneh
"""





