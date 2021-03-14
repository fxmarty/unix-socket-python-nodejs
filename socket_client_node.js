const net = require('net');

var mysocket = net.createConnection('./uds_socket');

mysocket.on("connect", function() {
    console.log("connect")
});

mysocket.on("data", function(data) {
    console.log(data.toString())
    message1();
    setTimeout(message2, 3000);
});

function message1() {
    mysocket.write('My answer to you <3');
}

function message2() {
    mysocket.write('stop');
}
