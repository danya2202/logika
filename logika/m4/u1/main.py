from PIL import Image, ImageFilter

with Image.open('man.jpg') as orig:
    print(orig.mode)
    print(orig.format)
    print(orig.size)

    bw_orig = orig.convert('L')
    bw_orig.show()
    bw_orig.save('grey.jpg')
    
    blur_orig = orig.filter(ImageFilter.BLUR)
    blur_orig.show()
    blur_orig.save("blur.jpg")
    
    pic_up = orig.transpose(Image.ROTATE_180)
    pic_up.show()
    pic_up.save('rotate.jpg')