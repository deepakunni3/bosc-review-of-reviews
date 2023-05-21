# bosc-review-of-reviews

This repository contains scripts for collating abstract reviews from EasyChair into a spreadsheet.

This prepared spreadsheet then serves as a starting point for BOSC Review of Reviews (ROR).

For a detailed SOP on how to go about BOSC ROR, take a look at [ROR-README.md](ROR-README.md)

# Installation

First set up a virtual environment using `venv` (optional but recommended).

```sh
python3 -m venv env
source env/bin/activate
```

Then install the required dependencies:
```sh
pip install -r requirements.txt
```

# Running

```sh
Usage: collate_reviews.py [OPTIONS] INPUT_FILENAME OUTPUT_FILENAME
Try 'collate_reviews.py --help' for help.
```

The input is typically a text file with all the submissions and their corresponding reviews.

Check the [ROR-README.md](ROR-README.md) for instructions on how to prepare the input for the script.

Once the input (e.g. `reviews.txt`) is prepared, you can parse it as follows:
```sh
python collate_reviews.py reviews.txt parsed_reviews.tsv
```

You can then import `parsed_reviews.tsv` into Excel or Google Spreadsheets for review.
