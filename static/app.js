$(document).ready(function(){
    var socket = io();

    socket.on('connect', function () {
      console.log('socket client connected');
    });


    socket.on('disconnect', function () {
      console.log('socket client disconnected');
    });

    socket.on('gps-change', function (content) {
        console.log("gps: " + content.data);
        $('#gps-wb').text(content.data);
      });

    socket.on('control-change', function (content) {
        console.log("controls: " + content.data);
        //$('#gps-wb').text(content.data);
      });

    socket.on('cam-change', function () {
        console.log("cam changed");
        $('#cam').attr("src", "static/pic/cam-wb.jpg?"+ (new Date()));
    });

    socket.on('map-change', function(){
        console.log("map changed");
        $('#map3d-t').attr("src", "static/maps/map-wb-t.png?"+ (new Date()));
        $('#map3d-f').attr("src", "static/maps/map-wb-f.png?"+ (new Date()));
        $('#map3d-r').attr("src", "static/maps/map-wb-r.png?"+ (new Date()));
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
        console.log('d-sending post msg');
        //socket.emit('wb-navi-commands','d');
        const url = 'http://localhost:5000/gps-wb';
        const data = {
            name : 'ass'
        }
        $.post(url,data,(d,status) =>{
            console.log(status)
        })
    });
})

/*
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
*/