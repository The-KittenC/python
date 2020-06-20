mingwen_src = 'abcdefghijklmnopqrstuvwxyz'
miwen_tar   = 'defghijklmnopqrstuvwxyzabc'
A = input('输入小写英文文字加密:')
while A.islower() == 0:
    A = input('输入正确的小写英文加密:')
B = ''
for single_char in A:
    if single_char in mingwen_src:
        index = mingwen_src.index(single_char)
        B = B + miwen_tar[index]
    else:
        B = B + single_char
        print('加密后:' + B)
else:
    print('请输入小写英文:')


C = ''
for jiemi in B:
    if jiemi in miwen_tar:
        index = miwen_tar.index(jiemi)
        C = C + mingwen_src[index]
    else:
        C = C + miwen_tar
print('解密后:' + C)

    