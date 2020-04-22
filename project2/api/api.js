const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const cors = require("cors");

//Middlewares
app.use(bodyParser.json());
app.use(cors());

// Listtening on PORT 3001
app.listen(3001);

// Connect to Influx db
const Influx = require("influxdb-nodejs");
const client = new Influx("http://127.0.0.1:8086/stock");

app.get("/:company", (req, res) => {
  console.log("calling query: "+ req.params.company.toUpperCase());
  client
    .query(req.params.company.toUpperCase())
    .then((data) => {
        console.log("Data: " + data.results.series);
        if(data.results.series !== undefined){
            res.json((data.results[0].series[0].values));
        }
    })
    .catch(console.error);
});
