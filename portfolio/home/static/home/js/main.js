$(document).ready(loadContent);

// Set listener to loadContent content on popstate event.
$(window).on("popstate", function() {
    // $("#search-input").val("");
    loadContent();
});

// Set listener to loadContent when nav link is clicked.
$(function() {
    if (Modernizr.history) {
        // history is support.  Use cool method.

        // hijack the nav click event
        $(".nav a").on("click", function(event) {
            event.preventDefault();
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

function stupid() {
    $('#email-form').on('submit', function(event) {
        event.preventDefault();
        testSubmit();
    });
}

function getEmailContent() {
    console.log("test");
    $.ajax({
        method: "get",
        url: "/email/",
        success: function(data){
            $("#email-container").html(data);
            stupid();
        }
    });
}

function testSubmit() {
    console.log("test");
    $.ajax({
        method: "post",
        url: "/email/",
        data: {
            name: $('#id_name').val(),
            email: $('#id_email').val(),
            text: $('#id_text').val()},
        success: function(data){
            $("#email-container").html(data);
            stupid();
        }
    });
}

// Load content from django database into page.
function loadContent() {
    _href = window.location.pathname;
    console.log(_href);
    // Not a fan of this conditional.  It is a hacky fix to original load of page
    if (_href === "/") {_href = "/projects";}
    $.ajax({
        method: "post",
        url: "/content",
        data: {
            page: _href
        },
        success: function(data){
            $("#content-box").html(data);
            switchActive(_href);
            if (_href === "/contact") {
                getEmailContent();
                stupid();
            }
        }
    });
}

// Switches active higlighted nav button in main nav.
function switchActive (_href) {
    $(".nav a").removeClass("active");
    $('a[href="' + _href + '"]').addClass("active");
}



/* All functions belowed copied from Django documentation.
 * link = https://docs.djangoproject.com/en/1.10/ref/csrf/
 * these functions ensure csrf token passed through with AJAX POST requests
*/
// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
