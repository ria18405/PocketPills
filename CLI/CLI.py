import csv
import hashlib
import subprocess
import matplotlib.pyplot as plt
import numpy as np
# plt.ion()
import math
import mysql.connector as mc
mydb=mc.connect(host="localhost",
  user="root",
  passwd="xxxx",auth_plugin='mysql_native_password',database="Health")
def MainScreen():
    print("Login as:")
    print("1.User\n2.Doctor\n3.Company\n4.Lab\n5.Delivery Agency\n6.Retailer\n0.Exit")
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
    if logch==6:
        RetailerMenu()
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
    encpass=hashlib.md5(passw.encode()).hexdigest()
    for d in reguser:
        if d[0]==id and d[1]==encpass:
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

    encpass = hashlib.md5(passw.encode()).hexdigest()
    for d in reguser:
        if d[0] == id and d[1] == encpass:
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

    encpass = hashlib.md5(passw.encode()).hexdigest()
    for d in reguser:
        if d[0] == id and d[1] == encpass:
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
    encpass = hashlib.md5(passw.encode()).hexdigest()
    for d in reguser:
        if d[0] == id and d[1] == encpass:
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
    encpass = hashlib.md5(passw.encode()).hexdigest()
    for d in reguser:
        if d[0] == id and d[1] == encpass:
            daquery(id)
            return
    print("Wrong ID/Password, going to Main screen")
    MainScreen()

def RetailerMenu():
    print("Login as Retailer/User:")
    print("ID:")
    id=input()
    print("Password")
    passw=input()
    reguser=[]
    with open('userpass.csv', newline='') as file:
        spamreader = csv.reader(file, delimiter=',', quotechar='"')
        for row in spamreader:
            reguser.append(row)
    encpass=hashlib.md5(passw.encode()).hexdigest()
    for d in reguser:
        if d[0]==id and d[1]==encpass:
            retquery(id)
            return
    print("Wrong ID/Password, going to Main screen")
    MainScreen()

