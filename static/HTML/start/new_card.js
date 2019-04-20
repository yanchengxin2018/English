new_card = new Vue({
    el: '#new_card',
    data: {
        english: ' ',
        chinese: ' ',
        pronunciation: ' ',
        show: true
    }
});

//新词卡提交
function new_card_commit() {
    post(`${ip}/main/new_card_commit/`, {'word_index': new_card.word_index}, card_show_success, card_show_faild)
}


let new_card_div_setting = [
    {'id': 'screen', 'left': 0, 'top': 0, 'width': 100, 'height': 155,},
    {'id': 'new_card', 'left': 0, 'top': 0, 'width': 100, 'height': 155, 'back_color': '#000000'},
    {'id': 'new_card_head', 'left': 0, 'top': 0, 'width': 100, 'height': 52,},
    {
        'id': 'new_card_body',
        'left': 0,
        'top': 46,
        'width': 100,
        'height': 57,
        'back_image': '/static/HTML/start/word_back.jpg'
    },
    {'id': 'new_card_ok', 'left': 35, 'top': 120, 'width': 30, 'height': 15, 'o': 4, 'back_color': '#FFFFFF'},
    {'id': 'new_body_english', 'left':10, 'top': 10, 'width': 80, 'height': 8, 'back_color': '#FFFFFF',o:5},
    {'id': 'new_body_english_text', 'left':0, 'top': -2, 'width': 80, 'height': 8,},
    {'id': 'new_body_pronunciation', 'left':10, 'top': 22, 'width': 80, 'height': 8, 'back_color': '#FFFFFF',o:5},
    {'id': 'new_body_pronunciation_text','left':0, 'top': 1, 'width': 80, 'height': 8},


    {'id': 'new_body_chinese', 'left':10,'top': 35, 'width': 80, 'height': 8, 'back_color': '#FFFFFF',o:5},
    {'id': 'new_body_chinese_text',  'left':0, 'top': 1, 'width': 80, 'height': 8,},


    {'id': 'new_card_ok_text', 'top': -3, 'left': 1, 'width': 30, 'height': 10,},

];


let new_card_font_setting = [
    {'id': 'new_body_english', 'size': 7, 'text-align': 'center', 'font-family': 'Microsoft JhengHei'},
    {'id': 'new_body_pronunciation', 'size': 5, 'text-align': 'center'},
    {'id': 'new_body_chinese', 'size': 5, 'text-align': 'center'},
    {'id': 'new_card_ok_text', 'size': 13, 'text-align': 'center', 'font-family': 'Microsoft JhengHei',},
];


//显示新卡片
function show_new_card() {
    clear();
    $('#new_card').css('left','0');
    $('#new_card_body').css('background-image',`url("${new_card.back_image}")`);

    // new_card.show=true;
    // div_init(new_card_div_setting);
    // font_init(new_card_font_setting);
    // clear(new_card);
    // new_card.show=true;

}









