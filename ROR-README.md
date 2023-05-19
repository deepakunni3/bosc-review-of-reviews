# SOP for BOSC Review of Reviews (RORs)

Since 2020, the BOSC Organizing Committee has conducted Review of Reviews (RORs), a process where all abstract reviews submitted by reviewers are checked to make sure that the reviews meet the following criteria:

- Reviews are constructive
- Reviews do not resort to strong language when providing criticism
- Reviews are not biased
- Reviews do not violate the [BOSC Review Process](https://github.com/OBF/bosc_materials/blob/master/BOSC_review_process.md)
- Reviews do not violate [BOSC/OBF Code of Conduct](https://github.com/OBF/obf-docs/tree/master/code-of-conduct)

This document serves as a starting point for conducting Review of Reviews (RORs) for BOSC.

The goal of the ROR process is to ensure that no problematic reviews makes its way to the authors.
At BOSC we try our best to make sure that the reviews are welcoming, constructive, and informative
while ensuring that the reviews meet the aforementioned criteria and expectations.

Couple of things to know ahead of time:

- **Scale:** Each year, we typically have 50-70 abstract submissions, each of which are assigned 2-3 reviewers. 
That means there are ~150-200 reviews that need to be reviewed. This might not seem that daunting, but it will 
be when there is a looming deadline (see below).

- **Time:** Each year, the reviewers start reviewing submissions right after the abstract submission deadline.
The reviewers have, on average, 8-10 days to review their assigned abstracts. The ROR process can start only
after all the reviews are in. There might also be last minute reviews that didn’t make the deadline, so it is
good to be aware of some last minute reviews pooling in.

Following are steps that needs to happen for the ROR:

1. Build a ROR subcommittee
2. Prepare a timeline
3. Ensure necessary privileges on EasyChair
4. Preparation of ROR Spreadsheet
5. Review of Reviews
6. Redactions

Each of the steps are explained in detail below with references to useful resources.

## 1. Build a ROR subcommittee

The lead of the ROR subcommittee should contact 2-3 members of the BOSC Organizing Committee (or members of the
BOSC Abstract Review Committee) to be part of the ROR subcommittee. Typically the subcommittee involves members
of the Organizing Committee. 

This task can be done well in advance, in coordination with the BOSC Organizing Committee.
To set expectations it is always advisable to define the subcommittee at the very beginning.
For example, you can create the subcommittee and request for volunteers at the same the BOSC Organizing
Committee starts meeting regularly.

## 2. Prepare a timeline

Prepare a timeline on when and what needs to happen.
Feel free to reach out to the Organizing Committee or previous ROR leads to clarify how to go about this process.

## 3. Ensure necessary privileges on EasyChair

Ensure that you have the necessary privileges on EasyChair.

You should be able to:

- Bulk download reviews from EasyChair
- Edit existing reviews on EasyChair

Please reach out to Nomi Harris (BOSC Chair) if you are not able to do any of the above.

## 4. Preparation of ROR spreadsheet

If you have the necessary privileges on EasyChair then you will be able to download all submissions as a Word file.
This file describes all submissions, reviews, and additional metadata.

> **Note:** If you were a reviewer and you had marked any submission as a conflict of interest for BOSC Abstract Review
> then these submissions will not be part of the downloaded Word file. You will have to request someone on the ROR
> subcommittee (or someone from the BOSC Organizing Committee) to provide the missing submissions and their corresponding
> reviews.


To prepare a spreadsheet out of this Word file, you need to do the following:

- Copy over contents of the Word file into a text file
- Remove the topmost line from the text file (this includes the 'Review List' line and the 'Submission index' line)
- Save this text file (Take a look at [examples/sample_reviews.txt](examples/sample_reviews.txt) for an example of the formatting)
- You can then parse this text file using the instructions in the [README](README.md)
- After parsing you will get a TSV (Take a look at [examples/collated_sample_reviews.tsv](examples/collated_sample_reviews.tsv))
- You can load this TSV into Google Spreadsheet or Excel Spreadsheet
- Fix formatting and make it more readable
- Add new columns (to the right) for each member in the ROR subcommittee (Take a look at [examples/sample_review_of_reviews_spreadsheet.xlsx](examples/sample_review_of_reviews_spreadsheet.xlsx))

Now you can share this spreadsheet with other members of the ROR subcommittee.

> **Note:** It is recommended to create a Google Spreadsheet and share that with the ROR subcommittee.


## 5. Review of Reviews

The reviews can happen in two phases:

### First Phase

Assign a series of reviews to members of the ROR subcommittee.
It is recommended to split the reviews equally across all members.

If a member has a conflict of interest with a review (this usually happens when they are assigned to review
a review that they themselves wrote) then they can request someone else in the ROR subcommittee to look
at them.

Each member then goes through their assigned reviews and flag problematic ones.
Ideally, each review should have been reviewed by two people. But this may not always be possible.

### Second Phase

Go through the previously flagged reviews.
Bring the flagged reviews for a discussion on Slack.
If they need more deliberation then arrange a meet on Zoom.

Classify the flagged reviews into one of three categories:
- **No change required:** These are reviews that do not require any changes
- **Minor redaction:** These are reviews that require some words or sentences to be removed or rephrased.
- **Full redaction:** These are reviews that require a full redaction

## 6. Redactions

For reviews that require minor redaction, you can go ahead and make the redaction yourself,
while keeping track of what you changed.

For reviews that require a full redaction, you need to discuss with Nomi - and/or others in the
BOSC Organizing Committee. This typically also involves contacting the reviewer of the problematic
review and letting them know about the redaction.

You should finish the review and redactions (if any) before the author notification deadline.

If you have any questions then you can reach out to Nomi Harris and Karsten Hokamp.

Also, be sure to announce that you will be making edits to some reviews as part of the ROR. This can
typically happen on Slack at the appropriate channel dedicated for abstract reviewers.


# Timeline

Here is an example of a timeline for ROR used in 2023:

Abstract Submission Deadline: Apr 20, 2023
Assignments to review abstracts: Apr 22, 2023
Due date for reviews: May 01, 2023
Notifications to authors of Submissions: May 11, 2023

Based on the timeline above, the time window for conducting ROR would be between May 02 to May 10.
