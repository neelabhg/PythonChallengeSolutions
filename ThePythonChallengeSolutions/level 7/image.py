from PIL import Image, ImageFilter

original = Image.open('oxygen.png')
print original.format, original.size, original.mode

# From http://stackoverflow.com/questions/1109422/getting-list-of-pixel-values-from-pil
pixels = list(original.getdata())
width, height = original.size
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

# print pixels[94][628]
# original.show()

message = chr(pixels[43][0][0])

for i in range(86):
    message += chr(pixels[43][5 + 7*i][0])

print 'message: ', message

next_level = "".join([chr(x) for x in [105, 110, 116, 101, 103, 114, 105, 116, 121]])
print 'next level: ', next_level

raw_input('Press a key to exit')
