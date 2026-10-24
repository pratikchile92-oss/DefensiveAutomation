# Test Plan — Suspicious Login Alert Triage

## Objective
To verify that login alerts are classified correctly.

## Sample Test Cases

| Test | Failed Attempts | Successful Login After Failures | Expected Result |
|---|---:|---|---|
| 1 | 1 | No | Low Risk |
| 2 | 4 | No | Medium Risk |
| 3 | 8 | No | High Risk |
| 4 | 4 | Yes | High Risk |
| 5 | Missing | No | Manual Review |
| 6 | -1 | No | Invalid Data |
| 7 | 3 | No | Medium Risk |
| 8 | 0 | No | Low Risk |

## Test Procedure
1. Run `python login_triage.py`.
2. Observe the classification for each sample alert.
3. Compare the output with the expected result.
4. Record any mismatch and correct the code.

## Evaluation
The prototype passes when every test case produces the expected classification.

## Safety Check
The program only classifies alerts. It does not lock accounts or modify user access. A human analyst must approve any further action.

Additional Test Execution Results

The following test cases were executed using Python and produced the expected outputs:

Input	Expected Output	Actual Output	Status
-1 failed attempts	Invalid Data	Invalid Data	Pass
3 failed attempts	Medium Risk	Medium Risk	Pass
0 failed attempts	Low Risk	Low Risk	Pass

These tests verify the program’s handling of negative input, three failed login attempts, and zero failed attempts.
