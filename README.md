# SEMrush Organic Overview URL Opener

## Description
This Flask-based web application simplifies the process of opening multiple SEMrush Organic Overview reports. It takes a list of domains and automatically generates and opens URLs for the SEMrush Organic Overview tool, trying different domain variations (with and without 'www') to ensure you get the data you need.

## Features
- Input multiple domains using comma separation
- Automatically generates variations of each domain (e.g., example.com and www.example.com)
- Creates SEMrush Organic Overview URLs for each domain variation
- Dark mode interface with purple accents for comfortable viewing
- Displays all generated URLs before opening them
- Shows the total number of domains being processed
- Opens URLs in your default browser with a delay to prevent overwhelming

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Setup
1. Clone this repository or download the files
2. Install the required dependencies:
```bash
pip install flask
```

### File Structure
```
semrush-url-opener/
│
├── app.py
├── templates/
│   └── index.html
└── README.md
```

## Usage
1. Start the application:
```bash
python app.py
```
2. Open your web browser and go to `http://localhost:5000`
3. Enter your domains in the text area, separated by commas
   Example: example.com, website.com, mysite.com
4. Click "Generate URLs" to see all the SEMrush URLs that will be created
5. Click "Open All URLs" to open each URL in your default browser

## How It Works
1. **Domain Input**: The application takes a comma-separated list of domains
2. **URL Generation**: For each domain, it:
   - Creates variations (with/without 'www')
   - Generates the corresponding SEMrush Organic Overview URL
3. **Display**: Shows all generated URLs on the page
4. **Opening**: Opens each URL in your default browser with a 2-second delay between each

## Troubleshooting
- If URLs don't open, check your default browser settings
- If the application doesn't start, ensure port 5000 is available
- For large numbers of domains, be aware that your browser may block some popups

## Contributing
Feel free to fork this repository and submit pull requests for any improvements.

## License
This project is available for free use and modification.