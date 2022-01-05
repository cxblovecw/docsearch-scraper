const fs = require('fs');
const { argv } = require('process');

const [,,APPLICATION_ID,API_KEY,INDEX_NAME,START_URLS] = argv;

console.log(APPLICATION_ID,API_KEY,INDEX_NAME,START_URLS);
 
fs.writeFileSync('./.env',`APPLICATION_ID=${APPLICATION_ID}
API_KEY=${API_KEY}
CHROMEDRIVER_PATH=./chromedriver`);


fs.writeFileSync('./config.json',`{
  "index_name": "${INDEX_NAME}",
  "start_urls": [
    "${START_URLS}"
  ],
  "stop_urls": [],
  "selectors": {
    "lvl0": "h1",
    "lvl1": "h2",
    "lvl2": "h3",
    "lvl3": "h4",
    "lvl4": "h5",
    "lvl5": "h6",
    "text": "p, li",
    "lang": {
      "selector": "/html/@lang",
      "type": "xpath",
      "global": true
    }
  },
  "custom_settings": {
    "attributesForFaceting": [
      "lang"
    ]
  }
}`)