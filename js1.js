(function ($) {
    var audio = document.getElementById("xs");
    var source = document.getElementById("mySource");
    var duration = 0;     //总时间
    var currenttime = 0;     //剩余时间
    var all_nub = 0;
    var playing = false; /* 判断小说是否播放过了 */
    var frist_load = true;  /* 判断第一次加载 */
    var up_load = false; /* 上次加载 */
    var pagesize = 10;
    audio.volume = 1.0;   //音量
    ajax(novel_id);

    function ajax(novel_j) {
        var page = Math.ceil(novel_j / pagesize);
        $.ajax({
            url: "/api.php?c=Json&id=" + tingid + "&page=" + page + "&pagesize=" + pagesize,
            type: "get",
            dataType: "JSONP",
            async: false,
            headers: {"sign": $.now()},
            success: function (msg) {
                if (up_load) {
                    UpsetList(msg);
                    up_load = false
                } else {
                    setList(msg)
                }
            },
            error: function (msg) {
                console.log(msg)
            }
        })
    }

    function setList(msg) {
        var list = msg.playlist;
        for (var i = 0; i < list.length; i++) {
            var strHtml = '<li class="section-item" id="item' + list[i].pid + '" data-path="' + list[i].file + '" data-url="' + list[i].url + '">' + '<div class="column1">' + '<div class="column1-l">' + '<span class="section-number" style="">' + list[i].pid + '</span>' + '<i class="playing"></i>' + '</div>' + '<span class="set">' + list[i].trackName + '</span>' + '</div>' + '<div class="column2">' + msg.announcer + '</div>' + '</li>';
            $('.section-body').append(strHtml)
        }
        if (frist_load) {
            all_nub = msg.limit;
            defaultStart(novel_id);
            frist_load = false
        }
    }

    function UpsetList(msg) {
        var list = msg.playlist;
        for (var i = list.length - 1; i >= 0; i--) {
            var strHtml = '<li class="section-item" id="item' + list[i].pid + '" data-path="' + list[i].file + '" data-url="' + list[i].url + '">' + '<div class="column1">' + '<div class="column1-l">' + '<span class="section-number" style="">' + list[i].pid + '</span>' + '<i class="playing"></i>' + '</div>' + '<span class="set">' + list[i].trackName + '</span>' + '</div>' + '<div class="column2">' + msg.announcer + '</div>' + '</li>';
            $('.section-body').prepend(strHtml)
        }
    }

    /* 当前正在播放的在的li jquery对象 */
    var click_li;

    function defaultStart(id) {
        if (id <= all_nub) {
            click_li = $("#item" + id);
            var path = click_li.data("path"), url = click_li.data("url"),
                title = getTitle(click_li.find(".set").text()),
                nub = $(".section-body li").eq(0).find(".section-number").text();
            setCookie(tingid + "_setNAME", title, 48);
            setCookie(tingid + "_setURL", url, 48);
            setCookie("index_setID", tingid, 48);
            JieXi(JieMa(path));
            click_li.siblings().removeClass("section-pause");
            click_li.addClass("section-active").siblings().removeClass("section-active");
            if (click_li.find(".section-number").text() == nub && nub >= pagesize) {
                up_load = true;
                ajax(nub - pagesize)
            }
            if (click_li.next().length != 1) {
                click_li = $(".section-body li").eq($(".section-body li").length - 1);
                nub = parseInt(click_li.find(".section-number").text());
                if (Math.ceil(nub / (pagesize + 1)) <= Math.ceil(all_nub / (pagesize + 1)) && isInteger(nub)) {
                    frist_load = false;
                    ajax(nub + 1)
                }
            }
        }
    };

    /* 判断是不是整数 */
    function isInteger(obj) {
        return obj % pagesize === 0
    }

    $(".section-body ").on("click", "li", function () {
        var url = $(this).data("url");
        top.location.href = url
    });
    /* 上集 */
    $(".player-prev").click(function () {
        var nub = parseInt(click_li.find(".section-number").text());
        if (nub > 1) {
            var prev_li = click_li.prev();
            var url = prev_li.data("url");
            top.location.href = url
        }
    });
    /* 下集 */
    $(".player-next").click(function () {
        var nub = parseInt(click_li.find(".section-number").text());
        if (nub < all_nub) {
            var next_li = click_li.next();
            var url = next_li.data("url");
            top.location.href = url
        }
    });
    //播放
    $('.player-play').click(function () {
        click_li.removeClass('section-pause');
        play();
    });
    //暂停
    $('.player-pause').click(function () {
        if (playing) {
            click_li.addClass('section-pause').siblings().removeClass('section-pause');
            toPlay("pause");
            $(this).hide();
            $('.player-play').show()
        }
    });
    audio.addEventListener("canplay", function () {
        $('.player-volume-position').css('width', (audio.volume * 100) + '%');
        duration = parseInt(audio.duration);
        $('.player-duration-time').text(conversionTime(duration));
        var p_height = $('.player-progress').width(), tag = false;
        $('.player-progress-control').mousedown(function (e) {
            tag = true
        });
        $(document).mouseup(function () {
            tag = false
        });
        $(".player-progress").mousemove(function (e) {
            if (tag) {
                var actLage = e.clientX - $(this).offset().left;
                if (actLage <= 0) {
                    actLage = 0
                } else if (actLage > p_height) {
                    actLage = p_height
                }
                var progressBP = progressBarPercentage(p_height, actLage);
                $('.player-progress-control').css('left', progressBP + '%');
                $('.player-progress-position').css('width', progressBP + '%');
                var SongProgress = progressBP * duration / 100;
                songProgressAdjust(SongProgress)
            }
        });
        $('.player-progress').click(function (e) {
            if (playing) {
                var actLage = e.clientX - $(this).offset().left, progressBP = progressBarPercentage(p_height, actLage);
                $('.player-progress-control').css('left', progressBP + '%');
                $('.player-progress-position').css('width', progressBP + '%');
                var SongProgress = progressBP * duration / 100;
                songProgressAdjust(SongProgress)
            }
        });
        var s_width = $('.player-volume-progress').width();
        $('.player-volume-progress').click(function (e) {
            var actLage = e.clientX - $(this).offset().left, progressBP = progressBarPercentage(s_width, actLage);
            $('.player-volume-position').css('width', progressBP + '%');
            audio.volume = progressBP / 100
        })
    });

    function play() {
        $('.top-set').text(click_li.find('.set').text());
        var txt = click_li.find('.set').text().split("_");
        $('.title h1').text(txt[1] + " " + txt[0]);
        toPlay("play");
        playing = true;
        $('.player-play').hide();
        $('.player-pause').show()
    }

    /* 自动播放下一集 */
    audio.onended = function () {
        playing = false;
        var nub = parseInt(click_li.find(".section-number").text());
        if (nub < all_nub) {
            click_li = click_li.next();
            nub = parseInt(click_li.find(".section-number").text());
            if (Math.ceil(nub / (pagesize + 1)) <= Math.ceil(all_nub / (pagesize + 1)) && isInteger(nub) && click_li.next().length != 1) {
                ajax(nub + 1)
            }
            var url = click_li.data("url");
            top.location.href = url
        } else {
            click_li.addClass('section-pause').siblings().removeClass('section-pause');
            toPlay("pause");
            $('.player-pause').hide();
            $('.player-play').show();
            alert("本书已播放完毕！");
        }
    };
    /* 时间 */
    $('.player-wolume-w').hover(function () {
        if (playing) {
            $('.player-volume-progress').show()
        }
    }, function () {
        $('.player-volume-progress').hide()
    });

    //---------------------------------------------------【功能：播放&暂停】
    function toPlay(toPlay) {
        if (toPlay === "play") {
            audio.play();
            playbackProgress("play");
            getBuffered()
        }
        if (toPlay === "pause") {
            audio.pause();
            playbackProgress("pause")
        }
    }

    //---------------------------------------------------【功能：缓冲进度】
    function getBuffered() {
        var buffered = audio.buffered, loaded;
        if (buffered.length) {
            loaded = 100 * buffered.end(0) / audio.duration;
            $('.player-progress-loaded').css("width", loaded + "%")
        }
        setTimeout(getBuffered, 1000);
    }

    //---------------------------------------------------【功能：播放进度，播放时间】
    function playbackProgress(playSwitch) {
        if (playSwitch === "play") {
            $('.play-info .img-box').removeAttr('style').css('animation', 'Circle 10s linear infinite 0s forwards');
            timer = setInterval(function () {
                timeall = duration;
                currenttime = audio.currentTime;
                songPlaybackTime(timeall, currenttime);
                $('.player-progress-control').css('left', currenttime / timeall * 100 + '%');
                $('.player-progress-position').css('width', currenttime / timeall * 100 + '%');
                if (audio.ended) {
                    clearInterval(timer)
                }
            }, 1000)
        }
        if (playSwitch === "pause") {
            $('.play-info .img-box').removeAttr('style').css('animation-play-state', 'paused');
            clearInterval(timer)
        }
    }

    //---------------------------------------------------【计算歌曲播放时间】
    function songPlaybackTime(timeall, currenttime) {
        if (currenttime < timeall) {
            leftTime = parseInt(currenttime);
            $('.player-current-time').text(conversionTime(leftTime))
        }
    }

    //---------------------------------------------------【功能：歌曲进度调节】
    function songProgressAdjust(time) {
        audio.currentTime = time;
    }

    //---------------------------------------------------【计算进度条的百分比】
    function progressBarPercentage(totalLength, actLage) {
        var Result = (parseInt(actLage) / parseInt(totalLength)) * 100;
        return Math.ceil(Result);
    }

    /* 秒转换成分秒 */
    function conversionTime(time) {
        var surplusMinite, surplusSecond, cTime;
        surplusMinite = Math.floor((time / 60) % 60);
        if (surplusMinite < 10) {
            surplusMinite = "0" + surplusMinite
        }
        surplusSecond = Math.floor(time % 60);
        if (surplusSecond < 10) {
            surplusSecond = "0" + surplusSecond
        }
        cTime = surplusMinite + ":" + surplusSecond;
        return cTime
    }

    function getTitle(u) {
        var tArr = u.split("_");
        return tArr[1] + " " + tArr[0];
    }

    function setHtmlTitle(str) {
        if (str == null) return null;
        var title = $(document).attr("title"), titArr = title.split("，");
        $("title").html(str + "在线收听，" + titArr[1]);
    }

    function JieMa(u) {
        var tArr = u.split("*"), str = '';
        for (var i = 0, n = tArr.length; i < n; i++) {
            str += String.fromCharCode(tArr[i]);
        }
        return str;
    }

    function JieXi(str) {
        str = str.split('$');
        if (str[1] === "tc") {
            var data = str[0].split('/');
            data = data[0] + '/' + data[1] + '/play_' + data[1] + '_' + data[2] + '.htm';
            $.ajax({
                type: 'get',
                url: "//c.ting22.com/tingchina.php",
                data: 'file=' + data,
                dataType: "jsonp",
                success: function (data) {
                    if (data.status) {
                        playing = false;
                        source.src = data.url;
                        audio.load();
                        play();
                    }
                }
            });
        } else if (str[1] === "xm") {
            var data = str[0].split('/'), oMeta = document.createElement('meta');
            oMeta.name = 'referrer';
            oMeta.content = 'never';
            document.getElementsByTagName('head')[0].appendChild(oMeta);
            playing = false;
            source.src = "http://mobile.ximalaya.com/mobile/redirect/free/play/" + data[1] + "/0";
            audio.load();
            play();
        } else {
            playing = false;
            source.src = str;
            audio.load();
            play()
        }
    }

    function getCookie(name) {
        var arr = document.cookie.match(new RegExp("(^| )" + name + "=([^;]*)(;|$)"));
        if (arr != null) {
            return decodeURI(arr[2]);
        }
        return null;
    }

    function setCookie(name, value, ihour) {
        var iH = ihour || 1;
        var exp = new Date;
        exp.setTime(exp.getTime() + iH * 60 * 60 * 1000);
        document.cookie = name + ("=" + encodeURI(value) + ";expires=" + exp.toGMTString() + ";path=/;");
    }
})(jQuery);