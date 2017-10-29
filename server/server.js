const express = require('express')
const cors = require('cors')
const app = express()
const path = require('path')
const { exec } = require('child_process');

app.use(cors());

app.get('/:testName', function (req, res) {
  const test = exec(`robot --listener ${path.resolve(__dirname + '/../listener.py')} ` +
                    `${path.resolve(__dirname + '/../tests/' + req.params.testName + '.robot')} ` + 
                    `${path.resolve(__dirname + '/../tests/Results')}`,
                    (err, stdout, stderr) => {
      if (err) {
        console.error(`exec error: ${err}`);
        return
      }
    })

  test.stdout.on('data', (data) => {
    console.log(data);
  });

  test.stderr.on('data', (data) => {
    console.error(data);
  });

  test.on('error', (error) => {
    console.error(error);
  });

  test.on('exit', function (code, signal) {
    console.log('child process exited with ' +
                `code ${code} and signal ${signal}`);
  });

  res.send('Starting listener');
});

app.listen(3001, function () {
  console.log('Example app listening on port 3000!')
});