print("包含字符串的Str");
print(ord('中')); #20013
print(chr(23922));#嵲
print('ABC'.encode('ascii'));#b'ABC'
print(b'ABC'.decode('ascii'));#ABC
print('中文'.encode('utf-8'));#b'\xe4\xb8\xad\xe6\x96\x87'
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'));#中文
print(len('ABC'));#3
print('Hello, %s' % 'Nancy');#Hello, Nancy
print('Hello %s, this is %s' % ('Nancy','Daisy'));#Hello Nancy, this is Daisy
print('your phone %d count is %f' % (13371860993, 10.05));#your phone 13371860993 count is 10.050000
