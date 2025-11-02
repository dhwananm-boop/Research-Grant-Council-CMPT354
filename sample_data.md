## Researcher

### Sample Data

<table border="1">
    <tr>
        <td><u>emailAddress</u></td>
        <td>firstName</td>
        <td>lastName</td>
        <td>Organization</td>
    </tr>
    <tr>
        <td>sanchitjain2003@gmail.com</td>
        <td>Sanchit</td>
        <td>Jain</td>
        <td>SFU Applied Science Computing Science</td>
    </tr>
    <tr>
        <td>kaisle@gmail.com</td>
        <td>Kaisle</td>
        <td>Stevenson</td>
        <td>SFU Applied Science Electronics</td>
    </tr>
    <tr>
        <td>nakul123@gmail.com</td>
        <td>Nakul</td>
        <td>Kaushik</td>
        <td>SFU Applied Science Computing Science</td>
    </tr>
    <tr>
        <td>san304@gmail.com</td>
        <td>Sanchit</td>
        <td>Ranjan</td>
        <td>SFU Applied Science Computing Science</td>
    </tr>
    <tr>
        <td>john.doe@example.com</td>
        <td>John</td>
        <td>Doe</td>
        <td>University of XYZ</td>
    </tr>
    <tr>
        <td>jane.smith@example.com</td>
        <td>Jane</td>
        <td>Smith</td>
        <td>ABC Corporation</td>
    </tr>
    <tr>
        <td>mark.johnson@example.com</td>
        <td>Mark</td>
        <td>Johnson</td>
        <td>XYZ Corporation</td>
    </tr>
    <tr>
        <td>sarah.white@example.com</td>
        <td>Sarah</td>
        <td>White</td>
        <td>University of ABC</td>
    </tr>
    <tr>
        <td>robert.green@example.com</td>
        <td>Robert</td>
        <td>Green</td>
        <td>DEF Foundation</td>
    </tr>
    <tr>
        <td>emily.williams@example.com</td>
        <td>Emily</td>
        <td>Williams</td>
        <td>University of XYZ</td>
    </tr>
    <tr>
        <td>adam.wilson@example.com</td>
        <td>Adam</td>
        <td>Wilson</td>
        <td>ABC Corporation</td>
    </tr>
    <tr>
        <td>lisa.taylor@example.com</td>
        <td>Lisa</td>
        <td>Taylor</td>
        <td>University of DEF</td>
    </tr>
    <tr>
        <td>eric.brown@example.com</td>
        <td>Eric</td>
        <td>Brown</td>
        <td>XYZ Corporation</td>
    </tr>
    <tr>
        <td>amy.jones@example.com</td>
        <td>Amy</td>
        <td>Jones</td>
        <td>DEF Foundation</td>
    </tr>
    <tr>
        <td>kevin.clark@example.com</td>
        <td>Kevin</td>
        <td>Clark</td>
        <td>University of ABC</td>
    </tr>
</table>

Pkey: {emailAddress}
FDs:

1. emailAddress $\rightarrow$ firstName
1. emailAddress $\rightarrow$ lastName
1. {emailAddress} $\rightarrow$ Organization

Closure: {emailAddress}<sup>+</sup> = {emailAddress, firstName, lastName, Organization} <br>
The given table is in BCNF.

## GrantCompetition

## Sample Data

<table border="1">
	<tr>
		<td><u>callNumber</u></td>
		<td>title</td>
		<td>applicationDeadline</td>
		<td>description</td>
		<td>area</td>
		<td>status
	</tr>
	<tr>
		<td>1</td>
		<td>Going Quantum</td>
		<td>2024-04-10</td>
		<td>quantum computing competition</td>
		<td>Quantum Computing</td>
		<td>open</td>
	</tr>
	<tr>
		<td>2</td>
		<td>Decoding impact of Covid-19</td>
		<td>2024-04-05</td>
		<td>big data competition</td>
		<td>Data Science</td>
		<td>closed</td>
	</tr>
	<tr>
		<td>3</td>
		<td>Innovating Food</td>
		<td>2024-03-23</td>
		<td>Using hardware to revolutionize agriculture</td>
		<td>Electronics</td>
		<td>closed</td>
	</tr>
	<tr>
		<td>4</td>
		<td>AI for UI</td>
		<td>2024-04-27</td>
		<td>Using AI to revolutionize UI</td>
		<td>UI Design</td>
		<td>open</td>
	</tr>
	<tr>
		<td>5</td>
		<td>Plan Ecology</td>
		<td>2024-04-04</td>
		<td>Use technologies to calculate your carbon footprint</td>
		<td>Fullstack development</td>
		<td>closed</td>
	</tr>
