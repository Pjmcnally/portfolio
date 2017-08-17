$(document).ready(loadContent);

// Set listener to loadContent content on popstate event.
$(window).on("popstate", function() {
    $("#search-input").val("");
    loadContent();
});

// Set listener to loadContent when nav link is clicked.
$(function() {
    if (Modernizr.history) {
        // history is support.  Use cool method.

        // hijack the nav click event
        $(".class-link").on("click", function(event) {
            event.preventDefault();
            var _href = $(this).attr("href");

            // change the url without a page refresh and add a history entry.
            history.pushState(null, null, _href);

            // load the content
            loadContent();
        });
        // hijack the nav click event
        $(".level-link").on("click", function(event) {
            event.preventDefault();
            var _href = $(this).attr("href");

            // Change the url without a page refresh and add a history entry.
            history.pushState(null, null, _href);

            // Scroll to new hash.
            scrollTopOrHash();
        });
    } else {
        // History not supported.  Nothing Fancy here.
    }
});

// event listener to intercept form submission and instead load content
$("#search-form").on("submit", function(event) {
    event.preventDefault();
    loadContent();
});

// event listener to load content on value change in search field.
$("#search-input").on("input", function(event) {
    event.preventDefault();
    removeHash();
    loadContent();
});

// event listener to load content when ritual checkbox value changes
$(".btn").on("click", function(event) {
    event.target.blur();

    var val = $(this).val();
    if (val === "") {
        $(this).val("yes");
    } else if (val === "yes") {
        $(this).val("no");
    } else {
        $(this).val("");
    }
    removeHash();
    loadContent();
});

function removeHash () {
    if (window.location.hash) {
        history.pushState(null, null, window.location.pathname + window.location.search);
    }
}

// Load content from django database into page.
function loadContent () {
    var _href = window.location.pathname;
    var clss = parseClassRef(_href);
    $.ajax({
        method: "post",
        url: "/spellbook/spells",
        data: {
            class: clss,
            rit: $("#rit-btn").val(),
            con: $("#con-btn").val(),
            com_v: $("#v-btn").val(),
            com_s: $("#s-btn").val(),
            com_m: $("#m-btn").val(),
            search: $("#search-input").val(),
        },
        success: function(data){
            $("#content-box").html(data);
            switchActive(clss);
            showLevelLink();
            scrollTopOrHash();
        }
    });
}

function scrollTopOrHash () {
    var hash = window.location.hash;
    if (hash) {
        $('html, body').animate({scrollTop: $(hash).offset().top}, 0);
    } else {
        $('html,body').scrollTop(0);
    }
}

// function to show active level links in internal nav-bar
function showLevelLink() {
    $(".level-link").addClass("hidden");
    $("#ll-search").removeClass("hidden");
    $.each($(".spell-level-header"), function (index, value) {
        var link = "#ll-" + value.id;
        $(link).removeClass("hidden");
    });
}

// Parses class string from href.
function parseClassRef (_href) {
    var clssRe = /class\/([\w]+)/;
    try {
        clss = _href.match(clssRe)[1];
        return clss;
    } catch(err) {
        return "";
    }
}

// Switches active higlighted nav button in main nav.
function switchActive (clss) {
    $(".class-link").parent().removeClass("active");
    if (clss) {
        clss_id = "#" + clss;
    } else {
        clss_id = "#all";
    }
    $(clss_id).parent().addClass("active");
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
