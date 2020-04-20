import csv
import math
import mysql.connector as mc
mydb=mc.connect(host="localhost",
  user="root",
  passwd="iamtheannabelle",auth_plugin='mysql_native_password',database="Health")
def MainScreen():
    print("Login/Signup as:")
    print("1.User\n2.Doctor\n3.Company\n4.Lab\n5.Delivery Agency\n0.Exit")
    logch=int(input())
    if logch==1:
        UserMenu()
    if logch==2:
        DoctorMenu()
    if logch==3:
        CompanyMenu()
    if logch==4:
        LabMenu()
    if logch==5:
        DAMenu()
    if logch==0:
        exit(0)

def UserMenu():
    print("Login as user:")
    print("ID:")
    id=input()
    print("Password")
    passw=input()
    reguser=[]
    with open('userpass.csv', newline='') as file:
        spamreader = csv.reader(file, delimiter=',', quotechar='"')
        for row in spamreader:
            reguser.append(row)
    for d in reguser:
        if d[0]==id and d[1]==passw:
            usquery(id)
            return
    print("Wrong ID/Password, going to Main screen")
    MainScreen()

def DoctorMenu():
    print("Login as Doctor:")
    print("ID:")
    id = input()
    print("Password")
    passw = input()
    reguser = []
    with open('docpass.csv', newline='') as file:
        spamreader = csv.reader(file, delimiter=',', quotechar='"')
        for row in spamreader:
            reguser.append(row)
    for d in reguser:
        if d[0] == id and d[1] == passw:
            docquery(id)
            return
    print("Wrong ID/Password, going to Main screen")
    MainScreen()

def CompanyMenu():
    print("Login as Company:")
    print("ID:")
    id = input()
    print("Password")
    passw = input()
    reguser = []
    with open('companypass.csv', newline='') as file:
        spamreader = csv.reader(file, delimiter=',', quotechar='"')
        for row in spamreader:
            reguser.append(row)
    for d in reguser:
        if d[0] == id and d[1] == passw:
            compquery(id)
            return
    print("Wrong ID/Password, going to Main screen")
    MainScreen()

def LabMenu():
    print("Login as Lab:")
    print("ID:")
    id = input()
    print("Password")
    passw = input()
    reguser = []
    with open('labpass.csv', newline='') as file:
        spamreader = csv.reader(file, delimiter=',', quotechar='"')
        for row in spamreader:
            reguser.append(row)
    for d in reguser:
        if d[0] == id and d[1] == passw:
            labquery(id)
            return
    print("Wrong ID/Password, going to Main screen")
    MainScreen()

def DAMenu():
    print("Login as DeliveryAgency:")
    print("ID:")
    id = input()
    print("Password")
    passw = input()
    reguser = []
    with open('dapass.csv', newline='') as file:
        spamreader = csv.reader(file, delimiter=',', quotechar='"')
        for row in spamreader:
            reguser.append(row)
    for d in reguser:
        if d[0] == id and d[1] == passw:
            daquery(id)
            return
    print("Wrong ID/Password, going to Main screen")
    MainScreen()

