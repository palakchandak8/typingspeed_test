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
