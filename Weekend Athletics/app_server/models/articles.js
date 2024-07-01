const mongoose = require('mongoose');

const articleSchema = new mongoose.Schema({
    title: {type: String, required: true, index: true},
    category: {type: String, required:true, index: true},
    image: {type: String, required: true},
    date: {type: Date, required: true},
    body: {type: String, required: true},
    author: {type: String, required: true}
});

const Article = mongoose.model('articles', articleSchema);
module.exports = Article;