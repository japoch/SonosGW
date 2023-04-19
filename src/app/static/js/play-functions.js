/**
* play-functions.js
*/
var currTrack = '';
var playing = false;
var mute = false;

function checkChange() {
    $.getJSON('/info-light').done(function (data) {
        $('#track-title').text(data['title']);
        if (currTrack != data['title']) {
            loadData();
        }
    });
}

function loadData() {
    $.getJSON('/info').done(function (data) {
        $('#track-title').text(data['title']);
        $('#track-artist').text(data['artist']);
        $('#track-album').text(data['album']);
        $('.card').empty();
        $('.card').html('<span class="image-wrap card" style="position:relative; display:inline-block; background:url(' + data['image'] + ') no-repeat center center; width: 400px; height: 400px;" /><img style="opacity:0" id="track-image" src="' + data['image'] + '"></span>');

        currTrack = data['title'];
        playing = data['playing'];
        mute = data['mute'];
    });
}

$(document).ready(function () {
    loadData();

    /**
    $("img").load(function () {
        $(this).wrap(function () {
            return '<span class="image-wrap ' + $(this).attr('class') + '" style="position:relative; display:inline-block; background:url(' + $(this).attr('src') + ') no-repeat center center; width: ' + $(this).width() + 'px; height: ' + $(this).height() + 'px;" />';
        });
        $(this).css("opacity", "0");
    });
    */

    setInterval("checkChange()", 1000);

    $('#next').click(function () {
        $.ajax('/next');
        loadData();
    });

    $('#previous').click(function () {
        $.ajax('/previous');
        loadData();
    });

    $('#pause').click(function () {
        if (playing == true) {
            $.ajax('/pause');
            playing = false;

            $('#pause').html('<span class="oi oi-media-play" title="play" aria-hidden="true"></span> Play');
        }
        else {
            $.ajax('/play');
            playing = true;

            $('#pause').html('<span class="oi oi-media-pause" title="pause" aria-hidden="true"></span> Pause');
        }
    });

    $('#volume_down').click(function () {
        $.ajax('/volume_down');
        if (mute == true) {
            $.ajax('/volume_unmute');
            mute = false;
            $('#volume_mute').html('<span class="oi oi-volume-off" title="volume off" aria-hidden="true"></span> Mute');
        }
    });

    $('#volume_up').click(function () {
        $.ajax('/volume_up');
        if (mute == true) {
            $.ajax('/volume_unmute');
            mute = false;
            $('#volume_mute').html('<span class="oi oi-volume-off" title="volume off" aria-hidden="true"></span> Mute');
        }
    });

    $('#volume_mute').click(function () {
        if (mute == true) {
            $.ajax('/volume_unmute');
            mute = false;
            $('#volume_mute').html('<span class="oi oi-volume-off" title="volume off" aria-hidden="true"></span> Mute');
        }
        else {
            $.ajax('/volume_mute');
            mute = true;
            $('#volume_mute').html('<span class="oi oi-volume-off" title="volume off" aria-hidden="true"></span> Unmute');
        }
    });

    $('#track_01').click(function () {
        $.ajax('/track_01');
    });

    $('#track_02').click(function () {
        $.ajax('/track_02');
    });

    $('#track_03').click(function () {
        $.ajax('/track_03');
    });

    $('#track_04').click(function () {
        $.ajax('/track_04');
    });

});
