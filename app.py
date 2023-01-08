from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
import sqlite3

class App(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("Δισκογραφική Εταιρεία")

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {}

        for F in (MainMenu, AddStartPage, showArtist,showSoloArtist, showBand, showBandMember, showSong, showAgent, showContract, showAlbum, showStudio,
        showWriter, showPartnership, artistResults, bandMemberResults, bandResults, songResults,agentResults,contractResults, albumResults, studioResults,
        writerResults, partnershipResults, DeleteStartPage, deleteArtist, deleteSoloArtist, deleteBand, deleteBandMember, deleteSong, deleteAgent,
        deleteContract, deleteAlbum, deleteStudio,deleteWriter, deletePartnership,deleteSoloArtistResults, deleteBandResults, deleteSongResults,
        deleteBandMemberResults, deleteAgentResults, deleteContractResults,deleteAlbumResults, deleteStudioResults, deleteWriterResults, deletePartnershipResults):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class MainMenu(tk.Frame):
   def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = "Βάσεις Δεδομένων - Project\n",
                           font = 'Arial 25').grid(row=0, column=0)

        tk.Label(self, text ="Μέλη Ομάδας:\nΣτούρα Θεοδώρα\n Τσαναή Σμαράγδα",
                   font = 'Arial 15',
                   bg ='grey').grid(row=0, column=2)
        tk.Label(self, text ="Ομάδα 35: Δισκογραφική Εταιρεία\n",
                   font = 'Arial 20 ').grid(row=2, column=0, padx = 5)

        tk.Label(self, text ="Επιλέξτε ποια λειτουργία θα θέλατε να εκτελέσετε\n",
                   font = 'Arial 15').grid(row=3, column=0, padx = 5)

        buttonadd = ttk.Button(self, text ="Add Data",
        command = lambda : controller.show_frame(AddStartPage))

        buttonadd.grid(row = 4, column = 0,ipady=10, ipadx=100, padx = 20, pady = 10)
        buttondelete = ttk.Button(self, text ="Delete Data",
        command = lambda : controller.show_frame(DeleteStartPage))

        buttondelete.grid(row = 5, column = 0, ipady=10, ipadx=100,padx = 20, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command= exit).grid(row = 5, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)

class AddStartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = "Βάσεις Δεδομένων - Project\n",
                           font = 'Arial 25').grid(row=0, column=0)

        tk.Label(self, text ="Μέλη Ομάδας:\nΣτούρα Θεοδώρα\n Τσαναή Σμαράγδα",
                   font = 'Arial 15',
                   bg ='grey').grid(row=0, column=2)
        tk.Label(self, text ="Ομάδα 35: Δισκογραφική Εταιρεία\n",
                   font = 'Arial 20 ').grid(row=2, column=0, padx = 5)

        tk.Label(self, text ="Επιλέξτε σε ποια κατηγορία \nθέλετε να εισάγετε νέα δεδομένα\n",
                   font = 'Arial 15').grid(row=3, column=0, padx = 5)

        buttonArtist = ttk.Button(self, text ="Artist",
        command = lambda : controller.show_frame(showArtist))
        buttonArtist.grid(row = 4, column = 0, ipady=10, ipadx=20,padx = 10, pady = 10)

        buttonAgent = ttk.Button(self, text ="Αgent",
        command = lambda : controller.show_frame(showAgent))
        buttonAgent.grid(row = 5, column = 0, ipady=10, ipadx=20, padx = 10, pady = 10)

        buttonContract = ttk.Button(self, text ="Contract",
        command = lambda : controller.show_frame(showContract))
        buttonContract.grid(row = 6, column = 0, ipady=10, ipadx=20, padx = 10, pady = 10)

        buttonSong = ttk.Button(self, text = "Song",
        command = lambda: controller.show_frame(showSong))
        buttonSong.grid(row = 7, column = 0, ipady=10, ipadx=20, padx = 10, pady = 10)

        buttonAlbum = ttk.Button(self, text ="Album",
        command = lambda : controller.show_frame(showAlbum))
        buttonAlbum.grid(row = 4, column = 1, ipady=10, ipadx=20, padx = 10, pady = 10)

        buttonStudio = ttk.Button(self, text ="Studio",
        command = lambda : controller.show_frame(showStudio))
        buttonStudio.grid(row = 5, column = 1, ipady=10, ipadx=20, padx = 10, pady = 10)

        buttonWriter = ttk.Button(self, text ="Writer",
        command = lambda : controller.show_frame(showWriter))
        buttonWriter.grid(row = 6, column = 1, ipady=10, ipadx=20, padx = 10, pady = 10)

        buttonPartnership = ttk.Button(self, text ="Partnership",
        command = lambda : controller.show_frame(showPartnership))
        buttonPartnership.grid(row = 7, column = 1, ipady=10, ipadx=20, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 9, column = 1, ipady=10, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command= exit).grid(row = 9, column = 2, ipady=10, ipadx=15, padx = 10, pady = 10)

