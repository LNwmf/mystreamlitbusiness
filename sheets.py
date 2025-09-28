import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def connect_to_sheet():
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name('streamlitcredentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("Business Submissions (Test)").sheet1  # Change to your sheet name
    return sheet

def submit_business_to_sheet(business_name, description, website, image_url, category, email):
    sheet = connect_to_sheet()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    row = [timestamp, business_name, description, website, image_url, category, email]
    sheet.append_row(row)

#Test
if __name__ == "__main__":
    # Test submitting a sample business
    submit_business_to_sheet(
        business_name="Test Business",
        description="This is a test description.",
        website="https://example.com",
        image_url="https://example.com/logo.png",
        category="Test Category",
        email="testemail.com",
    )
    print("✅ Test data submitted!")
