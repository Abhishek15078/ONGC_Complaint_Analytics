async function analyzeComplaint() {

    const complaint =
        document.getElementById("complaint").value;

    const department =
        document.getElementById("department").value;

    const group =
        document.getElementById("group").value;

    const software =
        document.getElementById("software").value;

    const hw_flag =
        parseInt(
            document.getElementById("hw_flag").value
        );

    if (complaint.trim().length < 5) {

        alert("Complaint must contain at least 5 characters.");

        return;
    }

    document.getElementById("loading").style.display = "block";

    document.getElementById("results").innerHTML = "";

    try {

        const response =
            await fetch(
                "https://ongc-complaint-api.onrender.com/predict-all",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        text: complaint,

                        department: department,

                        group: group,

                        software: software,

                        hw_flag: hw_flag

                    })
                }
            );

        const data = await response.json();

        document.getElementById("loading").style.display = "none";

        let priorityClass = "";

        switch (data.priority.toLowerCase()) {

            case "low":
                priorityClass = "priority-low";
                break;

            case "medium":
                priorityClass = "priority-medium";
                break;

            case "high":
                priorityClass = "priority-high";
                break;

            case "critical":
                priorityClass = "priority-critical";
                break;
        }

        const slaClass =
            data.sla_prediction
                .toLowerCase()
                .includes("breached")
                ? "sla-bad"
                : "sla-good";

        const totalHours =
            parseFloat(
                data.estimated_resolution_hours
            );

        const days =
            Math.floor(totalHours / 24);

        const hours =
            Math.round(totalHours % 24);

        document.getElementById("results").innerHTML =

            `
        <div class="results-grid">

            <div class="card">

                <h3>Priority</h3>

                <p class="${priorityClass}">
                    ${data.priority}
                </p>

            </div>

            <div class="card">

                <h3>SLA Status</h3>

                <p class="${slaClass}">
                    ${data.sla_prediction}
                </p>

            </div>

            <div class="card">

                <h3>Resolution Time</h3>

                <p>
                    ${days} Days ${hours} Hours
                </p>

            </div>

        </div>
        `;

    }
    catch (error) {

        document.getElementById("loading").style.display = "none";

        document.getElementById("results").innerHTML =

            `
            <div class="error">
                Unable to connect to FastAPI server.
                Please ensure backend is running.
            </div>
            `;
    }
}
document
.getElementById("dashboardBtn")
.addEventListener(
    "click",
    function(){

        window.open(
            "https://app.powerbi.com/groups/me/reports/414e4b06-74a5-41a1-b229-69dfa6009f85/042c66563d0b7a85d830?experience=power-bi",
            "_blank"
        );

    }
);