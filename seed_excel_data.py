import random
import pandas as pd
from faker import Faker
from faker_schools import institution_names

fake = Faker()

provinces = ["Bengo", "Benguela", "Bié", "Cabinda",
             "Cuando Cubango", "Cuanza Norte", "Cuanza Sul", "Cunene", "Huambo", "Namibe"]

num_rooms_range = [1, 20]

data_sets = []

while len(data_sets) < 1000:
    name = random.choice(institution_names)
    email = fake.email()
    num_rooms = random.randint(*num_rooms_range)
    province = random.choice(provinces)

    if not any(data_set["Nome"] == name and data_set["Email"] == email and data_set["Número de salas"] == num_rooms and data_set["Província"] == province for data_set in data_sets):
        data_set = {
            "Nome": name,
            "Email": email,
            "Número de salas": num_rooms,
            "Província": province
        }
        data_sets.append(data_set)

df = pd.DataFrame(data_sets)

df.to_excel("schools.xlsx", index=False, header=True)
