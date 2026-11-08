# Abid Gateway | عابِد

Arabic-first concept and simulation of an international USD freelancer collection gateway for Egypt.

> **Simulation only.** No InstaPay/bank integration, real USD account or IBAN issuance, custody, FX conversion or payment execution. Do not enter real financial or personal data.

## Concept
Explore a compliant gateway concept to receive international USD proceeds and settle to EGP through authorized financial partners. A real service requires licensed partners, regulatory and legal review, KYC/KYB, AML/CFT, consumer disclosures, security certification and written integration approval. No InstaPay affiliation or endorsement is claimed.

## Prototype
- Responsive Arabic RTL dashboard in violet/orange.
- Demo USD balance, fabricated transactions and indicative EGP calculation.
- Lightweight Node HTTP API simulation bound to loopback; no persistence or external network calls.
- Architecture, workflow, security, threat model, compliance boundary and provenance notes.

## Run (Node 20+)
```sh
npm install
npm run dev
npm run api # another terminal, localhost:8787
npm test
npm run build
``

See [Architecture](docs/ARCHITECTURE.md), [Security](docs/SECURITY_POLICY.md), [Compliance](docs/COMPLIANCE.md), [IP declaration](docs/IP_DECLARATION.md), [timestamp log](evidence/TIMESTAMP_LOG.md).

Git history and crypto receipts can support provenance; they do not alone establish sole inventorship or provide legal certainty. Code license: MIT; third-party trademark rights excluded.
