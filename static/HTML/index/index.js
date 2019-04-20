window.onload=start;
rule=500;


let index_div_setting=[
    {id:'index',w:100,h:155,b_i:'http://172.16.10.35:8000/static/HTML/index/back.png'},

    {id:'index_start',t:8,l:3,w:20,h:10,b_c:'#fff4d8',o:2,tou:0.9},

    {id:'index_census',t:115,l:18,w:20,h:10,b_c:'#fff4d8',o:2,tou:0.9},
    {id:'index_help',t:80,l:1,w:20,h:10,b_c:'#fff4d8',o:2,tou:0.9},
    {id:'index_talk',t:70,l:60,w:20,h:10,b_c:'#fff4d8',o:2,tou:0.9},

    {id:'index_exit',t:35,l:80,w:20,h:10,b_c:'#fff4d8',o:2,tou:0.9},
];

let index_font_setting=[
    {id:'index_start',size:6,'text-align':'center','font-family':'Microsoft JhengHei'},
    {id:'index_census',size:6,'text-align':'center','font-family':'Microsoft JhengHei'},
    {id:'index_help',size:6,'text-align':'center','font-family':'Microsoft JhengHei'},
    {id:'index_exit',size:6,'text-align':'center','font-family':'Microsoft JhengHei'},
    {id:'index_talk',size:6,'text-align':'center','font-family':'Microsoft JhengHei'},
];



function start() {
    auto_width('index');
    div_init(index_div_setting,r=rule);
    font_init(index_font_setting,r=rule);
    let talk_obj=$('#index_talk');
    let rotate=-30;
    setInterval(function () {
        rotate=rotate+2;
        talk_obj.css('transform',`rotate(${rotate}deg)`);
    },200)
}







