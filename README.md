Automated Suspicious Login Alert Triage System

RedKross Research Foundation Internship Project

1. Project Overview

The Automated Suspicious Login Alert Triage System is a Python-based defensive automation prototype that classifies login alerts according to failed login attempts and successful login activity after repeated failures.

The system assigns a risk category to each sample alert so that potentially suspicious events can be prioritized for further investigation.

Intern ID: 2442

Project Repository: DefensiveAutomation

2. Problem Statement

Repeated failed login attempts can indicate password guessing or other suspicious activity. When many alerts need to be reviewed, manually prioritizing them can be time-consuming.

This project demonstrates a basic rule-based approach to classifying sample login alerts. It provides a simple starting point for understanding defensive automation and security alert triage.

A risk classification is an indication for review, not proof that an account has been compromised.

3. Project Objectives

* Develop a simple Python-based login alert classifier.
* Categorize alerts using predefined rules.
* Identify high-risk patterns for further investigation.
* Handle missing and invalid input values.
* Document the workflow and test cases.
* Demonstrate responsible security automation with human oversight.

4. Technologies Used

Technology	Purpose
Python	Implements the classification logic
Visual Studio Code	Code editing and program execution
GitHub	Source code hosting and version control
Markdown	Project documentation

5. How the System Works

The system accepts two inputs:

* failed_attempts: Number of failed login attempts.
* success_after_failures: Whether a successful login occurred after the failures.

The program checks the inputs against predefined conditions and returns a risk classification.

Risk Classification Rules

Condition	Classification
Missing failed-attempt value	Manual Review
Negative failed-attempt value	Invalid Data
More than 5 failed attempts	High Risk
3 or more failed attempts followed by a successful login	High Risk
3 to 5 failed attempts without a subsequent successful login	Medium Risk
Fewer than 3 failed attempts	Low Risk

The program checks missing and negative values before applying the risk thresholds.

6. Sample Output

The program includes five sample alerts.

User	Failed Attempts	Result
Amit	1	Low Risk
Rahul	4	Medium Risk
Neha	8	High Risk
Priya	4, followed by success	High Risk
Unknown	Missing	Manual Review

These are sample records used to demonstrate the program’s behavior. They are not records collected from a real authentication system.

7. How to Run the Project

Prerequisites

* Python 3 installed on your computer.
* A terminal or Visual Studio Code.

Steps

1. Clone or download this repository.
2. Open the project folder in Visual Studio Code.
3. Open the terminal in the project directory.
4. Run the following command:

python login_triage.py

5. Review the classifications printed in the terminal.

If the python command is unavailable on Windows, try:

py login_triage.py

8. Testing and Validation

The program was executed with the five sample alerts included in login_triage.py.

The following additional tests were also executed:

Test Input	Expected Result	Observed Result
classify_login(-1)	Invalid Data	Invalid Data
classify_login(3)	Medium Risk	Medium Risk
classify_login(0)	Low Risk	Low Risk

These results matched the expected classifications.

The complete test plan is documented in test_plan.md. Test cases that have not been executed should be verified separately before being reported as passed.

9. Project Files

File	Description
login_triage.py	Main Python program
README.md	Project overview and usage instructions
technical_report.md	Technical report describing the project
design_document.md	Design, decision logic, risks, and limitations
workflow.md	Workflow and proposed response process
test_plan.md	Test cases and recorded test results

10. Security and Safety Considerations

This project is a learning prototype. It does not connect to live authentication systems or take action against user accounts.

* High-risk alerts should be investigated by an authorized person.
* Missing or unclear information should be reviewed manually.
* The system should not automatically lock accounts based solely on these sample rules.
* Real deployments should include access controls, audit logs, privacy safeguards, and human approval for consequential actions.

11. Limitations

* The system uses fixed rules rather than a trained machine-learning model.
* It processes sample data and is not connected to a live security monitoring platform.
* Failed-attempt counts alone cannot confirm malicious activity.
* It does not currently analyze IP addresses, timestamps, device details, or historical login patterns.
* Its classifications may produce false positives or false negatives.

12. Future Improvements

Possible improvements include:

1. Read alerts from CSV or JSON files.
2. Include timestamps, source IP addresses, and device information.
3. Add automated unit tests for all classification rules.
4. Store results in a structured audit log.
5. Evaluate performance against a larger representative dataset.
6. Integrate with an authorized monitoring platform in a controlled environment.
7. Require human approval before account-related actions.

Video Demonstration

Watch the explanatory video demonstrating the project, Python code, program output, workflow, testing, and technical documentation.
https://drive.google.com/file/d/15dwCEXAa-HnDu02XsMddo0UMpb0vrDfI/view?usp=drivesdk

14. References

* Python Documentation
* OWASP Authentication Cheat Sheet
* NIST Computer Security Incident Handling Guide

⸻

Project: Automated Suspicious Login Alert Triage System
Intern ID: 2442
Organization: RedKross Research Foundation
