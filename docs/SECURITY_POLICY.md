# Security Policy
Prototype safeguards: loopback bind, GET-only allowlisted paths, no body parsing or persistence, no secrets, JSON content type, no-store and nosniff headers, explicit demo flags and Node tests. Report vulnerabilities privately; never include real customer/account details.

Production gates: threat review, dependency audit/SBOM, penetration testing, authN/authZ, key rotation, webhook signature and replay defense, rate limits, immutable audit, encryption, incident response, backup/recovery, privacy impact and partner certification. Not implemented here.
