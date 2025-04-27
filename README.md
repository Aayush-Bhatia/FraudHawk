
# FraudHawk - Fraud Detection Engine for Cross-Border Payments

## Overview
FraudHawk is a fraud detection engine specifically designed to monitor and detect anomalies in cross-border payment transactions. It processes transaction data streamed via Fluvio and flags suspicious activities before the Stellar settlement process. This system aims to identify potential fraudulent activities, including money laundering, in real-time, ensuring enhanced security for international payments.

FraudHawk integrates AI and blockchain technology to provide an effective solution for fraud prevention in cross-border transactions.

## Key Features
- **Real-Time Monitoring:** Continuously processes and monitors transaction data streamed via Fluvio.
- **Anomaly Detection:** Flags any unusual patterns or discrepancies in transaction data that could suggest fraudulent activities.
- **Money Laundering Detection:** Uses advanced algorithms to detect potential money laundering behaviors in transactions.
- **Stellar Integration:** Anomalies are flagged before transactions are settled on the Stellar network, adding a layer of fraud prevention.
- **Blockchain Transparency:** Ensures that all transaction data is transparent and immutable, offering additional security.

## How It Works
1. **Data Streaming:** FraudHawk receives transaction data in real time via Fluvio, a streaming platform that supports high-throughput data streams.
2. **Pattern Recognition:** The engine continuously analyzes the data for any unusual patterns that deviate from typical transaction behaviors.
3. **Fraud Flagging:** If any discrepancies or suspicious activities are detected, such as potential money laundering, the transaction is flagged for further review.
4. **Pre-settlement Check:** The flagged transactions are reviewed before the Stellar settlement process to prevent fraudulent transactions from being completed.
5. **Blockchain Integrity:** All flagged transactions are recorded on the blockchain for full transparency and traceability.




## Usage

1. Start the fraud detection engine:

   ```bash
   python fraudhawk.py
   ```

2. Stream transaction data to the engine and monitor flagged transactions in real-time.

## Authors
- **Sarthak Makkar**
- **Hardik Arora**
- **Mayank Arora**
- **Aayush Bhatia**

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
