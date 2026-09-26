# Firewall Filtering Tests

## Purpose

This document records the procedure for testing the firewall controls required by the Cryptography and Network Security assessment.

The assessment instructions do not provide the laboratory IP addresses, network ranges, protected service, or service port. Therefore, no network values or test results have been invented.

## 1. Required Lab Parameters

| Parameter | Value |
|---|---|
| Student records server IP | `[TO BE PROVIDED BY ASSESSOR]` |
| Guest network/subnet | `[TO BE PROVIDED BY ASSESSOR]` |
| Authorised staff network/subnet | `[TO BE PROVIDED BY ASSESSOR]` |
| Protected service | `[TO BE PROVIDED BY ASSESSOR]` |
| Service port | `[TO BE PROVIDED BY ASSESSOR]` |
| Firewall machine/host | `[TO BE CONFIRMED]` |
| Firewall operating system | `[TO BE CONFIRMED]` |
| Firewall technology | `[TO BE CONFIRMED]` |

## 2. Required Firewall Policy

The intended policy is:

1. Block guest-network access to the student records server.
2. Permit the authorised staff network to access the service specified by the assessor.
3. Block other inbound access to that service.
4. Test one permitted connection and two blocked connections.

The exact firewall commands will depend on the operating system and firewall technology used in the authorised laboratory.

## 3. Test Procedure

### Test 1 — Authorised Staff Access

**Purpose:** Confirm that an authorised staff connection to the specified service is permitted.

**Source:** `[STAFF CLIENT IP]`

**Destination:** `[RECORDS SERVER IP]`

**Port:** `[SERVICE PORT]`

**Command used:** `[INSERT LAB-APPROVED TEST COMMAND]`

**Expected result:** Connection succeeds.

**Actual result:** `[RECORD AFTER LAB TEST]`

**Status:** `[PASS/FAIL]`

### Test 2 — Guest Network Access

**Purpose:** Confirm that a guest-network connection to the records server is blocked.

**Source:** `[GUEST CLIENT IP]`

**Destination:** `[RECORDS SERVER IP]`

**Port:** `[SERVICE PORT]`

**Command used:** `[INSERT LAB-APPROVED TEST COMMAND]`

**Expected result:** Connection is blocked.

**Actual result:** `[RECORD AFTER LAB TEST]`

**Status:** `[PASS/FAIL]`

### Test 3 — Other Inbound Access

**Purpose:** Confirm that an unauthorised source outside the staff network cannot access the protected service.

**Source:** `[UNAUTHORISED CLIENT IP]`

**Destination:** `[RECORDS SERVER IP]`

**Port:** `[SERVICE PORT]`

**Command used:** `[INSERT LAB-APPROVED TEST COMMAND]`

**Expected result:** Connection is blocked.

**Actual result:** `[RECORD AFTER LAB TEST]`

**Status:** `[PASS/FAIL]`

## 4. Evidence

The following evidence will be added after the assessor provides the laboratory parameters and the tests are performed:

- Firewall configuration/rule output.
- Command used for each connection test.
- Output showing the permitted connection.
- Output showing the two blocked connections.
- Relevant screenshots if required by the assessor.

## 5. Reproducibility

The final record should contain the:

- source IP/network,
- destination server IP,
- service and port,
- firewall technology,
- exact firewall commands,
- exact connection-test commands,
- expected outcomes,
- actual outcomes.
