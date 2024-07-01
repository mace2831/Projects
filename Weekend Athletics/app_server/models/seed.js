//bring in db connection and schema
const Mongoose = require('./db');
const Article = require('./articles');

//read seed data
var fs = require('fs');
var articles = JSON.parse(fs.readFileSync('./data/blogs.json', 'utf8'))

//delete existing recors, then insert seed data
const seedDB = async()=>{
    await Article.deleteMany({});
    await Article.insertMany(articles);
};

//close MongoDB connection
seedDB().then(async()=>{
    await Mongoose.connection.close();
    process.exit(0);
});