from xml.etree import ElementTree

tree = ElementTree.parse('demo.xml').getroot()
parent_map = {c: p for p in tree.iter() for c in p}

item = tree.find('pc').find('pc_item')
print(parent_map[item].tag)


def remove_all_by_tag(root, tag):
    if root.tag == tag:
        root.clear()
        return
    for subitem in root.findall(tag):
        remove_all_by_tag(subitem, tag)


