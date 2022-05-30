from xml.etree.ElementTree import tostring
import xml.etree.cElementTree as ET
from xml.dom import minidom

from Model.lecture_class import lecture


class lectureWriter:
    def __init__(self, l: lecture) -> None:

        self.__root__ = ET.Element("lecture_class")
        self.__root__.set("courseID", l.get_courseID())
        self.__root__.set("course", l.get_course())
        self.__root__.set("room", l.get_room())
        self.__root__.set("date", l.get_date())
        self.__root__.set("time_from", l.get_time_from())
        self.__root__.set("time_until", l.get_time_until())
        self.__root__.set("zoom", l.get_zoom())

    def save(self) -> None:
        tree = ET.ElementTree(self.__root__)
        tree.write("../XML/lecturedata.xml")


def prettify(elem):
    """retunerer en pretty-printed XML string"""
    elem.getroot()
    rough_string = tostring(elem, 'utf-8')
    reparesed = minidom.parseString(rough_string)
    return reparesed.topprettyxml(indent="  ")
