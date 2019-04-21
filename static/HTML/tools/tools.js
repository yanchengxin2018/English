//修改div尺寸{id:'',t:,l:,r:,w:,h:,b_c:'',b_i:'',o:,b:''}
ip = 'http://129.211.14.136:8006';

function div_init(div_list, r = 500) {

    for (let i = 0; i < div_list.length; i++) {
        let data = div_list[i];
        let obj = $(`#${data['id']}`);
        obj.css('position', 'absolute');

        //定位
        obj.css('top', r * data['t'] / 100 + 'px');
        obj.css('left', r * data['l'] / 100 + 'px');
        obj.css('right', r * data['r'] / 100 + 'px');
        obj.css('width', r * data['w'] / 100 + 'px');
        obj.css('height', r * data['h'] / 100 + 'px');

        //背景颜色
        let back_color = data['b_c'];
        if (back_color !== 0) obj.css('background-color', back_color);

        //背景图片
        let back_image = data['b_i'];
        if (back_image !== 0) {
            obj.css('background-image', `url("${back_image}")`);
            obj.css('background-size', '100% auto');
            obj.css('background-repeat', 'no-repeat');
        }

        //圆角
        let border_radius = data['o'];
        if (border_radius !== 0) {
            obj.css('border-radius', r * border_radius / 100 + 'px');
        }

        //边框
        let border = data['b'];
        if (border !== 0) obj.css('border', `${border} solid 1px`);

        //透明
        obj.css('opacity', data['tou']);


        //旋转
        let rotate = data['x'];
        if (border !== 0) obj.css('transform', `rotate(${rotate}deg)`);

        //链接
        let src = data['s'];
        if (src) {
            obj.css('cursor', 'pointer');
            obj.attr('onclick', `window.location=\'${src}\'`);
        }

        //隐藏
        let overflow = data['overflow'];
        if (overflow) {
            obj.css('overflow', overflow);
        }

    }
}


//修改文字尺寸{id:'',size:,'text-align':'center','font-family':'Microsoft JhengHei'}
function font_init(div_list, r = 500) {
    for (let i = 0; i < div_list.length; i++) {
        let data = div_list[i];
        let obj = $(`#${data['id']}`);

        //文字大小
        obj.css('font-size', r * data['size'] / 100 + 'px');

        //文字位置
        let text_align = data['text-align'];
        if (text_align) obj.css('text-align', text_align);

        //文字字体
        let font_family = data['font-family'];
        if (font_family) obj.css('font-family', font_family);

    }
}


//get请求
function get(url, data, success_function, faild_function) {
    $.ajax({
        url: url,
        async: true,
        contentType: "application/x-www-form-urlencoded",
        data: data,
        dataType: "json",
        success: success_function,
        error: faild_function,
        //timeout:300,
        type: 'get',
    });
}

//post请求
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


function auto_width(div_id) {


    if(rule===0) {
        let obj = $(`#${div_id}`);
        obj.css('width','100%');
        rule=obj.css('width').replace('px','');
    }
}

















