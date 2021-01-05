color = 0xF0384E
red = color >> 16
green = color >> 8 & 0xFF
blue = color & 0xFF
print(red,green,blue)
print(hex(red),hex(green),hex(blue))

