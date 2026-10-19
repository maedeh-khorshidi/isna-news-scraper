# ISNA News Scraper

A Python-based web scraping project for collecting and structuring sports news articles from [ISNA (Iranian Students' News Agency)](https://www.isna.ir), one of Iran's major news agencies.

## Overview

This project automates the collection of sports news from ISNA's archive pages. It uses Selenium to access web pages, BeautifulSoup to parse HTML content, and Pandas to organize and export the extracted information into a structured CSV dataset.

The collected data can be used for data analysis, Persian Natural Language Processing (NLP), text classification, topic modeling, and other machine learning applications.

## Features

- **Automated web scraping:** Collects articles from ISNA's sports news archive.
- **Multiple sports categories:** Supports football/futsal, wrestling/combat sports, and ball and net sports.
- **Article information extraction:** Retrieves article titles, URLs, summaries, full text, publication dates, and news codes.
- **Persian text handling:** Preserves Persian text and removes zero-width non-joiner characters from extracted fields.
- **Structured data export:** Saves collected articles to a CSV file using UTF-8 with BOM encoding for improved compatibility with spreadsheet software.
- **Configurable pagination:** Allows the number of archive pages to be adjusted.

## Technologies Used

- Python
- Selenium
- BeautifulSoup
- Pandas
- CSV

## Extracted Data

The output dataset contains the following fields:

| Column | Description |
|---|---|
| `sport_tag` | Sports category of the article |
| `title` | Article headline |
| `url` | Original article URL |
| `content` | Full article text |
| `published date` | Publication date |
| `summary` | Article summary |
| `news_code` | Article identifier |

## Getting Started

### Prerequisites

- Python 3.10 or later
- Google Chrome
- An internet connection

### Installation

Clone the repository:

```bash
git clone https://github.com/maedeh-khorshidi/isna-news-scraper.git
cd isna-news-scraper
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install pandas beautifulsoup4 selenium
```

### Run the Scraper

Run the Python script:

```bash
python "import pandas as pd.py"
```

The script launches Chrome, visits the selected sports archive pages, extracts article information, and collects the results in a Pandas DataFrame.

**Note:** The current implementation uses a Windows-specific output path. Update the output path in the script to a directory on your own system before running it. Selenium may manage the compatible Chrome driver automatically, depending on your environment and Selenium version.

## Project Structure

```text
isna-news-scraper/
├── import pandas as pd.py
├── isna_sports_complete.csv
└── README.md
```

The CSV file contains the collected sports news dataset.

## Potential Applications

The collected dataset can support:

- Persian news text analysis
- Sports news classification
- Topic modeling
- News trend analysis
- NLP and machine learning experiments

## Limitations

- The current version focuses on selected sports categories.
- Archive collection is limited by the configured number of pages.
- Website HTML structure changes may require updates to the extraction logic.
- Some articles may contain missing fields or extraction errors.

## Responsible Use

This project is intended for educational, research, and data analysis purposes. Please respect ISNA's website terms, applicable copyright requirements, and server load when collecting content. Retain links to the original articles when redistributing or using the collected data.

## Author

**Maedeh Khorshidi**

[GitHub Profile](https://github.com/maedeh-khorshidi)