def usquery(id):
    id = int(id)
    mycursor = mydb.cursor()
    print("Select Query:")
    print("1:Best doctors near me:")
    print("2:Authenticity of a Medicine:")
    print("3:Better alternatives to a drug:")
    print("4:Quantity of a Drug:")
    print("5:Price of a Drug:")
    print("6:Chat with a Doctor(BONUS):")
    print("7:Alternative drugs based on order history (BONUS)")
    print("8:Orders vs Date BAR-CHART(BONUS)")
    print("0:MainScreen")
    ch=int(input())
    if ch==1:
        mycursor.execute("Select city from Userr where UID="+str(id))
        city=mycursor.fetchall()[0][0]
        mycursor.execute("SELECT Doctor.DID, Doctor.dname, Doctor.Phone, Qualifications, specialization, AVG(DoctorReviews.Rating),Doctor.StreetAdress FROM Doctor,DoctorReviews,Appointment,OpenSlots WHERE Doctor.DID=OpenSlots.DID and OpenSlots.SID=Appointment.SID and Appointment.AID=DoctorReviews.AID AND Doctor.city=\""+city+"\" group by Doctor.did")
        res=mycursor.fetchall()
        if len(res)==0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Phone:%5s Qualifications:%s Speciality:%s Rating:%5s, Address:%5s"%(d[0],d[1],d[2],d[3],d[4],round(d[5],2),d[6]+" "+city))
    if ch==2:
        print("Input Drug Name:")
        drug=input()
        mycursor.execute("SELECT Drug.DrID,Drug.Drname, AVG(DrugReviews.rating) FROM Drug,DrugReviews,Orderr WHERE DrugReviews.OID=Orderr.OID AND Orderr.DrID=Drug.DrID AND Drug.Drname=\""+drug+"\" group by Drug.DRID")
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
        mycursor.execute("SELECT Drug.drID,Drug.drname,sickness,symptoms,avg(DrugReviews.Rating),Drug.price from Drug,Orderr,DrugReviews where DrugReviews.OID = Orderr.OID AND Drug.DrID=Orderr.DrID   AND ( Drug.symptoms LIKE '%"+symp+"%' OR Drug.sickness LIKE '%"+sickness+"%') group by Drug.drid")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Sickness: %s symptoms: %s Rating:%5s Price:%s"%(d[0],d[1],d[2],d[3], round(d[4],2),d[5]))
            dridpr = set()
            for d in res:
                dridpr.add(d[0])
            mycursor.execute(
                "SELECT Drug.drID,Drug.drname,sickness,symptoms,Drug.price from Drug where ( Drug.symptoms LIKE '%" + symp + "%' OR Drug.sickness LIKE '%" + sickness + "%')")
            res = mycursor.fetchall()
            for d in res:
                if d[0] not in dridpr:
                    print("ID:%s Name:%s Sickness: %s symptoms: %s Price:%s" % (d[0], d[1], d[2], d[3], d[4]))

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
        print("Input your <user ID + 1000> as user no.")
        print("Start every message with <Doctor ID> to send a message to the Doctor")
        subprocess.call("./user")

    if ch==7:
        mycursor.execute("SELECT symptoms,sickness from Orderr,Drug where uid="+str(id)+" and Drug.drid=Orderr.drid group by Drug.drid order by sum(Orderr.price/Drug.price) desc;")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            symp = res[0][0]
            sickness = res[0][1]
            mycursor.execute(
                "SELECT Drug.drID,Drug.drname,sickness,symptoms,avg(DrugReviews.rating),Drug.price from Drug,Orderr,DrugReviews where DrugReviews.OID = Orderr.OID AND Drug.DrID=Orderr.DrID   AND ( Drug.symptoms LIKE '%" + symp + "%' OR Drug.sickness LIKE '%" + sickness + "%') group by Drug.drid")
            res = mycursor.fetchall()

            for d in res:
                print("ID:%s Name:%s Sickness: %s symptoms: %s Rating:%5s Price:%s" % (d[0], d[1],d[2],d[3], round(d[4], 2), d[5]))
            dridpr=set()
            for d in res:
                dridpr.add(d[0])
            mycursor.execute(
                "SELECT Drug.drID,Drug.drname,sickness,symptoms,Drug.price from Drug where ( Drug.symptoms LIKE '%" + symp + "%' OR Drug.sickness LIKE '%" + sickness + "%')")
            res = mycursor.fetchall()
            for d in res:
                if d[0] not in dridpr:
                    print("ID:%s Name:%s Sickness: %s symptoms: %s Price:%s" % (d[0], d[1],d[2],d[3],  d[4]))
    if ch==8:
        mycursor.execute("select odate,count(*) from Orderr where uid="+str(id)+" group by odate order by odate asc")
        res=mycursor.fetchall()

        objects = ()
        for d in res:
            objects+=(d[0],)
        y_pos = np.arange(len(objects))
        counts = []
        for d in res:
            counts.append(d[1])


        plt.bar(y_pos, counts, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('No. of orders')
        plt.title('Orders on some date')
        plt.show(block=False)


    if ch==0:
        MainScreen()
        return
    print("\n\n")
    usquery(id)

def docquery(id):
    id = int(id)
    mycursor = mydb.cursor()
    print("Select Query:")
    print("1:Upcoming appointments:")
    print("2:Upcoming open slots:")
    print("3:Drug for some sickness or symptoms:")
    print("4:Reviews of drugs prescribed:")
    print("5:Reviews for appointments:")
    print("6:Chat with a patient(BONUS)")
    print("7:Alternative drugs to prescribe based on history(BONUS)")
    print("8:Open-Slots vs Date BAR-CHART (BONUS)")
    print("9:Appointments vs Date BAR-CHART (BONUS)")
    print("0:MainScreen")
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
                print("Open Slots ID:%s Time:%5s Date:%5s" % (d[0], d[1], d[2]))

    if ch==3:
        print("Input symptoms:")
        symp = input()
        print("Input Sickness")
        sickness = input()
        mycursor.execute(
            "SELECT Drug.drID,Drug.drname,sickness,symptoms,avg(DrugReviews.rating),Drug.price from Drug,Orderr,DrugReviews where DrugReviews.OID = Orderr.OID AND Drug.DrID=Orderr.DrID   AND ( Drug.symptoms LIKE '%" + symp + "%' OR Drug.sickness LIKE '%" + sickness + "%') group by Drug.drid")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Sickness: %s symptoms: %s Rating:%5s Price:%s" % (d[0], d[1],d[2],d[3], round(d[4], 2), d[5]))
            dridpr = set()
            for d in res:
                dridpr.add(d[0])
            mycursor.execute(
                "SELECT Drug.drID,Drug.drname,sickness,symptoms,Drug.price from Drug where ( Drug.symptoms LIKE '%" + symp + "%' OR Drug.sickness LIKE '%" + sickness + "%')")
            res = mycursor.fetchall()
            for d in res:
                if d[0] not in dridpr:
                    print("ID:%s Name:%s Sickness: %s symptoms: %s Price:%s" % (d[0], d[1], d[2], d[3], d[4]))
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
        print("Input your <Doctor ID> as user no.")
        print("Start every message with <user ID + 1000> to send a message to the Doctor")
        subprocess.call("./user")

    if ch==7:
        mycursor.execute(
            "SELECT symptoms,sickness FROM Drug,Prescription WHERE Drug.drID=Prescription.drid AND Prescription.DID=" + str(id) + " group by Drug.drid order by count(*);")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            symp = res[0][0]
            sickness = res[0][1]
            mycursor.execute(
                "SELECT Drug.drID,Drug.drname,sickness,symptoms,avg(DrugReviews.rating),Drug.price from Drug,Orderr,DrugReviews where DrugReviews.OID = Orderr.OID AND Drug.DrID=Orderr.DrID   AND ( Drug.symptoms LIKE '%" + symp + "%' OR Drug.sickness LIKE '%" + sickness + "%') group by Drug.drid")
            res = mycursor.fetchall()

            for d in res:
                print("ID:%s Name:%s Sickness: %s symptoms: %s Rating:%5s Price:%s" % (
                d[0], d[1], d[2], d[3], round(d[4], 2), d[5]))
            dridpr = set()
            for d in res:
                dridpr.add(d[0])
            mycursor.execute(
                "SELECT Drug.drID,Drug.drname,sickness,symptoms,Drug.price from Drug where ( Drug.symptoms LIKE '%" + symp + "%' OR Drug.sickness LIKE '%" + sickness + "%')")
            res = mycursor.fetchall()
            for d in res:
                if d[0] not in dridpr:
                    print("ID:%s Name:%s Sickness: %s symptoms: %s Price:%s" % (d[0], d[1], d[2], d[3], d[4]))
    if ch==8:
        mycursor.execute("select sdate,count(*) from OpenSlots where did="+str(id)+" group by sdate order by sdate asc")
        res=mycursor.fetchall()

        objects = ()
        for d in res:
            objects+=(d[0],)
        y_pos = np.arange(len(objects))
        counts = []
        for d in res:
            counts.append(d[1])
        plt.bar(y_pos, counts, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('No. of Open Slots')
        plt.title('Open Slots on some date')
        plt.show(block=False)

    if ch==9:
        mycursor.execute("select sdate,count(*) from OpenSlots,Appointment where Openlots.sid=Appointment.sid and did="+str(id)+" group by sdate order by sdate asc")
        res=mycursor.fetchall()

        objects = ()
        for d in res:
            objects+=(d[0],)
        y_pos = np.arange(len(objects))
        counts = []
        for d in res:
            counts.append(d[1])
        plt.bar(y_pos, counts, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('No. of Appointments')
        plt.title('Appointments on some date')
        plt.show(block=False)

    if ch==0:
        MainScreen()
        return
    print("\n\n")
    docquery(id)
def compquery(id):
    id = int(id)
    mycursor = mydb.cursor()
    print("Select Query:")
    print("1:Price of Drugs sold by the company:")
    print("2:Drugs ordered which are sold by the company:")
    print("3:Quantity of the drugs:")
    print("4:Alternative drugs by other companies and their prices:")
    print("5:Reviews of drugs sold by the company:")
    print("6:Most frequent sickness and symptoms(BONUS)")
    print("7:Company Market-Share PIE-CHART(BONUS)")
    print("8:Drug Market-Share PIE-CHART(BONUS)")
    print("9:Drug orders vs date BAR-CHART(BONUS) ")
    print("0:MainScreen")
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
        mycursor.execute("SELECT OID,Drug.drID,Drug.price,Orderr.Price FROM Orderr,Drug WHERE Drug.DrID=Orderr.DrID AND CID="+str(id))
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("Order ID:%s Drug ID:%s Quantity:%d Price:%5s" % (d[0], d[1], int(d[3])/int(d[2]),d[3]))

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
            "SELECT Drug.drID,Drug.drname,sickness,symptoms,avg(DrugReviews.rating),CID,Drug.price from Drug,Orderr,DrugReviews where DrugReviews.OID = Orderr.OID AND Drug.DrID=Orderr.DrID   AND ( Drug.symptoms LIKE '%" + symp + "%' OR Drug.sickness LIKE '%" + sickness + "%') group by Drug.drid")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Sickness: %s symptoms: %s Rating:%5s Company ID:%s Price:%s" % (d[0], d[1], d[2],d[3], round(d[4], 2),d[5], d[6]))
            dridpr = set()
            for d in res:
                dridpr.add(d[0])
            mycursor.execute(
                "SELECT Drug.drID,Drug.drname,sickness,symptoms,cid,Drug.price from Drug where ( Drug.symptoms LIKE '%" + symp + "%' OR Drug.sickness LIKE '%" + sickness + "%')")
            res = mycursor.fetchall()
            for d in res:
                if d[0] not in dridpr:
                    print("ID:%s Name:%s Sickness: %s symptoms: %s Company ID:%s Price:%s" % (d[0], d[1], d[2], d[3],d[4], d[5]))
    if ch == 5:
        mycursor.execute("SELECT Drug.DrID,DrName,Avg(DrugReviews.rating) FROM Drug,Orderr,DrugReviews WHERE Drug.DrID=Orderr.DrID AND Orderr.OID = DrugReviews.OID AND Drug.CID="+str(id)+" group by Drug.drid;")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Rating:%5s" % (d[0], d[1], round(d[2], 2)))
    if ch==6:
        mycursor.execute(
            "SELECT symptoms,sum(Orderr.price/Drug.price) FROM Drug,Orderr WHERE Drug.DrID=Orderr.DrID group by symptoms order by sum(Orderr.price/Drug.price) desc")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            print("Most frequent symptoms by order history:")
            i = 3
            for d in res:
                print("Symptoms:%s Quantity ordered of drugs for that symptom:%d" % (d[0], int(d[1])))
                i -= 1
                if i < 1:
                    break
        print("\n")
        mycursor.execute(
            "SELECT sickness,sum(Orderr.price/Drug.price) FROM Drug,Orderr WHERE Drug.DrID=Orderr.DrID group by sickness order by sum(Orderr.price/Drug.price) desc")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            print("Most frequent sickness by order history:")
            i = 3
            for d in res:
                print("Sickness:%s Quantity ordered of drugs for that sickness:%d" % (d[0], int(d[1])))
                i -= 1
                if i < 1:
                    break
    if ch==7:
        mycursor.execute(
            "SELECT CID, sum(Orderr.price/Drug.price) FROM Orderr,Drug WHERE Drug.DrID=Orderr.DrID GROUP BY Drug.cid order by sum(Orderr.price/Drug.price) desc")
        res = mycursor.fetchall()
        su=0
        loc=-1
        i=0
        for d in res:
            if d[0]==id:
                loc=i
            i+=1
            su+=d[1]
        if loc>5:
            labels = res[loc][0],res[0][0],res[1][0],res[2][0],res[3][0],'others'
            sizes = [res[loc][1], res[0][1], res[1][1], res[2][1],res[3][1],su-res[loc][1]-res[0][1]-res[1][1]-res[2][1]-res[3][1]]
            colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red','purple']
            explode = (0.1, 0, 0, 0,0,0)  # explode 1st slice
        else:
            labels = res[0][0], res[1][0], res[2][0], res[3][0],res[4][0], 'others'
            sizes =  [res[0][1], res[1][1], res[2][1], res[3][1],res[4][1],su - res[0][1] - res[1][1] - res[2][1] - res[3][1]-res[4][1]]
            colors = ['gold','yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'purple']
            explode=()
            for i in range(6):
                if i==loc:
                    explode=explode+(0.1,)
                else:
                    explode=explode+(0,)

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show(block=False)

    if ch==8:
        mycursor.execute(
            "SELECT Drug.DRID FROM Orderr,Drug WHERE Drug.DrID=Orderr.DrID AND CID=" + str(
                id)+" group by Drug.drid order by sum(Orderr.price/Drug.price) desc")
        res = mycursor.fetchall()
        if len(res)==0:
            dr=-1
        else:
            dr=res[0][0]
        # print(dr)
        mycursor.execute(
            "SELECT Drug.DrID, sum(Orderr.price/Drug.price) FROM Orderr,Drug WHERE Drug.DrID=Orderr.DrID GROUP BY Drug.drid order by sum(Orderr.price/Drug.price) desc")
        res = mycursor.fetchall()
        # print(res)
        su = 0
        loc = -1
        i = 0
        for d in res:
            if d[0] == dr:
                loc = i
            i += 1
            su += d[1]
        if loc > 5:
            labels = res[loc][0], res[0][0], res[1][0], res[2][0], res[3][0], 'others'
            sizes = [res[loc][1], res[0][1], res[1][1], res[2][1], res[3][1],
                     su - res[loc][1] - res[0][1] - res[1][1] - res[2][1] - res[3][1]]
            colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'purple']
            explode = (0.1, 0, 0, 0, 0, 0)  # explode 1st slice
        else:
            labels = res[0][0], res[1][0], res[2][0], res[3][0], res[4][0], 'others'
            sizes = [res[0][1], res[1][1], res[2][1], res[3][1], res[4][1],
                     su - res[0][1] - res[1][1] - res[2][1] - res[3][1] - res[4][1]]
            colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'purple']
            explode = ()
            for i in range(6):
                if i == loc:
                    explode = explode + (0.1,)
                else:
                    explode = explode + (0,)

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show(block=False)

    if ch==9:
        print("Enter Drug-ID")
        drid=input()
        mycursor.execute("select odate,sum(Orderr.price/Drug.price) from Orderr,Drug where Drug.drid=Orderr.drid and Drug.drid="+str(drid)+" group by odate order by odate asc")
        res=mycursor.fetchall()

        objects = ()
        for d in res:
            objects+=(d[0],)
        y_pos = np.arange(len(objects))
        counts = []
        for d in res:
            counts.append(int(d[1]))


        plt.bar(y_pos, counts, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Quantity ordered')
        plt.title('Quantity ordered on some date')
        plt.show(block=False)
    if ch == 0:
        MainScreen()
        return
    print("\n\n")
    compquery(id)

def labquery(id):
    id = int(id)
    mycursor = mydb.cursor()
    print("Select Query:")
    print("1:Tests performed or to be performed by the lab")
    print("2:Patient Details:")
    print("3:Competitive labs in the same city:")
    print("4:Diagnostic reports generated by the lab:")
    print("5:Reviews of Tests:")
    print("6:Most popular tests worldwide and most popular tests in lab's city(BONUS):")
    print("7:Lab Market-Share PIE-CHART (BONUS)")
    print("8:Test Market-Share PIE-CHART (BONUS)")
    print("9:Tests vs date BAR-CHART (BONUS)")
    print("0:MainScreen")
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
        mycursor.execute("SELECT Lab.LabID, Lab.lname, Lab.tests, AVG(LabReviews.rating) FROM Test,Lab,LabReviews WHERE Lab.LabID=Test.LabID AND Test.Tid=LabReviews.Tid and city=\""+city+"\" group by Lab.labid;")
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
                print("Report ID:%s Test ID:%s User ID:%s Date:%s Remarks:%s" % (d[0], d[1],d[2], d[3], d[4]))
    if ch == 5:
        mycursor.execute(
            "SELECT Test.TID, rating FROM Test,LabReviews WHERE Test.TID=LabReviews.TID AND Test.LabID="+str(id))
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("Test ID:%s Rating:%5s" % (d[0],round(d[1], 2)))
    if ch==6:
        print("Most Popular Worldwide:")
        mycursor.execute("Select Tests,count(*) from Test group by tests order by count(*) desc")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            i = 3
            for d in res:
                print("Test type:%s Number of tests:%s" % (d[0], d[1]))
                i -= 1
                if i < 1:
                    break
        print("\n")
        mycursor.execute("Select city from Lab where labid="+str(id))
        city=mycursor.fetchall()[0][0]

        mycursor.execute("Select Test.Tests,count(*) from Test,Lab where Lab.labid=Test.labid and Lab.city=\""+city+"\" group by  tests order by count(*) desc")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            print("Most Popular tests in " + city + ":")
            i = 3
            for d in res:
                print("Test type:%s Number of tests:%s" % (d[0], d[1]))
                i -= 1
                if i < 1:
                    break
    if ch==7:
        mycursor.execute(
            "SELECT LabID, count(*) FROM Test GROUP BY labid order by count(*) desc")
        res = mycursor.fetchall()
        su=0
        loc=-1
        i=0

        for d in res:
            if d[0]==id:
                loc=i
            i+=1
            su+=d[1]
        # print(loc)
        if loc>5:
            labels = res[loc][0],res[0][0],res[1][0],res[2][0],res[3][0],'others'
            sizes = [res[loc][1], res[0][1], res[1][1], res[2][1],res[3][1],su-res[loc][1]-res[0][1]-res[1][1]-res[2][1]-res[3][1]]
            colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red','purple']
            explode = (0.1, 0, 0, 0,0,0)  # explode 1st slice
        else:
            labels = res[0][0], res[1][0], res[2][0], res[3][0],res[4][0], 'others'
            sizes =  [res[0][1], res[1][1], res[2][1], res[3][1],res[4][1],su - res[0][1] - res[1][1] - res[2][1] - res[3][1]-res[4][1]]
            colors = ['gold','yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'purple']
            explode=()
            for i in range(6):
                if i==loc:
                    explode=explode+(0.1,)
                else:
                    explode=explode+(0,)
            # print(explode)

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show(block=False)

    if ch==8:
        mycursor.execute(
            "SELECT Tests,count(*) FROM Test where labid="+str(id)+"  group by Tests order by count(*) desc")
        res = mycursor.fetchall()
        if len(res)==0:
            dr=-1
        else:
            dr=res[0][0]
        # print(dr)
        mycursor.execute("SELECT Tests,count(*) FROM Test  group by Tests order by count(*) desc")
        res = mycursor.fetchall()
        # print(res)
        # print(res)
        su = 0
        loc = 0
        i = 0
        for d in res:
            if d[0] == dr:
                loc = i
            i += 1
            su += d[1]
        if loc > 5:
            labels = res[loc][0], res[0][0], res[1][0], res[2][0], res[3][0], 'others'
            sizes = [res[loc][1], res[0][1], res[1][1], res[2][1], res[3][1],
                     su - res[loc][1] - res[0][1] - res[1][1] - res[2][1] - res[3][1]]
            colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'purple']
            explode = (0.1, 0, 0, 0, 0, 0)  # explode 1st slice
        else:
            labels = res[0][0], res[1][0], res[2][0], res[3][0], res[4][0], 'others'
            sizes = [res[0][1], res[1][1], res[2][1], res[3][1], res[4][1],
                     su - res[0][1] - res[1][1] - res[2][1] - res[3][1] - res[4][1]]
            colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'purple']
            explode = ()
            for i in range(6):
                if i == loc:
                    explode = explode + (0.1,)
                else:
                    explode = explode + (0,)

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show(block=False)

    if ch==9:
        mycursor.execute("select tdate,count(*) from Test where labid="+str(id)+" group by tdate order by tdate asc")
        res=mycursor.fetchall()

        objects = ()
        for d in res:
            objects+=(d[0],)
        y_pos = np.arange(len(objects))
        counts = []
        for d in res:
            counts.append(d[1])


        plt.bar(y_pos, counts, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('No. of tests')
        plt.title('Tests on some date')
        plt.show(block=False)

    if ch == 0:
        MainScreen()
        return
    print("\n\n")
    labquery(id)

def daquery(id):
    id = int(id)
    mycursor = mydb.cursor()
    print("Select Query:")
    print("1:Upcoming deliveries:")
    print("2:Update delivery status:")
    print("3:Competitive DeliveryAgency in some delivery city:")
    print("4:Delivery Details:")
    print("5:Reviews of Deliveries:")
    print("6:Most popular delivery areas(BONUS):")
    print("7:DeliveryAgency Market-Share PIE-CHART (BONUS)")
    print("8:DeliveryArea Market-Share PIE-CHART (BONUS)")
    print("9:Deliveries vs date BAR-CHART (BONUS)")
    print("0:MainScreen")
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
            "SELECT Delivery.daid,DAname,avg(DeliveryReviews.rating) FROM Orderr,Delivery,DeliveryAgency,DeliveryReviews WHERE Orderr.OID=Delivery.OID and Delivery.DaID=DeliveryAgency.DaID AND Delivery.DeID=DeliveryReviews.DeID and Orderr.city=\""+city+"\" group by delivery.DAID;")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("DeliveryAgency ID:%s Name:%s  Rating:%s " % (d[0], d[1], round(d[2], 2)))

    if ch==4:
        print("Input DeliveryID")
        deid=int(input())
        mycursor.execute("select deid,Orderr.streetadress,Orderr.city,phone,destatus,eta,daid from Orderr,delivery,Userr where Userr.uid=Orderr.uid and Orderr.oid=delivery.oid and delivery.deid="+str(deid))
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("Delivery ID:%s Address:%s city:%s phone:%s status:%s eta:%s" % (d[0], d[1], d[2], d[3],d[4],d[5]))

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
        mycursor.execute(
            "SELECT Orderr.postalcode,sum(price) FROM Delivery,Orderr WHERE Orderr.OID=Delivery.OID GROUP BY Orderr.postalcode order by sum(price) desc;")

        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            i=3
            for d in res:
                print("Delivery Area:%s\t Sum of prices of orders:%s" % (d[0], round(d[1],2)))
                i-=1
                if i<1:
                    break
    if ch==7:
        mycursor.execute(
            "SELECT delivery.daid,sum(Orderr.price) FROM delivery,Orderr where Orderr.oid=delivery.oid GROUP BY daid order by count(*) desc")
        res = mycursor.fetchall()
        su=0
        loc=-1
        i=0

        for d in res:
            if d[0]==id:
                loc=i
            i+=1
            su+=d[1]
        # print(loc)
        if loc>5:
            labels = res[loc][0],res[0][0],res[1][0],res[2][0],res[3][0],'others'
            sizes = [res[loc][1], res[0][1], res[1][1], res[2][1],res[3][1],su-res[loc][1]-res[0][1]-res[1][1]-res[2][1]-res[3][1]]
            colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red','purple']
            explode = (0.1, 0, 0, 0,0,0)  # explode 1st slice
        else:
            labels = res[0][0], res[1][0], res[2][0], res[3][0],res[4][0], 'others'
            sizes =  [res[0][1], res[1][1], res[2][1], res[3][1],res[4][1],su - res[0][1] - res[1][1] - res[2][1] - res[3][1]-res[4][1]]
            colors = ['gold','yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'purple']
            explode=()
            for i in range(6):
                if i==loc:
                    explode=explode+(0.1,)
                else:
                    explode=explode+(0,)
            # print(explode)

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show(block=False)

    if ch==8:
        mycursor.execute(
            "SELECT postalcode,sum(Orderr.price) FROM delivery,Orderr where Orderr.oid=delivery.oid and daid="+str(id)+"  group by postalcode order by sum(price) desc")
        res = mycursor.fetchall()
        if len(res)==0:
            dr=-1
        else:
            dr=res[0][0]
        # print(dr)
        mycursor.execute("SELECT postalcode,sum(Orderr.price) FROM delivery,Orderr where Orderr.oid=delivery.oid group by postalcode order by sum(price) desc")
        res = mycursor.fetchall()
        # print(res)
        # print(res)
        su = 0
        loc = 0
        i = 0
        for d in res:
            if d[0] == dr:
                loc = i
            i += 1
            su += d[1]
        if loc > 5:
            labels = res[loc][0], res[0][0], res[1][0], res[2][0], res[3][0], 'others'
            sizes = [res[loc][1], res[0][1], res[1][1], res[2][1], res[3][1],
                     su - res[loc][1] - res[0][1] - res[1][1] - res[2][1] - res[3][1]]
            colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'purple']
            explode = (0.1, 0, 0, 0, 0, 0)  # explode 1st slice
        else:
            labels = res[0][0], res[1][0], res[2][0], res[3][0], res[4][0], 'others'
            sizes = [res[0][1], res[1][1], res[2][1], res[3][1], res[4][1],
                     su - res[0][1] - res[1][1] - res[2][1] - res[3][1] - res[4][1]]
            colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'purple']
            explode = ()
            for i in range(6):
                if i == loc:
                    explode = explode + (0.1,)
                else:
                    explode = explode + (0,)

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show(block=False)

    if ch==9:
        mycursor.execute("select eta,count(*) from delivery where daid="+str(id)+" group by eta order by eta asc")
        res=mycursor.fetchall()

        objects = ()
        for d in res:
            objects+=(d[0],)
        y_pos = np.arange(len(objects))
        counts = []
        for d in res:
            counts.append(d[1])


        plt.bar(y_pos, counts, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('No. of deliveries')
        plt.title('Deliveries on some date')
        plt.show(block=False)

    if ch == 0:
        MainScreen()
        return
    print("\n\n")
    daquery(id)

def retquery(id):
    id = int(id)
    mycursor = mydb.cursor()
    print("Select Query:")
    print("1:Are we getting better prices for medicines from the online store?:")
    print("2:Count the orders placed by that retailer:")
    print("3:Which drugs are in high demand?:")
    print("4:Better alternatives to a drug :")
    print("5:Reviews of drugs they are selling have satisfactory results:")
    print("6:Alternative drugs based on order history (BONUS)")
    print("7:Orders vs Date BAR-CHART(BONUS)")
    print("0:MainScreen")
    ch=int(input())
    if ch==1:
        print("Input Drug Name:")
        drug = input()
        mycursor.execute("SELECT DrID,DrName,Price FROM Drug WHERE DRName=\"" + drug + "\";")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Price:%s" % (d[0], d[1], d[2]))
    if ch==2:
        mycursor.execute(
            "SELECT OID,Drug.DrID,Drname,symptoms,sickness,Orderr.price/Drug.price FROM Drug,Orderr WHERE Drug.DrID=Orderr.DrID and UID="+str(id))
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("Order ID:%s DrID:%s Drug:%s Symptoms%s Sickness%s Quantity ordered:%d" % (d[0], d[1], d[2], d[3], d[4], int(d[5])))

    if ch==3:
        mycursor.execute(
            "SELECT Drug.DrID,Drname,symptoms,sickness,sum(Orderr.price/Drug.price) FROM Drug,Orderr WHERE Drug.DrID=Orderr.DrID group by Drug.drid order by sum(Orderr.price/Drug.price) desc")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:

            i = 3
            for d in res:
                print("DrID:%s Drug:%s Symptoms%s Sickness%s Quantity ordered:%d" % (d[0],d[1],d[2],d[3], int(d[4])))
                i -= 1
                if i < 1:
                    break

    if ch==4:
        print("Input symptoms:")
        symp = input()
        print("Input Sickness")
        sickness = input()
        mycursor.execute(
            "SELECT Drug.drID,Drug.drname,sickness,symptoms,avg(DrugReviews.rating),Drug.price from Drug,Orderr,DrugReviews where DrugReviews.OID = Orderr.OID AND Drug.DrID=Orderr.DrID   AND ( Drug.symptoms LIKE '%" + symp + "%' OR Drug.sickness LIKE '%" + sickness + "%') group by Drug.drid")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            for d in res:
                print("ID:%s Name:%s Sickness: %s symptoms: %s Rating:%5s Price:%s" % (
                d[0], d[1], d[2], d[3], round(d[4], 2), d[5]))
            dridpr = set()
            for d in res:
                dridpr.add(d[0])
            mycursor.execute(
                "SELECT Drug.drID,Drug.drname,sickness,symptoms,Drug.price from Drug where ( Drug.symptoms LIKE '%" + symp + "%' OR Drug.sickness LIKE '%" + sickness + "%')")
            res = mycursor.fetchall()
            for d in res:
                if d[0] not in dridpr:
                    print("ID:%s Name:%s Sickness: %s symptoms: %s Price:%s" % (d[0], d[1], d[2], d[3], d[4]))
    if ch==5:
        print("Input Drug ID:")
        drugid = input()
        if ch == 5:
            mycursor.execute(
                "SELECT Drug.DrID,DrName,Avg(DrugReviews.rating) FROM Drug,Orderr,DrugReviews WHERE Drug.DrID=Orderr.DrID AND Orderr.OID = DrugReviews.OID AND Drug.drid="+str(drugid)+ " group by Drug.drid")
            res = mycursor.fetchall()
            if len(res) == 0:
                print("No results.")
            else:
                for d in res:
                    print("DrugID:%s Name:%s Rating:%5s" % (d[0],d[1], round(d[2], 2)))

    if ch==6:
        mycursor.execute("SELECT symptoms,sickness from Orderr,Drug where uid="+str(id)+" and Drug.drid=Orderr.drid group by Drug.drid order by sum(Orderr.price/Drug.price) desc;")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("No results.")
        else:
            symp = res[0][0]
            sickness = res[0][1]
            mycursor.execute(
                "SELECT Drug.drID,Drug.drname,sickness,symptoms,avg(Drugreviews.rating),Drug.price from Drug,Orderr,DrugReviews where DrugReviews.OID = Orderr.OID AND Drug.DrID=Orderr.DrID   AND ( Drug.symptoms LIKE '%" + symp + "%' OR Drug.sickness LIKE '%" + sickness + "%') group by Drug.drid")
            res = mycursor.fetchall()

            for d in res:
                print("ID:%s Name:%s Sickness: %s symptoms: %s Rating:%5s Price:%s" % (d[0], d[1],d[2],d[3], round(d[4], 2), d[5]))
            dridpr=set()
            for d in res:
                dridpr.add(d[0])
            mycursor.execute(
                "SELECT Drug.drID,Drug.drname,sickness,symptoms,Drug.price from Drug where ( Drug.symptoms LIKE '%" + symp + "%' OR Drug.sickness LIKE '%" + sickness + "%')")
            res = mycursor.fetchall()
            for d in res:
                if d[0] not in dridpr:
                    print("ID:%s Name:%s Sickness: %s symptoms: %s Price:%s" % (d[0], d[1],d[2],d[3],  d[4]))

    if ch==7:
        mycursor.execute("select odate,count(*) from Orderr where uid="+str(id)+" group by odate order by odate asc")
        res=mycursor.fetchall()

        objects = ()
        for d in res:
            objects+=(d[0],)
        y_pos = np.arange(len(objects))
        counts = []
        for d in res:
            counts.append(d[1])


        plt.bar(y_pos, counts, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('No. of orders')
        plt.title('Orders on some date')
        plt.show(block=False)

    if ch==0:
        MainScreen()
        return
    print("\n\n")
    retquery(id)

MainScreen()