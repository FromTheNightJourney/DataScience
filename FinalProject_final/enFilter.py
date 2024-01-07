import csv
import os
import json

# Specify the directory containing your files
directory = 'unedited'

# Specify the output CSV file
output_csv = 'output.csv'

# Initialize a list to store data from all files
all_data = []

# Iterate through files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)

        # Open and read each file
        with open(file_path, 'r') as file:
            data = json.loads(file.read())

            # Process the data and extract required values
            message_id = 1
            for chat_entry in data['chat_log']:
                match_id = 4000
                champion_name = chat_entry['champion_name']
                time = chat_entry['time']
                sent_to = chat_entry['sent_to']
                message = chat_entry['message']
                association_to_offender = chat_entry['association_to_offender']
                
                for y in data['players']:
                    # Access the "scores" section within each "player"
                    scores = y.get('scores', {})

                    # Extract kills, deaths, and assists from "scores"
                    kills = int(scores.get('kills', 0))
                    deaths = int(scores.get('deaths', 0))
                    assists = int(scores.get('assists', 0))
                    outcome = y.get('outcome', 0)

                label = ""
                kda = round((kills + assists) / (deaths if deaths != 0 else 1), 2)
                # Append the data to the list
                all_data.append([message_id, match_id, champion_name, time, sent_to, message, association_to_offender, kills, deaths, assists, outcome, label, kda])
                message_id += 1

# Write all data to a CSV file
with open(output_csv, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write header
    csv_writer.writerow(['message_id', 'match_id', 'champion_name', 'time', 'sent_to', 'message', 'association_to_offender', 'kills', 'deaths', 'assists', 'outcome'])

    # Write data to the CSV file
    csv_writer.writerows(all_data)