from xml.etree import ElementTree

tree = ElementTree.parse('demo.xml').getroot()
parent_map = {c: p for p in tree.iter() for c in p}

item = tree.find('pc').find('pc_item')
print(parent_map[item].tag)


def remove_nodes_recursive(root, remove_tag):
    remove_list = []
    for child in root:
        if child.tag == remove_tag:
           remove_list.append(child)

    for child in remove_list:
        root.remove(child)

    for child in root:
        remove_nodes_recursive(child, remove_tag)