</table>

Pkey: callNumber
Assumptions: 2+ grant competitions can have the same title
FDs:

1. callNumber $\rightarrow$ title, applicationDeadline
   Non-trivial FDs:
1. title $\rightarrow$ description, area, status
   Closure:
1. {callNumber}<sup>+</sup> = {title, applicationDeadline, description, area, status} => Pkey
1. {title}<sup>+</sup> = {title, description, area, status}

A table called `Grants` can be created with `callNumber, applicationDeadline, status`. Following BCNF decomposition, a second table can be created called `GrantDetails` which will have `title, description, area` but since a `title` can be same for 2 + competitions, `applicationDeadline` will not be the pkey for `GrantDetails`, hence it makes sense to use `callNumber, title, description, area, status` instead of `title, description, area, status`. Furthermore, if `title` is added as a column to `GrantDetails`, it will include redundancy. Therefore, following BCNF decomposition:
`Grants:`

<table border="1">
	<tr>
		<td><u>callNumber</u></td>
		<td>applicationDeadline</td>
		<td>Status</td>
	</tr>
	<tr>
		<td>1</td>
		<td>2024-04-10</td>
		<td>open</td>
	</tr>
	<tr>
		<td>2</td>
		<td>2024-04-05</td>
		<td>closed</td>
	</tr>
	<tr>
		<td>3</td>
		<td>2024-03-23</td>
		<td>closed</td>
	</tr>
	<tr>
		<td>4</td>
		<td>2024-04-27</td>
		<td>open</td>
	</tr>
	<tr>
		<td>5</td>
		<td>2024-04-04</td>
		<td>closed</td>
	</tr>
</table>

`GrantDetails:`

<table border="1">
	<tr>
		<td><u>callNumber</u></td>
		<td>title</td>
		<td>description</td>
		<td>area</td>
		</tr>
	<tr>
		<td>1</td>
		<td>Go Quantum!</td>
		<td>quantum computing competition</td>
		<td>Quantum Computing</td>
		</tr>
	<tr>
		<td>2</td>
		<td>Data for the better</td>
		<td>big data competition</td>
		<td>Data Science</td>
		</tr>
	<tr>
		<td>3</td>
		<td>Hardware Something</td>
		<td>Using hardware to revolutionize agriculture</td>
		<td>Electronics</td>
		</tr>
	<tr>
		<td>4</td>
		<td>Ai UI</td>
		<td>Using AI to revolutionize UI</td>
		<td>UI Design</td>
	</tr>
	<tr>
		<td>5</td>
		<td>Eco Plan</td>
		<td>Use technologies to calculate your carbon footprint</td>
		<td>Fullstack development</td>
	</tr>
</table>

# Grant Proposals

## Sample Data

