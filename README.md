# Automated User Tracker

The goal of his project was to create an easy way for the University of Denver's Makerspace to track how many 
users are coming into the space. 

The project collects three important pieces of data:
* Time and date
* Which DU school they are associated with 
* What is their reason of visit

## Data
Collecting data is important because it will allow us to identify and analyze trends and 

### Time/Date: 
Gathering time will allow us to understand when students are using the space which will allow us to better schedule employees
to meet the demand.

### School:
Knowing what background students are coming from is important. Our makerspace is open to everyone on campus so being able to 
adjust things in the space such as teaching styles to give students a better experience.

### Reason:
Knowing which equipment is being utilized will allow us to know which equipment to upgrade and expand.We will also be able
to analyze which workshops are popular and increase their frequency if needed.

## Design
Our design choice was a simple box with two sets of buttons for the different school's on campus and the reason of visit.
The reason for this choice was in the past when we had complex sign-in methods such as a form that required a lot of 
fields to fill in it was difficult to get students to sign in. Our goal with the design was to keep it simple.

![Front](https://github.com/Jarob-H/userAutomation/blob/master/Project%20Pictures/IMG_3762.jpg)

The Raspberry Pi had a custom spot inside the box that allowed the box to be plugged into power and perpials without the
need to take apart the box.

![Back](https://github.com/Jarob-H/userAutomation/blob/master/Project%20Pictures/IMG_3764.jpg)

On The inside the PI sits in the corner. 

![Inside](https://github.com/Jarob-H/userAutomation/blob/master/Project%20Pictures/IMG_3765.jpg)

## Fabrication

To create the box we turned the STl/3MF file from Solidworks into a file type that could easily be Laser engraved. We 
then laser cut the box completely out of one sheet of wood. 

## Future Work
Our error handling and verification is not perfect and should be improved on. Currently, our program forces the user to 
sequentially put in a school and then a reason. This does stop someone from macilisly spamming the buttons, however does 
not verify that each input is indeed a unique user. 

To combat this in the future I would also like to implement an RFID scanner that checks a user ID. If a person tries then 
to spam a button the program can then throw out duplicates.

By implementing an ID system we also open up the possibility of creating a system that remembers a user and then that user 
does not need to press the buttons each time. Using an ID system however creates new challenges such as the proper storage 
of user data.

We would also like to add a green and red LED so users are able to tell if their entry was successful.

## Collaborators

| Username   |Contribution|Linkedin ![img.png](https://img.icons8.com/color/40/linkedin.png)|Github Link ↘️|
|------------|---|------|---------------------------|
|Jarob Heffner|Code Development|www.linkedin.com/in/jarob-heffner-85a880142/|www.github.com/Jarob-H|
|Ryan Farrell|CAD and Electrical Design|https://www.linkedin.com/in/ryan-farrell-/|https://github.com/ryanfarrell987|
|Corey Valenti|Code Development|www.linkedin.com/in/corey-valenti-1aba79193//|www.github.com/CoreyValenti|
