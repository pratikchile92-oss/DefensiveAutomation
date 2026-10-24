# Automated Suspicious Login Alert Triage System

## Project Overview
This project helps reduce repetitive security triage work by classifying suspicious login alerts based on failed login attempts and login success after failures.

## Problem
Security teams receive many login alerts. Manually reviewing every alert takes time.

## Decision Logic
- 0–2 failed attempts: Low Risk
- 3–5 failed attempts: Medium Risk
- More than 5 failed attempts: High Risk
- 3 or more failed attempts followed by a successful login: High Risk
- Missing data: Manual Review
- Negative attempts: Invalid Data

## Safe Actions
The prototype classifies alerts only. It does not block users or change accounts. A human analyst must review high-risk alerts before taking action.

## How to Run
1. Install Python 3.
2. Open a terminal in the project folder.
3. Run: `python login_triage.py`

## Testing
Sample cases include low, medium, and high risk alerts, successful login after failures, and missing data.

## Limitations and Risks
- Sample data is simulated.
- The rules may produce false positives or false negatives.
- Real authentication logs and production integrations are not included.
- Human review is required before security actions.

## Evaluation
Test the sample alerts and verify that each alert receives the expected classification.
