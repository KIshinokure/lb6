from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Мой сайт</title>
        </head>
        <body>
            <h1>Добро пожаловать на мой сайт!</h1>
            <p>Это главная страница</p>
            <a href="/hello">Перейти к приветствию</a>
        </body>
    </html>
    """

@app.get("/hello", response_class=HTMLResponse)
def hello_page():
    return """
    <html>
        <body>
            <h1>Страница приветствия</h1>
            <p>Примеры:</p>
            <ul>
                <li><a href="/hello/Иван">Привет, Иван</a></li>
                <li><a href="/hello/Мария">Привет, Мария</a></li>
                <li><a href="/hello/Пётр">Привет, Пётр</a></li>
            </ul>
            <a href="/">На главную</a>
        </body>
    </html>
    """

@app.get("/hello/{name}", response_class=HTMLResponse)
def hello_name(name: str):
    return f"""
    <html>
        <body>
            <h1>Привет, {name}!</h1>
            <p>Рады видеть вас на нашем сайте</p>
            <a href="/hello">Назад к списку</a> | 
            <a href="/">На главную</a>
        </body>
    </html>
    """