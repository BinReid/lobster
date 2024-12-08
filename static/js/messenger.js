// messenger.js
document.addEventListener("DOMContentLoaded", function () {
    const messageForm = document.querySelector('form');
    
    messageForm.addEventListener('submit', function (e) {
        e.preventDefault();
        
        const messageInput = messageForm.querySelector('input[name="message"]');
        const messageText = messageInput.value;
        
        if (messageText) {
            // Отправка сообщения через AJAX
            fetch(messageForm.action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: 'message=' + encodeURIComponent(messageText)
            })
            .then(response => response.json())
            .then(data => {
                // Динамическое добавление сообщения на страницу
                const messagesDiv = document.querySelector('.messages');
                const newMessage = document.createElement('div');
                newMessage.classList.add('message');
                newMessage.innerHTML = `<span class="sender">${data.sender}</span>: <span class="text">${data.text}</span>`;
                messagesDiv.appendChild(newMessage);
                
                messageInput.value = '';  // Очистка поля ввода
            });
        }
    });
});
