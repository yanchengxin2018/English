window.onload = start_onload;
ip = 'http://172.16.10.35:8000';
new_card = '';
update_card = '';
info_card = '';
rule = 0;

function start_onload() {
    let screen_obj = $('#screen');
    if (rule === 0) {
        screen_obj.css('width', '100%');
        rule = screen_obj.css('width').replace('px', '');
    }

    div_init(new_card_div_setting);
    font_init(new_card_font_setting);

    div_init(update_card_div_setting);
    font_init(update_card_font_setting);
    update_card_build_keys();

    div_init(info_card_div_setting);
    font_init(info_card_font_setting);
    clear();
    get_word_card();
}


function card_show_success(data) {
    let card_type = data['card_type'];
    if (card_type === 'new_card') {
        new_card.word_index = data['word_index'];
        new_card.english = data['english'];
        new_card.chinese = data['chinese'];
        new_card.pronunciation = data['pronunciation'];
        new_card.back_image = data['back_image'];
        show_new_card();
    } else if (card_type === 'update_card') {
        update_card.chinese = data['chinese'];
        update_card.word_index = data['word_index'];
        update_card.update_image = data['update_image'];



        show_update_card();
    }
    else if (card_type === 'strengthen_card') {
        update_card.chinese = data['chinese'];
        update_card.word_index = data['word_index'];
        show_update_card();
    }


    else if (card_type === 'info_card') {
        info_card.is_right = data['is_right'];
        info_card.english = data['english'];
        info_card.spell = data['spell'];
        info_card.level_alter = data['level_alter'];
        info_card.next_memory_time = data['next_memory_time'];
        info_card.pronunciation = data['pronunciation'];
        info_card.chinese = data['chinese'];
        info_card.info_image = data['info_image'];

        show_info_card();
    }


}


function clear() {
    $('#new_card').css('left','-5000px');
    $('#update_card').css('left','-5000px');
    $('#info_card').css('left','-5000px');
}


function card_show_faild(data) {
    console.log(data);
    console.log('错误显示卡片');

}


function get_word_card() {
    get(`${ip}/main/get_word_card/`, {}, card_show_success, card_show_faild);
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

//修改div尺寸
// {'id':'xxx','left':'00','top':'00','width':'00','height':'00','back_color':'xxx','back_image':'xxx','o':5,},
function div_init(div_list, r = rule) {
    for (let i = 0; i < div_list.length; i++) {
        let data = div_list[i];
        let obj = $(`#${data['id']}`);
        obj.css('position', 'absolute');
        // obj.css('border','red solid 1px');


        obj.css('width', r * data['width'] / 100 + 'px');

        obj.css('height', r * data['height'] / 100 + 'px');
        obj.css('left', r * data['left'] / 100 + 'px');
        obj.css('top', r * data['top'] / 100 + 'px');
        let back_image = data['back_image'];
        if (back_image !== 0) {
            obj.css('background-image', `url("${back_image}")`);
            obj.css('background-size', '100% auto');
            obj.css('background-repeat', 'no-repeat');
        }
        let back_color = data['back_color'];
        if (back_color !== 0) {
            obj.css('background-color', back_color);
        }

        let border_radius = data['o'];
        if (border_radius !== 0) {
            obj.css('border-radius', r * border_radius / 100 + 'px');
        }
        let border = data['border'];
        if (border !== 0) {
            obj.css('border', `${border} solid 1px`);
        }
    }
}

// {'id':'xxx','size':0.05,'r'=rule,'text-align':'xxx','font-family':'xxx',}
function font_init(div_list, r = rule) {
    for (let i = 0; i < div_list.length; i++) {
        let data = div_list[i];
        let obj = $(`#${data['id']}`);
        obj.css('font-size', r * data['size'] / 100 + 'px');
        let text_align = data['text-align'];
        if (text_align) {
            obj.css('text-align', text_align);
        }
        let font_family = data['font-family'];
        if (font_family) {
            obj.css('font-family', font_family);
        }
    }
}


























