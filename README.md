# Web-Scraper

Small Python Indeed scraper prototype that extracts job information and appends results to CSV.

## Setup and repository reference

### Project structure

- [Indeed_job.py](Indeed_job.py)
- [Job_results.csv](Job_results.csv)
- [requirements.txt](requirements.txt)
- [tests](tests)

### Getting started

```bash
git clone https://github.com/Raimal-Raja/Web-Scraper.git
cd Web-Scraper
```

Create and activate a virtual environment, then install the project dependencies:

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r "requirements.txt"
```

Application entry point:

```bash
python Indeed_job.py
```

### Configuration and limitations

Live scraping depends on site permissions, browser availability, current page markup, and anti-bot responses. Passing syntax checks does not verify live collection. Browser-handling code does not guarantee access.

### Maintenance fixes

- Use each extracted job ID in its URL.
- Write the CSV header only once.
- Handle missing markup and optional company fields; bound HTTP requests.

### Validation

Audit: 2026-10-08. Repository structure, setup instructions and description were reviewed. 2 existing Python files passed syntax checks; changed files and new regression tests were checked separately. 2 regression tests passed. Syntax checks do not establish full runtime correctness. External APIs, live scraping, GUI interaction, notebook training and production deployment were not comprehensively exercised.

```bash
python -m unittest discover -s tests -v
```

### Repository description

The short GitHub description is provided in [REPOSITORY_DESCRIPTION.md](REPOSITORY_DESCRIPTION.md).

### Contributions

Describe the issue, reproduction steps, environment, and expected behavior when proposing a change. Keep generated environments, credentials, and unnecessary build artifacts out of new commits.

### License

No top-level license file was found during this review.
