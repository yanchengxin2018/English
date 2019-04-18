window.onload = start;
ratio = 1.3;
ip = 'http://172.16.10.35:8000';

function start() {

    let log_obj = $('#log');
    let username_obj = $('#username');
    let password_obj = $('#password');
    let div_username_obj = $('#div_username');
    let div_password_obj = $('#div_password');
    let ok_obj = $('#ok');
    let screen_obj = $('#screen');


    let log_obj_width = log_obj.css('width').replace('px', '');
    let log_obj_height = log_obj_width * ratio;
    log_obj.css('height', log_obj_height);
    let font_size=log_obj_width * 0.06;
    username_obj.css('font-size',font_size);
    password_obj.css('font-size',font_size);
    div_username_obj.css('font-size',font_size);
    div_password_obj.css('font-size',font_size);
    ok_obj.css('font-size',font_size);
    screen_obj.css('font-size',font_size);


}

function commit() {
    let username_obj = $('#username');
    let password_obj = $('#password');
    let username_val = username_obj.val();
    let password_val = password_obj.val();
    let url = `${ip}/user/log/`;
    let data = {'username': username_val, 'password': password_val};
    let success_function = commit_success;
    let faild_function = faild_success;
    post(url, data, success_function, faild_function)
}


//get请求
function post(url, data, success_function, faild_function) {
    $.ajax({
        url: url,
        async: true,
        contentType: "application/x-www-form-urlencoded",
        data: data,
        dataType: "json",
        success: success_function,
        error: faild_function,
        //timeout:300,
        type: 'post',
    });
}

function commit_success() {
    let username_obj=$('#username');
    username_obj.css('border','#8c63ff solid 1px');
    let password_obj=$('#password');
    password_obj.css('border','#8c63ff solid 1px');
    let screen_obj = $('#screen');
    screen_obj.empty();
    screen_obj.css('color', 'dodgerblue');
    screen_obj.append('登录成功!2秒钟后跳转到菜单页...');
    setTimeout(function () {
    window.location.href = `${ip}/static/HTML/index/index.html`;
    },2000)
}

function faild_success(data) {
    let screen_obj = $('#screen');
    screen_obj.css('color','red');
    let response_data = data['responseJSON'];
    let error = response_data['tips'];
    screen_obj.append(error);
}

