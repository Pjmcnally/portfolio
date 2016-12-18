function loadContent() {
    console.log("content should be loaded");
}

// Set listener to loadContent when nav link is clicked.
$(function() {
    if (Modernizr.history) {
        // history is support.  Use cool method.

        // hijack the nav click event
        $(".nav a").on("click", function(event) {
            event.preventDefault();
            switchActive($(this));
            _href = $(this).attr("href");

            // change the url without a page refresh and add a history entry.
            history.pushState(null, null, _href);

            // load the content
            loadContent();
        });
    } else {
        // History not supported.  Nothing Fancy here.
    }
});

// Switches active higlighted nav button in main nav.
function switchActive (elem) {
    $(".nav a").removeClass("active");
    elem.addClass("active");
}