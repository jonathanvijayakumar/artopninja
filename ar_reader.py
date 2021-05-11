from autosarfactorymain import autosarfactory
import json

"""
Author: Jonathan Vijayakumar
Summary: This project communicates with `autosarfactorymain` to read and parse ARXML and populate data!
Date: 11-05-2021

This class receives file names from the server and opens the appropriate file on the disk. 
Then the parsed ARXML from autosarfactorymain is processed and results are sent back to the python server from here. 
"""


class ArReader:

    """Singleton constructio"""
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

        """
        Loops through autosar data and populates a list of : delimited 
        strings denoting AUTOSAR elements in a tree fashion
        """

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

    # Singleton instance
    instance = None

    def __init__(self):
        if not ArReader.instance:
            ArReader.instance = ArReader.__ArReader()


# For testing purpose
# ArReader().instance.open(
#     r"C:\Personal Files\Jonathan\Work\AUTOSAR\thesis\artopninja\autosarfactorymain\Examples\generated\CanNetwork.arxml")
# print(ArReader().instance.getElements())
