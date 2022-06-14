import base64
import datetime
from gpiozero import Button
from github import Github
from github import InputGitTreeElement




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


class gitHub:
    def __init__(self):
        user = "GithubUsername"
        password = "*********"
        g = Github(user, password)
        repo = g.get_user().get_repo('git-test')  # repo name
        file_list = [
            'C:\\Users\jesse\Dropbox\Swell-Forecast\git-test\index.html',
            'C:\\Users\jesse\Dropbox\Swell-Forecast\git-test\margin_table.html'
        ]
        file_names = [
            'index.html',
            'margin_table.html'
        ]
        commit_message = 'python commit'
        master_ref = repo.get_git_ref('heads/master')
        master_sha = master_ref.object.sha
        base_tree = repo.get_git_tree(master_sha)

        element_list = list()
        for i, entry in enumerate(file_list):
            with open(entry) as input_file:
                data = input_file.read()
            if entry.endswith('.png'):  # images must be encoded
                data = base64.b64encode(data)
            element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
            element_list.append(element)

        tree = repo.create_git_tree(element_list, base_tree)
        parent = repo.get_git_commit(master_sha)
        commit = repo.create_git_commit(commit_message, tree, [parent])
        master_ref.edit(commit.sha)


def main():
    while(True):
        schoolName=school()
        reasonVisit=reason(schoolName)
        ct = datetime.datetime.now()

if __name__ == "__main__":
    main()




