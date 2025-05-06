async function submitGuess() {
  const guess = document.getElementById("guessInput").value;
  const response = await fetch("/play", {
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ session_id: "user1", seed: "Rock", guess: guess })
  });
  const result = await response.json();
  document.getElementById("feedback").innerText = result.message;
}
