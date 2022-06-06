# Production Engineering - Week 1 - Portfolio Site

A portfolio website for the week 1 hackathon of the Production Engineering Track. This project was developed with Flask, HTML/CSS, JavaScript. This project was developed by Tanzir Hasan, Ryson Wang, Krish Thawni

## Components of the Website

### Landing Page

Here is the landing page:

![Landing Page](https://github.com/MLH-Fellowship/project-gigachad-giraffes/blob/main/READMEimg/LandingPage.png)

A tagline, name, and photo can be placed at the top. An about me section, a skills section, an education section, and an experience section are below. Jinja templating can be used to add additional elements in the skills, education, and experience section.

![Jinja Templating](https://github.com/MLH-Fellowship/project-gigachad-giraffes/blob/main/READMEimg/JinjaFormatted.png)

<br>

### Hobbies

Here is the hobbies page. 

![Hobbies Page](https://github.com/MLH-Fellowship/project-gigachad-giraffes/blob/main/READMEimg/Hobbies.png)

There is a carousel that is jinja templated and can be used to add an infinite number of hobbies.

<br>

### Project

Here is the projects page.

![Project Page](https://github.com/MLH-Fellowship/project-gigachad-giraffes/blob/main/READMEimg/Projects.png)

A grid of projects will be displayed. This grid is jinja templated and additional projects can be added infinitely.

A map of all the places you've been are at the bottom and can be modified by changing visited.csv.

![Map](https://github.com/MLH-Fellowship/project-gigachad-giraffes/blob/main/READMEimg/Map.png)

<br>

## Tasks

In the hackathon the following tasks were completed:

### GitHub Tasks
- [x] Create Issues for each task below
- [x] Work on each task in a new branch
- [x] Open a Pull Request when a task is finished to get feedback

### Portfolio Tasks
- [x] Add a photo of yourself to the website
- [x] Add an "About youself" section to the website.
- [x] Add your previous work experiences
- [x] Add your hobbies (including images)
- [x] Add your current/previous education
- [x] Add a map of all the cool locations/countries you visited

### Flask Tasks
- [x] Get your Flask app running locally on your machine using the instructions below.
- [x] Add a template for adding multiple work experiences/education/hobbies using [Jinja](https://jinja.palletsprojects.com/en/3.0.x/api/#basics)
- [x] Create a new page to display hobbies.
- [x] Add a menu bar that dynamically displays other pages in the app


## Installation

Install all dependencies with Python and pip:

```bash
pip install -r requirements.txt
```

## Running

Start flask development server to run this project
```bash
$ export FLASK_ENV=development
$ flask run
```

Access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

