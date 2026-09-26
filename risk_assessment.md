# Risk Assessment

## 1. Assets, Vulnerabilities, and Consequences

| Asset                                             | Vulnerability                              | Possible Consequence                                                            |
| ------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------- |
| Student records server                            | Guest network access to the records server | Unauthorized users may access or interfere with confidential student records.   |
| Student record files transferred between campuses | Unencrypted file transfers                 | Student information could be exposed or intercepted during transmission.        |
| Staff accounts and access credentials             | Weak staff passwords                       | Attackers may gain unauthorized access to staff accounts and protected systems. |

## 2. Risk Ranking

| Rank | Risk                                       | Likelihood | Impact | Reason                                                                                        |
| ---- | ------------------------------------------ | ---------- | ------ | --------------------------------------------------------------------------------------------- |
| 1    | Guest access to the student records server | High       | High   | Guest network access creates a direct opportunity for unauthorized access to student records. |
| 2    | Unencrypted file transfers                 | High       | High   | Files transferred without encryption may be intercepted and exposed during transmission.      |
| 3    | Weak staff passwords                       | High       | Medium | Weak passwords make staff accounts easier to compromise.                                      |

## 3. Recommended Controls

| Risk                                       | Recommended Control                                                                              |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| Guest access to the student records server | Configure firewall rules to block guest network access to the student records server.            |
| Unencrypted file transfers                 | Use encryption to protect files during transfer and verify their integrity using SHA-256 hashes. |
| Weak staff passwords                       | Enforce strong password requirements for staff accounts.                                         |

## 4. Risk Treatment and Implementation

### Guest Network Access

Firewall rules should restrict access to the student records server so that only authorized networks and users can connect. Guest networks should be separated from systems containing confidential student information.

### Unencrypted File Transfers

Student records should be encrypted before being transferred between campuses. The cryptography tool demonstrates this approach by encrypting and decrypting a sample student record.

SHA-256 hashing can also be used to verify whether the file has been modified. During testing, the student record was intentionally changed after the baseline hash was created. The tool detected the change and reported:

`Integrity check failed: file has changed.`

### Weak Staff Passwords

Staff accounts should use strong passwords with minimum length and complexity requirements. Multi-factor authentication can also provide an additional layer of protection where supported.

## 5. Overall Security Approach

The proposed controls address confidentiality, integrity, and access control:

* **Confidentiality:** Encryption protects student records from unauthorized disclosure.
* **Integrity:** SHA-256 hash comparison detects unauthorized modifications.
* **Access Control:** Firewall restrictions limit access to authorized networks and users.
* **Authentication:** Strong staff passwords help reduce unauthorized account access.

## 6. Conclusion

The risk assessment identifies three important security risks affecting the student records system. The recommended controls combine network security, encryption, integrity verification, and stronger authentication practices to reduce these risks and improve the protection of student information.