<table border="1">
    <tr>
        <td><u>proposalNumber</u></td>
        <td>requestedAmount</td>
        <td>applicationStatus</td>
        <td>awardedAmount</td>
        <td>date</td>
        <td>callNumber<sup>Fkey: Grants.callNumber</sup></td>
        <td>principalInvestigator<sup>Fkey: Researcher.emailAddress</sup></td>
        <td>collaborators<sup>Fkey: Researcher.emailAddress</sup></td>
		<td>ReviewAssignment<sup>Fkey: ReviewAssignment.assignmentID</sup></td>
    </tr>
    <tr>
        <td>1006</td>
        <td>$2500</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>1</td>
        <td>nakul123@gmail.com</td>
        <td>san304@gmail.com, john.doe@example.com</td>
    </tr>
    <tr>
        <td>1007</td>
        <td>$1800</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>2</td>
        <td>john.doe@example.com</td>
        <td>sanchitjain2003@gmail.com, kaisle@gmail.com</td>
    </tr>
    <tr>
        <td>1008</td>
        <td>$3200</td>
        <td>not awarded</td>
        <td>-</td>
        <td>-</td>
        <td>3</td>
        <td>kaisle@gmail.com</td>
        <td>sanchitjain2003@gmail.com, nakul123@gmail.com</td>
    </tr>
    <tr>
        <td>1009</td>
        <td>$4200</td>
        <td>awarded</td>
        <td>$3800</td>
        <td>2024-04-10</td>
        <td>4</td>
        <td>san304@gmail.com</td>
        <td>nakul123@gmail.com, kaisle@gmail.com</td>
    </tr>
    <tr>
        <td>1010</td>
        <td>$1500</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>5</td>
        <td>sanchitjain2003@gmail.com</td>
        <td>nakul123@gmail.com, san304@gmail.com</td>
    </tr>
    <tr>
        <td>1011</td>
        <td>$2700</td>
        <td>awarded</td>
        <td>$2300</td>
        <td>2024-03-20</td>
        <td>1</td>
        <td>nakul123@gmail.com</td>
        <td>san304@gmail.com, john.doe@example.com</td>
    </tr>
    <tr>
        <td>1012</td>
        <td>$1900</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>2</td>
        <td>john.doe@example.com</td>
        <td>sanchitjain2003@gmail.com, kaisle@gmail.com</td>
    </tr>
    <tr>
        <td>1013</td>
        <td>$3500</td>
        <td>not awarded</td>
        <td>-</td>
        <td>-</td>
        <td>3</td>
        <td>kaisle@gmail.com</td>
        <td>sanchitjain2003@gmail.com, nakul123@gmail.com</td>
    </tr>
    <tr>
        <td>1014</td>
        <td>$4000</td>
        <td>awarded</td>
        <td>$3600</td>
        <td>2024-04-12</td>
        <td>4</td>
        <td>san304@gmail.com</td>
        <td>nakul123@gmail.com, kaisle@gmail.com</td>
    </tr>
    <tr>
        <td>1015</td>
        <td>$1600</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>5</td>
        <td>sanchitjain2003@gmail.com</td>
        <td>nakul123@gmail.com, san304@gmail.com</td>
    </tr>
</table>

Pkey: `proposalNumber`<br>
Fkeys: `callNumber`<sup>`Grants.callNumber`</sup>, `principalInvestigator`<sup>`Researchers.emailAddress`</sup>, `collaborators`<sup>`Researchers.emailAddress`</sup><br>
Assumption: `emailAddress` of `principalInvestigator` can never be a value in the corresponding cell of `collaborators` column<br>

FDs:

1. proposalNumber $\rightarrow$ requestedAmount, applicationStatus, awardedAmount, date
2. proposalNumber, callNumber $\rightarrow$ principalInvestigator, collaborators
3. proposalNumber, primaryInvestigator, collaborators $\rightarrow$ callNumber

Converting to 1NF first since `collaborators` column is not atomic.

