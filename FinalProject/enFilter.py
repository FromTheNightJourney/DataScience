import pandas as pd
import langid

# Load your data into a pandas DataFrame
df = pd.read_csv('test.csv')  # Replace 'your_data.csv' with the actual filename

# Function to identify the language of a given text
def detect_language(text):
    try:
        lang, confidence = langid.classify(text)
        return lang
    except Exception as e:
        print(f"Error processing text: {text}. Error: {e}")
        return 'unknown'

# Apply language detection to the 'message' column and create a new column 'language'
df['language'] = df['message'].apply(detect_language)

# Filter out non-English entries
df = df[df['language'] == 'en']

# Drop the 'language' column as it is no longer needed
df = df.drop(columns=['language'])

# Save the cleaned data to a new file
df.to_csv('clean.csv', index=False)  # Replace 'cleaned_data.csv' with the desired filename

print("Done.")