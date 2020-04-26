import matplotlib.pyplot as plt
import numpy as np
import django
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse
def usquery_2(mycursor,drug):

    output = []
    mycursor.execute(
        "SELECT Drug.DrID,Drug.Drname, AVG(DrugReviews.rating) FROM Drug,DrugReviews,Orderr WHERE DrugReviews.OID=Orderr.OID AND Orderr.DrID=Drug.DrID AND Drug.Drname=\"" + drug + "\" group by Drug.DRID")
    res = mycursor.fetchall()
    if len(res) == 0:
        print("No results.")
    else:
        for d in res:
            output.append("ID:%s Name:%s Rating:%5s" % (d[0], d[1], round(d[2], 2)))
            print("ID:%s Name:%s Rating:%5s" % (d[0], d[1], round(d[2], 2)))
    return output
def usquery_4(mycursor,drug):
    output = []
    mycursor.execute("SELECT DrID,DrName,Quantity FROM Drug WHERE DRName=\"" + drug + "\";")
    res = mycursor.fetchall()
    if len(res) == 0:
        print("No results.")
    else:
        for d in res:
            output.append("ID:%s Name:%s Quantity:%s" % (d[0], d[1], d[2]))
            print("ID:%s Name:%s Quantity:%s" % (d[0], d[1], d[2]))
    return output
def usquery_5(mycursor,drug):
    output=[]
    mycursor.execute("SELECT DrID,DrName,Price FROM Drug WHERE DRName=\"" + drug + "\";")
    res = mycursor.fetchall()
    if len(res) == 0:
        print("No results.")
    else:
        for d in res:
            output.append("ID:%s Name:%s Price:%s" % (d[0], d[1], d[2]))
            print("ID:%s Name:%s Price:%s" % (d[0], d[1], d[2]))

    return output
def usquery_3(mycursor,symp,sickness ):
    output=[]
    mycursor.execute(
        "SELECT Drug.drID,Drug.drname,sickness,symptoms,avg(DrugReviews.Rating),Drug.price from Drug,Orderr,DrugReviews where DrugReviews.OID = Orderr.OID AND Drug.DrID=Orderr.DrID   AND ( Drug.symptoms LIKE '%" + symp + "%' OR Drug.sickness LIKE '%" + sickness + "%') group by Drug.drid")
    res = mycursor.fetchall()
    if len(res) == 0:
        output.append("No results.")
        print("No results.")
    else:
        for d in res:
            output.append("ID:%s Name:%s Sickness: %s symptoms: %s Rating:%5s Price:%s" % (
            d[0], d[1], d[2], d[3], round(d[4], 2), d[5]))
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
                output.append("ID:%s Name:%s Sickness: %s symptoms: %s Price:%s" % (d[0], d[1], d[2], d[3], d[4]))
                print("ID:%s Name:%s Sickness: %s symptoms: %s Price:%s" % (d[0], d[1], d[2], d[3], d[4]))
    return output

def usquery_1(mycursor, id):
    output=[]
    mycursor.execute("Select city from Userr where UID=" + str(id))
    city = mycursor.fetchall()[0][0]
    print(city)
    mycursor.execute(
        "SELECT Doctor.DID, Doctor.dname, Doctor.Phone, Qualifications, specialization, AVG(DoctorReviews.Rating),Doctor.StreetAdress FROM Doctor,DoctorReviews,Appointment,OpenSlots WHERE Doctor.DID=OpenSlots.DID and OpenSlots.SID=Appointment.SID and Appointment.AID=DoctorReviews.AID AND Doctor.city=\"" + city + "\" group by Doctor.did")
    res = mycursor.fetchall()
    if len(res) == 0:
        output.append("No results.")
        print("No results.")
    else:
        for d in res:
            output.append("ID:%s Name:%s Phone:%5s Qualifications:%s Speciality:%s Rating:%5s, Address:%5s" % (
            d[0], d[1], d[2], d[3], d[4], round(d[5], 2), d[6] + " " + city))
            print("ID:%s Name:%s Phone:%5s Qualifications:%s Speciality:%s Rating:%5s, Address:%5s" % (
            d[0], d[1], d[2], d[3], d[4], round(d[5], 2), d[6] + " " + city))

    return output


def usquery_7(mycursor,id):
    mycursor.execute("select odate,count(*) from Orderr where uid=" + str(id) + " group by odate order by odate asc")
    res = mycursor.fetchall()

    objects = ()
    for d in res:
        objects += (d[0],)
    y_pos = np.arange(len(objects))
    counts = []
    for d in res:
        counts.append(d[1])

    plt.bar(y_pos, counts, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('No. of orders')
    plt.title('Orders on some date')
    plt.show(block=False)

    canvas = FigureCanvas(plt)
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response