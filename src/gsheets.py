import gspread
import yaml
from google.oauth2.service_account import Credentials


# Function to authenticate and fetch spreadsheet data
def get_spreadsheet_data(spreadsheet_id, sheet_name, credentials_file):
    # Define the required Google Scopes
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive.readonly",
    ]

    # Authenticate using the service account credentials
    creds = Credentials.from_service_account_file(credentials_file, scopes=scopes)

    # Initialize the gspread client
    client = gspread.authorize(creds)

    # Open the spreadsheet and select the sheet
    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)

    # Get all values from the sheet
    data = sheet.get_all_records()

    return data


# Function to convert data to YAML format
def convert_to_yaml(data):
    return yaml.dump(data, default_flow_style=False, sort_keys=False)


# Main function to fetch and output as YAML
def main():
    spreadsheet_id = "your_spreadsheet_id_here"  # Replace with your spreadsheet ID
    sheet_name = "Sheet1"  # Replace with your sheet name
    credentials_file = (
        "path_to_credentials.json"  # Path to your Google service account credentials
    )

    # Get the spreadsheet data
    data = get_spreadsheet_data(spreadsheet_id, sheet_name, credentials_file)

    # Convert to YAML
    yaml_data = convert_to_yaml(data)

    # Print the formatted YAML output
    print(yaml_data)


if __name__ == "__main__":
    main()
