// Mở modal chọn dịch vụ
function openModal() {
  document.getElementById('service-modal').classList.remove('hidden');
}

// Đóng modal
function closeModal() {
  document.getElementById('service-modal').classList.add('hidden');
}

// Lưu dịch vụ đã chọn vào localStorage hoặc biến tạm
function confirmServices() {
  const checkboxes = document.querySelectorAll('.checkbox-group input[type="checkbox"]');
  const selectedServices = [];

  checkboxes.forEach(cb => {
    if (cb.checked) {
      selectedServices.push(cb.value);
    }
  });

  if (selectedServices.length === 0) {
    alert("Vui lòng chọn ít nhất một dịch vụ.");
    return;
  }

  // Lưu vào localStorage để dùng cho step 3
  localStorage.setItem('selectedServices', JSON.stringify(selectedServices));

  closeModal();
}

// Chuyển sang bước 3
function goToStep3() {
  const clinic = document.getElementById('clinic').value;
  if (!clinic) {
    alert("Vui lòng chọn phòng khám.");
    return;
  }

  const services = JSON.parse(localStorage.getItem('selectedServices') || '[]');
  if (services.length === 0) {
    alert("Vui lòng chọn ít nhất một dịch vụ.");
    return;
  }

  // Lưu thông tin vào localStorage
  localStorage.setItem('selectedClinic', clinic);
  // Chuyển trang
  window.location.href = "step3.html";
}
