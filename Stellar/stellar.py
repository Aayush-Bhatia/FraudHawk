from stellar_sdk import Server, Keypair, TransactionBuilder, Network
import requests  # or wherever your fraud detection model is hosted

# Stellar Setup
server = Server(horizon_url="https://horizon-testnet.stellar.org")
source_secret = "SOURCE_ACCOUNT_SECRET"
destination_public = "DESTINATION_ACCOUNT_PUBLIC"

source_keypair = Keypair.from_secret(source_secret)
source_public = source_keypair.public_key
account = server.load_account(source_public)

# Function to check fraud detection before settlement
def is_transaction_legit(transaction_data):
    # Simulate your fraud detection model
    response = requests.post("http://your-fraud-model/api/check", json=transaction_data)
    result = response.json()
    return result.get("is_legit", False)

# Transaction data you want to check
transaction_data = {
    "source": source_public,
    "destination": destination_public,
    "amount": "100",
    "currency": "XLM"
}

# Run fraud check
if is_transaction_legit(transaction_data):
    print("Transaction is legit. Proceeding to settlement...")

    # Build and submit Stellar transaction
    transaction = (
        TransactionBuilder(
            source_account=account,
            network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
            base_fee=100
        )
        .add_text_memo("Fraud Check Passed")
        .append_payment_op(
            destination=destination_public,
            amount=transaction_data["amount"],
            asset_code="XLM"
        )
        .set_timeout(30)
        .build()
    )

    transaction.sign(source_keypair)
    response = server.submit_transaction(transaction)
    print(f"Transaction successful: {response['hash']}")

else:
    print("Transaction flagged by fraud detection. Settlement stopped.")
