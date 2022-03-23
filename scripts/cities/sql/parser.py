import pandas as pd
import click
import os
import csv

@click.command()
@click.argument('cities')
@click.argument('stadiums')

def parser(cities,stadiums):
    with open(stadiums) as stadium_csvfile:
        stadium_file = csv.reader(stadium_csvfile)
        i=0
        stade_city = ""
        for line in stadium_file:
            if i>0:
                stade_city = line[2]
            with open(cities) as city_csvfile:
                with open('output/sql/cities.sql', 'a') as city_sql:
                    city_file = csv.reader(city_csvfile)
                    j=0
                    for line in city_file:
                        if j>0 and stade_city != "" and (stade_city in line[0]):
                            nb_people = line[6].replace(",","")
                            if line[1] == "time immemorial":
                                city_sql.write(f"INSERT INTO CITY_DIM (CITY_ID,START_DATE_ID,PEOPLE_NB) VALUES (\"{stade_city}\", {1}, {nb_people});\n")
                            elif line[1] == "18th century":
                                city_sql.write(f"INSERT INTO CITY_DIM (CITY_ID,START_DATE_ID,PEOPLE_NB) VALUES (\"{stade_city}\", {1700}, {nb_people});\n")
                            else:
                                city_sql.write(f"INSERT INTO CITY_DIM (CITY_ID,START_DATE_ID,PEOPLE_NB) VALUES (\"{stade_city}\", {line[1]}, {nb_people});\n")
                        j+=1
            i+=1

if __name__ == "__main__":
    parser()