var express = require('express');
var router = express.Router();
var controller = require('../controllers/mma');

/*Get mma page*/
router.get('/', controller.mma);

module.exports = router;