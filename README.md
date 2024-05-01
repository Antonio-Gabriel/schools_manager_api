# Schools manager

An application to manage informations about schools.

## Features

- [x] Adding basic CRUD to manage schools informations

- [x] When registering a school, an error is returned if the province does not exist.

- [x] Load provinces based in a local JSON file with all the provinces available

- [x] Create the documentation of the projects explaining all of the endpoints, their status and responses

- [x] Adding stractegies to upload bulk data from excel about schools and persits into the database

- [x] If the document being sent is not in the format: name, email, room number, province, it will not be accepted.

- [x] If the document sent is empty, it will also return an error.

- [x] Publish the image of the project in dockerhub

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

[Swagger documentation](https://schools-manager-api.onrender.com/docs#/)

[DockerHub hosted project](https://hub.docker.com/repository/docker/antoniogabriel534/webapi/general)

## Where I can get faker data

In the root directory of the project, you can find a script called `seed_excel_data.py`, the script was made to generate false data related to the institution, although it is not perfect, but you can use it to do this.

You can also find a file called `schools.xlsx` which already has around 1000 fake schools generated that you can use to upload them.

to run do the command below:

```bash
python3 seed_excel_data.py
```

## Made by

Antonio Gabriel (AG)
