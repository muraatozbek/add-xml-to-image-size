import xml.etree.ElementTree as ET
import os
import glob
import cv2
import time
import shutil


xml_dir='/path/of/folder/xml/'
images_dir='/path/of/image/folder/'

xmls=glob.glob(xml_dir+"*") # give the direction of XMl file this will out put full path with xml file
images=glob.glob(images_dir+"*") # give the direction of Image file this will out put full path with image file


    
#Taking only names removing ext ie .xml
xmls_names=[]
for xml in xmls:
    xml=xml.split("/")[-1]
    ext=xml.split(".")[-1]
    xml=xml.replace(ext,"")
    xmls_names.append(xml)
    
    
#Taking only names removing ext ie .images
images_names=[]
for image in images:
    image=image.split("/")[-1]
    ext=image.split(".")[-1]
    image=image.replace(ext,"")
    images_names.append(image)
writer_counter=0   
for xmls_name in xmls_names:
    try:
        if xmls_name in images_names:
            # print(xmls_name)
            read_xml=xml_dir+xmls_name+"xml"
            img=cv2.imread(images_dir+xmls_name+"jpg")
            img_width,img_hight,dept = img.shape
            tree = ET.parse(read_xml)
            root = tree.getroot()
            element_size = root.find('size')
            if not element_size:  # careful!
                doc = ET.parse(read_xml)
                root_node = doc.getroot()
                child = ET.SubElement(root_node, "size")
                group1  = ET.SubElement(child,"width")
                group1.text = str(img_width)
                group2  = ET.SubElement(child,"height")
                group2.text = str(img_hight)
                group3  = ET.SubElement(child,"depth")
                group3.text = ("3.0")
                tree = ET.ElementTree(root_node)
                writer_counter=writer_counter+1
            
        tree.write(read_xml)
    except:
        print(xmls_name + "Not found")
print(writer_counter)