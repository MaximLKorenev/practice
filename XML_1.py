import xml.etree.ElementTree as ETree

xml1 = ETree.parse('demo.xml')
root = xml1.getroot()
count = 0


def walk_xml(root):
    global count
    for i in range(len(root)):
        print(root[i].tag, root[i].attrib, root[i].text)
        if "name" in root[i].attrib.keys():
            count += 1
        if len(root[i]) > 1:
            walk_xml(root[i])
    return count


print(walk_xml(root))