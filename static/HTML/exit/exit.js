window.onload=start;
ip='http://172.16.10.35:8000';


function start() {
    let exit_obj=$('#exit');
    let screen_obj = $('#screen');
    let exit_width=exit_obj.css('width').replace('px','');
    let exit_heigh=exit_width*1.55;
    exit_obj.css('height',exit_heigh);
    let font_size=exit_width*0.05;
    screen_obj.css('font-size',font_size);
    setTimeout(exit,1000);
}

function exit() {
    $.ajax({
        url: `${ip}/user/logout/`,
        async: true,
        contentType: "application/x-www-form-urlencoded",
        data: {},
        dataType: "json",
        success: exit_success,
        error: exit_faild,
        //timeout:300,
        type: 'get',
    });
}


function exit_success() {
    let screen_obj = $('#screen');
    screen_obj.empty();
    screen_obj.css('color', 'dodgerblue');
    screen_obj.append('退出成功!2秒钟后跳转到主页...');
    setTimeout(function () {
    window.location.href = `${ip}/url/main`;
    },2000)
}

function exit_faild(data) {
    let screen_obj = $('#screen');
    screen_obj.css('border','#ff383f solid 1px');
    screen_obj.append('未知原因造成注册失败!');
}





