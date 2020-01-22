import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#currently only works with PNG images 
class ImageParser:
    def __init__(self, image):
        self.imagelocation = image
    def ParseImageData(self, plot):
        pass
    def ConvertImage(self):
        self.importedImage = mpimg.imread(self.imagelocation)
        print(self.importedImage)
        
        