class showArtist(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please select the type of artist you desire\n to load additional data""",font = 'Arial 18').grid(row = 4, column = 0, padx = 5)

        buttonSoloArtist = ttk.Button(self, text ="Solo Artist",
        command = lambda : controller.show_frame(showSoloArtist))
        buttonSoloArtist.grid(row = 5, column = 0,ipady=10, ipadx=50, padx = 10, pady = 10)

        buttonBand = ttk.Button(self, text ="Band",
        command = lambda : controller.show_frame(showBand))
        buttonBand.grid(row = 6, column = 0,ipady=10, ipadx=50, padx = 10, pady = 10)

        buttonBandMember = ttk.Button(self, text ="Band Member",
        command = lambda : controller.show_frame(showBandMember))
        buttonBandMember.grid(row = 7, column = 0,ipady=10, ipadx=50, padx = 10, pady = 10)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(AddStartPage))
        buttonAddStartPage.grid(row = 8, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 5, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = ttk.Button(self, text="Exit",command = exit).grid(row = 8, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

class showSoloArtist(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the following \nartist's information:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)


        tk.Label(self, text ="Artist_ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        value0 = tk.Entry(self, width = 20)
        value0.grid(row=1, column=1, padx=5)

        tk.Label(self, text ="First Name:",font = 'Arial 15').grid(row=2, column=0, padx = 5)
        value1 = tk.Entry(self, width = 20)
        value1.grid(row=2, column=1, padx=5)

        tk.Label(self, text ="Middle Name:",font = 'Arial 15').grid(row=3, column=0, padx = 5)
        value2 = tk.Entry(self, width = 20)
        value2.grid(row=3, column=1, padx=5)

        tk.Label(self, text ="Last Name:",font = 'Arial 15').grid(row=4, column=0, padx = 5)
        value3 = tk.Entry(self, width = 20)
        value3.grid(row=4, column=1, padx=5)

        tk.Label(self, text ="SSN:",font = 'Arial 15').grid(row=5, column=0, padx = 5)
        value4 = tk.Entry(self, width = 20)
        value4.grid(row=5, column=1, padx=5)

        tk.Label(self, text ="Phone:",font = 'Arial 15').grid(row=6, column=0, padx = 5)
        value5 = tk.Entry(self, width = 20)
        value5.grid(row=6, column=1, padx=5)

        tk.Label(self, text ="Address:",font = 'Arial 15').grid(row=7, column=0, padx = 5)
        value6 = tk.Entry(self, width = 20)
        value6.grid(row=7, column=1, padx=5)

        tk.Label(self, text ="City:",font = 'Arial 15').grid(row=8, column=0, padx = 5)
        value7 = tk.Entry(self, width = 20)
        value7.grid(row=8, column=1, padx=5)

        tk.Label(self, text ="Area:",font = 'Arial 15').grid(row=9, column=0, padx = 5)
        value8 = tk.Entry(self, width = 20)
        value8.grid(row=9, column=1, padx=5)

        tk.Label(self, text ="ZIP:",font = 'Arial 15').grid(row=10, column=0, padx = 5)
        value9 = tk.Entry(self, width = 20)
        value9.grid(row=10, column=1, padx=5)

        tk.Label(self, text ="Birthdate:",font = 'Arial 15').grid(row=11, column=0, padx = 5)
        value10 = tk.Entry(self, width = 20)
        value10.grid(row=11, column=1, padx=5)

        tk.Label(self, text ="Passing Date:",font = 'Arial 15').grid(row=12, column=0, padx = 5)
        value11 = tk.Entry(self, width = 20)
        value11.grid(row=12, column=1, padx=5)

        tk.Label(self, text ="Sex:",font = 'Arial 15').grid(row=13, column=0, padx = 5)
        value12 = tk.Entry(self, width = 20)
        value12.grid(row=13, column=1, padx=5)


        tk.Label(self, text ="Artist 'Stage' Name:",font = 'Arial 15').grid(row=14, column=0, padx = 5)
        value13 = tk.Entry(self, width = 20)
        value13.grid(row=14, column=1, padx=10)

        tk.Label(self, text ="Artist genre:",font = 'Arial 15').grid(row=15, column=0, padx = 5)
        value14 = tk.Entry(self, width = 20)
        value14.grid(row=15, column=1, padx=10)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(AddStartPage))

        buttonAddStartPage.grid(row = 16, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 17, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: SoloArtistSubmit(value0.get(), value1.get(), value2.get(), value3.get(), value4.get(), value5.get(),
                    value6.get(),value7.get(), value8.get(), value9.get(), value10.get(), value11.get(), value12.get(),value13.get(),value14.get()))

        buttonSubmit.grid(row = 16, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = ttk.Button(self, text="Exit",command = exit).grid(row = 16, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

def SoloArtistSubmit(artistID, fname, mname, lname, SSN, phone, address, city, area, zip, bday, passingdate, sex, name, genre):

    conn = sqlite3.connect('Diskographiki.db')

    conn.execute("""insert into artist values(?,?,?);""",
            (artistID, name, genre))

    conn.execute("""insert into solo_artist values(?,?,?,?,?,?,?,?,?,?,?,?,?);""",
            (artistID, fname, mname, lname, SSN, phone, address, city, area, zip, bday, passingdate, sex))

    conn.commit()
    conn.close()
    app.show_frame(artistResults)

class artistResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The artist has been added on our database\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(AddStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)

class showBand(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the following \nband's information:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)
        tk.Label(self, text ="Band ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        value0 = tk.Entry(self, width = 20)
        value0.grid(row=1, column=1, padx=5)

        tk.Label(self, text ="Band name:",font = 'Arial 15').grid(row=2, column=0, padx = 5)
        value1 = tk.Entry(self, width = 20)
        value1.grid(row=2, column=1, padx=5)

        tk.Label(self, text ="Formation Date:",font = 'Arial 15').grid(row=3, column=0, padx = 5)
        value2 = tk.Entry(self, width = 20)
        value2.grid(row=3, column=1, padx=5)

        tk.Label(self, text ="Artist genre:",font = 'Arial 15').grid(row=4, column=0, padx = 5)
        value3 = tk.Entry(self, width = 40)
        value3.grid(row=4, column=1, padx=10)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(AddStartPage))
        buttonAddStartPage.grid(row = 5, column = 0, ipady=5, ipadx=15,padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 6, column = 0, ipady=5, ipadx=15,padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: bandSubmit(value0.get(), value1.get(), value2.get(),value3.get()))
        buttonSubmit.grid(row = 5, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 5, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

def bandSubmit(artistID, bandName, formationDate,genre):

    conn = sqlite3.connect('Diskographiki.db')
    conn.execute("""insert into artist values(?,?,?);""",
            (artistID, genre, bandName))

    conn.execute("""insert into band values(?,?,?);""",
            (artistID, bandName, formationDate))

    conn.commit()
    conn.close()
    app.show_frame(bandResults)

class bandResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The band has been added on our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)
        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(AddStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15,padx = 10, pady = 10)

class showBandMember(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the following \nband's member information:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)

        tk.Label(self, text ="Artist_ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        value0 = tk.Entry(self, width = 20)
        value0.grid(row=1, column=1, padx=5)

        tk.Label(self, text ="First Name:",font = 'Arial 15').grid(row=2, column=0, padx = 5)
        value1 = tk.Entry(self, width = 20)
        value1.grid(row=2, column=1, padx=5)

        tk.Label(self, text ="Middle Name:",font = 'Arial 15').grid(row=3, column=0, padx = 5)
        value2 = tk.Entry(self, width = 20)
        value2.grid(row=3, column=1, padx=5)

        tk.Label(self, text ="Last Name:",font = 'Arial 15').grid(row=4, column=0, padx = 5)
        value3 = tk.Entry(self, width = 20)
        value3.grid(row=4, column=1, padx=5)

        tk.Label(self, text ="SSN:",font = 'Arial 15').grid(row=5, column=0, padx = 5)
        value4 = tk.Entry(self, width = 20)
        value4.grid(row=5, column=1, padx=5)

        tk.Label(self, text ="Phone:",font = 'Arial 15').grid(row=6, column=0, padx = 5)
        value5 = tk.Entry(self, width = 20)
        value5.grid(row=6, column=1, padx=5)

        tk.Label(self, text ="Address:",font = 'Arial 15').grid(row=7, column=0, padx = 5)
        value6 = tk.Entry(self, width = 20)
        value6.grid(row=7, column=1, padx=5)

        tk.Label(self, text ="City:",font = 'Arial 15').grid(row=8, column=0, padx = 5)
        value7 = tk.Entry(self, width = 20)
        value7.grid(row=8, column=1, padx=5)

        tk.Label(self, text ="Area:",font = 'Arial 15').grid(row=9, column=0, padx = 5)
        value8 = tk.Entry(self, width = 20)
        value8.grid(row=9, column=1, padx=5)

        tk.Label(self, text ="ZIP:",font = 'Arial 15').grid(row=10, column=0, padx = 5)
        value9 = tk.Entry(self, width = 20)
        value9.grid(row=10, column=1, padx=5)

        tk.Label(self, text ="Birthdate:",font = 'Arial 15').grid(row=11, column=0, padx = 5)
        value10 = tk.Entry(self, width = 20)
        value10.grid(row=11, column=1, padx=5)

        tk.Label(self, text ="Passing Date:",font = 'Arial 15').grid(row=12, column=0, padx = 5)
        value11 = tk.Entry(self, width = 20)
        value11.grid(row=12, column=1, padx=5)

        tk.Label(self, text ="Sex:",font = 'Arial 15').grid(row=13, column=0, padx = 5)
        value12 = tk.Entry(self, width = 20)
        value12.grid(row=13, column=1, padx=5)

        tk.Label(self, text ="Band ID:",font = 'Arial 15').grid(row=17, column=0, padx = 5)
        value13 = tk.Entry(self, width = 20)
        value13.grid(row=17, column=1, padx=5)

        tk.Label(self, text ="Join Date:",font = 'Arial 15').grid(row=19, column=0, padx = 5)
        value14 = tk.Entry(self, width = 20)
        value14.grid(row=19, column=1, padx=5)

        tk.Label(self, text ="Leave Date:",font = 'Arial 15').grid(row=20, column=0, padx = 5)
        value15 = tk.Entry(self, width = 20)
        value15.grid(row=20, column=1, padx=5)

        tk.Label(self, text ="Role:",font = 'Arial 15').grid(row=21, column=0, padx = 5)
        value16 = tk.Entry(self, width = 20)
        value16.grid(row=21, column=1, padx=5)

        tk.Label(self, text ="Artist 'Stage' Name:",font = 'Arial 15').grid(row=1, column=2, padx = 0)
        value17 = tk.Entry(self, width = 20)
        value17.grid(row=1, column=3, padx=10)

        tk.Label(self, text ="Artist genre:",font = 'Arial 15').grid(row=2, column=2, padx = 0)
        value18 = tk.Entry(self, width = 20)
        value18.grid(row=2, column=3, padx=10)


        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(AddStartPage))

        buttonAddStartPage.grid(row = 23, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 24, column = 0, ipady=5, ipadx=15,padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: bandMemberSubmit(value0.get(), value1.get(), value2.get(), value3.get(), value4.get(), value5.get(),
                    value6.get(),value7.get(), value8.get(), value9.get(), value10.get(), value11.get(), value12.get(),value13.get(),value14.get(),value15.get(),
                    value16.get(),value17.get(),value18.get()))

        buttonSubmit.grid(row = 23, column = 2, ipady=5, ipadx=15,padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 23, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

def bandMemberSubmit(artistID, fname, mname, lname, SSN, phone, address, city, area, zip, bday, passingdate, sex, bandID, join_date, leave_date, role, name, genre):

    conn = sqlite3.connect('Diskographiki.db')

    conn.execute("""insert into artist values(?,?,?);""",
            (artistID, name, genre))

    conn.execute("""insert into solo_artist values(?,?,?,?,?,?,?,?,?,?,?,?,?);""",
            (artistID, fname, mname, lname, SSN, phone, address, city, area, zip, bday, passingdate, sex))

    conn.execute("""insert into belongs_to values(?,?,?,?,?);""",
            (bandID, artistID, join_date, leave_date, role))

    conn.commit()
    conn.close()
    app.show_frame(bandMemberResults)

class bandMemberResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The band's member has been added on our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)
        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(AddStartPage))

        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 2, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)

class showSong(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the following \nsong's information:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)

        tk.Label(self, text ="Song ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        value0 = tk.Entry(self, width = 20)
        value0.grid(row=1, column=1, padx=5)

        tk.Label(self, text ="Writer ID:",font = 'Arial 15').grid(row=2, column=0, padx = 5)
        value1 = tk.Entry(self, width = 20)
        value1.grid(row=2, column=1, padx=5)

        tk.Label(self, text ="Name:",font = 'Arial 15').grid(row=3, column=0, padx = 5)
        value2 = tk.Entry(self, width = 20)
        value2.grid(row=3, column=1, padx=5)

        tk.Label(self, text ="Length:",font = 'Arial 15').grid(row=4, column=0, padx = 5)
        value3 = tk.Entry(self, width = 20)
        value3.grid(row=4, column=1, padx=5)

        tk.Label(self, text ="Genre:",font = 'Arial 15').grid(row=5, column=0, padx = 5)
        value4 = tk.Entry(self, width = 20)
        value4.grid(row=5, column=1, padx=5)

        tk.Label(self, text ="Composition Date:",font = 'Arial 15').grid(row=6, column=0, padx = 5)
        value5 = tk.Entry(self, width = 20)
        value5.grid(row=6, column=1, padx=5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(AddStartPage))
        buttonAddStartPage.grid(row = 6, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 7, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: songSubmit(value0.get(), value1.get(), value2.get(), value3.get(),value4.get(),value5.get()))
        buttonSubmit.grid(row = 6, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 6, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)


def songSubmit(songID, writerID, songName, length, genre, composition_date):

    conn = sqlite3.connect('Diskographiki.db')
    conn.execute("""insert into song values(?,?,?,?);""",
            (songID, songName, length, genre))

    conn.execute("""insert into composed values(?,?,?);""",
            (songID, writerID, composition_date))

    conn.commit()
    conn.close()
    app.show_frame(songResults)

class songResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The song has been added on our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)
        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(AddStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)

class showAgent(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the following \nagent's information:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)

        tk.Label(self, text ="Agent ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        value0 = tk.Entry(self, width = 20)
        value0.grid(row=1, column=1, padx=5)

        tk.Label(self, text ="First Name:",font = 'Arial 15').grid(row=2, column=0, padx = 5)
        value1 = tk.Entry(self, width = 20)
        value1.grid(row=2, column=1, padx=5)

        tk.Label(self, text ="Middle Name:",font = 'Arial 15').grid(row=3, column=0, padx = 5)
        value2 = tk.Entry(self, width = 20)
        value2.grid(row=3, column=1, padx=5)

        tk.Label(self, text ="Last Name:",font = 'Arial 15').grid(row=4, column=0, padx = 5)
        value3 = tk.Entry(self, width = 20)
        value3.grid(row=4, column=1, padx=5)

        tk.Label(self, text ="Partnership Type:",font = 'Arial 15').grid(row=5, column=0, padx = 5)
        value4 = tk.Entry(self, width = 20)
        value4.grid(row=5, column=1, padx=5)

        tk.Label(self, text ="SSN:",font = 'Arial 15').grid(row=6, column=0, padx = 5)
        value5 = tk.Entry(self, width = 20)
        value5.grid(row=6, column=1, padx=5)

        tk.Label(self, text ="Phone:",font = 'Arial 15').grid(row=7, column=0, padx = 5)
        value6 = tk.Entry(self, width = 20)
        value6.grid(row=7, column=1, padx=5)

        tk.Label(self, text ="Address:",font = 'Arial 15').grid(row=8, column=0, padx = 5)
        value7 = tk.Entry(self, width = 20)
        value7.grid(row=8, column=1, padx=5)

        tk.Label(self, text ="City:",font = 'Arial 15').grid(row=9, column=0, padx = 5)
        value8 = tk.Entry(self, width = 20)
        value8.grid(row=9, column=1, padx=5)

        tk.Label(self, text ="Area:",font = 'Arial 15').grid(row=10, column=0, padx = 5)
        value9 = tk.Entry(self, width = 20)
        value9.grid(row=10, column=1, padx=5)

        tk.Label(self, text ="ZIP:",font = 'Arial 15').grid(row=11, column=0, padx = 5)
        value10 = tk.Entry(self, width = 20)
        value10.grid(row=11, column=1, padx=5)

        tk.Label(self, text ="Birthdate:",font = 'Arial 15').grid(row=12, column=0, padx = 5)
        value11 = tk.Entry(self, width = 20)
        value11.grid(row=12, column=1, padx=5)

        tk.Label(self, text ="Passing Date:",font = 'Arial 15').grid(row=13, column=0, padx = 5)
        value12 = tk.Entry(self, width = 20)
        value12.grid(row=13, column=1, padx=5)

        tk.Label(self, text ="Sex:",font = 'Arial 15').grid(row=14, column=0, padx = 5)
        value13 = tk.Entry(self, width = 20)
        value13.grid(row=14, column=1, padx=5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(AddStartPage))
        buttonAddStartPage.grid(row = 15, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 16, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: agentSubmit(value0.get(), value1.get(), value2.get(), value3.get(), value4.get(), value5.get(),
                    value6.get(),value7.get(), value8.get(), value9.get(), value10.get(), value11.get(), value12.get(),value13.get()))
        buttonSubmit.grid(row = 15, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = ttk.Button(self, text="Exit",command = exit).grid(row = 16, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

def agentSubmit(agentID, fname, mname, lname, partnership_type, SSN, phone, address, city, area, zip, bday, passingdate, sex, artistID):

    conn = sqlite3.connect('Diskographiki.db')
    conn.execute("""insert into agent values(?,?,?,?,?,?,?,?,?,?,?,?,?,?);""",
            agentID, fname, mname, lname, partnership_type, SSN, phone, address, city, area, zip, bday, passingdate, sex)

    conn.commit()
    conn.close()
    app.show_frame(agentResults)

class agentResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The agent has been added on our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)
        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(AddStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)

class showContract(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the following \ncontract's information:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)

        tk.Label(self, text ="Contract ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        value0 = tk.Entry(self, width = 20)
        value0.grid(row=1, column=1, padx=5)

        tk.Label(self, text ="Artist ID:",font = 'Arial 15').grid(row=2, column=0, padx = 5)
        value1 = tk.Entry(self, width = 20)
        value1.grid(row=2, column=1, padx=5)

        tk.Label(self, text ="Start Date:",font = 'Arial 15').grid(row=3, column=0, padx = 5)
        value2 = tk.Entry(self, width = 20)
        value2.grid(row=3, column=1, padx=5)

        tk.Label(self, text ="End Date:",font = 'Arial 15').grid(row=4, column=0, padx = 5)
        value3 = tk.Entry(self, width = 20)
        value3.grid(row=4, column=1, padx=5)

        tk.Label(self, text ="Sign Date:",font = 'Arial 15').grid(row=5, column=0, padx = 5)
        value4 = tk.Entry(self, width = 20)
        value4.grid(row=5, column=1, padx=5)

        tk.Label(self, text ="Estimated End:",font = 'Arial 15').grid(row=6, column=0, padx = 5)
        value5 = tk.Entry(self, width = 20)
        value5.grid(row=6, column=1, padx=5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(AddStartPage))
        buttonAddStartPage.grid(row = 7, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 8, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: contractSubmit(value0.get(), value1.get(), value2.get(), value3.get(), value4.get(), value5.get()))
        buttonSubmit.grid(row = 7, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 7, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

def contractSubmit(contractID, artistID, start_date, end_date, sign_date, estimated_end):

    conn = sqlite3.connect('Diskographiki.db')
    conn.execute("""insert into conctract values(?,?,?,?,?,?);""",
            contractID, artistID, start_date, end_date, sign_date, estimated_end)

    conn.commit()
    conn.close()
    app.show_frame(contractResults)

class contractResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The contract has been added on our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)
        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(AddStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)

class showAlbum(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the following \nalbum's information:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)

        tk.Label(self, text ="Album ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        value0 = tk.Entry(self, width = 20)
        value0.grid(row=1, column=1, padx=5)

        tk.Label(self, text ="Name:",font = 'Arial 15').grid(row=2, column=0, padx = 5)
        value1 = tk.Entry(self, width = 20)
        value1.grid(row=2, column=1, padx=5)

        tk.Label(self, text ="Date Released:",font = 'Arial 15').grid(row=3, column=0, padx = 5)
        value2 = tk.Entry(self, width = 20)
        value2.grid(row=3, column=1, padx=5)

        tk.Label(self, text ="Unit Price:",font = 'Arial 15').grid(row=4, column=0, padx = 5)
        value3 = tk.Entry(self, width = 20)
        value3.grid(row=4, column=1, padx=5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(AddStartPage))
        buttonAddStartPage.grid(row = 5, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)


        buttonSubmit = ttk.Button(self, text = "Submit",
        command = lambda: albumSubmit(value0.get(), value1.get(), value2.get(), value3.get()))
        buttonSubmit.grid(row = 5, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 6, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 5, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

def albumSubmit(albumID, name, date_released, unit_price):

    conn = sqlite3.connect('Diskographiki.db')
    conn.execute("""insert into album values(?,?,?,?);""",
            albumID, name, date_released, unit_price)

    conn.commit()
    conn.close()
    app.show_frame(albumResults)

class albumResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The album has been added on our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)
        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(AddStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)

class showStudio(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the following \nstudio's information:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)

        tk.Label(self, text ="Studio ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        value0 = tk.Entry(self, width = 20)
        value0.grid(row=1, column=1, padx=5)

        tk.Label(self, text ="Studio Name:",font = 'Arial 15').grid(row=2, column=0, padx = 5)
        value1 = tk.Entry(self, width = 20)
        value1.grid(row=2, column=1, padx=5)

        tk.Label(self, text ="Phone:",font = 'Arial 15').grid(row=3, column=0, padx = 5)
        value2 = tk.Entry(self, width = 20)
        value2.grid(row=3, column=1, padx=5)

        tk.Label(self, text ="Street:",font = 'Arial 15').grid(row=4, column=0, padx = 5)
        value3 = tk.Entry(self, width = 20)
        value3.grid(row=4, column=1, padx=5)

        tk.Label(self, text ="City:",font = 'Arial 15').grid(row=5, column=0, padx = 5)
        value4 = tk.Entry(self, width = 20)
        value4.grid(row=5, column=1, padx=5)

        tk.Label(self, text ="Area:",font = 'Arial 15').grid(row=5, column=0, padx = 5)
        value5 = tk.Entry(self, width = 20)
        value5.grid(row=5, column=1, padx=5)

        tk.Label(self, text ="ZIP:",font = 'Arial 15').grid(row=6, column=0, padx = 5)
        value6 = tk.Entry(self, width = 20)
        value6.grid(row=6, column=1, padx=5)

        tk.Label(self, text ="Cost per hour:",font = 'Arial 15').grid(row=7, column=0, padx = 5)
        value7 = tk.Entry(self, width = 20)
        value7.grid(row=7, column=1, padx=5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(AddStartPage))
        buttonAddStartPage.grid(row = 8, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 9, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: agentSubmit(value0.get(), value1.get(), value2.get(), value3.get(), value4.get(), value5.get(),
                    value6.get(),value7.get()))
        buttonSubmit.grid(row = 8, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = ttk.Button(self, text="Exit",command = exit).grid(row = 8, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

def studioSubmit(studioID, studio_name, phone, street, city, area, zip, hrly_cost):

    conn = sqlite3.connect('Diskographiki.db')
    conn.execute("""insert into agent values(?,?,?,?,?,?,?,?);""",
            studioID, studio_name, phone, street, city, area, zip, hrly_cost)

    conn.commit()
    conn.close()
    app.show_frame(studioResults)

class studioResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The studio has been added on our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)
        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(AddStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)

class showWriter(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the following \nwriter's member information:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)

        tk.Label(self, text ="Writer ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        value0 = tk.Entry(self, width = 20)
        value0.grid(row=1, column=1, padx=5)

        tk.Label(self, text ="First Name:",font = 'Arial 15').grid(row=2, column=0, padx = 5)
        value1 = tk.Entry(self, width = 20)
        value1.grid(row=2, column=1, padx=5)

        tk.Label(self, text ="Middle Name:",font = 'Arial 15').grid(row=3, column=0, padx = 5)
        value2 = tk.Entry(self, width = 20)
        value2.grid(row=3, column=1, padx=5)

        tk.Label(self, text ="Last Name:",font = 'Arial 15').grid(row=4, column=0, padx = 5)
        value3 = tk.Entry(self, width = 20)
        value3.grid(row=4, column=1, padx=5)

        tk.Label(self, text ="SSN:",font = 'Arial 15').grid(row=5, column=0, padx = 5)
        value4 = tk.Entry(self, width = 20)
        value4.grid(row=5, column=1, padx=5)

        tk.Label(self, text ="Phone:",font = 'Arial 15').grid(row=6, column=0, padx = 5)
        value5 = tk.Entry(self, width = 20)
        value5.grid(row=6, column=1, padx=5)

        tk.Label(self, text ="Address:",font = 'Arial 15').grid(row=7, column=0, padx = 5)
        value6 = tk.Entry(self, width = 20)
        value6.grid(row=7, column=1, padx=5)

        tk.Label(self, text ="City:",font = 'Arial 15').grid(row=8, column=0, padx = 5)
        value7 = tk.Entry(self, width = 20)
        value7.grid(row=8, column=1, padx=5)

        tk.Label(self, text ="Area:",font = 'Arial 15').grid(row=9, column=0, padx = 5)
        value8 = tk.Entry(self, width = 20)
        value8.grid(row=9, column=1, padx=5)

        tk.Label(self, text ="ZIP:",font = 'Arial 15').grid(row=10, column=0, padx = 5)
        value9 = tk.Entry(self, width = 20)
        value9.grid(row=10, column=1, padx=5)

        tk.Label(self, text ="Birthdate:",font = 'Arial 15').grid(row=11, column=0, padx = 5)
        value10 = tk.Entry(self, width = 20)
        value10.grid(row=11, column=1, padx=5)

        tk.Label(self, text ="Passing Date:",font = 'Arial 15').grid(row=12, column=0, padx = 5)
        value11 = tk.Entry(self, width = 20)
        value11.grid(row=12, column=1, padx=5)

        tk.Label(self, text ="Sex:",font = 'Arial 15').grid(row=13, column=0, padx = 5)
        value12 = tk.Entry(self, width = 20)
        value12.grid(row=13, column=1, padx=5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(AddStartPage))

        buttonAddStartPage.grid(row = 14, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 15, column = 0, ipady=5, ipadx=15,padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: artistSubmit(value0.get(), value1.get(), value2.get(), value3.get(), value4.get(), value5.get(),
                    value6.get(),value7.get(), value8.get(), value9.get(), value10.get(), value11.get(), value12.get()))

        buttonSubmit.grid(row = 14, column = 2, ipady=5, ipadx=15,padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 14, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

def writerSubmit(writerID, fname, mname, lname, SSN, phone, address, city, area, zip, bday, passingdate, sex):

    conn = sqlite3.connect('Diskographiki.db')

    conn.execute("""insert into writer values(?,?,?,?,?,?,?,?,?,?,?,?,?);""",
            (artistID, fname, mname, lname, SSN, phone, address, city, area, zip, bday, passingdate, sex))

    conn.commit()
    conn.close()
    app.show_frame(writerResults)

class writerResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The writer has been added on our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(AddStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 2, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)

class showPartnership(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the partnership's details\nbetween agent and artist:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)

        tk.Label(self, text ="Artist ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        value0 = tk.Entry(self, width = 20)
        value0.grid(row=1, column=1, padx=5)

        tk.Label(self, text ="Agent ID:",font = 'Arial 15').grid(row=2, column=0, padx = 5)
        value1 = tk.Entry(self, width = 20)
        value1.grid(row=2, column=1, padx=5)

        tk.Label(self, text ="Start Date:",font = 'Arial 15').grid(row=3, column=0, padx = 5)
        value2 = tk.Entry(self, width = 20)
        value2.grid(row=3, column=1, padx=5)

        tk.Label(self, text ="End Date:",font = 'Arial 15').grid(row=4, column=0, padx = 5)
        value3 = tk.Entry(self, width = 20)
        value3.grid(row=4, column=1, padx=5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(AddStartPage))
        buttonAddStartPage.grid(row = 5, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)


        buttonSubmit = ttk.Button(self, text = "Submit",
        command = lambda: partnershipSubmit(value0.get(), value1.get(), value2.get(), value3.get()))
        buttonSubmit.grid(row = 5, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 6, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 5, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

def partnershipSubmit(artistID, agentID, start_date, end_date):

    conn = sqlite3.connect('Diskographiki.db')
    conn.execute("""insert into manages values(?,?,?,?);""",
            artistID, agentID, start_date, end_date)

    conn.commit()
    conn.close()
    app.show_frame(partnershipResults)

class partnershipResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The partnership has been added on our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)
        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(AddStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)

#klaseis kai sinartiseis gia tin leitourgia delete

class DeleteStartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = "Βάσεις Δεδομένων - Project\n",
                           font = 'Arial 25').grid(row=0, column=0)

        tk.Label(self, text ="Μέλη Ομάδας:\nΣτούρα Θεοδώρα\n Τσαναή Σμαράγδα",
                   font = 'Arial 15',
                   bg ='grey').grid(row=0, column=3)
        tk.Label(self, text ="Ομάδα 35: Δισκογραφική Εταιρεία\n",
                   font = 'Arial 20 ').grid(row=2, column=0, padx = 5)

        tk.Label(self, text ="Επιλέξτε σε ποια κατηγορία \nθέλετε να αφαιρέσετε δεδομένα\n",
                   font = 'Arial 15').grid(row=3, column=0, padx = 5)

        buttonArtist = ttk.Button(self, text ="Artist",
        command = lambda : controller.show_frame(deleteArtist))
        buttonArtist.grid(row = 4, column = 0, ipady=10, ipadx=20,padx = 10, pady = 10)

        buttonAgent = ttk.Button(self, text ="Αgent",
        command = lambda : controller.show_frame(deleteAgent))
        buttonAgent.grid(row = 5, column = 0, ipady=10, ipadx=20, padx = 10, pady = 10)

        buttonContract = ttk.Button(self, text ="Contract",
        command = lambda : controller.show_frame(deleteContract))
        buttonContract.grid(row = 6, column = 0, ipady=10, ipadx=20, padx = 10, pady = 10)

        buttonSong = ttk.Button(self, text = "Song",
        command = lambda: controller.show_frame(deleteSong))
        buttonSong.grid(row = 7, column = 0, ipady=10, ipadx=20, padx = 10, pady = 10)

        buttonAlbum = ttk.Button(self, text ="Album",
        command = lambda : controller.show_frame(deleteAlbum))
        buttonAlbum.grid(row = 4, column = 1, ipady=10, ipadx=20, padx = 10, pady = 10)

        buttonStudio = ttk.Button(self, text ="Studio",
        command = lambda : controller.show_frame(deleteStudio))
        buttonStudio.grid(row = 5, column = 1, ipady=10, ipadx=20, padx = 10, pady = 10)

        buttonWriter = ttk.Button(self, text ="Writer",
        command = lambda : controller.show_frame(deleteWriter))
        buttonWriter.grid(row = 6, column = 1, ipady=10, ipadx=20, padx = 10, pady = 10)

        buttonPartnership = ttk.Button(self, text ="Partnership",
        command = lambda : controller.show_frame(deletePartnership))
        buttonPartnership.grid(row = 7, column = 1, ipady=10, ipadx=20, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 9, column = 1, ipady=10, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command= exit).grid(row = 9, column = 2, ipady=10, ipadx=15, padx = 10, pady = 10)

class deleteArtist(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please select the type of artist you desire\n delete from the database""",font = 'Arial 18').grid(row = 4, column = 0, padx = 5)

        buttonSoloArtist = ttk.Button(self, text ="Solo Artist",
        command = lambda : controller.show_frame(deleteSoloArtist))
        buttonSoloArtist.grid(row = 5, column = 0,ipady=10, ipadx=50, padx = 10, pady = 10)

        buttonBand = ttk.Button(self, text ="Band",
        command = lambda : controller.show_frame(deleteBand))
        buttonBand.grid(row = 6, column = 0,ipady=10, ipadx=50, padx = 10, pady = 10)

        buttonBandMember = ttk.Button(self, text ="Band Member",
        command = lambda : controller.show_frame(deleteBandMember))
        buttonBandMember.grid(row = 7, column = 0,ipady=10, ipadx=50, padx = 10, pady = 10)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 8, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 5, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = ttk.Button(self, text="Exit",command = exit).grid(row = 8, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

class deleteSoloArtist(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the solo artist's ID\nto be deleted:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)
        tk.Label(self, text ="Artist ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        artistID = tk.Entry(self, width = 20)
        artistID.grid(row=1, column=1, padx=5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 5, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 6, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: deleteSoloArtistSubmit(artistID.get()))

        buttonSubmit.grid(row = 5, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 5, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)


def deleteSoloArtistSubmit(artistID):

    conn = sqlite3.connect('Diskographiki.db')
    conn.execute("""delete from solo_artist where artist_id = (?);""",
            (artistID, ))

    conn.execute("""delete from artist where artist_id = (?);""",
            (artistID, ))

    conn.commit()
    conn.close()
    app.show_frame(deleteSoloArtistResults)

class deleteSoloArtistResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The solo artist has been removed from our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)

class deleteBand(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the band's ID\nto be deleted:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)
        tk.Label(self, text ="Band ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        bandID = tk.Entry(self, width = 20)
        bandID.grid(row=1, column=1, padx=5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 5, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 6, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: deleteBandSubmit(bandID.get()))

        buttonSubmit.grid(row = 5, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 5, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

def deleteBandSubmit(bandID):

    conn = sqlite3.connect('Diskographiki.db')
    print(type(bandID))
    conn.execute("""delete from band where band_id = ?""",
            (bandID,) )

    conn.execute("""delete from artist_id where artist_id = ?""",
        (bandID,) )

    conn.commit()
    conn.close()
    app.show_frame(deleteBandResults)

class deleteBandResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The band has been removed from our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15,padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)

class deleteSong(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the song's ID\nto be deleted:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)
        tk.Label(self, text ="Song ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        songID = tk.Entry(self, width = 20)
        songID.grid(row=1, column=1, padx=5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 5, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 6, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: deleteSongSubmit(songID.get()))

        buttonSubmit.grid(row = 5, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 5, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

def deleteSongSubmit(songID):

    conn = sqlite3.connect('Diskographiki.db')
    conn.execute("""delete from song where song_id = (?);""",
            (songID, ))

    conn.execute("""delete from composed where song_id = (?);""",
            (songID, ))

    conn.commit()
    conn.close()
    app.show_frame(deleteSongResults)

class deleteSongResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The song has been removed from our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)

class deleteBandMember(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the band's member ID\nto be deleted:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)
        tk.Label(self, text ="Band's member ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        bandmemberID = tk.Entry(self, width = 20)
        bandmemberID.grid(row=1, column=1, padx=5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 5, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 6, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: deleteBandMemberSubmit(bandMemberID.get()))

        buttonSubmit.grid(row = 5, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 5, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

def deleteBandMemberSubmit(bandMemberID):

    conn = sqlite3.connect('Diskographiki.db')
    conn.execute("""delete from band where band_id = (?);""",
            (bandMemberID, ))

    conn.execute("""delete from belongs_to where band_id = (?);""",
            (bandMemberID, ))

    conn.commit()
    conn.close()
    app.show_frame(deleteBandMemberResults)

class deleteBandMemberResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The band member has been removed from our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)


class deleteAgent(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the agent's ID\nto be deleted:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)
        tk.Label(self, text ="Band ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        agentID = tk.Entry(self, width = 20)
        agentID.grid(row=1, column=1, padx=5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 5, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 6, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: deleteBandSubmit(agentID.get()))

        buttonSubmit.grid(row = 5, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 5, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)


def deleteAgentSubmit(agentID):

    conn = sqlite3.connect('Diskographiki.db')
    conn.execute("""delete from agent where agent_id = (?);""",
            (agentID, ))

    conn.execute("""delete from manages where agent_id = (?);""",
            (agentID, ))

    conn.commit()
    conn.close()
    app.show_frame(deleteAgentResults)

class deleteAgentResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The agent has been removed from our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15,padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)

class deleteContract(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the contract's ID\nto be deleted:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)
        tk.Label(self, text ="Band ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        contractID = tk.Entry(self, width = 20)
        contractID.grid(row=1, column=1, padx=5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 5, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 6, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: deleteBandSubmit(contractID.get()))

        buttonSubmit.grid(row = 5, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 5, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)


def deleteContractSubmit(contractID):

    conn = sqlite3.connect('Diskographiki.db')
    conn.execute("""delete from contract where contract_id = (?);""",
            (contractID, ))

    conn.commit()
    conn.close()
    app.show_frame(deleteContractResults)

class deleteContractResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The contract has been removed from our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15,padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)


class deleteAlbum(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the album's ID\nto be deleted:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)
        tk.Label(self, text ="Band ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        albumID = tk.Entry(self, width = 20)
        albumID.grid(row=1, column=1, padx=5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 5, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 6, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: deleteAlbumSubmit(albumID.get()))

        buttonSubmit.grid(row = 5, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 5, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)


def deleteAlbumSubmit(albumID):

    conn = sqlite3.connect('Diskographiki.db')
    conn.execute("""delete from album where album_id = (?);""",
            (albumID, ))

    conn.commit()
    conn.close()
    app.show_frame(deleteAlbumResults)

class deleteAlbumResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The album has been removed from our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15,padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)

class deleteStudio(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the studio's ID\nto be deleted:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)
        tk.Label(self, text ="Band ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        studioID = tk.Entry(self, width = 20)
        studioID.grid(row=1, column=1, padx=5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 5, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 6, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: deleteStudioSubmit(studioID.get()))

        buttonSubmit.grid(row = 5, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 5, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

def deleteStudioSubmit(studioID):

    conn = sqlite3.connect('Diskographiki.db')
    conn.execute("""delete from studio where studio_id = (?);""",
            (studioID, ))

    conn.commit()
    conn.close()
    app.show_frame(deleteStudioResults)

class deleteStudioResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The studio has been removed from our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15,padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)

class deleteWriter(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the writer's ID\nto be deleted:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)
        tk.Label(self, text ="Writer ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        writerID = tk.Entry(self, width = 20)
        writerID.grid(row=1, column=1, padx=5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 5, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 6, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: deleteWriterSubmit(writerID.get()))

        buttonSubmit.grid(row = 5, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 5, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

def deleteWriterSubmit(writerID):

    conn = sqlite3.connect('Diskographiki.db')
    conn.execute("""delete from writer where writer_id = (?);""",
            (writerID, ))

    conn.commit()
    conn.close()
    app.show_frame(deleteWriterResults)

class deleteWriterResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The writer has been removed from our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15,padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)


class deletePartnership(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """Please enter the agent's and artist's ID\nto be deleted from the partnership:\n""",font = 'Arial 18').grid(row = 0, column = 1, padx = 5)
        tk.Label(self, text ="Agent ID:",font = 'Arial 15').grid(row=1, column=0, padx = 5)
        agentID = tk.Entry(self, width = 20)
        agentID.grid(row=1, column=1, padx=5)

        tk.Label(self, text ="Artist ID:",font = 'Arial 15').grid(row=2, column=0, padx = 5)
        artistID = tk.Entry(self, width = 20)
        artistID.grid(row=2, column=1, padx=5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
                            command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 3, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 4, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonSubmit = ttk.Button(self, text = "Submit",
                    command = lambda: deletePartnershipSubmit(partnershipID.get()))

        buttonSubmit.grid(row = 3, column = 2, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 3, column = 3, ipady=5, ipadx=15, padx = 10, pady = 10)

def deletePartnershipSubmit(agentID, artistID):

    conn = sqlite3.connect('Diskographiki.db')
    conn.execute("""delete from manages where (agentID, artistID) values (?,?);""",
            (agentID, artistID))

    conn.commit()
    conn.close()
    app.show_frame(deletePartnershipResults)

class deletePartnershipResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = """The partnership between agent and artist\nhas been removed from our datebase\n""",font = 'Arial 18').grid(row = 0, column = 0, padx = 5)

        buttonAddStartPage = ttk.Button(self, text ="Start Page",
        command = lambda : controller.show_frame(DeleteStartPage))
        buttonAddStartPage.grid(row = 1, column = 0, ipady=5, ipadx=15,padx = 10, pady = 10)

        buttonMainMenu = ttk.Button(self, text ="Main Menu",
        command = lambda : controller.show_frame(MainMenu))
        buttonMainMenu.grid(row = 2, column = 0, ipady=5, ipadx=15, padx = 10, pady = 10)

        buttonExit = tk.Button(self, text="Exit",command = exit).grid(row = 1, column = 1, ipady=5, ipadx=15, padx = 10, pady = 10)

app = App()
app.mainloop()
