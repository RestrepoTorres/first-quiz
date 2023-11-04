
# General advices

The follow security recomendations were made using the OWASP Top 10 2021 as guideline[1].

**Employee Access Control:** limit the access of developers and support personal to code and data acording to their job necesities, not everyone needs to have full access (least privilege access principle).

**Data Backup:** Implement regular backups and disaster recovery plans to ensure data integrity and availability.

**Security Awareness Training**: Conduct security awareness training for employees, to ensure they are aware of security best practices.

**Vendor Security:** Assess the security of third-party vendors and APIs. Make sure they meet security standards, and **not have vulnerable or outdated components.**

**Regular Security Audits and Penetration Testing:** Periodically conduct security audits and penetration testing to identify vulnerabilities in application and infrastructure.

**Incident Response Plan:** Develop and document an incident response plan so our team knows how to respond to security incidents.

# Advice per technologie

**Kubernetes:** Have control to access to the Kubernetes API and limit who can access the cluster and what actions they are allowed to perform.[2]

**Cellphone apps:** Explicitly disallow other developers apps from accessing our app, store only non-sensitive data in cache files, have inputs validations, minimize the use of APIs that access sensitive data.[3]

**Web frontend:** Have input validations to prevent malicious injection. Use content security policy in order to prevent external scripts execution, always use HTTPS to encrypt data transmitted.[4]

**MySQL:** to avoid SQL injection in our data base we can use prepared statements (with parameterized queries).[5]

**Python backend:**  use TLS for  encrypting messages, configure different permissions for different API keys, not every endpoint will need the user's full account access.[6]




# References
[1] https://owasp.org/Top10/

[2] https://cheatsheetseries.owasp.org/cheatsheets/Kubernetes_Security_Cheat_Sheet.html 

[3] https://developer.android.com/privacy-and-security/security-tips#Networking

[4] https://medium.com/startit-up/how-to-secure-your-frontend-top-security-practices-b48c5735c61e 

[5] https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html

[6]
https://medium.com/startit-up/how-to-secure-your-frontend-top-security-practices-b48c5735c61e 