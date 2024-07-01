var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/mma', function(req, res, next) {
  res.render('mma', { title: 'MMA' });
});

router.get('/hockey', function(req, res, next) {
  res.render('hockey', { title: 'Hockey' });
});

router.get('/basketball', function(req, res, next) {
  res.render('basketball', { title: 'Basketball' });
});

router.get('/baseball', function(req, res, next) {
  res.render('baseball', { title: 'Baseball' });
});

router.get('/e_sports', function(req, res, next) {
  res.render('e_sports', { title: 'E-Sports' });
});



module.exports = router;
