
var inputNumber = $('#number');
var inputUrl = $('#url');
var videosubInputId = $('#videosub-input-id')

// id是唯一的,改成class就可以通用了
$('.update-btn').click(function (){
    var videoSubId = $(this).attr('data-id');
    // 这里的this指向的就是调用this的这个对象,就是button
    var videoSubNumber = parseInt($(this).attr('data-number'))
    var videoSubUrl = $(this).attr('data-url')

    inputNumber.val(videoSubNumber);
    inputUrl.val(videoSubUrl);
    videosubInputId.val(videoSubId);
});