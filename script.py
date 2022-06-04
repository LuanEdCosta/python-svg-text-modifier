from sys import argv
from time import time
from os import makedirs, path
from xml.dom.minidom import parse

try:
    file_path = argv[1] if len(argv) > 1 else input("SVG File Path: ")

    dom = parse(file_path)
    root = dom.documentElement
    texts = root.getElementsByTagName("text")

    if len(texts) == 0:
        print("\nNo text element was found. Aborting...")
        exit(0)

    for text in texts:
        layer_id = text.getAttribute("id")
        new_value = input("Type The Text For ({0}): ".format(layer_id))
        text_node = text.firstChild.childNodes[0]
        if text_node:
            text_node.nodeValue = new_value

    output_dir = "output"
    if not path.exists(output_dir):
        makedirs(output_dir)

    new_file_name = "svg_{0}.svg".format(int(time()))
    new_file_path = "{0}/{1}".format(output_dir, new_file_name)

    with open(new_file_path, "w") as file:
        file.write(dom.toxml())

    print("SVG File Created: {0}".format(new_file_path))
except KeyboardInterrupt:
    print("\nScript Cancelled")
except:
    print("\nFailed to Modify SVG")
