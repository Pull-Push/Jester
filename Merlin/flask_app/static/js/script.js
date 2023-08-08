var themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
var themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

const test = function(){
    alert("connected")
}


// Change the icons inside the button based on previous settings
if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    themeToggleLightIcon.classList.remove('hidden');
} else {
    themeToggleDarkIcon.classList.remove('hidden');
}

var themeToggleBtn = document.getElementById('theme-toggle');

themeToggleBtn.addEventListener('click', function() {

    // toggle icons inside button
    themeToggleDarkIcon.classList.toggle('hidden');
    themeToggleLightIcon.classList.toggle('hidden');

    // if set via local storage previously
    if (localStorage.getItem('color-theme')) {
        if (localStorage.getItem('color-theme') === 'light') {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        }

    // if NOT set via local storage previously
    } else {
        if (document.documentElement.classList.contains('dark')) {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        } else {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        }
    }
    
});

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
        "seed1" : document.getElementById("seed1").value,
        "seed2" :document.getElementById("seed2").value,
        "seed3" : document.getElementById("seed3").value,
        "message": document.getElementById('toenc').value
    };
    $.ajax({
        url: '/encrypt',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ 'key': cypher }),
        success: function(response) {
            console.log("Sent to Backend");
            socketio.emit("message", {data: response})
            toenc.value = "";
        },
        error: function(error) {
            console.log(error);
        }
    });
}
const decrypt = (text) => {
    let cypher = {
        "shift": document.getElementById("shift").value,
        "seed1" : document.getElementById("seed1").value,
        "seed2" :document.getElementById("seed2").value,
        "seed3" : document.getElementById("seed3").value,
        "message": text.innerHTML
    };
    $.ajax({
        url: '/decrypt',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ 'key': cypher }),
        success: function(response) {
            console.log("Sent to Backend");
            // socketio.emit("message", {data: response})
            // console.log(response)
            document.getElementById('lower').innerHTML = response
        },
        error: function(error) {
            console.log(error);
        }
    });
}

socketio.on("message", (data) =>{
    createMessage(data.name, data.message);
});

const sendMessage = () => {
    const message = document.getElementById("message")
    if (message.value == "") return;
    socketio.emit("message", {data: message.value})
    message.value = "";
};
