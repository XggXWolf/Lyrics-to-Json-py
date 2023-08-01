import json

def insert_lines_into_json_table(text, output_file):
    lines = text.splitlines()
    json_table = [line for line in lines]   
    with open(output_file, 'w') as file:
        json.dump(json_table, file, indent=2)

if __name__ == '__main__':
    # Replace 'input.txt' with the path to your text file
    input_file = 'input_example.txt'

    # Replace 'output.json' with the desired output JSON file path
    output_file = 'output.json'

    with open(input_file, 'r') as file:
        text = file.read()

    insert_lines_into_json_table(text, output_file)
    print(f"Lines inserted into '{output_file}' successfully.")
