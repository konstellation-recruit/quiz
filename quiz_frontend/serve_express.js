var vhost = require('vhost');
var path = require('path');
var express = require('express');
var https = require('https');
var http = require('http');
var fs = require('fs');
var app = express();

var options = {
  key: fs.readFileSync('/home/dev/keys/private.key'),
  cert: fs.readFileSync('/home/dev/keys/__taebit_com.crt'),
  ca: fs.readFileSync('/home/dev/keys/__taebit_com.ca-bundle')
};

http.createServer(app).listen(80);
https.createServer(options, app).listen(443);


// https://stackoverflow.com/questions/50033966/simple-subdomain-with-express


////////////////////////
var homeapp = express();
// https://stackoverflow.com/questions/7450940/automatic-https-connection-redirect-with-node-js-express
homeapp.enable('trust proxy');
homeapp.use((req, res, next) => {
     req.secure ? next() : res.redirect('https://' + req.headers.host + req.url);
});

homeapp.get('/hackathon/apply', function (req, res) { res.redirect( res.redirect('https://forms.gle/uyok8eXNbqcaopN19') ) })
homeapp.get('/hackathon', function (req, res) { res.redirect( res.redirect('https://www.notion.so/Global-DeFi-Online-HACKATHON-ab34f670634045398b2e79394ddfd707') ); })

homeapp.use(express.static(path.join(__dirname, 'build')));
homeapp.get('/*', function (req, res) {
    res.sendFile(path.join(__dirname, 'build', 'index.html'));
});



var dexapp = express();
// https://stackoverflow.com/questions/7450940/automatic-https-connection-redir>
dexapp.enable('trust proxy');
dexapp.use((req, res, next) => {
     req.secure ? next() : res.redirect('https://' + req.headers.host + req.url)
});

var dexdir = "/home/dev/taebit-interface-production";

dexapp.get('/hackathon', function (req, res) { res.redirect('https://www.naver.>
dexapp.use(express.static(path.join(dexdir, 'build')));
dexapp.get('/*', function (req, res) {
    res.sendFile(path.join(dexdir, 'build', 'index.html'));
});


app.use(vhost('taebit.com', homeapp));
app.use(vhost('testapp.taebit.com', dexapp));
