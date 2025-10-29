const BACKEND_URL = "http://localhost:8001";

document.getElementById("uploadPdfBtn").onclick = async () => {
  const fileInput = document.getElementById("pdfFile");
  const status = document.getElementById("pdfStatus");
  if (!fileInput.files.length) { status.textContent = "Select a PDF."; return; }
  const file = fileInput.files[0];
  status.textContent = "Uploading...";
  const fd = new FormData();
  fd.append("file", file);
  try {
    const res = await fetch(BACKEND_URL + "/api/upload-document", { method: "POST", body: fd });
    const j = await res.json();
    status.textContent = j.detail || "Indexed";
  } catch (e) {
    status.textContent = "Upload failed";
    console.error(e);
  }
};

document.getElementById("uploadImgBtn").onclick = async () => {
  const fileInput = document.getElementById("imgFile");
  const status = document.getElementById("imgStatus");
  if (!fileInput.files.length) { status.textContent = "Select an image."; return; }
  const file = fileInput.files[0];
  status.textContent = "Uploading...";
  const fd = new FormData();
  fd.append("file", file);
  try {
    const res = await fetch(BACKEND_URL + "/api/upload-image", { method: "POST", body: fd });
    const j = await res.json();
    status.textContent = j.detail || "Indexed";
  } catch (e) {
    status.textContent = "Upload failed";
    console.error(e);
  }
};

document.getElementById("askBtn").onclick = async () => {
  const q = document.getElementById("questionInput").value;
  const out = document.getElementById("answerArea");
  if (!q) { out.textContent = "Type a question."; return; }
  out.textContent = "Thinking...";
  try {
    const res = await fetch(BACKEND_URL + "/api/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: q })
    });
    const j = await res.json();
    out.innerHTML = "";
    if (j.answer) {
      const a = document.createElement("div");
      a.innerHTML = `<strong>Answer:</strong><div style="margin-top:8px">${j.answer}</div>`;
      out.appendChild(a);
    }
    if (j.sources) {
      const s = document.createElement("div");
      s.style.marginTop = "10px";
      s.innerHTML = `<strong>Sources:</strong><pre style="white-space:pre-wrap">${JSON.stringify(j.sources, null, 2)}</pre>`;
      out.appendChild(s);
    }
  } catch (e) {
    out.textContent = "Query failed";
    console.error(e);
  }
};
