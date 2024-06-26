/*Get Hockey view*/
const hockey = (req, res) => {
    res.render('hockey', {title: "Hockey"});
};

module.exports = {
    hockey
};