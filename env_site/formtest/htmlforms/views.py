from django.shortcuts import render
from htmlforms.models import  JsonEntry
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import unquote
import json
import psycopg2


def hello(request):
   return render(request, "hello.html")

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

def home_view(request):
# logic of view will be implemented here
  e = Entry(name = request.GET.get("your_name",False))
  e.save()
  print(e)
  return render(request, "home.html")



def json_basictest(request):
    # json_data = json.dumps({"key":"value", "a":1, "b":2})
    # print(json_data)
    # print("here!")
    # j = JsonEntry(entry=json_data)
    # j.save()
    conn = psycopg2.connect("dbname=names user=postgres password=halbred42")
    cur = conn.cursor()
    #execute a statement
    # print('PostgreSQL database version:')
    # cur.execute('SELECT version()')
    # db_version = cur.fetchone()
    # print(db_version)
    cur.execute('INSERT INTO public.htmlforms_jsonentry(id, entry)VALUES (44, \'{"title": "Biddhartha", "genres": ["Fiction", "Spirituality"], "published": true}\');')
    conn.commit()
    print("ok")
    # display the PostgreSQL database server version


    # cur.execute("select entry -> 'name' from htmlforms_jsonentry")
    # # close the communication with the PostgreSQL
    # rows = cur.fetchall()
    # print("The number of parts: ", cur.rowcount)
    # for row in rows:
    #     print(row)
    cur.close()
    conn.close()
    return render(request, "home.html")


def json_form(request):
   json_object = json.dumps(request.GET)
   print(json_object)
   j = JsonEntry(entry = json_object)
   j.save()
   return render(request, "jsonform.html")
@csrf_exempt

def krsform(request):
    json_object = json.dumps(request.GET)
    print("here in krsform python")
    return render(request, "fieldstest.html")
@csrf_exempt
def krsform1(request):
   json_object = json.dumps(request.GET)
   print("here in krsform1 python")
   json_clean = json_object.replace("\\", '')
   json_final = json_clean[2:len(json_clean)-6]

   conn = psycopg2.connect("dbname=names user=postgres password=halbred42")
   cur = conn.cursor()

  # print(is_json(json_final))
   getid = 'Select MAX(id) from htmlforms_jsonentry'
   cur.execute(getid)
   id = cur.fetchone()
   print(id[0])

   statement ='INSERT INTO public.htmlforms_jsonentry(id, entry)VALUES (' + str(id[0]+1) + ', \'' + json_final +'\' );'

   print(statement)
   cur.execute(statement)
   conn.commit()
   print("ok")
   # j = JsonEntry(entry = json_clean)
   # j.save()
   return render(request, "fieldstest.html")