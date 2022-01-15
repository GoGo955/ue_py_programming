from img_rec import img_rec
import glob

if __name__ == "__main__":
    files = glob.glob("pics/*")
    files = [file.replace("\\", "/") for file in files]

    for file in files:
        img_rec(file)
