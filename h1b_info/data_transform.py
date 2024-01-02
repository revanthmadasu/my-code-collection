import json
import pandas as pd
import openpyxl
all_data = open("./h1b_info/data/all_data.json")

with open("./h1b_info/data/all_data.json") as file:
    all_employers = json.load(file)
    transformed_array = []
    for employer in all_employers:
        employer_data = {
            "id": employer["id"],
            "name": employer["name"],
            "lca_score": (employer["grade"] and (employer["grade"]["lca_score"] if "lca_score" in employer["grade"] else '')) or '',
            "h1b_score": (employer["grade"] and (employer["grade"]["h1b_score"] if "h1b_score" in employer["grade"] else '')) or '',
            "lca_confidence": (employer["grade"] and (employer["grade"]["lca_confidence"] if "lca_confidence" in employer["grade"] else '')) or '',
            "h1b_confidence": (employer["grade"] and (employer["grade"]["h1b_confidence"] if "h1b_confidence" in employer["grade"] else '')) or '',
            "lca_max_salary": (employer["grade"] and (employer["grade"]["lca_max_salary"] if "lca_max_salary" in employer["grade"] else '')) or '',
            "h1b_uscis_status": (employer["grade"] and (employer["grade"]["h1b_uscis_status"] if "h1b_uscis_status" in employer["grade"] else '')) or '',
            "url": employer["url"]
        }
        transformed_array.append(employer_data)
    df = pd.DataFrame(transformed_array)
    df.to_excel('./h1b_info/data/transformed_data.xlsx')
