$(document).ready(function) {
    Change background image of div when changing pages
    $("button").click(function() {
        var Image imageUrl = "../img/alien.jpg";
        $(".box").css("background-image", "url(" + imageUrl + ")");

    });

});
}