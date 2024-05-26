import re
import json
import sys

def parse_log_file(file_path):
    pattern = re.compile(r'step (\d+): train loss ([\d.]+), val loss ([\d.]+)')
    
    results = {}
    i = 0
    with open(file_path, 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                step = int(match.group(1))
                train_loss = float(match.group(2))
                val_loss = float(match.group(3))
                results[i] = {'step': step, 'train_loss': train_loss, 'val_loss': val_loss}
                i += 1
    
    return results

def main(input_file, output_file):
    parsed_data = parse_log_file(input_file)
    
    for step, losses in parsed_data.items():
        print(f"Step {losses['step']}: Train Loss = {losses['train_loss']}, Val Loss = {losses['val_loss']}")
    
    with open(output_file, 'w') as file:
        json.dump(parsed_data, file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python parse.py <input_file> <output_file>.json")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not output_file.endswith('.json'):
        print("Error: Output file must be a JSON file.")
        sys.exit(1)

    main(input_file, output_file)
