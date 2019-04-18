window.onload = start;
ratio = 1.3;
ip = 'http://172.16.10.35:8000';

function start() {

    let reg_obj = $('#reg');
    let username_obj = $('#username');
    let password_obj = $('#password');
    let div_username_obj = $('#div_username');
    let div_password_obj = $('#div_password');
    let ok_obj = $('#ok');
    let screen_obj = $('#screen');


    let reg_obj_width = reg_obj.css('width').replace('px', '');
    let reg_obj_height = reg_obj_width * ratio;
    reg_obj.css('height', reg_obj_height);
    let font_size=reg_obj_width * 0.06;
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
    let url = `${ip}/user/reg/`;
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
    screen_obj.append('注册成功!2秒钟后跳转到登录页面...');
    setTimeout(function () {
    window.location.href = `${ip}/static/HTML/log/log.html`;
    },2000)
}

function faild_success(data) {
    let response_data = data['responseJSON'];
    let username_error = response_data['username'];
    let password_error = response_data['password'];
    let screen_obj = $('#screen');
    screen_obj.empty();
    screen_obj.css('color', 'red');
    let error = '';

    if (username_error) {
        error = error + `用户名:${username_error}`;
        let username_obj=$('#username');
        username_obj.css('border','#ff383f solid 1px')
    }
    if (password_error) {
        if(error){
            error = error + '<br>';
        }
        error = error + `密码:${password_error}`;
        let password_obj=$('#password');
        password_obj.css('border','#ff383f solid 1px')
    }
    if (!error) {
        screen_obj.append('未知原因造成注册失败!')
    } else {
        screen_obj.append(error)
    }
}
