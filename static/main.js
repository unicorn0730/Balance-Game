const chat = document.getElementById('chat');
const promptBox = document.getElementById('prompt');
const sendBtn = document.getElementById('send');

function addMessage(text, role) {
  const div = document.createElement('div');
  div.classList.add('message', role);
  div.textContent = text;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

async function sendPrompt() {
  const prompt = promptBox.value.trim();
  if (!prompt) return;
  addMessage(prompt, 'user');
  promptBox.value = '';
  sendBtn.disabled = true;
  try {
    const res = await fetch('/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt })
    });
    const data = await res.json();
    addMessage(data.response, 'assistant');
  } catch (err) {
    addMessage('Error: ' + err, 'assistant');
  } finally {
    sendBtn.disabled = false;
  }
}

sendBtn.addEventListener('click', sendPrompt);
promptBox.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendPrompt();
  }
});
