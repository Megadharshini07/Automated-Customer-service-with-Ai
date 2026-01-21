function sendMessage() {
body {
    background: linear-gradient(135deg, #667eea, #764ba2);
    font-family: 'Segoe UI', sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.app {
    width: 420px;
    background: white;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.header {
    background: #5a67d8;
    color: white;
    padding: 15px;
    text-align: center;
    font-size: 18px;
}

select {
    width: 100%;
    padding: 10px;
    border: none;
    outline: none;
}

#chat-box {
    height: 320px;
    padding: 10px;
    overflow-y: auto;
    background: #f7f7f7;
}

.user, .bot {
    margin: 8px 0;
    padding: 8px 12px;
    border-radius: 10px;
    max-width: 80%;
}

.user {
    background: #5a67d8;
    color: white;
    margin-left: auto;
}

.bot {
    background: #e2e8f0;
    color: #333;
}

.input-area {
    display: flex;
    border-top: 1px solid #ddd;
}

input {
    flex: 1;
    padding: 12px;
    border: none;
    outline: none;
}

button {
    background: #5a67d8;
    color: white;
    border: none;
    padding: 0 20px;
    cursor: pointer;
}
