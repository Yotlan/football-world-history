# COMPUTER SCIENCE COURSES

## TABLE OF CONTENTS

## INTRODUCTION

Computer Science is a wonderfull science. Indeed, this science is logical and use algorithm to execute some instruction. The first thing to do is to choose a language to develop some program with it. Bellow, you have a list of most use and popular computer sciences language and their uses :
- Python : Artificial Intelligence and Machine Learning (easy)
- JavaScript : Interaction on Web Development (easy)
- Java : Application Development (intermediate)
- R : Data Analysis (intermediate)
- C : All kind of Development (intermediate to advanced)
- C++ : All kind of Development (easy to intermediate)
- C# : Application and Web Development (intermediate)
- Go : Server-Side Development (easy to intermediate)
- PHP : Web Development (easy)
- SQL : Data Managment (easy)
- Swift : Mobile App Development on iOS (easy)
- Dart : Application Development (easy)
- Kotlin : Mobile App Development on Android OS (easy)
- Perl : Text Development (easy)
- Ruby : Application Development (easy)
- Rust : Application Development (intermediate to advanced)
- Scala : Cloud-Based Application Development (intermediate)

But first of all, it's important to prepare your computer to use language. In each folders bellow, you have a README file associate with an installing part :
- `learn-python/`
- `learn-javascript/`
- `learn-java/`
- `learn-c/`
- `learn-c++/`
- `learn-php/`
- `learn-sql/`

### GIT

Furthermore, a good programmer know essential GIT commands :
- `git clone https://github.com/username/repo.git` : You do it when you want to get a GIT project on your computer
- `git add .` : You do it first to add all modified and/or new files to your next commit
- `git commit -m "Your message"` : You do it after you add all files to present to your GIT project what you want to push
- `git push` : You do it last to push on your GIT project all your files
- `git push https://github.com/your-username/yourrepo.git` : You do it when it's your first push with GIT and when you generate a personnal access token (<https://github.com/settings/tokens>)
- `git pull` : You do it when you want to get the last update of the project
- `git status` : You do it you check if your up to date or no
- `git checkout -b branchname` : You do it when you want to create a new branch on your GIT project
- `git checkout branchname` : You do it when you want to switch on the *branchname* branch of your GIT project
- `git branch` : You do it when you want to list all your GIT project's branch
- `git branch -d branchname` : You do it when you want to delete the *branchname* branch of your GIT project
- `git merge branchname` : You do it when you want to merge the *branchname* branch of your GIT project when your current branch
- `git diff` : You do it when you want to list all conflict you have before merging

To conclude this part, it's important to know the existance of some git file and folder :
- `.git` folder is your GIT project folder. Do not take attention on it.
- `.gitignore` file is what your GIT project ignore when pushing. You add one element per row. Using regular expression is usefull when you want to generalize some ignore files folders

```
#Example of .gitignore file

#Ignore csv file
*.csv

#Ignore D2 folder
/csv/**/D2
```

- `README.md` file is what your GIT projects show when a user is on your GIT project web page

```md
# README EXAMPLE

## TABLE OF CONTENTS

- [MEANING](#meaning)
  * [COURSES](#courses)
  * [PROJECTS](#projects)
- [AUTHORS](#authors)
- [LICENSES](#licenses)
  * [LICENSE OF OUR DATASET](#license-of-our-dataset)
- [SOURCES](#sources)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## MEANING

### COURSES
To see all courses who used this dataset for example, you need to go in this folder :
- `courses/`

### PROJECTS
To see all projects based on this dataset, you need to go in this folder :
- `projects/`

## AUTHORS
- Yotlan LE CROM (<https://github.com/Yotlan>)
- Endy YU (<https://github.com/endyappel>)
- Samuel PENAULT (<https://github.com/Samuel-Penault>)

## LICENSES
- CC BY-NC-SA 4.0 (FBREF from Sports Reference)
- CC BY-SA 3.0 (Wikipedia)
- CC BY-NC-SA 4.0 (ENFA)

### LICENSE OF OUR DATASET
- CC BY-NC-SA 4.0

## SOURCES
- FBREF (<https://fbref.com/fr/>) from Sports Reference (<https://www.sports-reference.com>) for csv files in `csv/England/D1/Premier_League/equipes/*/*.csv` and `csv/England/D1/Premier_League/saisons/*.csv`
- Wikipedia (<https://en.wikipedia.org/wiki/Main_Page>) for csv files in `csv/England/D1/Premier_League/*.csv` and `csv/England/D1/Football_League_First_Division/saisons/*.csv`
- ENFA (<https://www.enfa.co.uk/>) for csv files in `csv/England/D1/Football_League_First_Division/equipes/*.csv`
```