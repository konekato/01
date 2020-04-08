from cryptographism import number as cn

def get_locker(method, plain, key):
    if method == "mono number":
        return cn.mono_number_locker(plain, key)
    elif method == "stairs number":
        return cn.stairs_number_locker(plain, key)
    elif method == "repetitive number":
        return cn.repetitive_number_locker(plain, key)
    else:
        return None

def get_unlocker(method, cipher, key):
    if method == "mono number":
        return cn.mono_number_unlocker(cipher, key)
    elif method == "stairs number":
        return cn.stairs_number_unlocker(cipher, key)
    elif method == "repetitive number":
        return cn.repetitive_number_unlocker(cipher, key)
    else:
        return None

def is_kind(kind):
    if kind == "lock" or kind == "unlock":
        return True
    return False

def is_locker(method):
    if get_locker(method, "", 0) is None:
        return False
    return True

def is_unlocker(method):
    if get_unlocker(method, "", 0) is None:
        return False
    return True

def is_method(method):
    if is_locker(method) or is_unlocker(method):
        return True
    return False

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
    "- stairs number\n"
    "- repetitive number"
)

print("lock or unlock ?")
kind = input()
if not is_kind(kind):
    print("\nplease answer 'lock' or 'unlock'")
    exit()

print(CHOOSE_MESSAGE)
method = input()
if not is_locker(method):
    print("\nmethod not exist")
    exit()

print("\nplease enter your text")
text = input()

print("\nplease enter your key")
try:
    key = int(input())
except ValueError:
    print("\nanswer the number")
    exit()

print("\n" + get_answer(kind, method, text, key))