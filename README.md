# Python ZIP File Handling and Testing

## Project Description

This project demonstrates how to handle ZIP files in Python, including creating ZIP archives and extracting their contents. It also includes automated tests to ensure the functionality of the scripts. This project is useful for understanding basic file operations in Python as well as learning the fundamentals of testing.

## Key Features

1. **ZIP Archiving**:
   - Scripts for compressing files into a ZIP archive.

2. **ZIP Extraction**:
   - Scripts for extracting contents from a ZIP archive.

3. **Automated Testing**:
   - Tests to verify the correct functionality of the ZIP handling scripts.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/iimaiorov/python-zip-file-handling.git
   ```
2. Navigate to the project directory:
   ```bash
   cd python-zip-file-handling
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- To create a ZIP archive, run `script_archive_zip.py`.
- To extract a ZIP archive, run `script_extract_zip.py`.
- Run tests to verify functionality:
   ```bash
   pytest
   ```

## Project Structure

- **data/**: Directory containing sample files for ZIP operations.
- **tests/**: Directory containing test scripts for automated testing.
- **script_archive_zip.py**: Script to archive files into a ZIP.
- **script_extract_zip.py**: Script to extract files from a ZIP.
