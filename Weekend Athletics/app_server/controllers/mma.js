/*Get MMA view*/
const mma = (req, res) => {
    res.render('mma', {title: "MMA"});
};

module.exports = {
    mma
};