$('#regist-submit').click(function(){
    var username = $('#username').val();
    var password = $('#password').val();
    var url = $(this).attr('data-url');
    var csrfToken = $('#django-csrf-token').val();

    if (!username || !password) {
        alert('缺少必要字段');
        return;
    }
    // 使用这个将前端数据传到后端
    $.ajax({
        url: url,
        type: 'post',
        data: {
            username: username,
            password: password,
            csrfmiddlewaretoken: csrfToken,
        }, //在后端post中return JsonResponse 到 data
        success: function (data){
            alert(data.msg)
            console.log(data)
        },
        fail: function (e){
            console.log('error:%s', e)
        }
    });
});

$('#login-submit').click(function(){
    var username = $('#username').val();
    var password = $('#password').val();
    var url = $(this).attr('data-url');
    var csrfToken = $('#django-csrf-token').val();

    if (!username || !password) {
        alert('缺少必要字段');
        return;
    }
    // 使用这个将前端数据传到后端
    $.ajax({
        url: url,
        type: 'post',
        data: {
            username: username,
            password: password,
            csrfmiddlewaretoken: csrfToken,
        }, //在后端post中return 到 data
        success: function (data){
            if (data.code){
                alert(data.msg)
            }
            else {
                window.location.href = '/client/video/ex' //跳转
            }
        },
        fail: function (e){
            console.log('error:%s', e)
        }
    });
});
