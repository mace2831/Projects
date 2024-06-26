/*Get Football view*/
const football = (req, res) => {
    res.render('football', {title: "Football"});
};

module.exports = {
    football
};