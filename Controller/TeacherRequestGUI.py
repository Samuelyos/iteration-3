from PyQt6 import QtWidgets, uic
from Model.lecture_class import lecture
from Model.sqlconn_class import SQLconn
from XLM.lectureWriter import lectureWriter
from XLM.lectureReader import lectureReader

# Loop der tager alle rækker i databasen over lektioner, og putter dem ind på en liste

class TeacherRequestGUI(QtWidgets.QDialog):
    """Klasse for selve ændring af lektioner GUI"""

    def __init__(self):  #
        super(TeacherRequestGUI, self).__init__()
        uic.loadUi('../View/Underviser_functionalGUI.ui', self)

        # Forbinder knapperne med funktioner i python
        self.buttonBox.clicked.connect(self.ok_button_pressed)
        self.pushButton.clicked.connect(self.push_button_pressed)
        self.addPush.clicked.connect(self.addPush_pressed)
        self.importXLM.clicked.connect(self.push_importXLM)
        self.writeXLM.clicked.connect(self.push_writeXLM)

        self.db = SQLconn()
        self.db.mycursor.execute("SELECT * FROM lectures")
        self.databaseLectures = self.db.mycursor.fetchall()
        self.lectureList = []
        for lec in range(len(self.databaseLectures)):
            self.lectureList.append(
                lecture(self.databaseLectures[lec][0], self.databaseLectures[lec][1], self.databaseLectures[lec][2], self.databaseLectures[lec][3], self.databaseLectures[lec][4], self.databaseLectures[lec][5]))

        # Kort loop der tilføjer et item i dropdown menuen, for hvert item i listen over lektioner
        for i in range(len(self.lectureList)):
            self.comboBox.addItem(self.lectureList[i].get_course())
        self.show()

    def push_button_pressed(self):

        # Når knappen "import" bliver trykket på, kaldes følgende linjer. Teksten i felterne bliver udskiftet med en lektion
        chosenLecture = self.comboBox.currentText()

        # chosenLect er en midlertidig variabel, der statisk opdaterer variablen oldLecture, afhængigt af hvad du vælger i
        # dropdown-menuen ved siden af import
        originalLecture = None
        for i in range(len(self.lectureList)):
            if chosenLecture == self.lectureList[i].get_course():
                originalLecture = self.lectureList[i]

        # Når man trykker på import bliver diverse labels udfyldt automatisk
        self.roomLabelOld.setText(f'{originalLecture.get_room()}')
        self.label.setText(f'{originalLecture.get_course()}')
        self.courseID_label.setText(f'{originalLecture.get_courseID()}')
        self.timeLabelS.setText(f'{originalLecture.get_time_from()}, {originalLecture.get_date()}')
        self.timeLabelE.setText(f'{originalLecture.get_time_until()}')
        self.roomLineEdit.setText(f'{originalLecture.get_room()}')

    def ok_button_pressed(self):
        """Ok knappen som lukker selve GUI"""
        self.db.mycursor.execute("DELETE from lectures where courseID = 200;")
        self.db.mydb.commit()
        print(self.db.mycursor.rowcount, "imports removed.")
        self.close()

    def addPush_pressed(self):
        """ Læser ændringerne fortaget i GUI, og opdatere admincheck i databasen med ændringerne efter OK"""

        # Læser indhold på labels og gemmer dem som variable
        courseLabel = self.label.text()
        courseIDLabel = self.courseID_label.text()
        dateWidgetLabel = self.calender.selectedDate().toString('yyyy-MM-dd')
        timeStartLabel = self.S2TimeEdit.dateTime().toString('hh:mm')
        timeEndLabel = self.E2TimeEdit.time().toString('hh:mm')
        roomLabel = self.roomLineEdit.text()

        # Hvis der ikke er nogle lektion, returneres dette i terminalen
        if courseLabel == "No Lecture imported":
            print('No Lecture was imported, please import and try again')

        # Hvis der er en lektion importeret, bliver denne tilføjet til admincheck tabellen i databasen
        else:
            insertStatement = f"INSERT INTO admincheck (courseID, course, room, `date`, timefrom, timeuntil) VALUES ('{courseIDLabel}','{courseLabel}', '{roomLabel}', '{dateWidgetLabel}',\
                    '{timeStartLabel}', '{timeEndLabel}')"
            self.db.mycursor.execute(insertStatement)
            self.db.mydb.commit()
            print(self.db.mycursor.rowcount, "record inserted.")

    def push_writeXLM(self):

        # Når knappen "import" bliver trykket på, kaldes følgende linjer. Teksten i felterne bliver udskiftet med en lektion
        chosenLecture = self.comboBox.currentText()

        # chosenLect er en midlertidig variabel, der statisk opdaterer variablen oldLecture, afhængigt af hvad du vælger i
        # dropdown-menuen ved siden af import
        exportLecture = None
        for i in range(len(self.lectureList)):
            if chosenLecture == self.lectureList[i].get_course():
                exportLecture = self.lectureList[i]

        # XLM kan kun tage strings som argumenter, derfor skal de attributter der ikke er strings først konverteres
        exportLecture.set_courseID(str(exportLecture.get_courseID()))
        exportLecture.set_date(str(exportLecture.get_date()))
        exportLecture.set_zoom(str(exportLecture.get_zoom()))

        LW = lectureWriter(exportLecture)
        LW.save()
        print('lecturedata.xml is updated with the chosen lecture!')


    def push_importXLM(self):

        importLecture = lectureReader().getlecture_class()
        insertStatement = f"INSERT INTO lectures (courseID, course, room, `date`, timefrom, timeuntil) VALUES ('{importLecture.get_courseID()}','{importLecture.get_course()}', '{importLecture.get_room()}', '{importLecture.get_date()}','{importLecture.get_time_from()}', '{importLecture.get_time_until()}')"
        self.db.mycursor.execute(insertStatement)
        self.db.mydb.commit()
        print(self.db.mycursor.rowcount, "record inserted.")
        self.close()

        self.db.mycursor.execute("SELECT * FROM lectures")
        self.databaseLectures = self.db.mycursor.fetchall()
        self.lectureList = []
        for lec in range(len(self.databaseLectures)):
            self.lectureList.append(
                lecture(self.databaseLectures[lec][0], self.databaseLectures[lec][1], self.databaseLectures[lec][2],
                        self.databaseLectures[lec][3], self.databaseLectures[lec][4], self.databaseLectures[lec][5]))

        self.comboBox.clear()
        # Kort loop der tilføjer et item i dropdown menuen, for hvert item i listen over lektioner
        for i in range(len(self.lectureList)):
            self.comboBox.addItem(self.lectureList[i].get_course())

        self.show()

        # Kort loop der tilføjer et item i dropdown menuen, for hvert item i listen over lektioner

