update_card = new Vue({
    el: '#update_card',
    data: {
        chinese: '',
        screen: '',
        show: true,
        Caps: false,

    }
});


//建造输入区
function update_card_build_keys() {
    let keys_obj = $('#update_card_keys');

    //第1行
    for (let i = 0; i < "QWERTYUIOP".length; i++) {
        let c = 'QWERTYUIOP'[i];
        keys_obj.append(`<div id=${c} class='key' onclick="key_function(this)">`);
        let key_obj = $(`#${c}`);
        key_obj.empty();
        key_obj.append(c.toLowerCase());
        key_obj.css('top', rule * 0.01);
        key_obj.css('left', rule * 0.01);
        key_obj.css('width', rule * 0.085);
        key_obj.css('height', rule * 0.085);
        let left = parseFloat(key_obj.css('left').replace('px', ''));
        key_obj.css('left', `${left + rule * i * 0.093}` + 'px');
        key_obj.css('font-size', `${rule * 0.08}px`);
    }
    //第2行
    for (let i = 0; i < 'ASDFGHJKL'.length; i++) {
        let c = 'ASDFGHJKL'[i];
        keys_obj.append(`<div id=${c} class='key' onclick="key_function(this)">`);

        let key_obj = $(`#${c}`);
        key_obj.empty();
        key_obj.append(c.toLowerCase());
        key_obj.css('top', rule * 0.105);
        key_obj.css('left', rule * 0.058);
        key_obj.css('width', rule * 0.085);
        key_obj.css('height', rule * 0.085);
        let left = parseFloat(key_obj.css('left').replace('px', ''));
        key_obj.css('left', `${left + rule * i * 0.093}` + 'px');
        key_obj.css('font-size', `${rule * 0.08}px`);


    }
    //第3行
    for (let i = 0; i < 'ZXCVBNM'.length; i++) {
        let c = 'ZXCVBNM'[i];
        keys_obj.append(`<div id=${c} class='key' onclick="key_function(this)">`);
        let key_obj = $(`#${c}`);
        key_obj.empty();
        key_obj.append(c.toLowerCase());
        key_obj.css('top', rule * 0.2);
        key_obj.css('left', rule * 0.16);
        key_obj.css('width', rule * 0.085);
        key_obj.css('height', rule * 0.085);
        let left = parseFloat(key_obj.css('left').replace('px', ''));
        key_obj.css('left', `${left + rule * i * 0.093}` + 'px');
        key_obj.css('font-size', `${rule * 0.08}px`);
    }

    let del_obj = $('#del');
    del_obj.css('font-size', `${rule * 0.07}px`);
    del_obj.css('top', `${rule * 0.2}px`);
    del_obj.css('left', `${rule * 0.815}px`);
    del_obj.css('width', `${rule * 0.12}px`);
    del_obj.css('height', `${rule * 0.085}px`);


    let caps_obj = $('#caps');
    caps_obj.css('font-size', `${rule * 0.07}px`);
    caps_obj.css('top', `${rule * 0.2}px`);
    caps_obj.css('left', `${rule * 0.01}px`);
    caps_obj.css('width', `${rule * 0.14}px`);
    caps_obj.css('height', `${rule * 0.085}px`);

    let dian_obj = $('#dian');
    dian_obj.css('font-size', `${rule * 0.07}px`);
    dian_obj.css('top', `${rule * 0.3}px`);
    dian_obj.css('left', `${rule * 0.01}px`);
    dian_obj.css('width', `${rule * 0.085}px`);
    dian_obj.css('height', `${rule * 0.085}px`);

    let gang_obj = $('#gang');
    gang_obj.css('font-size', `${rule * 0.07}px`);
    gang_obj.css('top', `${rule * 0.3}px`);
    gang_obj.css('left', `${rule * 0.85}px`);
    gang_obj.css('width', `${rule * 0.085}px`);
    gang_obj.css('height', `${rule * 0.085}px`);

    let kong_obj = $('#kong');
    kong_obj.css('font-size', `${rule * 0.06}px`);
    kong_obj.css('top', `${rule * 0.3}px`);
    kong_obj.css('left', `${rule * 0.105}px`);
    kong_obj.css('width', `${rule * 0.735}px`);
    kong_obj.css('height', `${rule * 0.085}px`);

}

