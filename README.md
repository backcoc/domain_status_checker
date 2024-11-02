# HTTPX-Toolkit Response Filter Script

This Python script automates the process of using `httpx-toolkit` to scan a list of domains for their HTTP status codes, filter the responses based on these status codes, and organize them into categorized files.

## Features
- Takes an input file with domain URLs.
- Runs `httpx-toolkit` with no color formatting.
- Filters and saves domains into separate files based on their HTTP status codes:
  - **200** responses
  - **30x** responses (e.g., 301, 302, 307)
  - **40x** responses (e.g., 403, 404)
  - **50x** responses (e.g., 500, 503)
- Organizes the filtered files into a dedicated subdirectory.

## Prerequisites
- **Python 3** installed on your system.
- **httpx-toolkit** must be installed and available in your system’s PATH.
- **grep** must be available on your system (most Unix-based systems have it by default).

## Usage

1. Clone or download this repository to your local machine.
2. Ensure the required tools are installed.
3. Run the script by following the instructions below.

### Running the Script

1. **Prepare an input file** containing the domains you want to scan. Each line should contain a URL in the format `http://example.com:port` or `https://example.com:port`.

2. **Execute the script** by running the following command in your terminal:
   ```bash
   python3 httpx_filter_script.py
3. **Provide the input file path when prompted by the script.

4. **The script will:

   - Run httpx-toolkit on the provided input file.
   - Create a subdirectory named httpx_responses.
   - Filter the responses and save them into the following files within the httpx_responses directory:
   - httpx_200.txt: Contains all domains with a 200 status code.
   - httpx_30x.txt: Contains all domains with 30x status codes (e.g., 301, 302).
   - httpx_40x.txt: Contains all domains with 40x status codes (e.g., 403, 404).
   - httpx_50x.txt: Contains all domains with 50x status codes (e.g., 500, 503).
   - Check the httpx_responses directory for the filtered files based on the status codes
  
### Script Explanation
The Python script performs the following steps:

- Takes an input file path from the user.
- Runs httpx-toolkit on the provided file with the --no-color option to avoid color codes in the output.
- Creates a directory named httpx_responses if it doesn’t already exist.
- Filters the output using grep to separate domains by status codes:
- [200] for successful responses.
- [30x] for redirections.
- [40x] for client errors.
- [50x] for server errors.
- Moves the filtered files into the httpx_responses directory.
### Dependencies
- httpx-toolkit
- grep (for filtering)
- Python 3
