from PIL import Image
import image
import os

def readDirectory(path,classe,arqv):
    for r, d, f in os.walk(path):
        for file in f:
            if '.bmp' in file:
                readImg(os.path.join(r, file),classe,arqv)



def readImg(path,classe,f):

    image = Image.open(path,'r')
    pix_val = list(image.getdata())

    tamList = len(pix_val)
    divList = int(tamList/50)

    controlList = 0
    resultList = list()
    contList = 0
    normList = 0

    for i in pix_val:

        if i != 255:
            contList += 1
            normList += 1

        if controlList == (divList - 1):
            resultList.append(contList)
            controlList = 0
            contList = 0

        controlList += 1

    for i in range(0,len(resultList)):
        f.write('%.5f' % round(float(resultList[i]/normList),5));
        f.write(' ')

    f.write(str(classe))
    f.write("\n")

def main():
    f = open("train.txt","w")

    readDirectory("./bart",0,f)
    readDirectory("./homer",1,f)
    readDirectory("./lisa",2,f)
    readDirectory("./maggie",3,f)
    readDirectory("./marge",4,f)
    
    f.close

if __name__ == "__main__":
    main()