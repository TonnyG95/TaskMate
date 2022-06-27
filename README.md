# TaskMate
![taskm8](https://user-images.githubusercontent.com/47572512/174821264-173b3e05-5664-4f6b-98c9-45585cd85bff.png)


![Screenshot_2_yctk2z](https://user-images.githubusercontent.com/47572512/174827801-8d72e86b-fd8d-405b-9821-5e1394dfebe3.png)

A deployed website can be found [Here](https://ci-task-mate.herokuapp.com/).

# Table of contents

1. [Introduction](#introduction)
    - [What is TaskMate](#what-is-taskmate)
    - [Idea behind project](#what-is-the-idea-behind-this-project)
    - [Technologies](#technologies)
2. [Features](#features)
    - [Included Features](#included-features)
    - [Future Implementations](#future-implementations)
3. [UI | UX](#ui--ux)
    - [UI](#ui)
    - [UX](#ux)
4. [Testing](#testing)
    - [User Story](#user-stories-1)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#automated-testing)
    - [User Testing](#user-testing)
5. [Deployment](#deployment)
    - [Heroku Deployment](#deployment)
    - [Froking](#forking-the-repository)
    - [Cloning](#creating-a-clone)
6. [Credits](#credits)
    -[Links](#links)
    - [Acknowledgements](#acknowledgements)
    


# Introduction

### What is TaskMate?

TaskMate is a free, simple yet powerful task manager app. Add your tasks, edit them, mark them as complete etc. Create your account and keep track of your task with TaskMate!

### What is the idea behind this project?
The plan with TaskMate was to create a simple,user-intuitive to-do app that is not overwhelmed, users. An excellent choice for people who want to log in to the website, add their tasks, and continue their day.


# Technologies 

### FrontEnd

- HTML (build up layout and content of the application.)
- CSS (custom styling and override Bootstrap stylings to fit with the theme of the app.)
- JavaScript (interactive functionalities of the app.)
- Bootstrap 5 (the responsive front-end framework to build the layout and style the app.)

### BackEnd

- Python (backend functionalities handling data, database interaction, and CRUD functionalities.)
- Django (the core framework used to build this app.)

### Requirements

- Asgiref
- Cloudinary
- Cloudinary
- Crispy Forms
- Gunicorn
- Psycopg
- Pytz
- Sqlparse
- Whitenoise


# Features

### Included Features

- Fully Responsive
- Simple UI
- Dark Mode
- Full CRUD Functionality 
- Login and Registration 
- Newsletter subscription powered by MailChimp


### Future Implementations

This project will keep receiving security and features updates. It will be in active development. The project's current state has all the basic functionalities needed for a user to track tasks. The site owner also has access to all the data through Django's default admin panel. The next phase will be adding more features to the site, enhancing user experience and control over the app. The following features are planned to be implemented:

- A better-designed admin dashboard for a site owner to manage the app and its data
- Contact form
- Help desk (zendesk type app)
- React version


# UI | UX 

## UI

The app is designed with Figma. The project can be found [Here](https://www.figma.com/file/3oRURKIFMvnJUpAbefiM0H/Untitled?node-id=0%3A1).

![Screenshot_6](https://user-images.githubusercontent.com/47572512/174840281-a61b415e-6d63-4214-af44-5899a3bc2760.png)


#### Assets

Header and Footer color: #212529\
Logo: #00a9ec\
Font: Robboto

![colors](https://user-images.githubusercontent.com/47572512/174842767-fa16dcf7-678b-4448-a393-3b289d39e9e2.png)


## UX 

### User Stories

- As a site user, I want to create an account to manage my task.
- As a Site User, I can view a list of tasks so I can organize myself
- As a Site User, I can add a new task to my list
- As a site user, I can create, read, update and delete tasks so that I can manage my tasks
- As a Site User, I can mark tasks as important, so I know what to prioritize
- As a Site User, I can mark tasks as done, so I know that I'm done with the task
- As a site admin, I want to be able to see my registered users
- As a site admin, I want to be able to manage tasks and users.

### Structure

The main goal of this project is to help users organize a day, and it is important to keep it as simple as possible so users can easily navigate without much trouble. Therefore the information architecture of this site is straightforward: a landing page where users get information about the service, a registration page where users can create an account, login page where users can log in and start adding tasks. 

# Testing

## Testing User Stories

### User Stories 

1. As a site User, I was able to create my account. 
    - by clicking on registration I was prompted to fill out a username, e-mail and password fields after I fill out the required information my account was created.    
2. As a Site User, I was able to access my task list.
    - While logged in in i can access tasks page where i can see my tasks.
3. As a Site User, I was able to add a new task to my list.
    - While logged in i was able to add new task to list and mark it as important or done on creation.
4. As a site user, I was able create, read, update and delete tasks.
    - While logged in i was able to create my task, edit my task, updated my task and delete my task.
5. As a Site User, I was able to mark tasks as important.
    - While logged in i was able to create my task marked as important, or click edit task and mark it important.
6. As a Site User, I was able change task status to complete.
    - - While logged in i was able to create my task marked as done, or click edit task and mark it done.
7. As a site Admin, I can see list of my registered users.
    - While logged in on admin panel i can see list of my users and i can manage them.
8. As a site Admin, i can manage content on my website.
    - While logged in on admin panel i can see list of tasks, check who is owner of this task and i can manage them.

## Manual Testing

### Common Testing

1. I tested following elements on every page:

- Logo redirection to home page
- Nav links
- Footer links
- Social links opening in new tab


2. I tested login required for tasks,edit and delete views everything worked as intended. 
3. I tested Login and registration pages, everything worked as intended.  
4. I tested that users can only edit and delete their own tasks.
5. I tested that displayed tasks are by logged in user only and that filters works as intended.
6. I test that newsletter works.
7. I tested responsive design and all pages are responsive. 
8. I tested that dark mode is working as intended and that sessions are saved properly. 

### Bugs and solutions

1. I had problem with all bootstrap dropdowns and hamburger menu.
    - The solution was to import bootstrap scrips separately because popper.js was not in a bundle.
2. Checkboxes did not work and task status did not change.
    - The solution was to add code that will make sure that on every redirect checkbox status is set to False and that was added before checkbox function so unless checkbox says differently status is False. 
3. Dark mode did not save sessions properly so on every page mode was reset to day.
    - There was typo in js code i was missing one " ; ".
4. There was a problem with heroku and github.
    - The solution was to redeploy my app and create new postgres database.

## Automated Testing

The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the HTML and CSS code used. [PEP8](http://pep8online.com/) Validator was used to validate the Python code used.  

### Results:

1. HTML Pages - Code Validation
    - No Errors

2. CSS stylesheet - Code Validation
    - No errors

3. JavaScript Testing
    - No errors

3. Python Files - Code Validation
    - No significant errors. \
    Files Tested

     task_mate/settings.py (AUTH_PASSWORD_VALIDATORS line too long) \
     task_mate/urls.py (No errors) \
     todo_app/admin.py (No errors) \
     todo_app/forms.py (No errors) \
     todo_app/models.py (No errors) \
     todo_app/urls.py (No errors) \
     users_app/views.py (No errors) \
     users_app/urls.py (No errors) \
     users_app/forms.py (No errors) 

### Browser Validation
Chrome \
Edge \
Firefox

### Performance and UX

![Screenshot_1](https://user-images.githubusercontent.com/47572512/175964259-38002711-e4b2-4671-bfb0-85b3159f9b06.png) 

Test with [web.dev](https://web.dev/). gave me those results 

![GTMetrix](https://user-images.githubusercontent.com/47572512/175963381-9dfa56be-1f83-45c3-b516-3e47ec126e48.png) 
Test with [GTMetrix](https://gtmetrix.com/). gave me those results 


### User testing
My mom was using TaskMate on daily as shopping list app and everything worked as intended.


# Deployment

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

Create the Heroku App:

Select "Create new app" in Heroku.
Choose a name for your app and select the location.
Attach the Postgres database:

In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
Prepare the environment and settings.py file:

In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
In your GitPod workspace, create an env.py file in the main directory.
Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
Add the SECRET_KEY value to the Config Vars in Heroku.
Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
In settings.py add the following sections:
Cloudinary to the INSTALLED_APPS list
STATICFILE_STORAGE
STATICFILES_DIRS
STATIC_ROOT
MEDIA_URL
DEFAULT_FILE_STORAGE
TEMPLATES_DIR
Update DIRS in TEMPLATES with TEMPLATES_DIR
Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']
Store Static and Media files in Cloudinary and Deploy to Heroku:

Create three directories in the main directory; media, storage and templates.
Create a file named "Procfile" in the main directory and add the following:
web: gunicorn project-name.wsgi
Go to the Deploy tab on Heroku and connect to GitHub, then to the required repository. Click on Deploy Branch and wait for the build to load. When the build is complete, the app can be opened through Heroku and enable automatic deployments.


# Forking the Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

Log into GitHub or create an account.
Locate the GitHub Repository.
At the top of the repository, on the right side of the page, select "Fork"
You should now have a copy of the original repository in your GitHub account.

# Creating a Clone

ow to run this project locally:

Install the GitPod Browser [extension.](https://www.gitpod.io/docs/browser-extension/)
After installation, restart the browser.
Log into GitHub or create an account.
Locate the GitHub Repository.
Click the green "GitPod" button in the top right corner of the repository. This will trigger a new gitPod workspace to be created from the code in github where you can work locally.
How to run this project within a local IDE, such as VSCode:

Log into [GitHub](https://github.com/).
Locate the [GitHub Repository.](https://github.com/TonnyG95/task-mate).
Under the repository name, click "Clone or download".
In the Clone with HTTPs section, copy the clone URL for the repository.
In your local IDE open the terminal.
Change the current working directory to the location where you want the cloned directory to be made.
Type 'git clone', and then paste the URL you copied in Step 3.
git clone https://github.com/USERNAME/REPOSITORY
Press Enter. Your local clone will be created.
Further reading and troubleshooting on cloning a repository from GitHub here

# Credits

### Links

### Acknowledgements