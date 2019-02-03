$(document).ready(loadContent);

// Set listener to loadContent content on popstate event.
$(window).on("popstate", function() {
    $("#search-input").val("");
    loadContent();
});

// event listener to intercept form submission and instead load content
$("#search-form").on("submit", function(event) {
    event.preventDefault();
    loadContent();
});

// event listener to load content on value change in search field.
$("#search-input").on("input", function(event) {
    event.preventDefault();
    loadContent();
});


// event listener to load content when ritual checkbox value changes
$(".search button").on("click", function(event) {
    event.target.blur();

    if ((this).id === "reset-adv-btn") {
        $(".adv-search .btn").val("");
    } else if ((this).id === "reset-class-btn") {
        $(".class-search .btn").val("");
    } else {
        var val = $(this).val();
        if (val === "") {
            $(this).val("true");
        } else if (val === "true") {
            $(this).val("false");
        } else {
            $(this).val("");
        }
    }

    loadContent();
});

function flipArrow(elem, selector) {
    arrow = $(elem).find(selector)
    if (arrow.hasClass("fa-angle-double-down")) {
        arrow.removeClass("fa-angle-double-down")
        arrow.addClass("fa-angle-double-up")
    } else if (arrow.hasClass("fa-angle-double-up")) {
        arrow.removeClass("fa-angle-double-up")
        arrow.addClass("fa-angle-double-down")
    }
}

function showOrHide (elem) {
    if (elem.hasClass("hidden")) {
        elem.removeClass("hidden")
    } else {
        elem.addClass("hidden")
    }
}

function shrinkOrExpand (elem) {
    if (elem.hasClass("shrunk")) {
        elem.removeClass("shrunk")
        elem.addClass("expanded")
    } else {
        elem.removeClass("expanded")
        elem.addClass("shrunk")
    }
}

function setSpellDetailListener () {
    // event listener to test spell link click
    $(".spell-header, .spell-footer, .spell-list-name").on('click', function(event) {
        if (event.target.tagName == 'A') {
            // Don't run javascript if link clicked on
            return
        }

        spell = $(this).parent()
        content_div = spell.children(".spell-content")

        if (spell.hasClass("empty")) {
            loadSpellDetail(content_div)
            spell.removeClass("empty")
            shrinkOrExpand(spell)
        } else {
            shrinkOrExpand(spell)
        }

        flipArrow(spell, ".flip")
    });
}

function setSpellLevelListener () {
    $(".spell-level").on('click', function(event) {
        showOrHide($(this).siblings(".spell-list"))
        flipArrow($(this).parent(), ".spell-level .fa")
    })
}

function loadSpellContent (target) {
    target.addClass('loader')
    target.html("<h3 class='loading spell-name'>Loading<span>.</span><span>.</span><span>.</span></h3>")
    $.ajax({
        method: "post",
        url: "/spellbook/get_spell_detail",
        data: {
            spell: target.parent().attr('id'),
        },
        success: function(data){
            target.removeClass("loader")
            target.html(data)
        }
    });
}

// Gets class buttons by boolean value and returns list
function getClassesString (bool) {
    classes = []
    filter = ".class-btn[value='" + bool + "']"
    $(filter).each(function(){
        classes.push($(this).attr('id'))
    })

    return classes
}

// Load content from django database into page.
function loadContent () {
    $.ajax({
        method: "post",
        url: "/spellbook/spells",
        data: {
            class_inc: getClassesString(true).join(" "),
            class_exc: getClassesString(false).join(" "),
            rit: $("#rit-btn").val(),
            con: $("#con-btn").val(),
            com_v: $("#v-btn").val(),
            com_s: $("#s-btn").val(),
            com_m: $("#m-btn").val(),
            search: $("#search-input").val(),
        },
        success: function(data){
            $("#spell-block").html(data);
            setSpellDetailListener()
            setSpellLevelListener()
        }
    });
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
