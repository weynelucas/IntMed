app.filter("replaceUnderscores", function () {
    return function(input) {
        return input.split("_").join(" ");
    }
});
