#  Research Grant Council Database

##  Introduction

This project provides a database blueprint for a government organization called the Research Grant Council. Its purpose is to efficiently manage the entire research grant lifecycle, including tracking grant competitions, processing applications, managing reviewers, and documenting meeting decisions. This setup ensures a structured and reliable process for grant review and decision-making.

##  Table of Contents

* Overview & Features
* Key Triggers
* Database Schema
* Project Assumptions

##  Overview & Features

This database solution is designed for integrity, automation, and reliability.

* **Data Integrity:** Foreign keys are used extensively to ensure referential integrity, maintaining accurate relationships between competitions, applications, and researchers.
* **Automation:** Key processes, such as updating application statuses and calculating awarded amounts, are automated using SQL triggers.
* **Error Handling:** Triggers actively prevent data conflicts, such as a reviewer being assigned to an application from their own institution.

###  Key Triggers

* `conflict_of_interest`: Prevents conflicts of interest by raising an error if a reviewer is associated with a researcher from the same institution.
* `award_money_generator`: Automatically generates an `amt_awarded` for grant applications when their status is updated to "Awarded."
* `status_updated` / `status_updated_not`: Automatically updates the application `app_status` to "Awarded" or "Not Awarded" based on the completion of reviews in meetings.

##  Database Schema

The schema is composed of 6 primary tables:

* `grant_Competition`
* `researcher`
* `grant_Application`
* `collaborators`
* `reviewer`
* `meetings`

---

### `grant_Competition`

Stores information about grant competitions.

* `cid`: **Primary Key.** Represents the competition ID.
* `title`: Title of the grant competition (e.g., "Quantum Computing Research Grant").
* `deadline`: Deadline for submitting grant proposals.
* `description`: Brief description of the grant competition.
* `area_of_study`: Area of study or research focus (e.g., "Computer Science", "Biology").
* `status`: Current status of the competition (open or closed).

### `researcher`

Contains details of researchers applying for grants.

* `rid`: **Primary Key.** Represents the researcher ID.
* `fName`: First name of the researcher.
* `lName`: Last name of the researcher.
* `emailID`: Email address of the researcher.
* `uni_name`: Name of the university or organization the researcher is affiliated with.

### `grant_Application`

Holds data about grant applications.

* `aid`: **Primary Key.** Represents the grant application ID.
* `amt_req`: Requested amount for the grant application.
* `cid`: *Foreign Key.* References `grant_Competition(cid)`.
* `principle_inv`: ID of the principal investigator for the grant application (references `researcher(rid)`).
* `app_status`: Status of the grant application (e.g., "submitted", "awarded", "not awarded").
* `amt_awarded`: Amount awarded for the grant application.
* `status_date`: Date of the status update of the grant application.

### `collaborators`

Represents the many-to-many relationship between grant applications and collaborators.

* `aid`: *Foreign Key.* References `grant_Application(aid)`.
* `collaborator_id`: *Foreign Key.* References `researcher(rid)`, representing the collaborator's ID.

### `reviewer`

Stores information about reviewers.

* `reviewer_id`: **Primary Key.** Represents the reviewer ID.
* `fName`: First name of the reviewer.
* `lName`: Last name of the reviewer.
* `emailID`: Email address of the reviewer.
* `institution_name`: Name of the institution or organization the reviewer is affiliated with.

### `meetings`

Tracks reviewer participation in grant selection committee meetings.

* `date`: Date of the meeting.
* `reviewer_id`: *Foreign Key.* References `reviewer(reviewer_id)`.
* `aid`: *Foreign Key.* References `grant_Application(aid)`.
* `reviewed`: Indicates whether the grant application has been reviewed (1 for reviewed, 0 for not reviewed).

##  Project Assumptions

The design of this database operates on the following key assumptions:

* **Principal Investigator and Collaborators:** Only the principal investigator applies for the grant. Other researchers involved are listed as collaborators.
* **Funds Allocation:** Funds are designated to the principal investigator, who is responsible for distribution.
* **Reviewers:** Each application will have three reviewers. Reviewers provide reviews in Boolean form (1 for granted, 0 for denial).
* **Meeting Participants:** Only reviewers participate in meetings discussing grant applications.
* **Decision Making Process:** Decisions are made during meetings, with applications discussed on specific dates. Multiple applications may be discussed on the same date, but no additional dates are assigned.
* **Automatic Award Generation:** If at least two out of three reviewers recommend granting money, the award will be granted automatically.
* **Automatic Status Update:** The status of an application will be updated to "Awarded" if at least two reviewers recommend granting money.
* **Amount Awarded Constraint:** The amount awarded is always less than the requested amount.
* **Automatic Status Date Update:** The `status_date` attribute is automatically updated after meetings to reflect the decision date.

---
