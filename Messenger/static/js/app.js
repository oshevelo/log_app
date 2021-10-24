let currentRecipient = '';
let chatInput = $('#chat-input');
let chatButton = $('#btn-send');
let userList = $('#user-list');
let messageList = $('#messages');

function updateUserList() {
    $.getJSON('api/users/', data => {
        userList.children('.user').remove();
        for (let i = 0; i < data.length; i++) {
            const userItem = `<a class="list-group-item user" id="${data[i].id}">${data[i]['username']}</a>`;
            $(userItem).appendTo('#user-list');
        }
        $('.user').click(() => {
            userList.children('.active').removeClass('active');
            let selected = event.target;
            $(selected).addClass('active');
            setCurrentRecipient(selected);
        });
    });
}

function drawMessage(message) {
    let position = 'left';
    const date = new Date(message.timestamp);
    if (message.user === currentUser) position = 'right';
    const messageItem = `
            <li class="message ${position}">
                <img class="avatar" src="${message.user.avatar}">
                <p class="username">${message.user.username}</p>
                <div class="text_wrapper">
                    <div class="text">${message.body}<br>
                        <span class="small">${date}</span>
                    </div>
                </div>
            </li>`;
    $(messageItem).appendTo('#messages');
}

function getConversation(user) {
    console.log(user);
    $.getJSON(`/messenger/api/message?target=${user.id}`, data => {
        messageList.children('.message').remove();
        for (let i = data.length - 1; i >= 0; i--) {
            drawMessage(data[i]);
        }
        messageList.animate({scrollTop: messageList.prop('scrollHeight')});
    });

}

function getMessageById(message) {
    id = JSON.parse(message).message
    $.getJSON(`/api/message/${id}/`, data => {
        if (data.user === currentRecipient ||
            (data.recipient === currentRecipient && data.user == currentUser)) {
            drawMessage(data);
        }
        messageList.animate({scrollTop: messageList.prop('scrollHeight')});
    });
}

function sendMessage(recipient, body) {
    $.post('/api/message/', {
        recipient: recipient,
        body: body
    })
    .fail(() => alert('Error! Check console!'));
}

function setCurrentRecipient(user) {
    currentRecipient = user.text;
    getConversation(user);
    enableInput();
}


function enableInput() {
    chatInput.prop('disabled', false);
    chatButton.prop('disabled', false);
    chatInput.focus();
}

function disableInput() {
    chatInput.prop('disabled', true);
    chatButton.prop('disabled', true);
}

$(document).ready(function () {
    updateUserList();
    disableInput();

// Todo: Connect for WS
    // const socket = new WebSocket('ws://' + window.location.host + '/ws?session_key=${sessionKey}')
    //
    // chatInput.keypress(e => {
    //     if (e.keyCode == 13)
    //         chatButton.click();
    // });
    //
    // chatButton.click(() => {
    //     if (chatInput.val().length > 0) {
    //         sendMessage(currentRecipient, chatInput.val());
    //         chatInput.val('');
    //     }
    // });
    //
    // socket.onmessage = e => getMessageById(e.data);
});



