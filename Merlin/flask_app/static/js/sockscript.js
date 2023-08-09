var socketio = io();
const messages = document.getElementById("messages")
const createMessage = (name, msg) => {
    const content = `
    <div class="text">
        <span>
            <strong>${name}</strong>: <span id="single" onclick="decrypt(this)">${msg}</span>
            </span>
            <span class="muted">
                ${new Date().toLocaleString()}
                </span>
        </div>
    `
    messages.innerHTML += content;
};

const encrypt = () => {
    let cypher = {
        "shift": document.getElementById("shift").value,
        "seed1": document.getElementById("seed1").value,
        "seed2": document.getElementById("seed2").value,
        "seed3": document.getElementById("seed3").value,
        "message": document.getElementById('toenc').value
    };
    $.ajax({
        url: '/encrypt',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ 'key': cypher }),
        success: function (response) {
            console.log("Sent to Backend");
            socketio.emit("message", { data: response })
            toenc.value = "";
        },
        error: function (error) {
            console.log(error);
        }
    });
}
const decrypt = (text) => {
    let cypher = {
        "shift": document.getElementById("shift").value,
        "seed1": document.getElementById("seed1").value,
        "seed2": document.getElementById("seed2").value,
        "seed3": document.getElementById("seed3").value,
        "message": text.innerHTML
    };
    $.ajax({
        url: '/decrypt',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ 'key': cypher }),
        success: function (response) {
            console.log("Sent to Backend");
            // socketio.emit("message", {data: response})
            // console.log(response)
            document.getElementById('lower').innerHTML = response
        },
        error: function (error) {
            console.log(error);
        }
    });
}

socketio.on("message", (data) => {
    createMessage(data.name, data.message);
});

const sendMessage = () => {
    const message = document.getElementById("message")
    if (message.value == "") return;
    socketio.emit("message", { data: message.value })
    message.value = "";
};