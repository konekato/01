# number.py -> 数字の羅列平文を暗号化

# mono_number_... -> 一つの数字で暗号作成
def mono_number_locker(plain, key):
    plain_array = list(map(int, str(plain)))
    cipher = ""

    for p in plain_array:
        cipher_num = p - key
        if cipher_num < 0:
            cipher_num += 10
        cipher += str(cipher_num)

    return cipher

# mono_number_locker() の複合
def mono_number_unlocker(cipher, key):
    cipher_array = list(map(int, str(cipher)))
    plain = ""

    for c in cipher_array:
        plain_num = c + key
        if plain_num > 9:
            plain_num -= 10
        plain += str(plain_num)

    return plain

# stairs_number_... -> key + 0,1,2,3...9 を引いて暗号作成
def stairs_number_locker(plain, key):
    plain_array = list(map(int, str(plain)))
    cipher = ""

    for p in plain_array:
        cipher_num = p - key
        if cipher_num < 0:
            cipher_num += 10
        cipher += str(cipher_num)

        key += 1
        if key > 9:
            key = 0

    return cipher

# stairs_number_locker() の複合
def stairs_number_unlocker(cipher, key):
    cipher_array = list(map(int, str(cipher)))
    plain = ""

    for c in cipher_array:
        plain_num = c + key
        if plain_num > 9:
            plain_num -= 10
        plain += str(plain_num)

        key += 1
        if key > 9:
            key = 0

    return plain