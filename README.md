# Indeed Job Scraper

This Python script scrapes job listings from Indeed.com (Pakistan) for a specified job title and exports the results to a CSV file.

## Features

- Scrapes job listings from Indeed.com (Pakistan)
- Extracts job title, company name, company location, and job URL
- Exports results to a CSV file
- Uses cloudscraper to bypass anti-bot measures

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- pip (Python package manager)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/indeed-job-scraper.git
   ```
2. Navigate to the project directory:
   ```
   cd indeed-job-scraper
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Open the `scrape_job()` function in the script.
2. Modify the `job_search` variable to specify the job title you want to search for.
3. Run the script:
   ```
   python indeed_job_scraper.py
   ```
4. The results will be saved in `Job_results.csv` in the same directory.

## Customization

- To change the target country, modify the `base_url` variable in the `scrape_job()` function.
- To adjust the number of results or add more fields, you may need to modify the scraping logic within the `scrape_job()` function.

## Dependencies

- [cloudscraper](https://github.com/VeNoMouS/cloudscraper): For bypassing Cloudflare's anti-bot page.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): For parsing HTML and extracting data.
- [pandas](https://pandas.pydata.org/): For creating and exporting data to CSV.

## Disclaimer

Web scraping may be against the terms of service of some websites. Use this script responsibly and ensure you have permission to scrape the target website. The authors are not responsible for any misuse of this script.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/indeed-job-scraper/issues) if you want to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
