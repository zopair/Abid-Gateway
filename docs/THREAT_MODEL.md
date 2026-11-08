# Threat Model
Assets: source integrity, signing keys, provenance and accurate demo boundaries. Risks: users confuse demo with service; accidental secrets/PII commit; malicious dependency/contribution; compromised CI or account; chronology/authorship overclaims.

Mitigations: conspicuous disclaimer, no financial input fields, minimal dependencies, localhost API, review contributions, least-privilege Actions, branch protection, signed local commits, public key fingerprint, artifact hashes and independent timestamp receipts. Real payment processing, KYC/AML, production uptime and partner certification are out of scope.