def usquery(id):
    mycursor = mydb.cursor()
    print("Select Query:")
    print("1:Best doctors near me:")
    print("2:Authenticity of a Medicine:")
    print("3:Better alternatives to a drug:")
    print("4:Quantity of a Drug:")
    print("5:Price of a Drug:")
    print("6:MainScreen")
    ch=int(input())
    if ch==1:
        mycursor.execute("Select city from userr where UID="+str(id))
        city=mycursor.fetchall()[0][0]
        mycursor.execute("SELECT Doctor.DID, Doctor.dname, doctor.Phone, AVG(DoctorReviews.Rating),Doctor.StreetAdress FROM Doctor,DoctorReviews,Appointment,OpenSlots WHERE Doctor.DID=Openslots.DID and OpenSlots.SID=Appointment.SID and Appointment.AID=DoctorReviews.AID AND Doctor.city=\""+city+"\" group by Doctor.did")
        res=mycursor.fetchall()
        if len(res)==0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Phone:%5s Rating:%5s, Address:%5s"%(d[0],d[1],d[2],round(d[3],2),d[4]+" "+city))
    if ch==2:
        print("Input Drug Name:")
        drug=input()
        mycursor.execute("SELECT Drug.DrID,Drug.Drname, AVG(DrugReviews.rating) FROM Drug,DrugReviews,Orderr WHERE DrugReviews.OID=Orderr.OID AND Orderr.DrID=Drug.DrID AND Drug.Drname=\""+drug+"\" group by drug.drid")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Rating:%5s"%(d[0],d[1],round(d[2],2)))
    if ch==3:
        print("Input symptoms:")
        symp=input()
        print("Input Sickness")
        sickness=input()
        mycursor.execute("SELECT Drug.drID,Drug.drname,avg(Drugreviews.rating),Drug.price from Drug,Orderr,DrugReviews where DrugReviews.OID = Orderr.OID AND Drug.DrID=Orderr.DrID   AND ( Drug.symptoms LIKE '%"+symp+"%' OR Drug.sickness LIKE '%"+sickness+"%') group by Drug.drid")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Rating:%5s Price:%s"%(d[0],d[1],round(d[2],2),d[3]))

    if ch==4:
        print("Input Drug Name:")
        drug = input()
        mycursor.execute("SELECT DrID,DrName,Quantity FROM Drug WHERE DRName=\""+drug+"\";")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Quantity:%s" % (d[0], d[1], d[2]))
    if ch==5:
        print("Input Drug Name:")
        drug = input()
        mycursor.execute("SELECT DrID,DrName,Price FROM Drug WHERE DRName=\""+drug+"\";")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Price:%s" % (d[0], d[1], d[2]))
    if ch==6:
        MainScreen()
        return
    usquery(id)

def docquery(id):
    mycursor = mydb.cursor()
    print("Select Query:")
    print("1:Upcoming appointments:")
    print("2:Upcoming open slots:")
    print("3:Drug for some sickness or symptoms:")
    print("4:Reviews of drugs prescribed:")
    print("5:Reviews for appointments:")
    print("6:MainScreen")
    ch=int(input())
    if ch==1:
        print("Input date:")
        date=input()
        mycursor.execute("SELECT AID,UID,STIME,SDATE FROM Appointment,OpenSlots WHERE Appointment.SID=OpenSlots.SID AND OpenSlots.DID="+str(id)+" AND OpenSlots.SDate >=\""+date+"\"")
        res=mycursor.fetchall()
        if len(res)==0:
            print("No results.")
        else:
            for d in res:
                print("Appointment ID:%s UserID:%s Time:%5s Date:%5s"%(d[0],d[1],d[2],d[3]))

    if ch==2:
        print("Input date:")
        date = input()
        mycursor.execute(
            "SELECT SID,STIME,SDATE FROM OpenSlots WHERE OpenSlots.DID=" + str(
                id) + " AND OpenSlots.SDate >=\"" + date + "\"")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("Appointment ID:%s Time:%5s Date:%5s" % (d[0], d[1], d[2]))

    if ch==3:
        print("Input symptoms:")
        symp = input()
        print("Input Sickness")
        sickness = input()
        mycursor.execute(
            "SELECT Drug.drID,Drug.drname,avg(Drugreviews.rating),Drug.price from Drug,Orderr,DrugReviews where DrugReviews.OID = Orderr.OID AND Drug.DrID=Orderr.DrID   AND ( Drug.symptoms LIKE '%" + symp + "%' OR Drug.sickness LIKE '%" + sickness + "%') group by Drug.drid")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Rating:%5s Price:%s" % (d[0], d[1], round(d[2], 2), d[3]))

    if ch==4:
        mycursor.execute("SELECT Drug.DrID,Drname,Avg(DrugReviews.rating) FROM Drug,Prescription,Orderr,DrugReviews WHERE Drug.drID=Prescription.drid and Prescription.DrID=Orderr.DrID AND Orderr.OID = DrugReviews.OID AND Prescription.DID="+str(id)+" group by Drug.drid;")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Rating:%s" % (d[0], d[1], round(d[2],2)))
    if ch==5:
        mycursor.execute("SELECT Appointment.AID,DoctorReviews.rating FROM Appointment,DoctorReviews,OpenSlots WHERE Appointment.SID=OpenSlots.SID AND DoctorReviews.AID=Appointment.AID AND OpenSlots.DID="+str(id))
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("Appointment ID:%s Rating:%s" % (d[0], round(d[1],2)))
    if ch==6:
        MainScreen()
        return
    docquery(id)

