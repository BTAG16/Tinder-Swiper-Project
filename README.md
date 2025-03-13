# Tinder Auto Liker Bot

This Python script automates logging into Tinder using Facebook credentials and liking profiles.

## Features
- Logs into Tinder using Facebook credentials.
- Accepts cookies and navigates through popups.
- Automates liking profiles.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required Python libraries:
  - `selenium`
  - `python-dotenv`

You can install them using:
```bash
pip install selenium python-dotenv
```

## Setup
1. Create a `.env` file in the same directory as the script and add your credentials:
   ```
   EMAIL=your_facebook_email
   PASSWORD=your_facebook_password
   ```
2. Install ChromeDriver to match your Chrome version.
3. Run the script:
   ```bash
   python tinder_auto.py
   ```

## How It Works
- Opens Tinder and clicks the login button.
- Logs in using Facebook credentials.
- Accepts location and notification prompts.
- Continuously likes profiles until an error occurs.

## License
This project is open-source and available under the MIT License.

