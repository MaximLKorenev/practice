import xml.etree.ElementTree as ETree

xml1 = ETree.parse('demo.xml')
root = xml1.getroot()


def remove_all_by_tag(root, tag):
    if root.tag == tag:
        root.clear()
        return
    for subitem in root.findall(tag):
        remove_all_by_tag(subitem, tag)


def find_parent(root):