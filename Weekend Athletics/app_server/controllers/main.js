/*Get homepage*/
const index = (req, res) => {
    res.render('index', {title:"Weekend Athletics"});
};

module.exports = {
    index
}