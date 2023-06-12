const form = document.getElementById('qrCodeForm');
const qrCodeResult = document.getElementById('qrCodeResult');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const websiteLink = document.getElementById('websiteLink').value;

  try {
    const response = await fetch(`http://tools.williamgay.me/api/generate_qr_code/?website_link=${websiteLink}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
    });

    const data = await response.json();

    if (response.ok) {
      qrCodeResult.innerHTML = `
        <p>QR Code generated successfully. Download link: 
            <a href="${data.qr_code_url}" download>Download QR Code</a>
        </p>
        `;
    } else {
      qrCodeResult.innerHTML = `
        <p>QR Code generation failed. Error: ${data.detail}</p>
        `;
    }
  } catch (error) {
    qrCodeResult.innerHTML = `
        <p>QR Code generation failed. Error: ${error.message}</p>
        `;
  }
});
