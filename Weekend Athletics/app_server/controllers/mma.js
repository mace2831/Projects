var fs = require('fs');
var blogs = JSON.parse(fs.readFileSync('./data/blogs.json','utf8'));

/*Get MMA view*/
const mma = (req, res) => {
    res.render('mma', {title: "MMA", blogs});
};

module.exports = {
    mma
};