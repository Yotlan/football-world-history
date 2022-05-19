# FOOTBALL HISTORY

## TABLE OF CONTENTS

- [MEANING](#meaning)
  * [FIRST DIVISION OF ENGLAND FOOTBALL : SEASONS FILES](#first-division-of-england-football--seasons-files)
  * [FIRST DIVISION OF ENGLAND FOOTBALL : SQUADS FILES](#first-division-of-england-football--squads-files)
  * [FIRST DIVISION OF ENGLAND FOOTBALL : GROUPED FILES](#first-division-of-england-football--grouped-files)
  * [SCRIPTS TO CLEAN DATA](#scripts-to-clean-data)
- [AUTHORS](#authors)
- [LICENSES](#licenses)
  * [LICENSE OF OUR DATASET](#license-of-our-dataset)
- [SOURCES](#sources)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>



## MEANING

### FIRST DIVISION OF ENGLAND FOOTBALL : SEASONS FILES
To have all the first division of england football seasons files since his creation in 1888, you need to take all csv files in these folders :
- `csv/England/D1/Football_League_First_Division/saisons/*.csv` (1888 - 1992)
- `csv/England/D1/Premier_League/saisons/*.csv` (1992 - 2021)

### FIRST DIVISION OF ENGLAND FOOTBALL : SQUADS FILES
To have all the first division of england football squads files since his creation in 1888, you need to take all csv files in these folders :
- `csv/England/D1/Football_League_First_Division/equipes/*.csv` (1888 - 1992)
- `csv/England/D1/Premier_League/equipes/*.csv` (1992 - 2021)

### FIRST DIVISION OF ENGLAND FOOTBALL : GROUPED FILES
This files regroup all csv files in one files to simplify data analysis or use. This file is automaticly generate with `scripts/python/produce_all_seasons_file.py`. You can take this file in these folders :
- `csv/England/D1/*.csv` (1888-2021)

### SCRIPTS TO CLEAN DATA
To have all scripts we used to clean data, you need to take all scripts files in these folders :
- `scripts/python/*.py` (python)
- `scripts/shell/*.sh` (shell)

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
