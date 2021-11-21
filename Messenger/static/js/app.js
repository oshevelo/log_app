let groupChatId = null;
let chatInput = $('#chat-input');
let chatButton = $('#btn-send');
let groupList = $('#group-list');
let userList = $('#user-list');
let messageList = $('#messages');
let groupListData = [];
let socket = null;

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
        // .then(() => updateUserList());
}
// function updateUserList() {
//     $.getJSON('user/', users => {
//         userList.children('.user').remove();
//         for (let i = 0; i < users.length; i++) {
//             const user = users[i];
//             if (user.id !== currentUserId) {
//                  const userItem = `<a class="list-group-item user">
//                     ${user['username']}
//                     <button class="btn-plus pull-right add-user" id="${user.id}" title="Add User for Group">+</button>
//                 </a>`;
//                 $(userItem).appendTo('#user-list');
//             }
//
//         }
//         $('.add-user').click(() => {
//             userList.children('.active').removeClass('active');
//             let selected = event.target;
//             $(selected).addClass('active');
//             setCurrentRecipient(selected);
//         });
//     });
// }

function drawMessage(message) {
    let position = 'left';
    const date = new Date(message.timestamp);
    if (message.sender.id === currentUserId) position = 'right';
    const messageItem = `
            <li class="message ${position}">
                <!-- <img class="avatar" src="${message.recipient.avatar}"> -->
                <p class="username ${position}">${message.recipient.username}</p>
                <div class="text_wrapper">
                    <div class="text">${message.body}<br>
                        <span class="small">${date}</span>
                    </div>
                </div>
            </li>`;
    $(messageItem).appendTo('#messages');
}

function getConversation(chat_group) {
    if (socket) {
        socket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };
    }
    socket = new WebSocket(
        'ws://' + window.location.host + '/ws/messenger/' + `?session_key=${sessionKey}&chat_group_id=${chat_group.id}`
    )

    socket.onmessage = (e) => getMessageById(e.data);

    $.getJSON(`/messenger/message/?group_chat_id=${chat_group.id}`, data => {
        messageList.children('.message').remove();
        for (let i = data.length - 1; i >= 0; i--) {
            drawMessage(data[i]);
        }
        messageList.animate({scrollTop: messageList.prop('scrollHeight')});
    });

}

function getMessageById(message) {
    console.log(message);
    id = JSON.parse(message).body
    $.getJSON(`/message/${id}/`, data => {
        if (data.user === groupChatId ||
            (data.recipient === groupChatId && data.user == currentUserId)) {
            drawMessage(data);
        }
        messageList.animate({scrollTop: messageList.prop('scrollHeight')});
    });
}

function sendMessage(groupId, body) {
    let currentGroup = groupListData.find(x => x.id === Number(groupId));
    let recipientId = currentGroup.participants[1].id; // Todo
    console.log(recipientId);
    // socket.onmessage = function(e) {
    //     const data = JSON.parse(e.data);
    //     const message = data['message'];
    //     document.querySelector('#chat-log').value += (message + '\n');
    // };
    //

    socket.send(JSON.stringify({
        recipient: {'id': recipientId},
        body: body
    }));

    // $.post('/message/', {
    //     recipient: {'id': recipientId},
    //     body: body
    // })
    // .fail(() => alert('Error! Check console!'));
}

function setCurrentRecipient(chat_group) {
    groupChatId = chat_group.id;
    console.log(chat_group);
    getConversation(chat_group);
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

    chatInput.keypress(e => {
        if (e.keyCode == 13)
            chatButton.click();
    });

    chatButton.click(() => {
        if (chatInput.val().length > 0) {
            sendMessage(groupChatId, chatInput.val());
            chatInput.val('');
        }
    });
});



