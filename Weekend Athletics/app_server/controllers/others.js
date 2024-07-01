var fs = require('fs');
var blogs = JSON.parse(fs.readFileSync('./data/blogs.json','utf8'));

/*Get MMA view*/
const others = (req, res) => {
    res.render('others', {title: "Other Sports", blogs});
};

module.exports = {
    others
};