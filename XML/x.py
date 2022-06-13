from Model.lecture_class import lecture
from XML.lectureWriter import lectureWriter
from XML.lectureReader import lectureReader
from Model.sqlconn_class import SQLconn

def main():

    dbxml = SQLconn()
    dbxml.mycursor.execute("SELECT * FROM lectures")
    dblecture = dbxml.mycursor.fetchall()
    objectlist = []
    for item in dblecture:
        objectlist.append(lecture(str(item[0]), item[1], item[2], str(item[3]), item[4], item[5], str(item[6])))


    objectlist[0].printout()
    LW = lectureWriter(objectlist[0])
    LW.save()
        #object.erase()


    inter = lectureReader().getlecture_class()
    print(inter)
    # print("Printing the new contents of the pharmacy")
    # pharmacy.printout()



if __name__ == '__main__':
    main()
