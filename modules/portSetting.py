import xml.etree.ElementTree as ET

def setSlot(slotPath, selServ):
    tree = ET.parse(slotPath+'/settings.xml')
    root_node = tree.getroot()
    p1 = [0,5545,5546,5547,5548]
    p2 = [0,5549,5550,5551,5552]
    port1 = str(p1[selServ])
    port2 = str(p2[selServ])
    for elem in root_node.iter('ServerParamaters'):
        elem.set('HttPort', port1)
        elem.set('HttpsPort', port2)
    tree.write(slotPath+'/settings.xml')


#reserve to take tagged data from xml
#for tag in root_node.findall('ServerParamaters'):
    #httpPort  = tag.get('HttPort')
    #httpsPort = tag.get('HttpsPort')