import matplotlib.pyplot as plt
import json
import sys

def plot_losses(input_file, output_file):
    with open(input_file) as file:
        json_data = file.read()

    results = json.loads(json_data)

    steps = [result['step'] for result in results.values()]
    train_losses = [result['train_loss'] for result in results.values()]
    val_losses = [result['val_loss'] for result in results.values()]

    plt.figure(figsize=(10, 6))
    plt.plot(steps, train_losses, label='Train Loss')
    plt.plot(steps, val_losses, label='Val Loss')

    plt.title('Train and Validation Loss Over Steps')
    plt.xlabel('Step')
    plt.ylabel('Loss')
    plt.legend()

    plt.grid(True)

    plt.savefig(output_file, dpi=300)

    # plt.show()

def main(input_file, output_file):
    plot_losses(input_file, output_file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python plot_losses.py <input_json_file>.json <output_image_file>.png")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.endswith('.json'):
        print("Error: Input file must be a JSON file.")
        sys.exit(1)

    if not output_file.endswith('.png'):
        print("Error: Output file must be a PNG file.")
        sys.exit(1)
        
    main(input_file, output_file)
