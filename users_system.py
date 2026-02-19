from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI(title="Користувачі")
users = []

@app.get("/", response_class=HTMLResponse)
def home():
    html = """
    <h1> Система управління користувачами</h1>
    <p>Доступні маршрути</p>
    <ul>
        <li>GET /user/get-all - всі користувачі</li>
        <li>GET /user/{login} -  конкретний користувач</li>
        <li>POST /user/add -додати користувача </li>
        <li>PUT /user/edit/{login} - зміна даних</li>
        <li>DELETE /user/delete - видалення користувача</li>
    </ul>
"""
    return HTMLResponse(content=html)

@app.post("/user/add")
def add_user(new_user: dict):
    """
        {
            "login":"...",
            "name":"...",
            "surname":"...",
            "age":20
        }
    """
    for user in users:
        if user["login"]==new_user["login"]:
            raise HTTPException(status_code=400,detail="Такий вже є")
    users.append(new_user)
    return {"Користувач додано": new_user}


@app.put("/user/edit/{login}")
def edit_user(login:str, new_data:dict):

    for user in users:
        if user["login"]==login:
            user.update(new_data)
        return "дані оновлено"
    raise HTTPException(status_code=404,detail="не знайдено")

@app.delete("/user/delete/{login}")
def delete_user(login:str):
    for user in users:
        if user["login"]==login:
            users.remove(user)
            return "видалено"
    raise HTTPException(status_code=404, detail="не знайдено")
    