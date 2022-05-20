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

### REGULAR EXPRESSION

It's something very important in computer science. Indeed, if you want to generalize choose of some folders, files or expressions, it's important to know regular expression. The following table explain how regular expression symbol work :

| Symbol | Match                                 |
|--------|---------------------------------------|
| .      | Any character                         |
| ^      | The starting symbol                   |
| $      | The last symbol                       |
| [ ]    | Set of matching character             |
| [^ ]   | Set of no-matching character          |
| ( )    | Sub expression                        |
| *      | Between 0 and INFINITE                |
| +      | Between 1 and INFINITE                |
| ?      | Between 0 and 1                       |
| {M,N}  | Between M and N                       |
| \|     | First expression or second expression |

We see some example to understand correctly how regular expression work (with the representation to an automaton).

__**Example 1 :**__

![ex1](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/Yotlan/football-world-history/master/courses/uml-diag/ex1.png)

Here we can see that we can enter whatever one symbol, it was accept.

__**Example 2 :**__

![ex2](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/Yotlan/football-world-history/master/courses/uml-diag/ex2.png)

Here we can see that we can enter the number of a we want (0 or n), it was accept. But other symbol ar not accept. 

__**Example 3 :**__

![ex3](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/Yotlan/football-world-history/master/courses/uml-diag/ex3.png)

Here it's the same pattern that previous part, but we need at least one a to be accept.

__**Example 4 :**__

![ex4](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/Yotlan/football-world-history/master/courses/uml-diag/ex4.png)

Here we can see that we can enter 0 or one a only to be accept.

__**Example 5 :**__

![ex5](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/Yotlan/football-world-history/master/courses/uml-diag/ex5.png)

Here we can see that we can enter a or b to be accept.

__**Example 6 :**__

![ex6](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/Yotlan/football-world-history/master/courses/uml-diag/ex6.png)

Here we can see that we can enter at least 2 a and at most 4 a to be accept.

__**Example 7 :**__

![ex7](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/Yotlan/football-world-history/master/courses/uml-diag/ex7.png)

Here we can see that we can enter only word begin with an a following by whatever symbol to be accept.

__**Example 8 :**__

![ex8](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/Yotlan/football-world-history/master/courses/uml-diag/ex8.png)

Here we can see that we can enter only word start with whatever symbol following and end by one a  to be accept.

__**Example 9 :**__

![ex9](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/Yotlan/football-world-history/master/courses/uml-diag/ex9.png)

Here we can see that we can enter only a b or c to be accept.

__**Example 10 :**__

![ex19](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/Yotlan/football-world-history/master/courses/uml-diag/ex10.png)

Here we can see that we can enter only d, e, ... or z. a b and c are not accept.

__**Special example :**__
The use of ( ) are to reffer these sub groups later in code (by use $1 or \1 (depending on the implementation) )

Input :

```java
$string1 = "Hello World\n";
if ($string1 =~ m/(H..).(o..)/) {
  print "We matched '$1' and '$2'.\n";
}
```

Output : 

```sh
java input.java
> We matched 'Hel' and 'o W'.
```

(This example if from Wikipedia (<https://en.wikipedia.org/wiki/Regular_expression>) )