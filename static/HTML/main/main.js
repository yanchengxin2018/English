rule=0;


let main_div_settings=[
    {id:'main_index',w:'100',h:'155',b_i:'http://129.211.14.136:8006/static/HTML/main/back.jpg'},
    {id:'jianjie_back',l:10,t:45,w:80,h:70,b_c:'#fff4d8',tou:0.4},
    {id:'jianjie',l:10,t:45,w:80,h:70},

];


let main_font_settings=[
    // {id:'screen_title_text',size:6,'text-align':'center','font-family':'Microsoft JhengHei'},
    // {id:'main_title',size:6,'text-align':'center','font-family':'Microsoft JhengHei'},


];


window.onload=main_start;

function main_start() {
    if(rule===0)auto_width('main_index');
    div_init(main_div_settings, r = rule);
    font_init(main_font_settings, r = rule);

}











