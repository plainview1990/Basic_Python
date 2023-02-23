def promptpay(transaction):
    if transaction <= 5000:
        print("ค่าธรรมเนียมการโอนเงินพร้อมเพย์ :")
        return 0
    elif 5000 <= transaction <= 30000:
        print("ค่าธรรมเนียมการโอนเงินพร้อมเพย์ :")
        return 2
    elif 30000 <= transaction <= 100000:
        print("ค่าธรรมเนียมการโอนเงินพร้อมเพย์ :")
        return 5     
    elif transaction > 100000:
        print("ค่าธรรมเนียมการโอนเงินพร้อมเพย์ :")
        return 10

print("จำนวนเงินที่โอนของท่าน :")
transaction = int(input())
print(promptpay(transaction),"บาท")

