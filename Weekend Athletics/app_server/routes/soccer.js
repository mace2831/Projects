var express = require('express');
var router = express.Router();
var controller = require('../controllers/soccer');

/*Get mma page*/
router.get('/', controller.soccer);

module.exports = router;