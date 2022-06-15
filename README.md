# Automated User Tracker

The goal of his project was to create an easy way for the University of Denver's Makerspace to track how many 
users are coming into the space. 

The project collects three important pieces of data:
* Time and date
* Which DU school they are associated with 
* What is their reason of visit

This data is important because it will us understand things such as what time and day of the week the space is most utilize.
We may also be able to analyze and predict traffic trends around things such as projects and finals. 

Knowing what background students are coming from is important. Our makerspace is open to everyone on campus so being able to 
adjust things in the space such as teaching styles to give students a better experience.

![Front](https://github.com/Jarob-H/userAutomation/blob/master/Project%20Pictures/IMG_3762.jpg)
![Back](https://github.com/Jarob-H/userAutomation/blob/master/Project%20Pictures/IMG_3764.jpg)
![Inside](https://github.com/Jarob-H/userAutomation/blob/master/Project%20Pictures/IMG_3765.jpg)
## Future Work

Our error handling and verification is not perfect and should be improved on. Currently, our program forces the user to 
sequentially put in a school and then a reason. This does stop someone from macilisly spamming the buttons, however does 
not verify that each input is indeed an unique user. 

To combat this in the future I would also like to implement an RFID scanner that checks an user ID. If a person tries then 
to spam a button the program can then throw out duplicates.

By implementing an ID system we also open up the possibility of creating a system that remembers a user and then that user 
does not need to press the buttons each time. Using an ID system however creates new challenges such as the proper storage 
of user data. 

## Collaborators

| Username   |Contribution|Linkedin|Github Link ↘️                |
|------------|---|------|---------------------------|
|Jarob Heffner|Code|www.linkedin.com/in/jarob-heffner-85a880142/|www.github.com/Jarob-H|
|Corey Valenti|UI Development|www.linkedin.com/in/corey-valenti-1aba79193//|www.github.com/CoreyValenti|
