## you will need:
- python 3 installed
- sec-api key
- open ai api key
- mongodb installed

## instructions to run the datascraping scripts
1. set up virtual environment with `python -m venv venv`
2. activate it with `venv\Scripts\activate` on windows or `source venv/bin/activate` on mac/linux
3. run `pip install -r requirements.txt` to install dependencies
4. create a .env file in directory with the following contents:

```
sec-api-key = '<enter your sec-api key here>'
open-ai-api-key = '<enter your open ai api key here>'
mongo-url = 'mongodb://localhost:27017/'
```
4. create a folder called `mongodata`
5. start up a local database with `mongod --dbpath=mongodata`
6. run the script with `python lexata_ds.py` with the following options:
- `-v` (optional - prints extra debugging information)
- `-m <company1> <company2> ... `
- `-f <filename of companies list>`
7. you can change the company in the `lexata_ds.py` file, and also change the text format and what is printed. html parsing is done by `sec10kparser.py`

## instructions to run the metadata script
IF AN ENVIRONMENT ALREADY EXISTS FROM THE PREVIOUS STEPS, SIMPLY SKIP TO STEP 5
1. set up virtual environment with `python -m venv venv`
2. activate it with `venv\Scripts\activate` on windows or `source venv/bin/activate` on mac/linux
3. run `pip install -r requirements.txt` to install dependencies
4. create a .env file in directory with the following contents:

```
sec-api-key = '<enter your sec-api key here>'
```
5. run the script with `python metadata_script.py"
