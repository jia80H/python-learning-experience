""" hashlib 和 hmac """
import hmac
import hashlib
# hmac 加密
h = hmac.new(b'12345678',b'abc')
result = h.hexdigest()
print(h)