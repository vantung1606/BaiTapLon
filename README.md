# 🏙️ Web Scraper: Mặt bằng cần bán tại Hà Nội - Alonhadat.com.vn

Dự án này sử dụng Python và Selenium để tự động thu thập thông tin các tin đăng **mặt bằng cần bán tại Hà Nội** từ trang [alonhadat.com.vn](https://alonhadat.com.vn). Dữ liệu được lưu dưới định dạng Excel và CSV, và script có thể được lên lịch để chạy tự động hàng ngày vào lúc 6h sáng.

## 📌 Thông tin thu thập

- **Tiêu đề**
- **Mô tả ngắn**
- **Diện tích**
- **Giá**
- **Địa chỉ**

## 🚀 Cách sử dụng

### 1. Clone repository

```bash
git clone https://github.com/vantung1606/BaiTapLon.git
cd BaiTapLon
```

### 2. Cài đặt thư viện cần thiết

Tạo môi trường ảo (khuyến nghị) và cài đặt yêu cầu:

```bash
pip install -r requirements.txt
```

**requirements.txt** gồm:
```txt
selenium
webdriver-manager
pandas
schedule
```

### 3. Chạy script thủ công

```bash
python alonhadat.py
```

File Excel/CSV sẽ được tạo theo định dạng:  
`alonhadat_hanoi_YYYY-MM-DD.xlsx`  
`alonhadat_hanoi_YYYY-MM-DD.csv`

### 4. Lên lịch tự động (mặc định 6h sáng mỗi ngày)

Script có sử dụng thư viện `schedule` để tự động chạy mỗi ngày lúc 6h sáng. Để script luôn chạy:

```bash
python alonhadat.py
```

> **Lưu ý**: Bạn cần giữ script này luôn hoạt động (chạy liên tục) hoặc cấu hình `cron` (Linux/macOS) hoặc Task Scheduler (Windows) để chạy script mỗi ngày.

## 📁 Cấu trúc file

```
.
├── main.py               # Script chính để crawl dữ liệu
├── requirements.txt      # Thư viện cần thiết
├── README.md             # Hướng dẫn sử dụng
└── alonhadat_hanoi_....  # Các file dữ liệu thu thập (Excel/CSV)
```

## ✅ Tính năng mở rộng (gợi ý)

- Gửi email kèm file mỗi sáng
- Giao diện người dùng đơn giản với Tkinter hoặc Streamlit
- Lưu dữ liệu vào database (MySQL, SQLite...)
