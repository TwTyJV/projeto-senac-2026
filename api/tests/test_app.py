from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def api_ex1():
    return """
    <html>
        <head>
        </head>
            <body>
                <h1> Olá mundo </h1>
            </body>
    </html>"""
