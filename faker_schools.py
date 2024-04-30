import random
from faker import Faker

fake = Faker()

institution_names = []

for _ in range(1000):
    name_components = []

    institution_type_options = ["Escola", "Colégio", "Instituto", "Centro Educacional",
                                "Universidade", "Faculdade", "Instituto Superior Politécnico", "Escola Superior Politécnica"]
    institution_type = random.choice(institution_type_options)

    name_modifiers = ["Nacional", "Privado",
                      "Público", "Internacional", "Bilingue"]
    name_modifier = random.choice(
        name_modifiers) if random.random() > 0.5 else ""

    name_components.append(institution_type)
    name_components.append(name_modifier)

    if institution_type == "Escola":
        name_components.append(fake.company())
    elif institution_type == "Universidade" or institution_type == "Faculdade":
        name_components.append(fake.first_name() + " " + fake.last_name())
    elif institution_type == "Instituto Superior Politécnico" or institution_type == "Escola Superior Politécnica":
        name_components.append(fake.city() + " " + institution_type)

    institution_name = " ".join(name_components)

    if len(institution_name.split()) == 1:
        institution_name += " Institute"

    institution_names.append(institution_name)
