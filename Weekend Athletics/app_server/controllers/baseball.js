/*Get Baseball view*/
const baseball = (req, res) => {
    res.render('baseball', {title: "Baseball"});
};

module.exports = {
    baseball
};