import requests

txn = {
    "Amount": 4300000.0,
    "SenderLocation": "India",
    "ReceiverLocation": "Russia",
    "IsFlaggedBefore": True,
    "DeviceType": "Mobile",
    "MerchantCategory": "Luxury",
    "DeviceChange": True,
    "TransactionGap": 2,
    "IsAmountUsualForUser": False,
    "txn_id": "txn_ui_001"
}

res = requests.post("http://127.0.0.1:8000/predict", json=txn)

print("📩 Response from ML API:")
print(res.json())
