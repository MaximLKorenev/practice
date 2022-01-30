import xml.etree.ElementTree as ETree

xml1 = ETree.parse('demo.xml')
root = xml1.getroot()


def walk_tree_recursive(root):
    ats = root.attrib.keys()
    print(root.tag.title())
    for k in ats:
        print(k, " : ", root.attrib[k])
    for child in root:
        walk_tree_recursive(child)


def tree_count_recursive(root, key):
    n = 0
    if key in root.attrib.keys():
        n = 1
    for child in root:
        n += tree_count_recursive(child, key)
    return n


def remove_all_by_tag(root, tag):
    if root.tag == tag:
        root.clear()
        return
    for subitem in root.findall(tag):
        remove_all_by_tag(subitem, tag)


def find_parent(root):
    