<table border="1">
    <tr>
        <td><u>proposalNumber</u></td>
        <td>requestedAmount</td>
        <td>applicationStatus</td>
        <td>awardedAmount</td>
        <td>date</td>
        <td>callNumber<sup>Fkey: Grants.callNumber</sup></td>
        <td>principalInvestigator<sup>Fkey: Researcher.emailAddress</sup></td>
        <td>collaborators<sup>Fkey: Researcher.emailAddress</sup></td>
    </tr>
    <tr>
        <td>1006</td>
        <td>$2500</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>1</td>
        <td>nakul123@gmail.com</td>
        <td>san304@gmail.com</td>
    </tr>
    <tr>
        <td>1006</td>
        <td>$2500</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>1</td>
        <td>nakul123@gmail.com</td>
        <td>john.doe@example.com</td>
    </tr>
    <tr>
        <td>1007</td>
        <td>$1800</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>2</td>
        <td>john.doe@example.com</td>
        <td>sanchitjain2003@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1007</td>
        <td>$1800</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>2</td>
        <td>john.doe@example.com</td>
        <td>kaisle@gmail.com</td>
    </tr>
    <tr>
        <td>1008</td>
        <td>$3200</td>
        <td>not awarded</td>
        <td>-</td>
        <td>-</td>
        <td>3</td>
        <td>kaisle@gmail.com</td>
        <td>sanchitjain2003@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1008</td>
        <td>$3200</td>
        <td>not awarded</td>
        <td>-</td>
        <td>-</td>
        <td>3</td>
        <td>kaisle@gmail.com</td>
        <td>nakul123@gmail.com</td>
    </tr>
    <tr>
        <td>1009</td>
        <td>$4200</td>
        <td>awarded</td>
        <td>$3800</td>
        <td>2024-04-10</td>
        <td>4</td>
        <td>san304@gmail.com</td>
        <td>nakul123@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1009</td>
        <td>$4200</td>
        <td>awarded</td>
        <td>$3800</td>
        <td>2024-04-10</td>
        <td>4</td>
        <td>san304@gmail.com</td>
        <td>kaisle@gmail.com</td>
    </tr>
    <tr>
        <td>1010</td>
        <td>$1500</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>5</td>
        <td>sanchitjain2003@gmail.com</td>
        <td>nakul123@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1010</td>
        <td>$1500</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>5</td>
        <td>sanchitjain2003@gmail.com</td>
        <td>san304@gmail.com</td>
    </tr>
    <tr>
        <td>1011</td>
        <td>$2700</td>
        <td>awarded</td>
        <td>$2300</td>
        <td>2024-03-20</td>
        <td>1</td>
        <td>nakul123@gmail.com</td>
        <td>san304@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1011</td>
        <td>$2700</td>
        <td>awarded</td>
        <td>$2300</td>
        <td>2024-03-20</td>
        <td>1</td>
        <td>nakul123@gmail.com</td>
        <td>john.doe@example.com</td>
    </tr>
    <tr>
        <td>1012</td>
        <td>$1900</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>2</td>
        <td>john.doe@example.com</td>
        <td>sanchitjain2003@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1012</td>
        <td>$1900</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>2</td>
        <td>john.doe@example.com</td>
        <td>kaisle@gmail.com</td>
    </tr>
    <tr>
        <td>1013</td>
        <td>$3500</td>
        <td>not awarded</td>
        <td>-</td>
        <td>-</td>
        <td>3</td>
        <td>kaisle@gmail.com</td>
        <td>sanchitjain2003@gmail.com</td>
	</tr>
</table>

Now that the table is in 1NF, we can see that `proposalNumber` column has duplicates which means `proposalNumber` column can no longer be the primary key of the table. We need a new key for distinguishing between different tuples. Thinking about it, it makes sense for the new primary key to be a composite key. So the new primary key is `{proposalNumber, primaryInvestigator, collaborators}`. Another option was `{proposalNumber, collaborators`} but there might be proposals in which there is only **1** `primaryInvestigator` and **no** `collaborators`.

