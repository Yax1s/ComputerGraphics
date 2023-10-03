"""
Function to generate one large json file showing all the translations from en to xx with id 
and utt for all the train sets
"""
def train_set(dataset):
    """
    Args:
        dataset: The variable containing the jsonl files.
    """
    filtered_data = []
    for jsonl_file in dataset:
            with open(jsonl_file, 'r', encoding='utf-8') as file:
                for line in file:
                    record = json.loads(line)
                    if 'partition' in record and record['partition'] == 'train':
                        filtered_data.append(record)
    with open('train-set.jsonl', "w") as outfile:
            for data in filtered_data:
                outfile.write(json.dumps(data) + "\n")
    print("Train set saved to jsonl file.")

    # Define the columns you want to extract
    columns_to_extract = ['id', 'utt']

    # Open the input and output files
    with open('train-set.jsonl', 'r') as input_file, open('filtered-train-set.jsonl', 'w') as output_file:
        # Iterate through each line in the input file
        for line in input_file:
            try:
                # Parse the line as JSON
                data = json.loads(line)

                # Create a new dictionary with only the specified columns
                extracted_data = {key: data[key] for key in columns_to_extract}

                # Convert the extracted data back to JSON and write to the output file
                output_file.write(json.dumps(extracted_data) + '\n')
            except json.JSONDecodeError:
                print(f"Skipping invalid JSON line: {line}")
    print("Train set successfully filtered.")

    # Open the input JSONL file for reading and the output JSONL file for writing
    with open('filtered-train-set.jsonl', 'r') as input_file, open('pretty-train-set.jsonl', 'w') as output_file:
        for line in input_file:
            try:
                # Parse each line as a JSON object
                data = json.loads(line)

                # Pretty-print the JSON data with an indentation of 4 spaces
                pretty_json = json.dumps(data, indent=4)

                # Write the pretty-printed JSON to the output file with a newline character
                output_file.write(pretty_json + '\n')
            except json.JSONDecodeError:
                print(f"Skipping invalid JSON line: {line}")

    print(f"Pretty-printed JSONL data saved to: pretty-train-set.jsonl")