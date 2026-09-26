# Risk Assessment

## 1. Assets, Vulnerabilities, and Consequences

| Asset | Vulnerability | Possible Consequence |
|---|---|---|
| Student records server | Guest network access to the records server | Unauthorized users may access or interfere with confidential student records. |
| Student record files transferred between campuses | Unencrypted file transfers | Student information could be exposed or intercepted during transmission. |
| Staff accounts and access credentials | Weak staff passwords | Attackers may gain unauthorized access to staff accounts and protected systems. |
## 2. Risk Ranking

| Rank | Risk | Likelihood | Impact | Reason |
|---|---|---|---|---|
| 1 | Guest access to the student records server | High | High | The scenario states that guest network access to the records server exists, creating a direct opportunity for unauthorized access to student records. |
| 2 | Unencrypted file transfers | High | High | Files are transferred between campuses without encryption, creating a risk of information exposure during transmission. |
| 3 | Weak staff passwords | High | Medium | Weak passwords make staff accounts easier to compromise, which could allow unauthorized access to protected systems. |
## 3. Recommended Controls

| Risk | Recommended Control |
|---|---|
| Guest access to the student records server | Configure firewall rules to block guest network access to the student records server. |
| Unencrypted file transfers | Use encryption to protect files during transfer and verify their integrity using SHA-256 hashes. |
| Weak staff passwords | Enforce strong password requirements for staff accounts. |