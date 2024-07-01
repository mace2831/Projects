var fs = require('fs');
var blogs = JSON.parse(fs.readFileSync('./data/blogs.json','utf8'));

/*Get MMA view*/
const soccer = (req, res) => {
    res.render('soccer', {title: "Soccer", blogs});
};

module.exports = {
    soccer
};