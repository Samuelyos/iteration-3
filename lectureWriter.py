from xml.etree.ElementTree import ElementTree, tostring
import xml.etree.cElementTree as ET
from xml.dom import minidom

from Model.lecture_class import lecture


class lectureWriter:
    def __init__(self, l: lecture) -> None:
        print("Writing root nodes")
        self.__root__ = ET.ElementTree("lecture_class")
        self.__root__.set("courseID", l.getcourseID())
        self.__root__.set("course", l.getcourse())
        self.__root__.set("date", l.getdate())
        self.__root__.set("time_from", l.gettime_from())
        self.__root__.set("time_until", l.gettime_until())
        self.__root__.set("zoom", l.getzoom())
        self.__available__ = ET.SubElement(self.__root__, "Available")
        for course in l.getAvailable():
            ET.SubElement(self.__available__, "course", {'name': course, 'room': str(l.getAvailable()[course])})
            print(tostring(self.__root__))

    def save(self) -> None:
        tree = ET.ElementTree(self.__root__)
        print(tree)
        tree.write("lecture_class.xml")


def prettify(elem):
    """retunerer en pretty-printed XML string"""
    elem.getroot()
    rough_string = tostring(elem, 'utf-8')
    reparesed = minidom.parseString(rough_string)
    return reparesed.topprettyxml(indent="  ")
