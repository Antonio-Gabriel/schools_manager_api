import pandas as pd


class PandasExcelManager:
    @classmethod
    def read_excel_file(cls, file):
        """read excel data"""
        doc_data = pd.read_excel(file, engine="openpyxl")

        if not set(["Nome", "Email", "Número de salas", "Província"]).issubset(doc_data.columns):
            return [], False

        schools = []
        for _, row in doc_data.iterrows():
            school = {
                "name": row["Nome"],
                "email": row["Email"],
                "numberOfRooms": row["Número de salas"],
                "province": row["Província"]
            }

            if not isinstance(school["numberOfRooms"], int) or school["numberOfRooms"] <= 0:
                return [], False

            schools.append(school)

        return schools, True
