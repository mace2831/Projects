var express = require('express');
var router = express.Router();
var controller = require('../controllers/baseball');

/*Get baseball page*/
router.get('/', controller.baseball);

module.exports = router;