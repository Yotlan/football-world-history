import pandas as pd
import click
import os
import csv

@click.command()
@click.argument('dates')

def parser(dates):
    with open(dates) as csvfile:
        with open('output/sql/date.sql', 'a') as date_sql:
            date_file = csv.reader(csvfile)
            i=0
            for line in date_file:
                if i>0: 
                    date_sql.write(f"INSERT INTO DATES_DIM (DATE_ID,NB_MONTH,NB_WEEK,NB_DAY) VALUES ({line[0]},{line[1]},{line[2]},{line[3]});\n")
                i+=1

if __name__ == "__main__":
    parser()