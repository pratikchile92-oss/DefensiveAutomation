Technical Report

Automated Suspicious Login Alert Triage System

Organization: RedKross Research Foundation
Intern ID: 2442
Project Type: Defensive Automation Concept
Technology: Python
GitHub Repository: https://github.com/pratikkhile92-oss/DefensiveAutomation

1. Abstract

This project presents a basic Automated Suspicious Login Alert Triage System developed using Python. It classifies login alerts into risk categories based on failed login attempts and whether a successful login occurred after repeated failures. The purpose is to help prioritize suspicious login events for further investigation.

2. Introduction

Repeated failed login attempts may indicate password guessing or other suspicious login activity. Reviewing every alert manually can take time. This project demonstrates a simple rule-based approach to categorize alerts and identify events that may need additional attention.

3. Objectives

* Classify login alerts into Low Risk, Medium Risk, High Risk, Manual Review, or Invalid Data.
* Apply understandable rules to sample login events.
* Demonstrate a basic defensive automation workflow.
* Identify situations requiring human investigation.
* Document testing, limitations, and future improvements.

4. Tools and Technologies

* Programming language: Python
* Code editor: Visual Studio Code
* Version control: GitHub
* Documentation: Markdown

5. Methodology

The project follows these steps:

1. Receive sample login alert information.
2. Check whether the failed-attempt value is missing or invalid.
3. Apply predefined risk-classification rules.
4. Display the classification for each sample alert.
5. Compare the displayed results with the expected results.

6. Implementation

The Python function classify_login() uses the following rules:

* Missing failed-attempt information: Manual Review.
* Negative failed-attempt count: Invalid Data.
* More than five failed attempts: High Risk.
* Three or more failed attempts followed by a successful login: High Risk.
* Three to five failed attempts without a subsequent successful login: Medium Risk.
* Fewer than three failed attempts: Low Risk.

The program processes sample alerts and prints the resulting classifications.

7. Implementation Results

The program was run using five sample login alerts.

Sample User	Failed Attempts	Successful Login After Failures	Result
Amit	1	No	Low Risk
Rahul	4	No	Medium Risk
Neha	8	No	High Risk
Priya	4	Yes	High Risk
Unknown	Missing	No	Manual Review

These results match the classification rules implemented in the program.

8. Testing and Evaluation

The program was executed with the five sample alerts listed above. The observed output matched the expected classifications for these cases.

Additional test cases documented in test_plan.md include zero attempts, negative values, three failed attempts, and missing data. Each additional case should be executed and its result verified before it is reported as tested.

9. Safety and Human Review

The project only classifies sample alerts. It does not connect to real authentication systems, block users, reset passwords, or perform automated account actions.

High-risk alerts should be investigated by an authorized person. Manual review is appropriate when information is missing or unclear. Any future integration with real systems should include access controls, audit logging, privacy safeguards, and human approval for consequential actions.

10. Limitations

* The program uses predefined rules rather than machine learning.
* It processes sample data and is not connected to a live login system.
* Failed-attempt counts alone cannot confirm an attack.
* The program does not currently analyze IP addresses, device details, location changes, or login history.
* Its classifications are intended to support triage, not replace a security investigation.

11. Recommendations for Future Improvement

* Accept login events from a structured CSV or JSON file.
* Add timestamps, source IP addresses, and device information.
* Record classifications in an audit log.
* Add automated unit tests for all classification rules.
* Evaluate the rules against a larger, representative dataset.
* Require human approval before taking action against an account.

12. Conclusion

The Automated Suspicious Login Alert Triage System demonstrates how basic Python rules can categorize sample login alerts by risk level. It provides a foundation for a more comprehensive defensive automation solution while keeping consequential security decisions under human control.

13. References

1. Python Documentation: https://docs.python.org/3/
2. OWASP Authentication Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
3. NIST Computer Security Incident Handling Guide, SP 800-61 Rev. 2: https://csrc.nist.gov/pubs/sp/800/61/r2/final
4. Project Repository: https://github.com/pratikkhile92-oss/DefensiveAutomation

14. Supporting Evidence

Add genuine screenshots of the Python program running and its output. Additional screenshots may show the repository files and verified test results. Do not include screenshots of tests that have not actually been performed.
