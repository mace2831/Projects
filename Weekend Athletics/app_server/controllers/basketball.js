/*Get Basketball view*/
const basketball = (req, res) => {
    res.render('basketball', {title: "Basketball"});
};

module.exports = {
    basketball
};