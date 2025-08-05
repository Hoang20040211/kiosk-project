let foundPatient = false;

async function goToStep2() {
  const cccd = document.getElementById("cccd").value.trim();
  if (!cccd) {
    alert("Vui lòng nhập số CCCD.");
    return;
  }

  try {
    const response = await fetch(`http://localhost:8000/patients/patients/by-cccd/${cccd}`);
    if (!response.ok) throw new Error("Không tìm thấy bệnh nhân.");

    const data = await response.json();
    document.getElementById("fullname").textContent = data.full_name;
    document.getElementById("dob").textContent = data.date_of_birth;
    document.getElementById("gender").textContent = data.gender;
    document.getElementById("phone").textContent = data.phone_number;
    document.getElementById("address").textContent = data.address;
    document.getElementById("patient-info").style.display = "block";
    document.getElementById("next-button").style.display = "block";

  } catch (error) {
    // Không có bệnh nhân → hiển thị form nhập thông tin
    renderManualForm(cccd);
  }
}

function renderManualForm(cccd) {
  const container = document.getElementById("manual-form-container");
  container.innerHTML = `
    <h4>Không tìm thấy bệnh nhân. Vui lòng nhập thông tin:</h4>
    <label>Họ tên:</label>
    <input type="text" id="full_name" />

    <label>Ngày sinh:</label>
    <input type="date" id="dob" />

    <label>Giới tính:</label>
    <div class="gender-group">
      <label><input type="radio" name="gender" value="Nam" /> Nam</label>
      <label><input type="radio" name="gender" value="Nữ" /> Nữ</label>
      <label><input type="radio" name="gender" value="Khác" /> Khác</label>
    </div>

    <label>Số điện thoại:</label>
    <input type="text" id="phone" />

    <label>Email:</label>
    <input type="text" id="email" />

    <label>Địa chỉ:</label>
    <input type="text" id="address" />

    <div class="button-group">
      <button class="btn primary" onclick="submitNewPatient('${cccd}')">Gửi & Tiếp tục</button>
    </div>  `;
  container.style.display = "block";
}

async function submitNewPatient(cccd) {
  const full_name = document.getElementById("full_name").value.trim();
  const date_of_birth = document.getElementById("dob").value;
  const gender = document.querySelector('input[name="gender"]:checked')?.value;
  const phone_number = document.getElementById("phone").value.trim();
  const email = document.getElementById("email").value.trim();
  const address = document.getElementById("address").value.trim();

  if (!full_name || !date_of_birth || !gender || !phone_number || !email || !address) {
    alert("Vui lòng điền đầy đủ thông tin.");
    return;
  }

  try {
    const payload = {
      full_name,
      gender,
      date_of_birth,
      phone_number,
      email,
      address,
      cccd,
      users_id: 1 // hoặc lấy từ session nếu có
    };

    const res = await fetch("http://localhost:8000/patients/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    if (!res.ok) throw new Error("Không thể lưu bệnh nhân");

    alert("Đã thêm bệnh nhân mới.");
    window.location.href = "step2.html";

  } catch (err) {
    alert("Lỗi khi lưu thông tin: " + err.message);
  }
}

function goToStep2Page() {
  window.location.href = "step2.html";
}
