$(function() {
    let doc = document;
    let domain = window.location.hostname;
    $('[data-toggle="tooltip"]').tooltip();
    $('.drawer-toggler').on('click', function(e) { $('.drawer').css('left', '0');
        $('.main-header nav').append('<div class="drawer-backdrop"></div>');
        e.preventDefault(); });
    $('.main-header nav').on('click', '.drawer-backdrop', function(e) { $('.drawer').css('left', '-100%');
        $(this).remove();
        e.preventDefault(); });
    $(doc).click(function() { if ($('.nav-menu li ul').is(':visible')) { $('.nav-menu li').removeClass('open'); } }).on('keyup', function(e) { var keycode = e.keyCode; if (keycode === 113) $('.input-search').focus();
        e.preventDefault(); });
    $('.nav-menu > li.dropdown > a').click(function(e) { $(this).parent('li').toggleClass('open');
        e.preventDefault();
        e.stopPropagation(); });
    window.displayBoxIndex = -1;
    var Navigate = function(diff) {
        displayBoxIndex += diff;
        var oBoxCollection = $('.search-results li');
        if (displayBoxIndex >= oBoxCollection.length)
            displayBoxIndex = 0;
        if (displayBoxIndex < 0)
            displayBoxIndex = oBoxCollection.length - 1;
        var cssClass = 'selected';
        oBoxCollection.removeClass(cssClass).eq(displayBoxIndex).addClass(cssClass);
    }
    var ua = navigator.userAgent.toLowerCase();
    var isAndroid = ua.indexOf('android') > -1;
    var delay = (function() { var timer = 0; return function(callback, ms) { clearTimeout(timer);
            timer = setTimeout(callback, ms); }; })();
    let timeout = null;
    $('.input-search').on('keyup input', function(e) {
        var keycode = e.keyCode;
        if (isAndroid) { var valid = (e.keyCode !== 40 && e.keyCode !== 38 && e.keyCode !== 27); } else { var valid = (keycode > 47 && keycode < 58) || keycode === 32 || keycode === 8 || keycode === 46 || (keycode > 64 && keycode < 91) || (keycode > 95 && keycode < 112) || (keycode > 185 && keycode < 193) || (keycode > 218 && keycode < 223); }
        var keyword = $(this).val();
        clearTimeout(timeout);
        if (e.ctrlKey && e.keyCode == 86 && $(this).val().length >= 1) { timeout = setTimeout(function() { $('.search-results-wrap').html('<div class="spinner"><div class="rect1"></div><div class="rect2"></div><div class="rect3"></div><div class="rect4"></div><div class="rect5"></div></div>');
                searchBar(keyword);
                displayBoxIndex = -1; }, 250); } else if ((e.ctrlKey && e.keyCode == 65) || e.ctrlKey || e.altKey) { e.preventDefault(); return false; } else if (valid != false && $(this).val().length >= 1) { timeout = setTimeout(function() { $('.search-results-wrap').html('<div class="spinner"><div class="rect1"></div><div class="rect2"></div><div class="rect3"></div><div class="rect4"></div><div class="rect5"></div></div>');
                searchBar(keyword);
                displayBoxIndex = -1; }, 250); } else if (keycode == 13) {
            if ($('.search-results li.selected a').length == 1) { window.location = $('.search-results li.selected a').attr('href'); }
            e.preventDefault();
            return false;
        } else if ($(this).is(':focus') && keycode == 27) { $(this).blur();
            $('.nav-search').removeClass('active'); } else if (keycode == 40) { Navigate(1); } else if (keycode == 38) { Navigate(-1); } else { e.preventDefault(); return false; }
    }).focus(function(e) { window.displayBoxIndex = -1;
        $('.nav-search').addClass('active'); }).blur(function(e) { window.displayBoxIndex = -1;
        $('.search-results li').removeClass('selected'); });
    $('.search-results-wrap').on('mouseover', '.search-results li', function(e) { window.displayBoxIndex = $(this).data('index');
        $('.search-results li').removeClass('selected');
        $(this).addClass('selected'); }).on('mouseout', '.search-results', function(e) { window.displayBoxIndex = -1;
        $(this).children('li').removeClass('selected'); });
    $(doc).mouseup(function(e) {
        var container = $('.nav-search');
        if (!container.is(e.target) && container.has(e.target).length === 0) { container.removeClass('active'); }
    });

    function searchBar(keyword = '') {
        $.getJSON('/api?m=search&q=' + keyword, function(data) {
            var output = '<ul class="search-results">';
            if (data.total == 0) { output += '<div class="no-results">no results found</div>';
                adv = ''; } else {
                for (var i = 0; i < data.data.length; i++) { var anime = data.data[i]; var selected = ((i == 0) ? ' class="selected"' : ''); var episode = ((anime.episodes == 0) ? '?' : anime.episodes); var episodes = ((anime.episodes > 1) ? 'Episodes' : 'Episode');
                    output += '<li data-index="' + i + '">';
                    output += '<a href="/anime/' + anime.session + '" title="' + anime.title + '">';
                    output += '<img src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" data-src="' + anime.poster.replace('.jpg', '.th.jpg').replace('.png', '.th.png').replace('animepahe.com', window.location.hostname) + '" class="lazyload" alt="Thumbnail of ' + anime.title + '">';
                    output += '<div class="result-title">' + anime.title + '</div>';
                    output += '<div class="result-status"><strong>' + anime.type + '</strong> - ' + episode + ' ' + episodes + ' (' + anime.status + ')</div>';
                    output += '<div class="result-season">' + anime.season + ' ' + anime.year + '</div>';
                    output += '</a>'; '</li>'; }
                var adv = '<a href="/search?q=' + keyword.replace(/ /g, '+') + '" title="Advanced search for ' + keyword + '" class="adv-search">Advanced Search</a>';
            }
            $('.search-results-wrap').html(output);
        });
    }
    $('.close-ann-fakesite').on('click', function(e) { Cookies.set('ann-fakesite', 0, { expires: 30 }); });
});