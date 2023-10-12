from PIL import Image, ImageFilter


class ImageEditor():
    def __init__(self,filename):
        self.filename = filename
        self.original = None
        self.changed = []

    def open(self):
        try:
            self.original = Image.open(self.filename)
            self.original.show()
        except:
            print("Файл не існує")

    def do_left(self):
        left = self.original.transpose(Image.ROTATE_90)
        self.changed.append(left)
        
        left.save('left.png' + self.filename)

    def do_crop(self):
        box = (100, 100, 200, 200)
        cropped = self.original.crop(box)
    
        self.changed.append(cropped)
        
        cropped.save('croped.png' + self.filename)
    
    
    
img = ImageEditor('man.jpg')
img.open()

img.do_left()
img.do_crop()

img1 = ImageEditor('rotate.jpg')
img1.open()

img2 = ImageEditor('blur.jpg')
img2.open()

img3 = ImageEditor('grey.jpg')
img3.open()