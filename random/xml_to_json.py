import json
import xml.etree.ElementTree as ET

def xml_to_json(element):
    if element.tag == "object":
        obj_class = element.get("class")
        obj_data = {"name": None}
        sub_objects = []

        for sub_element in element:
            if sub_element.tag == "property" and sub_element.get("name") == "name":
                obj_data["name"] = sub_element.text
            elif sub_element.tag == "object":
                sub_objects.append(xml_to_json(sub_element))

        if obj_data["name"]:
            obj_data[obj_class] = sub_objects
            return obj_data

    return None

# Read XML from a file
xml_file_path = "path/to/your/xml/file.xml"
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Convert XML to JSON
json_data = xml_to_json(root)

# Save JSON to a file
json_file_path = "output.json"
with open(json_file_path, "w") as json_file:
    json.dump(json_data, json_file, indent=4)