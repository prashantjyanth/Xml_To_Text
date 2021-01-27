#----------------------------------------------------- xml to txt-------------------------------------------------------------
from pathlib import Path
import string
sl = list(string.ascii_uppercase)
nl = list(str(i) for i in range(0,10))
nl.extend(sl)
r = list(i for i in range(0,36))
dictionary = dict(zip(nl, r))
from bs4 import BeautifulSoup
import glob

imdir = 'G:\\yolo_ocr_data\\'
ext = ['xml']    # Add image formats here

files = []
[files.extend(glob.glob(imdir + '*.' + e)) for e in ext]
# print(files)
for file in files:
    txt = Path(file).read_text()
    cc = BeautifulSoup(txt)
    xmlw = cc.size.width.contents[0]
    xmll = cc.size.height.contents[0]
    l=[]
    cl = []
    xmlw=int(xmlw)
    xmlh = int(xmll)
    if xmlw>xmlh:
        obj=cc.find_all('object')
        with open(file.split('.')[0]+'.txt','a') as fl:
            for i in obj:
                n=i.find('name').contents[0]
                xmin=i.bndbox.find('xmin').contents[0]
                ymin=i.bndbox.find('ymin').contents[0]
                xmax=i.bndbox.find('xmax').contents[0]
                ymax=i.bndbox.find('ymax').contents[0]
                xmin,ymin,xmax,ymax=int(xmin),int(ymin),int(xmax),int(ymax)
                xc1 = (xmax+xmin)/2
                xc = xc1/xmlw
                xc=round(xc,6)
                yc1 = (ymax+ymin)/2
                yc = yc1/xmlh
                yc=round(yc,6)
                w1 = (xmax-xc1)*2/xmlw
                w1=round(w1,6)
                h1 = (ymax-yc1)*2 / xmlh
                h1=round(h1,6)
                strg = " ".join(str(x) for x in [dictionary[n],xc,yc,w1,h1])
    #             print(strg)
                fl.write(strg+'\n')
            fl.close()
    else:
        obj=cc.find_all('object')
        with open(file.split('.')[0]+'.txt','a') as fl:
            for i in obj:
                n=i.find('name').contents[0]
                xmin=i.bndbox.find('xmin').contents[0]
                ymin=i.bndbox.find('ymin').contents[0]
                xmax=i.bndbox.find('xmax').contents[0]
                ymax=i.bndbox.find('ymax').contents[0]
                xmin,ymin,xmax,ymax=int(xmin),int(ymin),int(xmax),int(ymax)
                xc1 = (xmax+xmin)/2
                xc = xc1/xmlh
                xc=round(xc,6)
                yc1 = (ymax+ymin)/2
                yc = yc1/xmlw
                yc=round(yc,6)
                w1 = (xmax-xc1)*2/xmlh
                w1=round(w1,6)
                h1 = (ymax-yc1)*2 / xmlw
                h1=round(h1,6)
                strg = " ".join(str(x) for x in [dictionary[n],xc,yc,w1,h1])
    #             print(strg)
                fl.write(strg+'\n')
            fl.close()
        
