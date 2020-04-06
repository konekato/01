from cryptographism import number as cn

# 以下デバッグ用
plain = input()
key = int(input())

cipher_str = cn.mono_number_locker(plain, key)
print(cipher_str)

print(cn.mono_number_unlocker(int(cipher_str), key))