//字母事件
function key_function(event) {
    let value = event.id;
    if (!update_card.Caps) {
        value = value.toLowerCase();
    }

    $('#update_card_screen_text').append(value);
    // update_card.screen = update_card.screen + value;
}

//空格/'/-事件
function kongge_function(event) {
    let obj = $(`#${event.id}`);
    let value = obj.attr('v');
    $('#update_card_screen_text').append(value);
    // update_card.screen = update_card.screen + value;
}


//大写事件
function caps_function() {
    let caps_obj = $('#caps');
    let keys = 'QWERTYUIOPASDFGHJKLZXCVBNM';
    if (update_card.Caps) {
        for (let i = 0; i < keys.length; i++) {
            let key_obj = $(`#${keys[i]}`);
            key_obj.empty();
            key_obj.append(keys[i].toLowerCase());
        }
        caps_obj.css('background', '#fff9fb');
        caps_obj.css('color', '#000000');
        update_card.Caps = false;
    } else {
        caps_obj.css('background', '#000000');
        caps_obj.css('color', '#fff9fb');
        for (let i = 0; i < keys.length; i++) {
            let key_obj = $(`#${keys[i]}`);
            key_obj.empty();
            key_obj.append(keys[i].toUpperCase());
        }
        update_card.Caps = true;
    }
}


//删除事件
function del_function() {
    let screen_obj=$('#update_card_screen_text');
    let val=screen_obj.text();
    val=val.substr(0, val.length - 1);
    screen_obj.empty();
    screen_obj.append(val);
}


//升级卡提交
function update_card_commit() {
    let data = {'word_index': update_card.word_index, 'spell': $('#update_card_screen_text').text()};
    post(`${ip}/main/update_card_commit/`, data, card_show_success, card_show_faild);
}


let update_card_div_setting = [
    {'id': 'screen', 'left': 0, 'top': 0, 'width': 100, 'height': 155,},
    {
        'id': 'update_card',
        'left': 0,
        'top': 0,
        'width': 100,
        'height': 155,
        'back_image': '/static/HTML/start/backs/test_word_back_4.jpg'
    },

    {'id': 'update_card_chinese', 'top': 12, 'left': 5, 'width': 90, 'height': 10, 'back_color': '#FFFFFF', 'o': 1},
    {'id': 'update_card_chinese_text', 'top': 1.5, 'left': 0, 'width': 90, 'height': 10, 'o': 1},

    {'id': 'update_card_screen', 'top': 30, 'left': 5, 'width': 90, 'height': 10, 'back_color': '#FFFFFF', 'o': 1},
    {'id': 'update_card_screen_text', 'top': 1.5, 'left': 0, 'width': 90, 'height': 10, 'o': 1},

    {'id': 'update_card_keys', 'top': 50, 'left': 2, 'width': 95, 'height': 40, 'back_color': '#dcdcdc', 'o': 1},

    {'id': 'update_card_ok', 'top': 100, 'left': 8, 'width': 80, 'height': 10, 'back_color': '#FFFFFF', 'o': 1},
    {'id': 'update_card_ok_text', 'top': 1.5, 'left': 0, 'width': 80, 'height': 10, 'o': 1},
];


let update_card_font_setting = [
    {'id': 'update_card_chinese_text', 'size': 6, 'text-align': 'center'},
    {'id': 'update_card_ok_text', 'size': 6, 'text-align': 'center'},
    {'id': 'update_card_screen_text', 'size': 7, 'text-align': 'center'},
];


//显示升级卡
function show_update_card() {
    clear();
    update_card.screen='';

    $('#update_card').css('background-image',`url("${update_card.update_image}")`);
    $('#update_card').css('left','0');


}
