import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('council.db')
cursor = conn.cursor()

def find_open_competitions(month):
    query = """
    SELECT G.callNumber, GD.title
    FROM Grants G
    JOIN GrantDetails GD ON G.callNumber = GD.callNumber
    WHERE strftime('%m', G.applicationDeadline) = :month
    AND EXISTS (
        SELECT 1
        FROM GrantProposals GP
        INNER JOIN ProposalDetails PD ON GP.proposalNumber = PD.proposalNumber
        WHERE GP.callNumber = G.callNumber
        AND PD.applicationStatus = 'submitted'
        AND PD.requestedAmount > 20000
    );
    """
    cursor.execute(query, {"month": month})
    results = cursor.fetchall()
    return results

def find_largest_amount(area):
    query = """
    SELECT PD.proposalNumber, PD.requestedAmount
    FROM ProposalDetails PD
    JOIN GrantProposals GP ON PD.proposalNumber = GP.proposalNumber
    JOIN Grants G on G.callNumber = GP.callNumber
    JOIN GrantDetails GD on GD.callNumber = G.callNumber
    WHERE GD.area = :area
    ORDER BY PD.requestedAmount DESC
    LIMIT 1;
    """
    cursor.execute(query, {"area": area})
    result = cursor.fetchone()
    return result

def find_awarded_before_date(date):
    query = """
    SELECT PD.proposalNumber, PD.awardedAmount
    FROM ProposalDetails PD
    WHERE PD.applicationStatus = 'awarded' AND PD.date < :date
    ORDER BY PD.awardedAmount DESC
    LIMIT 1;
    """
    cursor.execute(query, {"date": date})
    result = cursor.fetchone()
    return result

def average_requested_awarded_discrepancy(area):
    query = """
    SELECT AVG(ABS(PD.requestedAmount - PD.awardedAmount))
    FROM ProposalDetails PD
    JOIN GrantProposals GP ON PD.proposalNumber = GP.proposalNumber
    JOIN Grants G on G.callNumber = GP.callNumber
    JOIN GrantDetails GD on GD.callNumber = G.callNumber
    WHERE GD.area = :area;
    """
    cursor.execute(query, {"area": area})
    result = cursor.fetchone()[0]
    return result

def get_available_reviewers(proposal_number):
    query = """
    SELECT DISTINCT RD.reviewer
    FROM ReviewerDetails RD
    LEFT JOIN ReviewerAssignment RA ON RD.reviewer = RA.reviewers
    LEFT JOIN ReviewerConflicts RC ON RD.reviewer = RC.reviewer
    LEFT JOIN GrantProposals GP ON RD.reviewer = GP.principalInvestigator OR RD.reviewer = GP.collaborators
    WHERE RA.reviewers IS NULL
    AND RC.conflicts IS NULL
    AND (GP.proposalNumber != :proposalNumber OR GP.proposalNumber IS NULL)
    GROUP BY RD.reviewer
    HAVING COUNT(RA.reviewers) < 3;
    """
    cursor.execute(query, {"proposalNumber": proposal_number})
    results = cursor.fetchall()
    return results

def assign_reviewers(proposal_number, reviewers):
    query = """
    INSERT INTO ReviewerAssignment (grantCompetition, reviewers)
    VALUES (:proposalNumber, :reviewers);
    """
    cursor.execute(query, {"proposalNumber": proposal_number, "reviewers": reviewers})
    conn.commit()

def find_proposals_for_reviewer(name):
    query = """
    SELECT PD.proposalNumber
    FROM ProposalDetails PD
    INNER JOIN GrantProposals GP ON PD.proposalNumber = GP.proposalNumber
    INNER JOIN ReviewerAssignment RA ON GP.callNumber = RA.grantCompetition
    WHERE RA.reviewers = :name;
    """
    cursor.execute(query, {"name": name})
    results = cursor.fetchall()
    return results


def main():
    while True:
        print("\nSelect an option:")
        print("1. Find open competitions in a specific month with large proposals")
        print("2. Find the proposal requesting the largest amount in a specific area")
        print("3. Find the proposal awarded the largest amount before a specific date")
        print("4. Calculate the average requested/awarded discrepancy for an area")
        print("5. Assign reviewers to a proposal")
        print("6. Find proposals to review for a specific reviewer")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            month = input("Enter the month (1-12): ")
            competitions = find_open_competitions(month)
            print("Open competitions with large proposals:")
            for competition in competitions:
                print(f"Call Number: {competition[0]}, Title: {competition[1]}")
        elif choice == "2":
            area = input("Enter the area: ")
            proposal = find_largest_amount(area)
            print("Proposal with the largest requested amount:")
            print(f"Proposal Number: {proposal[0]}, Requested Amount: {proposal[1]}")
        elif choice == "3":
            date_str = input("Enter the date (YYYY-MM-DD): ")
            date = datetime.strptime(date_str, "%Y-%m-%d")
            proposal = find_awarded_before_date(date)
            print("Proposal awarded the largest amount before the specified date:")
            print(f"Proposal Number: {proposal[0]}, Awarded Amount: {proposal[1]}")
        elif choice == "4":
            area = input("Enter the area: ")
            discrepancy = average_requested_awarded_discrepancy(area)
            print(f"Average requested/awarded discrepancy for {area}: {discrepancy}")
        elif choice == "5":
            proposal_number = input("Enter the proposal number: ")
            reviewers = get_available_reviewers(proposal_number)
            print("Available reviewers:")
            for reviewer in reviewers:
                print(reviewer[0])
            selected_reviewers = input("Enter the reviewers (comma-separated): ")
            assign_reviewers(proposal_number, selected_reviewers)
            print("Reviewers assigned successfully.")
        elif choice == "6":
            name = input("Enter the reviewer's email address: ")
            proposals = find_proposals_for_reviewer(name)
            print(f"Proposals to review for {name}:")
            for proposal in proposals:
                print(f"Proposal Number: {proposal[0]}")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
