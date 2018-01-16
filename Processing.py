from uobitems import uobitems
from allredemption import allredemption

def processallitems():
    allitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        individual_items = a.split(",")
        if (individual_items[0] == "Leisure"):
            b = uobitems(individual_items[1], individual_items[2], individual_items[3],
                         individual_items[4],individual_items[5],individual_items[6])
            allitems.append(b)
    return allitems

def processretailitems():
    retailitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point=[]
        for pts in avaliableuobpts_file:
            point.append(int(pts))
        points= point[-1]
        individual_items = a.split(",")
        if (individual_items[0] == "Retail"):
            if (points >= int(individual_items[3])):
                c = uobitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6])
                retailitems.append(c)
    return retailitems

def processdiningitems():
    diningitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point = []
        for pts in avaliableuobpts_file:
            point.append(int(pts))
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[0] == "Dining"):
            if (points >= int(individual_items[3])):
                d = uobitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6])
                diningitems.append(d)
    return diningitems


def processleisureitems():
    leisureitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point = []
        for pts in avaliableuobpts_file:
            point.append(int(pts))
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[0] == "Leisure"):
            if (points >= int(individual_items[3])):
                e = uobitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6])
                leisureitems.append(e)
    return leisureitems



def processpoints():
    uob_allpoints =[]
    uob_currentpts =[]
    avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
    for j in avaliableuobpts_file:
        uob_allpoints.append(int(j))
    uobcurrentpts =  uob_allpoints[-1]
    uob_currentpts.append(uobcurrentpts)
    return uob_currentpts





def processallredemption():
    allredemptionList =[]
    allnovredemption=[]
    allredemption_file = open("file/allredemption.txt", "r")
    for i in  allredemption_file:
        list = i.split(',')
        s = allredemption(list[0], list[1], list[2], list[3], int(list[4]),list[5], list[6])

        allredemptionList.append(s)
    return allredemptionList
