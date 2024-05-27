import yaml
from jinja2 import Template
import os

# Function to load YAML content from a file
def load_yaml_from_file(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Define the Jinja2 template for UDT
template_content = '''
TYPE {{ entity_name }}
STRUCT
{% for field in fields %}
  {{ field.name }} : {{ field.datatype }}; (* {{ field.comment }} *)
{% endfor %}
END_STRUCT
END_TYPE
'''

# Function to generate UDT from YAML entity
def generate_udt_from_yaml(yaml_content, entity_name):
    data = yaml.safe_load(yaml_content)
    
    fields = []
    for use in data[entity_name]["uses"]:
        fields.append({"name": use, "datatype": "REAL", "comment": f"{use.replace('_', ' ').capitalize()} measurement"})

    for opt_use in data[entity_name].get("opt_uses", []):
        fields.append({"name": opt_use, "datatype": "REAL", "comment": f"Optional {opt_use.replace('_', ' ').capitalize()} measurement"})

    template = Template(template_content)
    return template.render(entity_name=entity_name, fields=fields)

# Function to save UDT code to a file
def save_udt_to_file(udt_code, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write(udt_code)

# Main function to load YAML, generate UDT, and save to file
def main(yaml_file_path, entity_name):
    yaml_content = load_yaml_from_file(yaml_file_path)
    udt_code = generate_udt_from_yaml(yaml_content, entity_name)
    
    # Generate the output file path
    base_name = os.path.splitext(yaml_file_path)[0]
    output_file_path = f"{base_name}_{entity_name}.udt"
    
    save_udt_to_file(udt_code, output_file_path)
    print(f"UDT file saved to: {output_file_path}")

# Specify the path to the YAML file and the entity name
yaml_file_path = 'path/to/your/yaml_file.yaml'
entity_name = 'Pump'

# Call the main function
main(yaml_file_path, entity_name)
