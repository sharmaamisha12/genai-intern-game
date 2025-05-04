let score = 0;
let history = [];

async function submitGuess() {
  const guess = document.getElementById("guessInput").value;
  const persona = document.getElementById("persona").value;
  if (!guess) return;

  const res = await fetch(`http://localhost:8000/api/guess`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-Persona": persona
    },
    body: JSON.stringify({ guess })
  });

  const data = await res.json();
  document.getElementById("guessInput").value = "";

  if (data.game_over) {
    document.getElementById("gameOver").classList.remove("hidden");
    return;
  }

  document.getElementById("result").textContent = `✅ ${data.message}`;
  document.getElementById("score").textContent = `Score: ${data.score}`;

  history.push(data.guess);
  if (history.length > 5) history.shift();

  const historyList = document.getElementById("historyList");
  historyList.innerHTML = "";
  history.forEach(item => {
    const li = document.createElement("li");
    li.textContent = item;
    historyList.appendChild(li);
  });

  document.getElementById("globalCount").textContent = `🌎 Global count: ${data.global_count}`;
}
