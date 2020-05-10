const express = require('express');
const app = express();
const https = require('https');
const port = 3025;

// app.use(express.static('./'));
app.get('/lights', (req, res) => {
    
    const spawn = require('child_process').spawn;
    const pythonProcess = spawn('python', ['./scripts/decora-wifi-fetch-status.py', 'griffibr@gmail.com', 'ILike#23']);

    pythonProcess.stdout.on('data', (data) =>{
        res.header('Access-Control-Allow-Origin', '*');
        data = data.toString();
        data = data.replace(/\'/g, "\"");
        data = data.replace(/false/gi, '"false"');
        data = data.replace(/true/gi, '"true"');
        data = data.replace(/none/gi, '"none"');

        const data2 = JSON.parse(data.replace(/\'/g, "\""));
        res.send(data2);
    });

});

app.get('/light_update/:switchid/:action/:dim', (req, res) => {
    var switchid = req.params.switchid;
    var action = req.params.action;
    var dim = req.params.dim | null;

    const spawn = require('child_process').spawn;
    const pythonProcess = spawn('python', ['./scripts/decora-wifi-update-attrib.py', 'griffibr@gmail.com', 'ILike#23', parseInt(switchid), action, parseInt(dim)]);

    res.header('Access-Control-Allow-Origin', '*');
    res.send('Mighta worked?' + switchid);
});

app.get('/makerTrigger/:action/:key', (req, res) => {
    const action = req.params.action;
    const apiKey = req.params.key;

    const options = {
        hostname: 'maker.ifttt.com',
        port: 443,
        path: '/trigger/' + action + '/with/key/' + apiKey,
        method: 'GET'
    }

    const makerReq = https.request(options, res => {
        console.log(`statusCode: ${res.statusCode}`);

        res.on('data', d => {
            process.stdout.write(d);
        });        
    });

    makerReq.on('error', error => {
        console.error(error);
    });
      
    makerReq.end();
});

app.listen(port, () => console.log(`App is listening on port ${port}`));
