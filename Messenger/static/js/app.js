let currentRecipient = '';
let chatInput = $('#chat-input');
let chatButton = $('#btn-send');
let groupList = $('#group-list');
let userList = $('#user-list');
let messageList = $('#messages');

let groupListData = [];

$(`<span>Current user: ${currentUserName}</span>`).appendTo('.current-user');

function updateGroupList() {
    $.getJSON('group-chat/', data => {
        groupListData = data;
        userList.children('.group').remove();
        for (let i = 0; i < data.length; i++) {
            const groupItem = `<a class="list-group-item group" id="${data[i].id}">${data[i]['name']}</a>`;
            $(groupItem).appendTo('#group-list');
        }
        $('.group').click(() => {
            groupList.children('.active').removeClass('active');
            let selected = event.target;
            $(selected).addClass('active');
            setCurrentRecipient(selected);
        });
    })
        .then(() => updateUserList());
}
function updateUserList() {
    $.getJSON('user/', users => {
        userList.children('.user').remove();
        for (let i = 0; i < users.length; i++) {
            const user = users[i];
            if (user.id !== currentUserId) {
                 const userItem = `<a class="list-group-item user">
                    ${user['username']}
                    <button class="btn-plus pull-right add-user" id="${user.id}" title="Add User for Group">+</button>
                </a>`;
                $(userItem).appendTo('#user-list');
            }

        }
        $('.add-user').click(() => {
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
    if (message.sender.id === currentUserId) position = 'right';
    const messageItem = `
            <li class="message ${position}">
                <img class="avatar" src="${message.recipient.avatar}">
                <p class="username">${message.recipient.username}</p>
                <div class="text_wrapper">
                    <div class="text">${message.body}<br>
                        <span class="small">${date}</span>
                    </div>
                </div>
            </li>`;
    $(messageItem).appendTo('#messages');
}

function getConversation(group_chat) {
    $.getJSON(`/messenger/message/?group_chat_id=${group_chat.id}`, data => {
        messageList.children('.message').remove();
        for (let i = data.length - 1; i >= 0; i--) {
            drawMessage(data[i]);
        }
        messageList.animate({scrollTop: messageList.prop('scrollHeight')});
    });

}

function getMessageById(message) {
    id = JSON.parse(message).message
    $.getJSON(`/messenger/message/${id}/`, data => {
        if (data.user === currentRecipient ||
            (data.recipient === currentRecipient && data.user == currentUserId)) {
            drawMessage(data);
        }
        messageList.animate({scrollTop: messageList.prop('scrollHeight')});
    });
}

function sendMessage(groupId, body) {
    let currentGroup = groupListData.find(x => x.id === Number(groupId));
    let recipientId = currentGroup.participants[1].id; // Todo

    $.post('/messenger/message/', {
        recipient: {'id': recipientId},
        body: body
    })
    // .fail(() => alert('Error! Check console!'));
}

function setCurrentRecipient(group_chat) {
    currentRecipient = group_chat.id;
    getConversation(group_chat);
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
    updateGroupList();
    disableInput();
    // let socket = new WebSocket(`ws://127.0.0.1:8000/?session_key=${sessionKey}`);

    const socket = new WebSocket('ws://' + window.location.host + '/ws?session_key=${sessionKey}')

    chatInput.keypress(e => {
        if (e.keyCode == 13)
            chatButton.click();
    });

    chatButton.click(() => {
        if (chatInput.val().length > 0) {
            sendMessage(currentRecipient, chatInput.val());
            chatInput.val('');
        }
    });

    socket.onmessage = e => getMessageById(e.data);
});



