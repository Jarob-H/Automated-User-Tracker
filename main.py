import base64
import json
import requests
from gpiozero import Button
import csv
from datetime import datetime
import time


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

def reason():
    reason = ""
    t_end = time.time() + 3#loop will run for 3 seconds
    while time.time() < t_end:
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
    else:
        reason="Other"
    return reason

def spreadSheet(schoolName, reasonVisit):
    with open('users.csv', mode='a') as user:
        user_writer = csv.writer(user, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        user_writer.writerow([datetime.now().strftime("%m-%d-%Y"),datetime.now().strftime("%H:%M"),schoolName,reasonVisit])


def push_to_github():
    token = "enter token here"#do not upload with actual key
    filename = "users.csv"#we only want to push the csv
    repo = "Jarob-H/userAutomation"#repo we are pushing to
    branch = "master"#branch we are pushing to

    url="https://api.github.com/repos/"+repo+"/contents/"+filename

    base64content=base64.b64encode(open(filename,"rb").read())

    data = requests.get(url+'?ref='+branch, headers = {"Authorization": "token "+token}).json()
    sha = data['sha']

    if base64content.decode('utf-8')+"\n" != data['content']:
        message = json.dumps({"message":"update",
                            "branch": branch,
                            "content": base64content.decode("utf-8") ,
                            "sha": sha
                            })

        resp=requests.put(url, data = message, headers = {"Content-Type": "application/json", "Authorization": "token "+token})

        print(resp)
    else:
        print("nothing to update")

def main():
    while True:
        spreadSheet(school(),reason())
        push_to_github()

if __name__ == "__main__":
    main()



