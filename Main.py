
from ImageRead import ImageParser
def main():
    img = ImageParser('./TestImages/stinkbug.png')
    img.ConvertImage()

if __name__ == "__main__":
    main()

print("program finished")