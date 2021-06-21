var ajaxCommentShow = $('#ajax-comment-show');

$('#comment-submit').click(function (){
    var content = $('#comment-content').val();
    var csrfToken = $('#django-csrf-token').val();
    var videoId = $(this).attr('data-video-id');
    var userId = $(this).attr('data-user-id');
    var url = $(this).attr('data-url');
    //前端使用驼峰式命名,python是下划线

    if (!content){
        alert("评论不能为空!")
        return;
    }

    $.ajax({
        url: url,
        type: 'post',
        data: {
            content: content,
            videoId: videoId,
            userId: userId,
            csrfmiddlewaretoken: csrfToken,
        },
        // data就是响应回来的数据
        success: function (data){
            // 因为对应的前端是div包装的
            ajaxCommentShow.html(' ')
            var _data = data.data.comment;
            var content = _data.content;
            var username = _data.username;
            var str = content + ' ' + username;
            ajaxCommentShow.html(str);
            // 这里的作用就是进行新增的评论排在第一位,但是刷新又到后面去了,在video_sub中对id进行反序就可以了
        },
        fail: function (e){
            console.log(e);
        }
    })
});