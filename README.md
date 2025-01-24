# Bundessprech

Bundessprech is a web-based application that allows users to analyze and visualize the usage of specific words or phrases in German Bundestag plenary session transcripts. The application provides insights into trends over time and supports filtering by party affiliation.

## Features

- Import and process Bundestag plenary session transcripts (XML format).
- Perform word-based searches across all transcripts.
- Visualize trends in word usage over time.
- Filter results by political party affiliation of speakers.

## Project Structure

- **backend**: Handles API endpoints and database logic.
- **reader**: Extracts data from XML files and processes it into a database.
- **ui**: User interface for searching and visualizing word usage trends.

## Requirements

- Python 3.8+
- Additional dependencies are listed in the `requirements.txt` files within each module.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bundessprech.git
   cd bundessprech
