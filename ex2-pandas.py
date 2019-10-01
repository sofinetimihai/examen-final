import sqlite3
import pandas as pd

with sqlite3.connect('db.sqlite3') as conn:
    examen_users_df = pd.read_sql_query("SELECT * from examen_users", conn)

    examen_users_df['full_name'] = examen_users_df['first_name'] + " " + examen_users_df['last_name']
    print(examen_users_df)
    examen_users_df.to_excel('output-ex2.xlsx')

    print("Standard variation: ", examen_users_df['number_of_login'].var())
    print("Mean: ", examen_users_df['number_of_login'].mean())

