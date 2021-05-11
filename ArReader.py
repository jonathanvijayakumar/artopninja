from autosarfactorymain import autosarfactory
import json

'''
AUTOSAR ARXML reader class
'''


class ArReader:

    class __ArReader:
        def open(self, file):
            self.root, self.status = autosarfactory.autosarfactory.read([file])

        def save(self):
            autosarfactory.save()

        def getElements(self):
            elements = {}
            for pkg in self.root.get_arPackages():
                self.recursiveFind(pkg, elements)

            return elements

        def recursiveFind(self, root, elements):

            elements['parent'] = root.get_shortName() + ':' + \
                root.tag + ':' + root.path

            children = []
            for child in root.get_elements():
                children.append(child.get_shortName() + ':' +
                                child.tag + ':' + child.path)

            elements['children'] = children

            for pkg in root.get_arPackages():
                chil_dict = {}
                elements['children'].append(chil_dict)
                self.recursiveFind(pkg, chil_dict)

    instance = None

    def __init__(self):
        if not ArReader.instance:
            ArReader.instance = ArReader.__ArReader()


# ArReader().instance.open(
#     r"C:\Personal Files\Jonathan\Work\AUTOSAR\thesis\artopninja\autosarfactorymain\Examples\generated\CanNetwork.arxml")
# print(ArReader().instance.getElements())
