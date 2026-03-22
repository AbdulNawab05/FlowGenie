async function generate() {
    const text = document.getElementById("inputText").value.trim();
    const output = document.getElementById("output");

    if (!text) {
        output.innerHTML = `<div class="empty-state">Please enter a prompt.</div>`;
        return;
    }

    output.innerHTML = `
        <div class="loading">
            <span>Generating flowchart</span>
            <span class="dots">
                <span></span>
                <span></span>
                <span></span>
            </span>
        </div>
    `;

    try {
        const res = await fetch("/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text })
        });

        const data = await res.json();

        if (!res.ok) {
            output.innerHTML = `<pre style="color:#b91c1c;">${data.error || "Backend error"}</pre>`;
            return;
        }

        if (!data.diagram || !data.diagram.startsWith("flowchart TD")) {
            output.innerHTML = `<pre style="color:#b91c1c;">Invalid Mermaid returned:\n${data.diagram || "No diagram returned"}</pre>`;
            return;
        }

        output.innerHTML = "";
        const mermaidDiv = document.createElement("div");
        mermaidDiv.className = "mermaid";
        mermaidDiv.textContent = data.diagram;
        output.appendChild(mermaidDiv);

        try {
            await mermaid.run({
                nodes: [mermaidDiv]
            });
        } catch (err) {
            console.error("Mermaid parse error:", err);
            output.innerHTML = `<pre style="color:#b91c1c;">Mermaid parse error:\n${data.diagram}</pre>`;
        }

    } catch (error) {
        console.error("Fetch error:", error);
        output.innerHTML = `<pre style="color:#b91c1c;">Connection error. Make sure the Flask server is running.</pre>`;
    }
}

function clearFlowchart() {
    document.getElementById("inputText").value = "";
    document.getElementById("inputText").style.height = "24px";
    document.getElementById("output").innerHTML = `<div class="empty-state">Your flowchart will appear here.</div>`;
}

const inputBox = document.getElementById("inputText");

inputBox.addEventListener("keydown", function(event) {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        generate();
    }
});

inputBox.addEventListener("input", function () {
    this.style.height = "24px";
    this.style.height = Math.min(this.scrollHeight, 140) + "px";
});