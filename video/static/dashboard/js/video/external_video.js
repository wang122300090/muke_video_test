// 用这个标识找元素,对应id

var videoEreaStatic = false;
var videoEditArea = $('#video-edit-area');

$('#open-add-video-btn').click(function (){
    if (!videoEreaStatic){
        videoEditArea.show();
        videoEreaStatic=true;
    } else {
        videoEditArea.hide();
        videoEreaStatic=false;
    }
})