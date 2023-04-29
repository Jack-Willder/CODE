function getRelease(page = 1, sort = 'episode_desc', limit = 30) {
    $.getJSON('/api?m=release&id=' + id + '&sort=' + sort + '&page=' + page, function(data) {
        var output = '<div class="episode-list row">';
        var paging = '<nav aria-label="Page navigation"><ul class="pagination justify-content-center">';
        if (data.total == 0) {
            output += '<div class="no-results text-center">no results found</div>';
            adv = '';
            paging = '';
        } else {
            for (var i = 0; i < data.data.length; i++) {
                var release = data.data[i];
                var selected = ((i == 0) ? ' class="selected"' : '');
                var episode = ((release.episode == 0) ? '?' : release.episode);
                var episodes = ((release.episode > 1) ? 'Episodes' : 'Episode');
                var now = Date.now() - (3 * 24 * 60 * 60 * 1000);
                var timestamp = +new Date(release.created_at);
                output += '<div class="episode-wrap col-12 col-sm-4">';
                output += '<div class="episode">';
                output += '<div class="episode-snapshot">';
                output += '';
                output += (release.snapshot.length === 0) ? '<img src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" alt="">' : '<img src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" data-src="' + release.snapshot.replace('i.animepahe.com', 'i.' + domain) + '" class="lazyload" alt="">';
                output += '<svg class="play-button" viewBox="0 0 150 150" alt="Play Video">';
                output += '<polygon points="20, 20, 20, 140, 120, 80" fill="#fff"></polygon>';
                output += '</svg>';
                if (release.disc.length === 0) { output += (timestamp > now) ? '<span class="episode-new">New</span>' : ''; } else { output += '<span class="episode-disc ' + release.disc + '">' + release.disc + '</span>'; }
                output += (release.filler == 1) ? '<span class="episode-filler">Filler</span>' : '';
                output += '<a href="/play/' + id + '/' + release.session + '" class="play">Watch ' + release.title + ' - ' + release.episode + ' Online</a>';
                output += '</div>';
                output += '<div class="episode-label-wrap">';
                output += '<div class="episode-label">';
                output += '<div class="episode-title-wrap">';
                if (release.duration != "00:00:00") { output += '<span class="episode-duration">' + release.duration + '</span>'; }
                output += '</div>';
                output += '<div class="episode-number-wrap">';
                output += (release.episode.length === 0) ? '' : '<div class="episode-number"><span class="text-hide">' + release.title + ' Episode </span>' + release.episode;
                output += (release.episode2 == 0) ? '' : '-' + release.episode2;
                output += ' ' + release.edition;
                output += '</div>';
                output += '</div>';
                output += '</div>';
                output += '</div>';
                output += '</div>';
                output += '</div>';
            }
            if (data.last_page != 1) {
                if (data.current_page == 1) { var prevDisable = firstDisable = ' disabled'; var prevPage = data.current_page; } else { var prevDisable = firstDisable = ''; var prevPage = data.current_page - 1; }
                if (data.current_page == data.last_page) { var nextDisable = lastDisable = ' disabled'; var nextPage = data.current_page; } else { var nextDisable = lastDisable = ''; var nextPage = data.current_page + 1; }
                paging += '<li class="page-item' + firstDisable + '">';
                paging += '<a class="page-link" data-page="1" data-sort="' + sort + '" title="Go to the First Page"><span aria-hidden="true">&laquo;</span><span class="sr-only">First</span></a>';
                paging += '</li>';
                paging += '<li class="page-item' + prevDisable + '">';
                paging += '<a class="page-link prev-page" data-page="' + prevPage + '" data-sort="' + sort + '" title="Go to Page ' + prevPage + '"><span aria-hidden="true">&lsaquo;</span><span class="sr-only">Prev</span></a>';
                paging += '</li>';
                paging += '<li class="page-item active">';
                paging += '<span class="page-link" title="We\'re on Page ' + data.current_page + ' of ' + data.last_page + '">' + data.current_page + '<span class="sr-only"> (current)</span></span>';
                paging += '</li>';
                paging += '<li class="page-item' + nextDisable + '">';
                paging += '<a class="page-link next-page" data-page="' + nextPage + '" data-sort="' + sort + '" title="Go to Page ' + nextPage + '"><span class="sr-only">Next</span><span aria-hidden="true">&rsaquo;</span></a>';
                paging += '</li>';
                paging += '<li class="page-item' + lastDisable + '">';
                paging += '<a class="page-link" data-page="' + data.last_page + '" data-sort="' + sort + '" title="Go to the Last Page"><span class="sr-only">Last</span><span aria-hidden="true">&raquo;</span></a>';
                paging += '</li>';
            } else { paging = ''; }
        }
        var episode_label = 'Episode';
        if (data.total > 1) episode_label = 'Episodes';
        $('.episode-count').html(episode_label + ' (' + data.total + ')');
        $('.episode-list-wrapper').html(output).append(paging);
    });
    console.log(output);
}