# Design Document
## Automated Suspicious Login Alert Triage System

### 1. Introduction
This project proposes a small defensive automation to reduce repetitive security triage work. It classifies suspicious login alerts using simple rules and helps a security analyst decide which alerts need attention first.

### 2. Operational Problem
Security teams may receive many login alerts every day. Manually checking every alert takes time and can delay investigation of high-risk events.

### 3. Input Data
The prototype uses sample login alert data:
- Username
- Number of failed login attempts
- Whether a successful login occurred after failures

The sample data is simulated and does not contain real user information.

### 4. Decision Logic
- Missing failed-attempt data: Manual Review
- Negative failed attempts: Invalid Data
- More than 5 failed attempts: High Risk
- 3 or more failed attempts followed by a successful login: High Risk
- 3–5 failed attempts: Medium Risk
- 0–2 failed attempts: Low Risk

### 5. Safe Actions
The program classifies alerts and displays the results. It does not automatically block accounts, reset passwords, or change permissions. A human analyst must review alerts and approve any account-related action.

### 6. Human Approval Points
- High-risk alerts require analyst review.
- Missing or invalid data must be checked manually.
- No account should be locked based only on this prototype's result.

### 7. Failure Modes
- Missing or incomplete input data
- Incorrect or misleading login logs
- False positives that flag legitimate users
- False negatives that fail to flag suspicious activity
- Program errors or unexpected input formats

### 8. Evaluation Approach
The prototype is evaluated using sample test cases covering low, medium, and high risk, successful login after failures, missing data, and invalid negative values. The actual output is compared with the expected result in `test_plan.md`.

### 9. Limitations and Risks
- This is a simple educational prototype.
- It uses simulated data, not live authentication logs.
- Thresholds are illustrative and may not suit every organization.
- It does not verify IP addresses, device details, geolocation, or user behaviour.
- It does not replace professional security monitoring.
- Human review is required before any defensive action.

### 10. Conclusion
This prototype demonstrates how simple rule-based automation can reduce repetitive alert sorting and help analysts prioritize suspicious login events while keeping important security decisions under human control.
