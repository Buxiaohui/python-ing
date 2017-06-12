''' threadlocal 的 下标计算'''
HASH_INCREMENT = 0x61c88647

''' len = 2^n '''
def magic_hash(len):
    x = ""
    for i in range(len):
        nextHashCode = i * HASH_INCREMENT + HASH_INCREMENT
        x = x+str((nextHashCode & (len - 1)))+" , "
    print(x)

magic_hash(16)
magic_hash(32)