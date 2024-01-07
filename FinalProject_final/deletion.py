import csv

def delete_column(input_file, output_file, column_index):
    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        data = [row for row in reader]

    # Delete the specified column
    for row in data:
        del row[column_index]

    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(data)

# Example usage
input_filename = 'csv/500KDA.csv'
output_filename = 'csv/500KDAfix.csv'
column_to_delete = 10  # Replace with the index of the column you want to delete

delete_column(input_filename, output_filename, column_to_delete)
