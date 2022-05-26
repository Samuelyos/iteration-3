from logging import root
import os
from xml.etree import ElementTree
from Model.lecture_class import lecture


class lectureReader:
    __file_name__ = 'lecture_class2.xml'

    def __init__(self):
        full_file = os.path.abspath(os.path.join('data', self.__file_name__))
        print(str(full_file))
        dom = ElementTree.parse(full_file)

        root = dom.getroot()
        courseID = root.attrib['courseID']
        course = root.attrib['course']
        room = root.attrib['room']
        date = root.attrib['date']
        time_from = root.attrib['time_from']
        time_until = root.attrib['time_until']
        zoom = root.attrib['zoom']

        print("New lecture in", course)

        self.__lecture__ = lecture(courseID, course, room, date, time_from, time_until, zoom)

    def getlecture_class(self) -> lecture:
        return self.__lecture__
