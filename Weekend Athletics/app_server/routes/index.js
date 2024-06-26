var express = require('express');
var router = express.Router();
const crtlMain = require('../controllers/main')
var fs = require('fs');
var blogs = JSON.parse(fs.readFileSync('./data/blogs.json', 'utf8'));

/* GET home page. */
router.get('/', crtlMain.index);

module.exports = router;