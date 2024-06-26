var express = require('express');
var router = express.Router();
var controller = require('../controllers/e_sports');

/*Get e-sports page*/
router.get('/', controller.e_sports);

module.exports = router;