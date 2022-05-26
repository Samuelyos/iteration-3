from Model.lecture_class import lecture
from lectureWriter import lectureWriter
from lectureReader import lectureReader
from Model.sqlconn_class import SQLconn




def main():

    dbxml = SQLconn()
    dbxml.mycursor.execute("SELECT * FROM lectures")
    dblecture = dbxml.mycursor.fetchall()
    objectlist = []
    for item in dblecture:
        objectlist.append(lecture(str(item[0]), item[1], item[2], str(item[3]), item[4], item[5], str(item[6])))


    objectlist[0].printout()
    print("Building the XML of the Dispensary")
    LW = lectureWriter(objectlist[0])
    print("Saving the XML of the Dispensary")
    LW.save()

    print("Erasing dispensary and retrieveing contents from the XML file")
    objectlist[0].erase()
    LR = lectureReader()
    objectlist[0].update(LR.getlecture_class())
    # print("Printing the new contents of the pharmacy")
    # pharmacy.printout()



if __name__ == '__main__':
    main()
