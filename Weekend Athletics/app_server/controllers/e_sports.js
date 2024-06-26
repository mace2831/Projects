/*Get E-Sports view*/
const e_sports = (req, res) => {
    res.render('e_sports', {title: "E-Sports"});
};

module.exports = {
    e_sports
};