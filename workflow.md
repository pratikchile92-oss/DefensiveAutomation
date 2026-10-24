# Workflow Diagram — Login Alert Triage

Start
  |
Receive Login Alert
  |
Validate Input Data
  |
Is data missing? -> Yes -> Manual Review
  |
  No
  |
Are failed attempts negative? -> Yes -> Invalid Data
  |
  No
  |
More than 5 failures? -> Yes -> High Risk
  |
  No
  |
3 or more failures followed by successful login?
  | Yes
  v
High Risk
  |
3–5 failures -> Medium Risk
  |
0–2 failures -> Low Risk
  |
Display result to Human Analyst
  |
Human approval required before account action
  |
End

## Safe Actions
- Classify and display alerts.
- Do not automatically block accounts.
- Human analyst reviews high-risk alerts.

Pseudocode

START
Read failed_attempts
Read success_after_failures
IF failed_attempts is missing:
    Display "Manual Review"
ELSE IF failed_attempts is less than 0:
    Display "Invalid Data"
ELSE IF failed_attempts is greater than 5:
    Display "High Risk"
ELSE IF failed_attempts is 3 or more
        AND success_after_failures is True:
    Display "High Risk"
ELSE IF failed_attempts is 3 or more:
    Display "Medium Risk"
ELSE:
    Display "Low Risk"
END
