$(document).ready(function(){
    var socket = io();

    socket.on('connect', function () {
      console.log('socket client connected');
    });


    socket.on('disconnect', function () {
      console.log('socket client disconnected');
    });

    $("#wb-up").on('click', () => {
        console.log('w');
        socket.emit('wb-navi-commands','w');
    });

    $('#wb-lt').on('click', () => {
        console.log('a');
        socket.emit('wb-navi-commands','a');
    });

    $('#wb-dn').on('click', () => {
        console.log('s');
        socket.emit('wb-navi-commands','s');
    });

    $('#wb-rt').on('click', () => {
        console.log('d');
        socket.emit('wb-navi-commands','d');
    });
})


document.getElementById('map3d').src = "static/pic/" + "20min.png";
document.getElementById('map3d').style.height = "400px";
document.getElementById('map3d').style.width = "800px";

function doSetTimeout(i) {
// setTimeout(function () { alert(i); }, 5000 * i);
setTimeout(function () {
    document.getElementById('cam').src = "static/pic/s" + i + ".png";
    document.getElementById('cam').style.height = "400px";
    document.getElementById('cam').style.width = "800px";
}, 4000 * i);
}

for (var i = 1; i <= 8; ++i) {
doSetTimeout(i);
}