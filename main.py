import base64
from gpiozero import Button
from github import Github
from github import InputGitTreeElement
import csv
import datetime

#Create Buttons with corresponding GPIO Pins
##############
##  School  ##
##############
ECS = Button(6)
Daniels = Button(26)
JK = Button(19)
Grad = Button(4)
Arts = Button(16)
Natural = Button(27)

##################
##    Reason    ##
##################
Study = Button(17)
Other = Button(22)
Project = Button(21)
Laser = Button(20)
Print = Button(13)
Workshop = Button(5)

def school():
    schoolName = ""
    while True:
        if ECS.is_pressed:
            schoolName = "ECS"
            break
        elif Daniels.is_pressed:
            schoolName = "Daniels"
            break
        elif JK.is_pressed:
            schoolName = "Joseph Kerbel"
            break
        elif Grad.is_pressed:
            schoolName = "Grad"
            break
        elif Arts.is_pressed:
            schoolName = "Arts/Humanities"
            break
        elif Natural.is_pressed:
            schoolName = "Natural Sci/Math"
            break
    return schoolName

def reason(schoolName):
    reason = ""
    while True:
        if Study.is_pressed:
            reason = "Study"
            break
        elif Other.is_pressed:
            reason = "Other"
            break
        elif Project.is_pressed:
            reason = "Project"
            break
        elif Laser.is_pressed:
            reason = "Laser"
            break
        elif Print.is_pressed:
            reason = "Print"
            break
        elif Workshop.is_pressed:
            reason = "Workshop"
            break
    return reason

def spreadSheet(schoolName, reasonVisit):
    with open('users.csv', mode='a') as user:
        user_writer = csv.writer(user, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        user_writer.writerow([datetime.datetime.now(),schoolName,reasonVisit])


def main():
    spreadSheet('ecs','printing')

if __name__ == "__main__":
    main()




