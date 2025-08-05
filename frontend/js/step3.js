window.onload = function () {
  // Giả lập thông tin bệnh nhân - bạn có thể thay bằng localStorage nếu cần
  const patientName = "Nguyễn Văn A";  // Lưu từ step1 nếu cần
  const clinicMap = {
    pk1: "Nội tổng hợp",
    pk2: "Nhi",
    pk3: "Tai Mũi Họng"
  };

  const clinicKey = localStorage.getItem('selectedClinic') || 'pk1';
  const clinicName = clinicMap[clinicKey] || "Không rõ";

  const services = JSON.parse(localStorage.getItem('selectedServices') || '[]');

  const stt = Math.floor(100 + Math.random() * 900);  // Random số thứ tự

  // Cập nhật DOM
  document.querySelector('#print-area .info-line:nth-child(2)').innerHTML = `<strong>Họ tên:</strong> ${patientName}`;
  document.querySelector('#print-area .info-line:nth-child(3)').innerHTML = `<strong>Phòng khám:</strong> ${clinicName}`;
  document.querySelector('#print-area .info-line:nth-child(4)').innerHTML = `<strong>Dịch vụ:</strong> ${services.join(', ')}`;
  document.querySelector('#print-area .info-line:nth-child(5)').innerHTML = `<strong>Số thứ tự:</strong> ${stt}`;
  document.querySelector('#print-area .info-line:nth-child(6)').innerHTML = `<strong>Mã QR:</strong> <span class="qr-placeholder">#${stt}-${clinicKey}</span>`;
}
