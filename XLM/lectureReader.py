import os
from xml.etree import ElementTree
from Model.lecture_class import lecture


class lectureReader:
    __file_name__ = 'lecture_class2.xml'

    def __init__(self) -> None:
        full_file = os.path.abspath(os.path.join('data', self.__file_name__))
        dom = ElementTree.parse(full_file)

        root = dom.getroot()
        self.__courseID__ = root.attrib['courseID']
        self.__course__ = root.attrib['course']
        self.__room__ = root.attrib['room']
        self.__date__ = root.attrib['date']
        self.__time_from__ = root.attrib['time_from']
        self.__time_until__ = root.attrib['time_until']
        self.__zoom__ = root.attrib['zoom']
        course = {}
        availiable = {}

        print("New lecture_class in ", course)
        for course in root.iter("room"):
            room_name = course.attrib['course']
            print("class was avalible", room_name)
            room_course = course.attrib['course']
            availiable[room_name] = room_course
            course = [room_name] = "complete me"
        self.__lecture__ = lecture(self.__courseID__, self.__course__, self.__room__, self.__date__, self.__time_from__,
                                   self.__time_until__, self.__zoom__)

    def getlecture_class(self) -> lecture:
        return self.__lecture__
