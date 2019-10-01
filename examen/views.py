from django.shortcuts import render


# Create your views here.


def home(request):
    with sqlite3.connect('db.sqlite3') as conn:
        examen_users_df = pd.read_sql_query("SELECT * from examen_users", conn)

        examen_users_df['full_name'] = examen_users_df['first_name']+" "+examen_users_df['last_name']
        print(examen_users_df)


    return render(request, "examen/home.html")
