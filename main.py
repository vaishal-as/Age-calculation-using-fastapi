from fastapi import FastAPI, Request , Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app import seperate

templates = Jinja2Templates(directory="templates")
myapp=FastAPI()
myapp.mount("/static", StaticFiles(directory="static"), name="static")
@myapp.get("/")
def home(request:Request):
    with open(r"C:\Users\Selvaprithiv\Desktop\Project1\login.html") as file:
        html_content=file.read()
        return HTMLResponse(content=html_content, status_code=200)

@myapp.get("/signup")
def input(request: Request):
    with open(r"C:\Users\Selvaprithiv\Desktop\Project1\static\Signup.html") as file:
            html_content=file.read()
            return HTMLResponse(content=html_content, status_code=200)

@myapp.post("/login")
async def login(request: Request, password : str=Form(...), confirm : str=Form(...)):
    if password != confirm:
         with open(r"C:\Users\Selvaprithiv\Desktop\Project1\static\Signup.html") as file:
            html_content=file.read()
            return HTMLResponse(content=html_content, status_code=200)
    else:
        with open(r"C:\Users\Selvaprithiv\Desktop\Project1\templates\input.html") as file:
            html_content=file.read()
            return HTMLResponse(content=html_content, status_code=200)

@myapp.post("/input")
def input(request: Request,):
     return templates.TemplateResponse("input.html", {"request": request})

@myapp.post("/output")
def output(request:Request,number:list=Form(...),name:list=Form(...)):
    values = dict(zip(number, name))
    result = seperate(values)
    result1=result["Teen"]
    result2=result["Young Adult"]
    result3=result["Adult"]
    result4=result["Old"]
    if result1==[]:
        result1="None"
    else:
        a=""
        for i in result1:
            a=a+i+","
        result1=a

    if result2==[]:
        result2="None"
    else:
        b=""
        for i in result2:
            b=b+i+","
        result2=b

    if result3==[]:
        result3="None"
    else:
        c=""
        for i in result3:
            c=c+i+","
        result3=c

    if result4==[]:
        result4="None"
    else:
        d=""
        for i in result4:
            d=d+i+","
        result4=d
    return templates.TemplateResponse("input.html", {"request": request,"result1": result1,"result2":result2,"result3":result3,"result4":result4})