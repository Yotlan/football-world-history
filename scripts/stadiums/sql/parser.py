import pandas as pd
import click
import os
import csv

@click.command()
@click.argument('stadiums')

def parser(stadiums):
    with open(stadiums) as stadium_csvfile:
        stadium_file = csv.reader(stadium_csvfile)
        i=0
        stade_name = ""
        stade_city = ""
        stade_capacity = 0
        stade_rank = 0
        for line in stadium_file:
            if i>0:
                stade_name = line[1]
                stade_city = line[2]
                stade_capacity = int(line[3].replace(",",""))
                stade_rank = line[0]
                with open('output/sql/stadiums.sql', 'a') as stadium_sql:
                    stadium_sql.write(f"INSERT INTO STADIUM_DIM  (STADIUM_ID,CITY_ID,MAX_PEOPLE_NB,RANK_STADIUM) VALUES (\"{stade_name}\",\"{stade_city}\",{stade_capacity},{stade_rank});\n")
                stade_name = ""
                stade_city = ""
                stade_capacity = 0
                stade_rank = 0
            i+=1

if __name__ == "__main__":
    parser()