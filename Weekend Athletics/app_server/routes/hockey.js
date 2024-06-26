var express = require('express');
var router = express.Router();
var controller = require('../controllers/hockey');

/*Get hockey page*/
router.get('/', controller.hockey);

module.exports = router;