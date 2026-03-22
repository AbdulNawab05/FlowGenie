const STORAGE_KEY = "jobFunnelApplications";

let applications = JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];

document.getElementById("addBtn").addEventListener("click", addApplication);

function addApplication() {
  const company = document.getElementById("company").value;
  const role = document.getElementById("role").value;
  const companyType = document.getElementById("companyType").value;
  const resumeName = document.getElementById("resumeName").value || "Default Resume";

  const status = document.getElementById("status").value;
  const stage = document.getElementById("stage").value;
  const dateApplied = document.getElementById("dateApplied").value;
  const notes = document.getElementById("notes").value;

  if (!company || !role || !dateApplied) {
    alert("Company, role and date are required.");
    return;
  }

  const application = {
    id: Date.now(),
    company,
    role,
    companyType,
    resumeName,
    status,
    stage,
    dateApplied,
    notes
  };

  applications.push(application);
  save();
  render();
  clearForm();
}

function save() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(applications));
}

function clearForm() {
  document.getElementById("company").value = "";
  document.getElementById("role").value = "";
  document.getElementById("notes").value = "";
}

function deleteApplication(id) {
  applications = applications.filter(app => app.id !== id);
  save();
  render();
}
function renderTable() {
  const tbody = document.querySelector("#appTable tbody");
  tbody.innerHTML = "";

  applications.forEach(app => {
    const tr = document.createElement("tr");

    tr.innerHTML = `
      <td>${app.company}</td>
      <td>${app.role}</td>
      <td>${app.resumeName}</td>
      <td>${app.status}</td>
      <td>${app.stage}</td>
      <td>${app.dateApplied}</td>
      <td><button onclick="deleteApplication(${app.id})">X</button></td>
    `;

    tbody.appendChild(tr);
  });
}
function renderFunnel() {
  const total = applications.length;
  const interviews = applications.filter(a =>
    a.status === "Interview" || a.status === "Offer"
  ).length;
  const offers = applications.filter(a => a.status === "Offer").length;

  const interviewRate = total ? Math.round((interviews / total) * 100) : 0;
  const offerRate = total ? Math.round((offers / total) * 100) : 0;

  document.getElementById("funnelStats").innerHTML = `
    Applied: ${total}<br>
    Interviews: ${interviews} (${interviewRate}%)<br>
    Offers: ${offers} (${offerRate}%)
  `;
}
function renderResumeFunnels() {
  const container = document.getElementById("resumeFunnels");
  container.innerHTML = "";

  const resumeMap = {};

  applications.forEach(app => {
    const name = app.resumeName || "Default Resume";

    if (!resumeMap[name]) {
      resumeMap[name] = { applied: 0, interviews: 0 };
    }

    resumeMap[name].applied++;

    if (app.status === "Interview" || app.status === "Offer") {
      resumeMap[name].interviews++;
    }
  });

  Object.keys(resumeMap).forEach(name => {
    const data = resumeMap[name];
    const rate = data.applied
      ? Math.round((data.interviews / data.applied) * 100)
      : 0;

    container.innerHTML += `
      <div style="margin-bottom:10px;">
        <strong>${name}</strong><br>
        Applied: ${data.applied}<br>
        Interviews: ${data.interviews} (${rate}%)
      </div>
    `;
  });
}
function renderRoleFunnels() {
  const container = document.getElementById("roleFunnels");
  container.innerHTML = "";

  const roleMap = {};

  applications.forEach(app => {
    const role = app.role.trim().toLowerCase();


    if (!roleMap[role]) {
      roleMap[role] = { applied: 0, interviews: 0 };
    }

    roleMap[role].applied++;

    if (app.status === "Interview" || app.status === "Offer") {
      roleMap[role].interviews++;
    }
  });

  Object.keys(roleMap).forEach(role => {
    const data = roleMap[role];

    // Safety: ignore tiny sample sizes
    if (data.applied < 5) return;

    const rate = Math.round((data.interviews / data.applied) * 100);

    container.innerHTML += `
      <div style="margin-bottom:10px;">
       <strong>${role.toUpperCase()}</strong>
        Applied: ${data.applied}<br>
        Interviews: ${data.interviews} (${rate}%)
      </div>
    `;
  });
}

