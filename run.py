from os import getenv
from src import app

if __name__ == "__main__":
    app.run(
            host=getenv('HOST'),
            port=getenv('PORT')
            )
