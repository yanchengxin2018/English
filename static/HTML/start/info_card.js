info_card = new Vue({
    el: '#info_card',
    data: {
        english: '',
        chinese: '',
        pronunciation: '',
        spell: '',
        is_right_show: '',
        next_memory_time: '',
        level_alter: '',
        show: true
    }
});

let info_card_div_setting = [
    {'id': 'screen', 'left': 0, 'top': 0, 'width': 100, 'height': 155,},
    {
        'id': 'info_card', 'top': 0, 'left': 0, 'width': 100, 'height': 155,
        'back_image': '/static/HTML/start/backs/info_card_back_0.jpg'
    },

    {'id': 'info_card_success_status', 'top': 10, 'left': 9, 'width': 82, 'height': 15, 'o': 1, 'border': '#000000',},
    {'id': 'info_card_success_status_text', 'top': 0, 'left': 0, 'width': 82, 'height': 2},


    {
        'id': 'info_card_body',
        'top': 25,
        'left': 9,
        'width': 82,
        'height': 95,
        'back_color': '#fff0ed',
        'border': '#000000',
    },


    {
        'id': 'info_card_body_word',
        'top': 10,
        'left': 6,
        'width': 70,
        'height': 11,
        'back_color': '#fffbfd',
        'o': 2,
        'border': '#000000',
    },
    {'id': 'info_card_body_input', 'top': 23, 'left': 6, 'width': 70, 'height': 11, 'o': 2, 'border': '#000000',},
    {
        'id': 'info_card_body_level',
        'top': 36,
        'left': 6,
        'width': 70,
        'height': 11,
        'back_color': '#fffbfd',
        'o': 2,
        'border': '#000000',
    },
        {
        'id': 'info_card_body_level_text',
        'top': 2,
        'left': 0,
        'width': 70,
        'height': 11,
    },
    {
        'id': 'info_card_body_time',
        'top': 49,
        'left': 6,
        'width': 70,
        'height': 11,
        'back_color': '#fffbfd',
        'o': 2,
        'border': '#000000',
    },
    {
        'id': 'info_card_body_pronunciation',
        'top': 62,
        'left': 6,
        'width': 70,
        'height': 11,
        'back_color': '#fffbfd',
        'o': 2, 'border': '#000000',
    },
            {
        'id': 'info_card_body_pronunciation_text',
        'top': 0,
        'left': 0,
        'width': 70,
        'height': 11,
    },
                {
        'id': 'info_card_body_chinese_text',
        'top': 2,
        'left': 0,
        'width': 70,
        'height': 11,
    },
    {
        'id': 'info_card_body_input_text',
        'top': 2,
        'left': 0,
        'width': 70,
        'height': 11,
    },
    {
        'id': 'info_card_body_time_text',
        'top': 2,
        'left': 0,
        'width': 70,
        'height': 11,
    },
    {
        'id': 'info_card_body_chinese',
        'top': 75,
        'left': 6,
        'width': 70,
        'height': 11,
        'back_color': '#fffbfd',
        'o': 2,
        'border': '#000000',
    },


    {
        'id': 'info_card_submit',
        'top': 120,
        'left': 9,
        'width': 82,
        'height': 15,
        'back_color': '#e9faff',
        'o': 1,
        'border': '#000000',
    },
    {'id': 'info_card_submit_text', 'top': 0, 'left': 0, 'width': 82, 'height': 2},
];

let info_card_font_setting = [
    {'id': 'info_card_success_status_text', 'size': 8, 'text-align': 'center', 'font-family': 'Microsoft JhengHei',},
    {'id': 'info_card_body_word_text', 'size': 8, 'text-align': 'center'},
    {'id': 'info_card_body_input_text', 'size': 8, 'text-align': 'center'},
    {'id': 'info_card_body_level_text', 'size': 6, 'text-align': 'center'},
    {'id': 'info_card_body_time_text', 'size': 5, 'text-align': 'center'},
    {'id': 'info_card_body_pronunciation_text', 'size': 6, 'text-align': 'center', 'font-family': 'Microsoft JhengHei',},
    {'id': 'info_card_body_chinese_text', 'size': 6, 'text-align': 'center'},
    {'id': 'info_card_submit_text', 'size': 8, 'text-align': 'center', 'font-family': 'Microsoft JhengHei',},
];


//显示新卡片
function show_info_card() {
    clear();
    $('#info_card').css('left','0');
    $('#info_card').css('background-image',`url("${info_card.info_image}")`);
    if (info_card.is_right) {
        $('#info_card_success_status').css('background-color', '#beffc4');
        $('#info_card_body_input').css('background-color', '#beffc4');
        $('#info_card_success_status_text').empty();
        $('#info_card_success_status_text').append('正 确');
        // info_card.is_right_show = '正 确'
    } else {
        $('#info_card_success_status').css('background-color', '#fff4d8');
        $('#info_card_body_input').css('background-color', '#fff4d8');
        $('#info_card_success_status_text').empty();
        $('#info_card_success_status_text').append('错 误');
        // info_card.is_right_show = '错 误'
    }

}




















