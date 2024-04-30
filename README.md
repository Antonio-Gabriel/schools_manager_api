# Schools manager

An application to manage informations about schools.

## Features

- [x] Adding basic CRUD to manage schools informations

- [x] When registering a school, an error is returned if the province does not exist.

- [x] Load provinces based in a local JSON file with all the provinces available

- [x] Create the documentation of the projects explaining all of the endpoints, their status and responses

- [x] Adding stractegies to upload bulk data from excel about schools and persits into the database

- [] If the document being sent is not in the format: name, email, room number, province, it will not be accepted.

- [x] If the document sent is empty, it will also return an error.

- [] Publish the image of the project in dockerhub

## How to start

To start the project on you local machine follow the steps below:

```bash
python3 -m venv venv

# For linux/macos
. venv/bin/activate

# For windown
. venv\Scripts\activate

pip install -r requirements.txt

python3 main.py
```

## Production version

To find the documentation of hosted api click on the link below:

[Swagger documentation](https://)

[DockerHub hosted project](https://)

## Where I can get faker data

On the project root dir you can find a script called `seed_excel_data.py`, the script was made to generate fake data related to institution, although that's not perfect, but you can use to do it.

to run do the command below:

```bash
python3 seed_excel_data.py
```

## Made by

Antonio Gabriel (AG)
