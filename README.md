# Kiosk Bệnh Viện

Hệ thống Kiosk hỗ trợ đăng ký khám bệnh gồm 3 bước:
1. Nhập CCCD hoặc thông tin bệnh nhân
2. Chọn dịch vụ khám
3. In phiếu

##

```bash
# 1. Tạo virtual env
python -m venv venv
source venv/bin/activate  # hoặc .\venv\Scripts\activate trên Windows

# 2. Cài đặt thư viện
pip install -r requirements.txt

# 3. Chạy server
uvicorn backend.app.main:app --reload
