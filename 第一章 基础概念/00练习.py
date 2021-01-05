 numColor = 0xF0384E
 exB = numColor >> 8
 red = exB >> 8
 red00 = red << 16
 exR = red00 ^ numColor
 green = exR >> 8
 blue = exR ^ green
 print('红色',red,'绿色',green.'蓝色'.blue)