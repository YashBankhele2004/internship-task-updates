import smtplib
from email.mime.text import MIMEText
from scripts.fetch_data import fetch_all_nifty50

THRESHOLD = {"RELIANCE": 2500, "TCS": 4000}

def send_email_alert(symbol, price):
    sender = "your_email@gmail.com"
    receiver = "your_email@gmail.com"
    msg = MIMEText(f"Stock: {symbol}\nLive Price: {price}")
    msg["Subject"] = "Stock Market Alert"
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, "your_password")
        server.sendmail(sender, receiver, msg.as_string())

if __name__ == "__main__":
    while True:
        prices = fetch_all_nifty50()
        for stock, price in prices.items():
            if price > THRESHOLD.get(stock, float('inf')):
                send_email_alert(stock, price)
        time.sleep(10)
