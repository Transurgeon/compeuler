from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter
from typing import List

def createLeaf(name: str):
    return Node(name)

def createSubtree(name: str, child: List[Node]):
    return Node(name, children=child)

def printTree(root):
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))
        
def exportGraph(root, filename):
    UniqueDotExporter(root).to_picture(filename)
    for line in UniqueDotExporter(root):
        print(line)
    
example = createSubtree("root", [Node("sub0B", bar=109, foo=4),
        Node("sub0A", children=None),Node("sub0B", bar=109, foo=4),
        Node("cedric", children=None),])
printTree(example)

exportGraph(example, "example.png")

