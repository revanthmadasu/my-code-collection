import json

data_0 = open("./h1b_info/data/0k_50k.json")
data_1 = open("./h1b_info/data/50k_100k.json")
data_2 = open("./h1b_info/data/100k_150k.json")
data_3 = open("./h1b_info/data/150k_200k.json")
data_4 = open("./h1b_info/data/200k_250k.json")
data_6 = open("./h1b_info/data/250k_300k.json")
data_7 = open("./h1b_info/data/300k_350k.json")
data_8 = open("./h1b_info/data/350k_400k.json")
data_9 = open("./h1b_info/data/400k_450k.json")


all_data_srcs = [data_0, data_1, data_2, data_3, data_4, data_6, data_7, data_8, data_9]
all_data_src_files = ["./h1b_info/data/0k_50k.json", "./h1b_info/data/50k_100k.json", "./h1b_info/data/100k_150k.json",
                        "./h1b_info/data/150k_200k.json", "./h1b_info/data/200k_250k.json", "./h1b_info/data/250k_300k.json",
                        "./h1b_info/data/300k_350k.json", "./h1b_info/data/350k_400k.json", "./h1b_info/data/400k_450k.json"]

data_colab = []
company_ids = set()

for file_path in all_data_src_files:
    with open(file_path) as file:
        file_content_json = json.load(file)
        for company in file_content_json['data']:
            if not company["id"] in company_ids:
                data_colab.append(company)
                company_ids.add(company["id"])
        # data_colab.extend(file_content_json['data'])


all_data = json.dumps(data_colab, indent = 4)
file = open(f'./h1b_info/data/all_data.json', 'w')
str_data = str(all_data)
str_data = str_data.replace("'", '"')
file.write(str_data)
file.close()

print(len(data_colab))