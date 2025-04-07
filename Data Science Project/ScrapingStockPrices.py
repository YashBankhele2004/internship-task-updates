from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import yfinance as yf

# ✅ Ensure ChromeDriver is installed and compatible with your browser version
options = webdriver.ChromeOptions()
options.headless = False  # Run with UI to debug issues

try:
    # ✅ Create the WebDriver instance first
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.moneycontrol.com/markets/indian-indices/nifty-50-9.html")

    # ✅ Now, define WebDriverWait after initializing driver
    wait = WebDriverWait(driver, 10)  

    # ✅ Try different selectors (check actual class names on the webpage)
    stock_name = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(@class, 'pcstname')]"))).text
    stock_price = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'inprice1')]"))).text

    print(f"Stock: {stock_name}, Price: {stock_price}")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()  # ✅ Ensure driver quits even if an error occurs

# ✅ Fetch historical stock data for NIFTY 50 using Yahoo Finance
nifty50 = yf.Ticker("^NSEI")  # "^NSEI" is the NIFTY 50 index symbol

# ✅ Get historical market data
hist_data = nifty50.history(period="1y")  # Last 1 year data

# ✅ Save to CSV
hist_data.to_csv("nifty50_data.csv")
print(hist_data.head())
