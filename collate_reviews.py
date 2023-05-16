import re
import csv
import json
from typing import Dict, List
import typer
from pathlib import Path


KNOWN_PROPERTIES = {
    "PC member", "Time", "Overall evaluation", 
    "Reviewer's confidence", "Confidential remarks for the program committee", "Relevant",
    "Available", "Open", "Updated", "Formatted", "Community", "Novelty", "Example", 
    "Runnable", "Quality score", "Suitability for a long talk", "Confidential remarks for the chair (optional)"
}
SKIPPED_PROPERTIES = {'Acceptance criteria', 'Additional desiderata', 'Overall rating and comments'}



def process_submission(submission_block: List) -> Dict:
    """
    Process a submission entry.

    Args:
        submission_block: Text block for a submission that includes the review

    Returns:
        A dictionary with reviews extracted from the submission block

    """
    submission = {"reviews": []}
    review_block = []
    current_property = None
    submission_id = None
    for element in submission_block:
        if element.startswith("[") and ' et al' not in element:
            # parse title
            m = re.search("\[\d{1,9}\]", element)
            submission_id = m.group()[1:-1]
            submission["id"] = submission_id
            m = re.search("\] (.+)", element)
            title = m.group()[1:]
            submission["title"] = title
            current_property = "title"
        elif element.startswith("----------"):
            # Process previous review block
            if review_block:
                review = process_review(submission_id, submission, review_block)
                submission["reviews"].append(review)
            # Mark start of a new review block
            review_block = [element]
        elif review_block:
            # If currently in review block context
            review_block.append(element)
        elif current_property:
            if current_property == "title":
                submission["authors"] = element
                current_property = None
        else:
            print(f"Ignoring line '{element}'")
    if review_block:
        review = process_review(submission_id, submission, review_block)
        submission["reviews"].append(review)
    return submission


def process_review(submission_id: str, submission: Dict, review_block: List) -> Dict:
    """
    Process a review for a submission.

    Args:
        submission_id: The submission ID
        submission: The submission object
        review_block: Text block for a review

    Returns:
        A dictionary with review metadata extracted from the review block

    """
    review = {"submission_id": submission_id}
    if "title" in submission:
        review["submission_title"] = submission["title"]
    if "authors" in submission:
        review["submission_authors"] = submission["authors"]
    review["properties"] = {}
    property_block = []
    current_property = None
    review_id = None
    for element in review_block:
        if element.startswith("----------"):
            m = re.match("-+\s(\w+\s+\d{1,3})\s", element)
            review_id = m.groups()[0]
            review["review_id"] = review_id
        elif re.search("^([\w(')\s]+):", element):
            m = re.match("^([\w(')\s]+):", element)
            if m.groups():
                p = m.groups()[0].strip()
                if p in KNOWN_PROPERTIES:
                    # known property
                    process_properties(submission_id, review, property_block)
                    current_property = p
                    property_block = [element]
                else:
                    property_block.append(element)
            else:
                if element.strip() not in SKIPPED_PROPERTIES:
                    property_block.append(element)
        else:
            if current_property and element.strip() not in SKIPPED_PROPERTIES:
                property_block.append(element)
    process_properties(submission_id, review, property_block)
    return review


def process_properties(submission_id, review, property_block) -> Dict:
    """
    submission_id: The submission ID
    review: The review object
    property_block: Text block for a property from a review

    Returns:
        A dictionary with the updated review metadata

    """
    property_name = None
    if property_block:
        first = property_block[0]
        m1 = re.match("^([\w(')\s]+):", first)
        if m1:
            property_name = m1.groups()[0].strip()
            if property_name in KNOWN_PROPERTIES:
                parts = first.split(":")
                property_value = ":".join(parts[1:]).strip()
                review[property_name] = property_value
            else:
                print(f"unknown property: {property_name}")
        for element in property_block[1:]:
            if element.strip() in SKIPPED_PROPERTIES:
                continue
            if not property_name:
                print(f"element has no accompanying property_name: '{element}'")
            if property_name not in {"Confidential remarks for the chair (optional)", "Confidential remarks for the program committee"}:
                field = f"{property_name} remarks"
            else:
                field = property_name
            if field in review:
                review[field] = f"{review[field]} {element.strip()}"
            else:
                review[field] = element.strip()
    return review


