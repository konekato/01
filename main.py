from cryptographism import number as cn

# 不要かも
def is_kind(kind):
    if kind == "lock" or kind == "unlock":
        return True
    return False

def get_locker(method, plain, key):
    if method == "mono number":
        return cn.mono_number_locker(plain, int(key))
    elif method == "stairs number":
        return cn.stairs_number_locker(plain, int(key))
    else:
        return "method not exist"

def get_unlocker(method, cipher, key):
    if method == "mono number":
        return cn.mono_number_unlocker(cipher, int(key))
    elif method == "stairs number":
        return cn.stairs_number_unlocker(cipher, int(key))
    else:
        return "method not exist"

# 命名変更必要
def get_answer(kind, method, text, key):
    if kind == "lock":
        return get_locker(method, text, key)
    elif kind == "unlock":
        return get_unlocker(method, text, key)
    else:
        return ""

CHOOSE_MESSAGE = (
    "\n"
    "choose kind of method\n"
    "- mono number\n"
    "- stairs number"
)

print("lock or unlock ?")
kind = input()
if not is_kind(kind):
    print("please answer 'lock' or 'unlock'\n")

print(CHOOSE_MESSAGE)
method = input()

print("\nplease enter your text")
text = input()

print("\nplease enter your key")
key = input()

print("\n" + get_answer(kind, method, text, key))