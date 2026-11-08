# Architecture
Prototype trust boundary: static Arabic RTL UI with fabricated records; Node built-in HTTP API bound to loopback; no third-party calls, persistence, financial data or credentials. Layers: presentation, read-only simulator, conceptual partner adapter (not implemented), provenance/security evidence.

Hypothetical regulated flow: partner KYC/KYB → partner allocates account details → authorized payment receipt and screening → verified reconciliation → FX quote/fees/customer consent → partner-authorized payout → partner confirmation/audit reference. Each live stage requires contracted, licensed institutions and regulatory/legal approval. No production readiness claim.
