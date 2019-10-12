# Athlete Database Depok

Athlete Database is a web application to show athletes in Depok and their achievements.

## Installation

Create python virtual environment and activate it before installing the dependencies

```bash
git clone https://github.com/izzuddinsyamil/athlete-database
cd athlete-database
python3 -m venv venv
. venv/bin/activate
```



Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies which listed in requirements.txt file.

```bash
pip install -r requirements.txt
```

## How to Run
This project use postgresql as database so you need to install it. After that, create `.env` file and type this and fill in the correct value for your local postgres settings

```
DB_NAME=<name of database>
DB_USER=<name of user>
DB_PASSWORD=<database password>
DB_HOST=127.0.0.1
DB_PORT=5432
```

Migrate the models into your local database

```
python manage.py migrate
```

Then run the app
```
python manage.py runserver
```
And then open your browser and input `http://localhost:8000/`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

staging url

(https://database-atlet-depok.herokuapp.com)

## License
[MIT](https://choosealicense.com/licenses/mit/)
