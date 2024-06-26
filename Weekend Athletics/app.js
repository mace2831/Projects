var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var handlebars = require('hbs');

//create the path
var indexRouter = require('./app_server/routes/index');
var usersRouter = require('./app_server/routes/users');
var baseballRouter = require('./app_server/routes/baseball');
var basketballRouter = require('./app_server/routes/basketball');
var e_sportsRouter = require('./app_server/routes/e_sports');
var footballRouter = require('./app_server/routes/football');
var hockeyRouter = require('./app_server/routes/hockey');
var mmaRouter = require('./app_server/routes/mma');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'app_server', 'views'));
app.set('view engine', 'hbs');

//setup handlebars
handlebars.registerPartials(__dirname + '/app_server/views/partials');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

//add the router
app.use('/', indexRouter);
app.use('/users', usersRouter);
app.use('/baseball', baseballRouter);
app.use('/basketball', basketballRouter);
app.use('/e_sports', e_sportsRouter);
app.use('/football', footballRouter);
app.use('/hockey', hockeyRouter);
app.use('/mma', mmaRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