<table border="1">
    <tr>
        <td><u>proposalNumber</u></td>
        <td>requestedAmount</td>
        <td>applicationStatus</td>
        <td>awardedAmount</td>
        <td>date</td>
        <td>callNumber<sup>Fkey: Grants.callNumber</sup></td>
        <td><u>principalInvestigator</u><sup>Fkey: Researcher.emailAddress</sup></td>
        <td><u>collaborators</u><sup>Fkey: Researcher.emailAddress</sup></td>
    </tr>
    <tr>
        <td>1006</td>
        <td>$2500</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>1</td>
        <td>nakul123@gmail.com</td>
        <td>san304@gmail.com</td>
    </tr>
    <tr>
        <td>1006</td>
        <td>$2500</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>1</td>
        <td>nakul123@gmail.com</td>
        <td>john.doe@example.com</td>
    </tr>
    <tr>
        <td>1007</td>
        <td>$1800</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>2</td>
        <td>john.doe@example.com</td>
        <td>sanchitjain2003@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1007</td>
        <td>$1800</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>2</td>
        <td>john.doe@example.com</td>
        <td>kaisle@gmail.com</td>
    </tr>
    <tr>
        <td>1008</td>
        <td>$3200</td>
        <td>not awarded</td>
        <td>-</td>
        <td>-</td>
        <td>3</td>
        <td>kaisle@gmail.com</td>
        <td>sanchitjain2003@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1008</td>
        <td>$3200</td>
        <td>not awarded</td>
        <td>-</td>
        <td>-</td>
        <td>3</td>
        <td>kaisle@gmail.com</td>
        <td>nakul123@gmail.com</td>
    </tr>
    <tr>
        <td>1009</td>
        <td>$4200</td>
        <td>awarded</td>
        <td>$3800</td>
        <td>2024-04-10</td>
        <td>4</td>
        <td>san304@gmail.com</td>
        <td>nakul123@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1009</td>
        <td>$4200</td>
        <td>awarded</td>
        <td>$3800</td>
        <td>2024-04-10</td>
        <td>4</td>
        <td>san304@gmail.com</td>
        <td>kaisle@gmail.com</td>
    </tr>
    <tr>
        <td>1010</td>
        <td>$1500</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>5</td>
        <td>sanchitjain2003@gmail.com</td>
        <td>nakul123@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1010</td>
        <td>$1500</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>5</td>
        <td>sanchitjain2003@gmail.com</td>
        <td>san304@gmail.com</td>
    </tr>
    <tr>
        <td>1011</td>
        <td>$2700</td>
        <td>awarded</td>
        <td>$2300</td>
        <td>2024-03-20</td>
        <td>1</td>
        <td>nakul123@gmail.com</td>
        <td>san304@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1011</td>
        <td>$2700</td>
        <td>awarded</td>
        <td>$2300</td>
        <td>2024-03-20</td>
        <td>1</td>
        <td>nakul123@gmail.com</td>
        <td>john.doe@example.com</td>
    </tr>
    <tr>
        <td>1012</td>
        <td>$1900</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>2</td>
        <td>john.doe@example.com</td>
        <td>sanchitjain2003@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1012</td>
        <td>$1900</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
        <td>2</td>
        <td>john.doe@example.com</td>
        <td>kaisle@gmail.com</td>
    </tr>
    <tr>
        <td>1013</td>
        <td>$3500</td>
        <td>not awarded</td>
        <td>-</td>
        <td>-</td>
        <td>3</td>
        <td>kaisle@gmail.com</td>
        <td>sanchitjain2003@gmail.com</td>
	</tr>
</table>

Now that this table is in 1NF, and primary key has been updated, we can do BCNF.
<br>
`proposalDetails`

Pkey: proposalNumber

<table border="1">
    <tr>
        <td><u>proposalNumber</u></td>
        <td>requestedAmount</td>
        <td>applicationStatus</td>
        <td>awardedAmount</td>
        <td>date</td>
    </tr>
    <tr>
        <td>1006</td>
        <td>$2500</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>1007</td>
        <td>$1800</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>1008</td>
        <td>$3200</td>
        <td>not awarded</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>1009</td>
        <td>$4200</td>
        <td>awarded</td>
        <td>$3800</td>
        <td>2024-04-10</td>
    </tr>
    <tr>
        <td>1010</td>
        <td>$1500</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>1011</td>
        <td>$2700</td>
        <td>awarded</td>
        <td>$2300</td>
        <td>2024-03-20</td>
    </tr>
    <tr>
        <td>1012</td>
        <td>$1900</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>1013</td>
        <td>$3500</td>
        <td>not awarded</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>1014</td>
        <td>$4000</td>
        <td>awarded</td>
        <td>$3600</td>
        <td>2024-04-12</td>
    </tr>
    <tr>
        <td>1015</td>
        <td>$1600</td>
        <td>submitted</td>
        <td>-</td>
        <td>-</td>
    </tr>
</table>

`grantProposals`

Pkey: `{proposalNumber, principalInvestigator, collaborators}`