def write_tsv(data: List, filename: str) -> None:
    """
    Write TSV.

    Args:
        data: Write data as TSV
        filename: The output filename

    """
    ordered_fields = ('Time', 'submission_id', 'submission_authors', 'submission_title', 'review_id', 'PC member', 'score_summary', 'remark_summary')
    with open(filename, 'w') as FH:
        writer = csv.DictWriter(FH, fieldnames=list(ordered_fields), delimiter='\t')
        writer.writeheader()
        for obj in data:
            record = {key: obj[key] for key in ordered_fields}
            writer.writerow(record)


def main(input_filename: Path, output_filename: Path):
    submissions = []
    submission_block = []
    with open(input_filename, encoding="utf-8") as FH:
        for line in FH:
            if line.startswith("[") and ' et al' not in line:
                submission = process_submission(submission_block)
                submissions.append(submission)
                submission_block = [line.rstrip()]
            else:
                submission_block.append(line.rstrip())
        if submission_block:
            submission = process_submission(submission_block)
        submissions.append(submission)

    # Summarize
    all_reviews = []
    for submission in submissions:
        if "reviews" in submission and submission["reviews"]:
            for review in submission["reviews"]:
                # Available	Available remarks	Community	Community remarks	Confidential remarks for the chair (optional)	Confidential remarks for the program committee	Example	Example remarks	Formatted	Formatted remarks	Novelty	Novelty remarks	Open	Open remarks	Overall evaluation	Overall evaluation remarks	PC member	Quality score	Quality score remarks	Relevant	Relevant remarks	Reviewer's confidence	Runnable	Runnable remarks	Suitability for a long talk	Suitability for a long talk remarks	Time	Updated	Updated remarks	review_id	submission_authors	submission_id	submission_title
                score_summary = [
                    f'Overall evaluation: {review["Overall evaluation"]}', f"Reviewer's confidence: " + review["Reviewer's confidence"], f'Relevant: {review["Relevant"]}',
                    f'Available: {review["Available"]}', f'Open: {review["Open"]}', f'Updated: {review["Updated"]}',
                    f'Formatted: {review["Formatted"]}', f'Community: {review["Community"]}', f'Novelty: {review["Novelty"]}',
                    f'Example: {review["Example"]}', f'Runnable: {review["Runnable"]}', f'Quality score: {review["Quality score"]}', f'Suitability for a long talk: {review["Suitability for a long talk"]}'
                ]
                score_summary_str = "\n\n".join(score_summary)

                remark_summary = [
                    f'Overall evaluation: {review["Overall evaluation remarks"]}', f"Confidential remarks for the program committee " + review["Confidential remarks for the program committee"], 
                    f'Relevant: {review["Relevant remarks"]}',
                    f'Available: {review["Available remarks"]}', f'Open: {review["Open remarks"]}', f'Updated: {review["Updated remarks"]}',
                    f'Formatted: {review["Formatted remarks"]}', f'Community: {review["Community remarks"]}', f'Novelty: {review["Novelty remarks"]}',
                    f'Example: {review["Example remarks"]}', f'Runnable: {review["Runnable remarks"]}', f'Quality score: {review["Quality score remarks"]}',
                    f'Suitability for a long talk: {review["Suitability for a long talk remarks"]}'
                ]
                remark_summary_str = "\n\n".join(remark_summary)
                review["score_summary"] = score_summary_str
                review["remark_summary"] = remark_summary_str
                all_reviews.append(review)

    #print(json.dumps(all_reviews, indent=2))
    write_tsv(data=all_reviews, filename=output_filename)



if __name__ == "__main__":
    typer.run(main)
