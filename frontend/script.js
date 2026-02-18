let startTime = 0;

fetch("/start")
.then(res => res.json())
.then(data => {
    document.getElementById("sentence").innerText = data.sentence;
    startTime = data.start_time;
});

function submitTest() {
    let typedText = document.getElementById("input").value;

    fetch("/result", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ typed: typedText, start: startTime })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("wpm").innerText = data.wpm;
        document.getElementById("accuracy").innerText = data.accuracy + "%";
        document.getElementById("time").innerText = data.time + "s";
    });
}
```

---

## Step 4: Commit All 3 Files on GitHub

For each file, click the pencil → paste the new code → scroll down → click **"Commit changes"** → commit to `main`.

---

## How Live Updates Work in Azure

Once you commit, this is the automatic flow:
```
You commit on GitHub
        ↓
GitHub Actions triggers automatically
        ↓
Builds & tests your code (2-3 mins)
        ↓
Deploys to Azure App Service
        ↓
Your live site updates — no manual steps!
