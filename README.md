# bosc-review-of-reviews

This repository contains scripts for collating abstract reviews from EasyChair.


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

```
python collate_reviews.py reviews.txt parsed_reviews.tsv
```

You can then import `parsed_reviews.tsv` into Excel or Google Spreadsheets for further review.

