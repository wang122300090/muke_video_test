// $('#user-status-submit').click(function (){
//     // 这里这样写,只对第一个按钮有用
//     var url = $(this).attr('data-url');
//     var userId = $(this).attr('data-user-id');
//     var csrfToken = $('#django-csrf-token').val();
//
//     $.ajax({
//         url: url,
//         type: 'post',
//         data:{
//             userId: userId,
//             csrfmiddlewaretoken: csrfToken,
//         },
//         success: function (data){
//             if (data.code == 0){
//                 alert(data.msg);
//                 window.location.href = window.location.href;
//             }else {
//                 alert(data.msg);
//             }
//         },
//         fail: function (e){
//             console(e);
//         }
//     })
// })


//对于click事件要绑定整个页面,才会对所有用户有效

$(document).on("click",'#user-status-submit',function (){
    // 这里这样写,只对第一个按钮有用
    var url = $(this).attr('data-url');
    var userId = $(this).attr('data-user-id');
    var csrfToken = $('#django-csrf-token').val();

    $.ajax({
        url: url,
        type: 'post',
        data:{
            userId: userId,
            csrfmiddlewaretoken: csrfToken,
        },
        success: function (data){
            if (data.code == 0){
                alert(data.msg);
                window.location.href = window.location.href;
            }else {
                alert(data.msg);
            }
        },
        fail: function (e){
            console(e);
        }
    })
})