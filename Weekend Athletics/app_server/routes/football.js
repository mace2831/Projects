var express = require('express');
var router = express.Router();
var controller = require('../controllers/football');

/*Get football page*/
router.get('/', controller.football);

module.exports = router;