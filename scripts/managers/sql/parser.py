import pandas as pd
import click
import os
import csv

@click.command()
@click.argument('managers')

def parser(managers):
    with open(managers) as csvfile:
        file = csv.reader(csvfile)
        with open(f'output/sql/managers.sql', 'a') as sql:
            i=0
            for line in file:
                if i>0:
                    date_begin = line[3].split()
                    manager_begin_career = int(date_begin[2])
                    date_end = line[4].split()
                    manager_end_career = ""
                    manager_end_month = ""
                    equipe_name = line[2]
                    if line[4] == "Present*":
                        manager_end_career = 2021
                        manager_end_month = "June"
                    else:
                        manager_end_career = int(date_end[2])
                        manager_end_month = date_end[1]
                    if manager_end_career >= 1995 and (manager_end_month not in ["August","September","November","October","December"]):
                        sql.write(f"INSERT INTO MANAGERS_DIM (SQUAD_ID,START_DATE_ID,END_DATE_ID,MANAGER_ID,NB_DAY) VALUES (\"{equipe_name}\",{manager_begin_career},{manager_end_career},\"{line[0]}\",{line[5]});\n")
                i+=1

if __name__ == "__main__":
    parser()