var express = require('express');
var router = express.Router();
var controller = require('../controllers/others');

/*Get others page*/
router.get('/', controller.others);

module.exports = router;