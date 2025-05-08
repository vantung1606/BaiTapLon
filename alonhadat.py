from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import time
import schedule
import datetime
import smtplib
from email.message import EmailMessage
import os


def crawl_data():
    print(f"\nBắt đầu chạy lúc {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 15)

    data = []
    page = 1

    while True:
        # 1. vào trang web chọn Hà Nội
        url = f"https://alonhadat.com.vn/nha-dat/can-ban/mat-bang/1/ha-noi/trang--{page}.html"
        print(f"Đang thu thập trang {page}: {url}")
        driver.get(url)
        time.sleep(3)

        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".content-item.item")))
        except:
            print("Không tìm thấy dữ liệu hoặc hết trang.")
            break

        listings = driver.find_elements(By.CSS_SELECTOR, ".content-item.item")
        if not listings:
            break
        # 2. Lấy tất cả dữ liệu(Tiêu đề, Mô tả, Địa chỉ, Diện tích, Giá) hiển thị ở bài viết.
        for listing in listings:
            try:
                title = listing.find_element(By.CSS_SELECTOR, ".ct_title").text.strip()
                description = listing.find_element(By.CSS_SELECTOR, ".ct_brief").text.strip()
                area = listing.find_element(By.CSS_SELECTOR, ".road-width").text.strip() if listing.find_elements(By.CSS_SELECTOR, ".road-width") else "Không có thông tin"
                price = listing.find_element(By.CSS_SELECTOR, ".ct_price").text.strip() if listing.find_elements(By.CSS_SELECTOR, ".ct_price") else "Không có giá"
                address = listing.find_element(By.CSS_SELECTOR, ".ct_dis").text.strip() if listing.find_elements(By.CSS_SELECTOR, ".ct_dis") else "Không có địa chỉ"

                data.append([title, description, area, price, address])
            except Exception as e:
                print(f"Lỗi lấy tin: {e}")
                continue
        page += 1

    driver.quit()

    # 3. Lưu dữ liệu vào file Excel và CSV
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    df = pd.DataFrame(data, columns=["Tiêu đề", "Mô tả", "Diện tích", "Giá", "Địa chỉ"])

    excel_file = f"alonhadat_hanoi_{today}.xlsx"
    csv_file = f"alonhadat_hanoi_{today}.csv"

    df.to_excel(excel_file, index=False)
    df.to_csv(csv_file, index=False, encoding='utf-8-sig')

    print(f"Đã lưu file Excel: {excel_file}")
    print(f"Đã lưu file CSV: {csv_file}")

 
# 4. Lên lịch chạy lúc 6h sáng hàng ngày
# schedule.every().day.at("06:00").do(crawl_data)
crawl_data()

print("Đang chờ đến 6h sáng mỗi ngày để chạy....")
while True:
    schedule.run_pending()
    time.sleep(60)
