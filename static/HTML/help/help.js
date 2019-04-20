rule=0;
window.onload=help_start;


let help_div_setting=[
    {id:'help',w:100,h:155,b_i:'http://172.16.10.35:8000/static/HTML/census/help.jpeg',},
    {id:'help_text',l:10,t:15,w:80,h:110,b_c:'#fff4d8',tou:0.7,o:5,},
    {id:'help_text_copy',l:10,t:15,w:80,h:110},
    {id:'help_text_title',l:10,t:15,w:60,h:10},
    {id:'help_text_context',l:10,t:35,w:60,h:50},
];

let help_font_setting=[
    {id:'help_text_title',size:5,'text-align':'center','font-family':'Microsoft JhengHei'},
    {id:'help_text_context',size:3,'text-align':'left','font-family':'Microsoft JhengHei'},
];


function help_start() {
    if(rule===0) {
        let help_obj = $('#help');
        help_obj.css('width','100%');
        rule=help_obj.css('width').replace('px','');
    }



    div_init(help_div_setting,r=rule);
    font_init(help_font_setting,r=rule);

}