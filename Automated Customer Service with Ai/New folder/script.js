function sendMessage() {
    let msg = document.getElementById('user-input').value;
    let domain = document.getElementById('domain').value;
    if(msg.trim()==='') return;

    let chat = document.getElementById('chat-box');
    chat.innerHTML += `<div class='user'><b>You:</b> ${msg}</div>`;

    fetch('/chat', {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({domain: domain, message: msg})
    })
    .then(res=>res.json())
    .then(data=>{
        chat.innerHTML += `<div class='bot'><b>AI:</b> ${data.reply}</div>`;
        chat.scrollTop = chat.scrollHeight;
    });

    document.getElementById('user-input').value='';
}
