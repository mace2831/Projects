var express = require('express');
var router = express.Router();
var controller = require('../controllers/basketball');

/*Get basketball page*/
router.get('/', controller.basketball);

module.exports = router;