<table border="1">
    <tr>
        <td><u>proposalNumber</u></td>
        <td>callNumber<sup>Fkey: Grants.callNumber</sup></td>
        <td><u>principalInvestigator</u><sup>Fkey: Researcher.emailAddress</sup></td>
        <td><u>collaborators</u><sup>Fkey: Researcher.emailAddress</sup></td>
    </tr>
    <tr>
        <td>1006</td>
        <td>1</td>
        <td>nakul123@gmail.com</td>
        <td>san304@gmail.com</td>
    </tr>
    <tr>
        <td>1006</td>
        <td>1</td>
        <td>nakul123@gmail.com</td>
        <td>john.doe@example.com</td>
    </tr>
    <tr>
        <td>1007</td>
        <td>2</td>
        <td>john.doe@example.com</td>
        <td>sanchitjain2003@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1007</td>
        <td>2</td>
        <td>john.doe@example.com</td>
        <td>kaisle@gmail.com</td>
    </tr>
    <tr>
        <td>1008</td>
        <td>3</td>
        <td>kaisle@gmail.com</td>
        <td>sanchitjain2003@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1008</td>
        <td>3</td>
        <td>kaisle@gmail.com</td>
        <td>nakul123@gmail.com</td>
    </tr>
    <tr>
        <td>1009</td>
        <td>4</td>
        <td>san304@gmail.com</td>
        <td>nakul123@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1009</td>
        <td>4</td>
        <td>san304@gmail.com</td>
        <td>kaisle@gmail.com</td>
    </tr>
    <tr>
        <td>1010</td>
        <td>5</td>
        <td>sanchitjain2003@gmail.com</td>
        <td>nakul123@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1010</td>
        <td>5</td>
        <td>sanchitjain2003@gmail.com</td>
        <td>san304@gmail.com</td>
    </tr>
    <tr>
        <td>1011</td>
        <td>1</td>
        <td>nakul123@gmail.com</td>
        <td>san304@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1011</td>
        <td>1</td>
        <td>nakul123@gmail.com</td>
        <td>john.doe@example.com</td>
    </tr>
    <tr>
        <td>1012</td>
        <td>2</td>
        <td>john.doe@example.com</td>
        <td>sanchitjain2003@gmail.com</td>
    </tr>
    <!-- Additional rows for each collaborator value -->
    <tr>
        <td>1012</td>
        <td>2</td>
        <td>john.doe@example.com</td>
        <td>kaisle@gmail.com</td>
    </tr>
    <tr>
        <td>1013</td>
        <td>3</td>
        <td>kaisle@gmail.com</td>
        <td>sanchitjain2003@gmail.com</td>
    </tr>
</table>

## Reviewer

### Sample Data

<table>
	<tr>
		<td><u>emailAddress</u></td>
		<td><u>proposalNumber</u><sup>Fkey: grantProposals.proposalNumber</sup></td>
		<td>coReviewers</td>
		<td>conflicts</td>
	</tr>

</table>

FDs:
1. emailAddress, proposalNumber $\rightarrow$ coReviewers
2. emailAddress, proposalNumber, coReviewers $\rightarrow$ conflicts
3. emailAddress, coReviewers $\rightarrow$ conflicts

This table is not in 1NF.

`ReviewDetails`
<table>
<tr>
		<td><u>emailAddress</u><sup>Fkey: Researchers.emailAddress</sup></td>
		<td><u>proposalNumber</u><sup>Fkey: grantProposals.proposalNumber</sup></td>
		<td>coReviewers</td>
	</tr>
</table>

`ConflictsWReviewers`
<table>
<tr>
		<td><u>emailAddress</u><sup>Fkey: Researchers.emailAddress</sup></td>
		<td>conflicts</td>
	</tr>
</table>

<!-- Assumption: Reviewers can be non-researchers as well who are good in their fields like politicians of a department, a civil servant, or people have academic knowledge who are typically not researchers. Therefore, it is not important to reference `Researchers.emailAddress` -->

## Review Assignment
### Sample Data
<table>
	<tr>
		<td style="border-bottom: 1px dotted;">ReviewAssignment</td>
		<td>grantCompetition<sup>Grants.callNumber</sup></td>
		<td>Reviewers<sup>Fkey: ReviewDetails.emailAddress</sup></td>
		<td>deadline</td>
		<td>status</td>
	</tr>
</table>

## Grant Selection Committee Meeting
### Sample Data
<table>
	<td>proposalNumber<sup>GrantProposal.proposalNumber</sup></td>
	<td>callNumber<sup>Grants.callNumber</sup></td>
	<td>Reviewers</td>

</table>
