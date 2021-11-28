let groupChatId = null;
let chatInput = $('#chat-input');
let chatButton = $('#btn-send');
let groupList = $('#group-list');
let userList = $('#user-list');
let messageList = $('#messages');
let editGroup = $('#edit-group');
let groupListData = [];
let socket = null;
let groupName = 'Chat';

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
            if(groupName !== event.target.firstChild.data) {
                groupList.children('.active').removeClass('active');
                let selected = event.target;
                    groupName = event.target.firstChild.data;
                    $('.panel-title').text(groupName);
                $(selected).addClass('active');
                groupChatId = selected.id;
                getConversation(selected);
                enableInput();
            }
        });
    })
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
                <p class="username ${position}">${message.sender.username}</p>
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
        socket.close()
    }
    socket = new WebSocket(
        'ws://' + window.location.host + '/ws/messenger/' + `?v=1&chat_group_id=${chat_group.id}&session_key=${sessionKey}`
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
    // $.getJSON(`/message/${JSON.parse(message).group_id}/`, data => {
        drawMessage(JSON.parse(message));
        messageList.animate({scrollTop: messageList.prop('scrollHeight')});
    // });
}

function sendMessage(groupId, body) {
    let currentGroup = groupListData.find(x => x.id === Number(groupId));
    let recipientId = currentGroup.participants[1].id; // Todo

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



