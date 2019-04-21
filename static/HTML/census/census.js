let rule = 0;

let census_div_settings = [
    {id: 'screen', w: '100', h: '155', b_i: 'http://129.211.14.136:8006/static/HTML/census/2.jpg '},

    {
        id: 'screen_title',
        l: '10',
        t: 12,
        w: '80',
        h: '15',
        b_i: 'http://129.211.14.136:8006/static/HTML/census/title.png'
    },
    {id: 'screen_title_text', t: -1, l: 3, r: '', w: '35', h: '10'},
    //
    {id: 'census_0', t: 35, l: 5, w: 90, h: 110, b_c: '#fff4d8', o: 5, b: '#000000', 'tou': 0.5},
    {id: 'census_1', t: 35, l: 5, w: 90, h: 110,},
    //
    {id: 'census_title', t: 3, l: 20, r: '', w: 50, h: 10},
    {id: 'census_body', t: 15, l: 10, r: '', w: 70, h: 90},

];


let census_font_settings = [
    {id: 'screen_title_text', size: 6, 'text-align': 'center', 'font-family': 'Microsoft JhengHei'},
    {id: 'census_title', size: 5, 'text-align': 'center', 'font-family': 'Microsoft JhengHei'},


];


window.onload = census_start;

function census_start() {
    if (rule === 0) auto_width('screen');


    let url = `${ip}/main/census/`;
    get(url, {}, census_success, census_faild);

}


function census_success(data) {
    let census_title_obj = $('#census_title');
    let screen_title_text_obj = $('#screen_title_text');
    census_title_obj.empty();
    screen_title_text_obj.empty();
    census_title_obj.append(`一共有${data['word_sum']}个单词`);
    screen_title_text_obj.append(`${data['name']}同学`);


    for (let level = 0; level < 15; level++) {
        $(`#level_${level}_num`).append(level);
        div_init([{
            id: `level_${level}`,
            l: 5,
            t: level * 5.8,
            w: 60,
            h: 5,
            b: '#000000',
            b_c: '#fff4d8',
            o: 2
        },], r = rule);
        font_init([{id: `level_${level}_ci`, size: 3.6, 'text-align': 'center',},], r = rule);
        let level_count = data[level];
        let n = Number(level_count);
        $(`#level_${level}_ci`).append(`${level_count}词`);
        let a = level_count / 16;
        let count_img = 'count_100.png';
        if (n <= 100) {
            n = n / 16;
            n = n * 5;
            div_init([{id: `level_${level}_line`, l: 10, t: 2.1, w: n, b: '#43ff3d',},], r = rule);
            $(`#level_${level}_line`).css('border', '#43ff3d solid 10px');
            count_img = 'count_100.png';


        } else if (100 < n && n <= 500) {
            n = n / 16;
            div_init([{id: `level_${level}_line`, l: 10, t: 2.1, w: n, b: '#4634ff',},], r = rule);
            $(`#level_${level}_line`).css('border', '#4634ff solid 10px');
            count_img = 'count_500.png';
        } else if (500 < n && n <= 1500) {
            n = n - 500;
            n = n / 16;
            n = n / 2;
            div_init([{id: `level_${level}_line`, l: 10, t: 2.1, w: n, b: '#ff1cea',},], r = rule);
            $(`#level_${level}_line`).css('border', '#ff1cea solid 10px');
            count_img = 'count_1500.png';
        } else if (1500 < n && n <= 4000) {
            n = n - 1500;
            n = n / 16;
            n = n / 5;
            div_init([{id: `level_${level}_line`, l: 10, t: 2.1, w: n, b: '#ff2020',},], r = rule);
            $(`#level_${level}_line`).css('border', '#ff2020 solid 10px');
            count_img = 'count_4000.png';
        } else {
            n = 4000;
            n = n - 1500;
            n = n / 16;
            n = n / 5;
            div_init([{id: `level_${level}_line`, l: 10, t: 2.1, w: n, b: '#ff2020',},], r = rule);
            $(`#level_${level}_line`).css('border', '#ff2020 solid 10px');
            count_img = 'count_4000.png';
        }




        div_init([{
            id: `level_${level}_img`, l: n + 12, t: 0, w: 5.3,
            b_i: `http://129.211.14.136:8006/static/HTML/census/${count_img}`
        },], r = rule);

        $(`#level_${level}_num`).css('top', rule * -0.01 + 'px');
        font_init([{
            id: `level_${level}_num`,
            size: 4,
            'text-align': 'right',
            'font-family': 'Microsoft JhengHei'
        }], r = rule)

    }

    div_init(census_div_settings, r = rule);
    font_init(census_font_settings, r = rule);
}


function census_faild(data) {
    console.log('失败');
    console.log(data);
    let census_title_obj = $('#census_title');
    let tips = data['responseJSON']['tips'];
    census_title_obj.append('记载失败:' + tips);
    div_init(census_div_settings, r = rule);
    font_init(census_font_settings, r = rule);
}









