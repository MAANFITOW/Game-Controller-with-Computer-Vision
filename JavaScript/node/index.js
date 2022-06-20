var express = require('express');
var app = express();
var spawn = require('child_process').spawn;

// Comenzamos abriendo el programa
var net = spawn('../net/NetApp/NetApp/bin/Debug/NetApp.exe');

net.stdout.on('data', function (data) {

    console.log("Recibi este mensaje: " + data.toString());
        
});
app.get('/', function(req, res) {

    console.log('Te mandaron un mensajito jiji ' + req.query.movimiento + ', ' + req.query.brincar);
    net.stdin.write(req.query.movimiento + ',' + req.query.brincar + ',' + req.query.acelerar + "\r\n");
    res.send('Hola pana')

});

app.use(express.static('public'));

app.listen(3000, function () {

    console.log('El servidor está activo!!!');

});