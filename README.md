# Follower_checker

Follower checker is an application that enables the automatic collection and comparison of the list of followers and users who are being followed. 

Project Purpose and Goal
The application was created to simplify the comparison of the follower list and the following list.
Using the application is designed to be simple and user-friendly.

The technology used and Explanation

The design of the application was done in Figma. The UI was built using Tkinter.
And automatic work is achieved thanks to the Selenium library and the Python programming language.

After starting the application, it is necessary to enter the username, password and start the check by pressing the button.
Using a browser, the application logs in to the profile and collects the necessary lists. After that, compares the lists, and using the Pandas library, writes followings who did not follow back into the Excel table and save that file.

Problems and Thought Process

The biggest problem of the application is the frequent change of HTML tags on the website, which Selenium uses for targeting.
This problem can be solved by periodically updating the application.

In order to use the Follower_checker, it is necessary that "chromedriver" is in the same directory as main.py.
