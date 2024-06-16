import csv

def txt_to_csv(input_file):
    # Read the input .txt file
    with open(input_file, 'r') as txtfile:
        lines = txtfile.readlines()

    # Strip newline characters from each line and split by commas
    data = [line.strip().split(',') for line in lines]

    # Write to a new .csv file
    output_file = input_file.replace('.txt', '.csv')
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

    # Read the contents of the .csv file and return it
    with open(output_file, 'r') as csv_readfile:
        csv_content = csv_readfile.read()

    return csv_content

# Example usage:
txt_file = './problem2.5/2-5.txt'
csv_content = txt_to_csv(txt_file)
print(csv_content)