def compquery(id):
    mycursor = mydb.cursor()
    print("Select Query:")
    print("1:Price of Drugs sold by the company:")
    print("2:Drugs ordered which are sold by the company:")
    print("3:Quantity of the drugs:")
    print("4:Alternative drugs by other companies and their prices:")
    print("5:Reviews of drugs sold by the company:")
    print("6:MainScreen")
    ch = int(input())
    if ch == 1:

        mycursor.execute("SELECT DrID,DrName,Price FROM Drug WHERE CID =" + str(id))
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Price:%s" % (d[0], d[1], d[2]))

    if ch == 2:
        mycursor.execute("SELECT OID,Drug.drID,Quantity,Orderr.Price FROM Orderr,Drug WHERE Drug.DrID=Orderr.DrID AND CID="+str(id))
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("Order ID:%s Drug ID:%s Quantity:%s Price:%5s" % (d[0], d[1], d[2],d[3]))

    if ch == 3:
        mycursor.execute("SELECT DrID,DrName,Quantity FROM Drug WHERE CID =" + str(id))
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Quantity:%s" % (d[0], d[1], d[2]))

    if ch == 4:
        print("Input symptoms:")
        symp = input()
        print("Input Sickness")
        sickness = input()
        mycursor.execute(
            "SELECT Drug.drID,Drug.drname,avg(Drugreviews.rating),CID,Drug.price from Drug,Orderr,DrugReviews where DrugReviews.OID = Orderr.OID AND Drug.DrID=Orderr.DrID   AND ( Drug.symptoms LIKE '%" + symp + "%' OR Drug.sickness LIKE '%" + sickness + "%') group by Drug.drid")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Rating:%5s Company ID:%s Price:%s" % (d[0], d[1], round(d[2], 2),d[3], d[4]))
    if ch == 5:
        mycursor.execute("SELECT Drug.DrID,DrName,Avg(DrugReviews.rating) FROM Drug,Orderr,DrugReviews WHERE Drug.DrID=Orderr.DrID AND Orderr.OID = DrugReviews.OID AND Drug.CID="+str(id)+" group by Drug.drid;")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Rating:%5s" % (d[0], d[1], round(d[2], 2)))
    if ch == 6:
        MainScreen()
        return
    compquery(id)

