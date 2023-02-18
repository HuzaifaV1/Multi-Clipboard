import sys
import clipboard
import json

# The file to save the data to
SAVED_DATA = 'clipboard.json'

def save_data(filepath, data):
    # Open the json file and dump the data
    with open(filepath, 'w') as f:        
        json.dump(data, f)

def load_data(filepath):
    # Try to open file and if theres no file return '{}' otherwise return data
    try: 
        # Open the json file and load data as a dictonary 
        with open(filepath, 'r') as f:
            data = json.load(f)        
            return data
    except:
        return {}

def save(data):
    key = input('Enter a key: ')
    # Assign a key to the information on the clipboard
    data[key] = clipboard.paste()
    # Save the data to the json file
    save_data(SAVED_DATA, data)
    print('Data Saved.')

def load(data):
    key = input('Enter a key: ')
    # Check if the key is in the json file
    if key in data:
        print('Data:', data)
        # Copy data to clipboard
        clipboard.copy(data[key])
        print('Data copied to clipboard.')
    else:
        print('Key does not exist.')

def list(data):
    # List data
    print(data)

def delete(data):
    key = input('Enter a key: ')
    # Delete the key
    del data[key]
    # Save data and load it again
    save_data(SAVED_DATA, data)
    load_data(SAVED_DATA)

def main():
    # Check if the command is valid
    if len(sys.argv) == 2:
        # Get the command
        command = sys.argv[1]
        # Load the saved data
        data = load_data(SAVED_DATA)

        if command == 'save':
            # Save data
            save(data)
        elif command == 'load':
            # Load Data
            load(data)
        elif command == 'list':
            # List Data
            list(data)
        elif command == 'delete':
            delete(data)
        else: 
            print('Unknown command.')
    else:
        print('Please pass exactly one command.')

main()