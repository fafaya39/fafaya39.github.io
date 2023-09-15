# coding=utf-8
import base64

print('锁言 - locktext')
print('版本：beta1.0.0')
while True:
    print('1.关于 2.解密 3.加密')
    user_select=input('>>> ')
    user_select_to_int=int(user_select)
    if user_select_to_int == 1:
        about='''锁言 - locktext
开发者:fafaya
fafaya的个人页：fafaya39.github.io
软件版本:beta1.0.0
目前可以实现base64加密'''
        print(about)
    if user_select_to_int == 2:
        try:
            print('请输入密文(base64)')
            users_text=input('>>> ')
            str2 = base64.b64decode(users_text.encode('utf-8')).decode()
            print(f'解密后的密文为：{str2}')
        except Exception:
            print('解密出现异常！请检查密文是否正确！')
    if user_select_to_int == 3:
        print('请输入密文')
        user_input=input('>>> ')
        str1=user_input
        base64_str = base64.b64encode(str1.encode('utf-8')).decode()
        print(f'加密后的密文为：{base64_str}')
        
    