def labquery(id):
    mycursor = mydb.cursor()
    print("Select Query:")
    print("1:Tests performed or to be performed by the lab")
    print("2:Patient Details:")
    print("3:Competitive labs in the same city:")
    print("4:Diagnostic reports generated:")
    print("5:Reviews of Tests:")
    print("6:MainScreen")
    ch = int(input())
    if ch == 1:

        mycursor.execute("SELECT TID,UID,TTIME, TDATE FROM Test WHERE LabID=" + str(id))
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("Test ID:%s User ID:%s Time:%s Date:%s" % (d[0], d[1], d[2],d[3]))

    if ch == 2:
        print("Input User ID")
        uid=int(input())
        mycursor.execute("SELECT distinct(Userr.UID),UName,Age,Gender,Phone FROM Test,Userr WHERE Test.UID="+str(uid)+" AND Userr.UID=Test.UID;")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("User ID:%s User name:%s Age:%s Gender:%s Phone:%s" % (d[0], d[1], d[2], d[3],d[4]))


    if ch == 3:
        mycursor.execute("Select city from lab where labID=" + str(id))
        city = mycursor.fetchall()[0][0]
        mycursor.execute("SELECT lab.LabID, lab.lname, lab.tests, AVG(LabReviews.rating) FROM Test,Lab,LabReviews WHERE Lab.LabID=Test.LabID AND Test.Tid=LabReviews.Tid and city=\""+city+"\" group by lab.labid;")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("LabID:%s LabName:%s  Rating:%s Tests:%s" % (d[0],d[1],round(d[3],2),d[2]))

    if ch == 4:
        mycursor.execute("SELECT DirID, Test.TID,UID, DiRDate,Remarks FROM Test,DiagnosticReports WHERE Test.TID=DiagnosticReports.TID AND Test.LabID="+str(id))
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("Report ID:%s Test ID:%s User ID:%s Date ID:%s Remarks:%s" % (d[0], d[1],d[2], d[3], d[4]))
    if ch == 5:
        mycursor.execute(
            "SELECT Test.TID, rating FROM Test,LabReviews WHERE Test.TID=LabReviews.TID AND Test.LabID="+str(id))
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("Test ID:%s Rating:%5s" % (d[0],round(d[1], 2)))
    if ch == 6:
        MainScreen()
        return
    labquery(id)

def daquery(id):
    mycursor = mydb.cursor()
    print("Select Query:")
    print("1:Upcoming deliveries:")
    print("2:Update delivery status:")
    print("3:Competitive labs in the some delivery city:")
    print("4:Most popular delivery areas:")
    print("5:Reviews of Deliveries:")
    print("6:MainScreen")
    ch = int(input())
    if ch == 1:
        print("Input Date:")
        date=input()
        mycursor.execute("SELECT DeID,Destatus,ETA FROM Delivery WHERE DAID="+str(id)+" and ETA>=\""+date+"\";")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("Delivery ID:%s Status:%s Date:%s" % (d[0], d[1],d[2]))

    if ch == 2:
        print("Input delivery ID")
        did = int(input())
        mycursor.execute("select DAID from delivery where deid="+str(did))
        # print(mycursor.fetchall()[0][0],id)
        if int(mycursor.fetchall()[0][0])!=int(id):
            print("Unauthorized request")
            daquery(id)
            return
        print("Input new status")
        status=input()
        mycursor.execute("UPDATE Delivery set Destatus=\""+status+"\" where DEID="+str(did))


    if ch == 3:
        print("Input city:")
        city=input()
        mycursor.execute(
            "SELECT Delivery.daid,DAname,avg(DeliveryReviews.rating) FROM orderr,Delivery,DeliveryAgency,DeliveryReviews WHERE orderr.OID=Delivery.OID and Delivery.DaID=DeliveryAgency.DaID AND Delivery.DeID=DeliveryReviews.DeID and Orderr.city=\""+city+"\" group by delivery.DAID;")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("DeliveryAgency ID:%s Name:%s  Rating:%s " % (d[0], d[1], round(d[2], 2)))

    if ch == 4:
        mycursor.execute(
            "SELECT Orderr.postalcode,COUNT(*) FROM Delivery,Orderr WHERE Orderr.OID=Delivery.OID GROUP BY orderr.postalcode order by count(*) desc;")

        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("Delivery Area:%s Orders:%s" % (d[0], d[1]))
    if ch == 5:
        mycursor.execute(
            "SELECT Delivery.deid,rating FROM Delivery,DeliveryReviews WHERE DeliveryReviews.DeID=Delivery.DeID AND Delivery.DaID=" + str(id))
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("Delivery ID:%s Rating:%5s" % (d[0], round(d[1], 2)))
    if ch == 6:
        MainScreen()
        return
    daquery(id)


MainScreen()