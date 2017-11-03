# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 00:56:12 2017

@author: Alexis  Martinez
 """
import os
from PIL import Image
import numpy as np
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET


### Estructura del archivo xml
root = Element('annotation')
tree = ElementTree(root)
folder = ET.SubElement(root,'folder')
filename = ET.SubElement(root,'filename')
path = ET.SubElement(root,'path')
source = ET.SubElement(root,'source')
database = ET.SubElement(source ,'database')
size = ET.SubElement(root,'size')
width = ET.SubElement(size,'width')
height = ET.SubElement(size,'height')
depth = ET.SubElement(size,'depth')
segmented = ET.SubElement(root,'segmented')
objects = ET.SubElement(root,'object')
name = ET.SubElement(objects,'name')
pose = ET.SubElement(objects,'pose')
truncated = ET.SubElement(objects,'truncated')
difficult = ET.SubElement(objects,'difficult')
bndbox = ET.SubElement(objects,'bndbox')
xmin = ET.SubElement(bndbox,'xmin')
ymin = ET.SubElement(bndbox,'ymin')
xmax = ET.SubElement(bndbox,'xmax')
ymax = ET.SubElement(bndbox,'ymax')


folder.text = 'fotos redes'

database.text = 'Viboras'
depth.text = "3"
segmented.text = "0"
difficult.text = "0"
pose.text = "Unspecified"
truncated.text = "0"
c = str(os.getcwd()) + "\ "
c = c[:-1]

for i in range(1,5):
    habitat = "viboras/h" + str(i) + ".jpg"
    print(habitat)
    image = Image.open(habitat)#.convert("RGBA")
    
    for j in range(1,6):
        vibora = "viboras/vib" + str(j) + ".png"
        print(vibora)
        vib = Image.open(vibora).convert("RGBA")
        
        name.text = "vib" + str(j)
        
        for k in range(10):
            size = np.random.randint(70,130)
            r = size/float(vib.width)
            sizeheight = int(vib.height * r)
            #vib = vib.rotate(np.random.randint(180))
            vib = vib.resize((size,sizeheight),Image.ANTIALIAS)
            image_copy = image.copy()
            width.text = str(image_copy.width)
            height.text = str(image_copy.height)
            
            
            
            posw = np.random.randint((image_copy.width - vib.width))
            xmin.text = str(posw)
            xmax.text = str(posw + vib.width)
            
            posh = np.random.randint((image_copy.height - vib.height))
            ymin.text = str(posh)
            ymax.text = str(posh + vib.height)
            
            position = (posw, posh)
            image_copy.paste(vib, position,vib)
            
            new_name = "viboras_" + str(i) + "_" + str(j) +"_"+ str(k)+ ".jpg"
            filename.text = new_name
            path.text = c + new_name
            
            new_namexml = "viboras_" + str(i) + "_" + str(j) +"_"+ str(k)+ ".xml"
            
            image_copy.save(new_name)
            tree.write(new_namexml)
        
        
        
    