function renderCompanyTypeFunnels() {
  const container = document.getElementById("companyTypeFunnels");
  container.innerHTML = "";

  const typeMap = {};

  applications.forEach(app => {
    const type = app.companyType || "Unknown";

    if (!typeMap[type]) {
      typeMap[type] = { applied: 0, interviews: 0 };
    }

    typeMap[type].applied++;

    if (app.status === "Interview" || app.status === "Offer") {
      typeMap[type].interviews++;
    }
  });

  let shown = false;

  Object.keys(typeMap).forEach(type => {
    const data = typeMap[type];

    if (data.applied < 5) return;

    shown = true;

    const rate = Math.round(
      (data.interviews / data.applied) * 100
    );

    container.innerHTML += `
      <div style="margin-bottom:10px;">
        <strong>${type}</strong><br>
        Applied: ${data.applied}<br>
        Interviews: ${data.interviews} (${rate}%)
      </div>
    `;
  });

  if (!shown) {
    container.innerHTML =
      "<p>More applications needed to analyze company types.</p>";
  }
}



function renderInsights() {
  const container = document.getElementById("insights");
  container.innerHTML = "";

  if (applications.length < 10) {
    container.innerText =
      "More data needed for reliable insights.";
    return;
  }

  renderResumeInsights();
}
function renderFollowUpReminder() {
  const container = document.getElementById("followUpAlert");
  container.innerHTML = "";

  const today = new Date();
  const FOLLOW_UP_DAYS = 21;

  const staleApps = applications.filter(app => {
    if (app.status !== "Applied") return false;

    const appliedDate = new Date(app.dateApplied);
    const diffDays =
      (today - appliedDate) / (1000 * 60 * 60 * 24);

    return diffDays >= FOLLOW_UP_DAYS;
  });

  if (staleApps.length === 0) return;

  container.innerHTML = `
    <strong>Follow-up suggested:</strong>
    ${staleApps.length} application(s) older than ${FOLLOW_UP_DAYS} days.
  `;
}


function render() {
  renderFollowUpReminder();
  renderTable();
  renderFunnel();
  renderResumeFunnels();
  renderRoleFunnels();
  renderCompanyTypeFunnels();
  renderInsights();
}

render();
function renderResumeInsights() {
  const container = document.getElementById("insights");

  // Group by resumeName
  const resumeMap = {};

  applications.forEach(app => {
    const name = app.resumeName || "Default Resume";

    if (!resumeMap[name]) {
      resumeMap[name] = { applied: 0, interviews: 0 };
    }

    resumeMap[name].applied++;

    if (app.status === "Interview" || app.status === "Offer") {
      resumeMap[name].interviews++;
    }
  });

  const resumes = Object.keys(resumeMap);

  // Safety: need at least 2 resumes with enough data
  const validResumes = resumes.filter(
    r => resumeMap[r].applied >= 5
  );

  if (validResumes.length < 2) {
    container.innerHTML += `<p>Not enough data to compare resumes.</p>`;
    return;
  }

  let html = `<h3>Resume Performance</h3>`;
  let bestResume = null;
  let bestRate = 0;

  validResumes.forEach(name => {
    const data = resumeMap[name];
    const rate = Math.round((data.interviews / data.applied) * 100);

    if (rate > bestRate) {
      bestRate = rate;
      bestResume = name;
    }

    html += `<p>
      <strong>${name}</strong>: ${rate}% interview rate
    </p>`;
  });

  html += `<p><em>Best performing resume: ${bestResume}</em></p>`;
  container.innerHTML += html;
}


