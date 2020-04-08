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

# repetitive_number_... -> 反復数で暗号作成 （入力：key=12 -> 121212.. が引かれる）
def repetitive_number_locker(plain, key):
    plain_array = list(map(int, str(plain)))
    key_array = list(map(int, str(key)))
    cipher = ""

    i = 0
    for p in plain_array:
        cipher_num = p - key_array[i]
        if cipher_num < 0:
            cipher_num += 10
        cipher += str(cipher_num)

        i = i+1 if i < (len(key_array) - 1) else 0

    return cipher

# repetitive_number_locker() の複合
def repetitive_number_unlocker(cipher, key):
    cipher_array = list(map(int, str(cipher)))
    key_array = list(map(int, str(key)))
    plain = ""

    i = 0
    for c in cipher_array:
        plain_num = c + key_array[i]
        if plain_num > 9:
            plain_num -= 10
        plain += str(plain_num)

        i = i+1 if i < (len(key_array) - 1) else 0

    return plain