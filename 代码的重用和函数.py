mingwen_src = 'abcdefghijklmnopqrstuvwxyz'
miwen_tar   = 'defghijklmnopqrstuvwxyzabc'

def JIAMI():
    global mingwen_src, miwen_tar
    global A
    B = ''
    for C in A:
        if C in mingwen_src:
            index = mingwen_src.index(C)
            B = B + miwen_tar[index]
        else:
            B = B + C
    return B

def JIEMI():
    global mingwen_src, miwen_tar
    C = ''
    for jiemi in JIAMI():
        if jiemi in miwen_tar:
            index = miwen_tar.index(jiemi)
            C = C + mingwen_src[index]
        else:
            C = C + miwen_tar
    return C


A = input('输入加密小写英文')
while A.islower() == 0:
    A = input('输入正确的小写英文加密:')
print('加密后:' + JIAMI())
print('解密后:' + JIEMI())
