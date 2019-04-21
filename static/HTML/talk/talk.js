rule=0;
window.onload=talk_start;


talk_div_setting=[
    {id:'screen',w:100,h:155,b:'#000000'},

    {id:'title',w:100,h:15,b_c:'#fff6e4',b:'#000000',o:2},
    {id:'main',w:15,h:15,s:'http://129.211.14.136:8006/url/index'},
    {id:'main_1',t:4.5,l:3,w:8,b:'#000000',x:-35},
    {id:'main_2',t:9.5,l:3,w:8,b:'#000000',x:35},
    {id:'title_text',t:1,l:0,w:100,h:15},

    {id:'show',t:16,w:100,h:122,o:2,b:'#000000',overflow:'auto'},

    {id:'input',t:139,w:100,h:15,o:2,b:'#000000'},
    {id:'text_div',t:2,l:2,w:78,h:10.5,o:2,b:'#000000'},
    // {id:'text',t:2,l:2,w:78,h:10.5,o:2,b:'#000000'},
    {id:'send',t:2,l:83,w:15,h:11,o:2,b:'#000000'},
];


talk_font_setting=[
    {id:'title_text',size:7,'text-align':'center','font-family':'Microsoft JhengHei'},
    {id:'send',size:7,'text-align':'center','font-family':'Microsoft JhengHei'},
    {id:'text',size:5,'font-family':'Microsoft JhengHei'},
    {id:'show',size:5,'font-family':'Microsoft JhengHei'},
];


function talk_start() {
    auto_width('screen');
    div_init(talk_div_setting,r=rule);
    font_init(talk_font_setting,r=rule);
    let url=`${ip}/talk/talk/`;
    get(url, {}, get_success, talk_faild);
    setInterval(xunhuan,5000);

}


function xunhuan() {
    let url=`${ip}/talk/talk/`;
    get(url, {}, get_success, talk_faild);
}


function get_success(data) {
    talk_success(data);
}
function post_success(data) {
    let text_obj=$('#text');
    text_obj.val('');
    talk_success(data);
}

function talk_success(data) {
    // let text_obj=$('#text');
    // text_obj.val('');
    let show_obj=$('#show');
    let title_text_obj=$('#title_text');
    title_text_obj.empty();
    title_text_obj.append(`聊天区(${data['user_count']})`);

    show_obj.empty();
    let results=data['results'];


    for(let i=0;i<results.length;i++)
    {
        let line_index=results.length-i-1;
        let line=results[line_index];
        let show_context='';
        if(line['myself'])
        {
            let head=`我(${line['name']})于${line['commit_time']}说道:`;
            let context=line['context'];
            context=`<text class="my_context">${context}</text>`;
            show_context=head+'<br>'+'&nbsp;&nbsp;'+context+'<br><br>';
        }
        else
        {
            let head=`${line['name']}童鞋于${line['commit_time']}说道:`;
            let context=line['context'];
            context=`<text class="other_context">${context}</text>`;
            show_context=head+'<br>'+'&nbsp;&nbsp;'+context+'<br><br>';
        }
        show_obj.append(show_context);
    }

}


function talk_faild(data) {
    console.log(data)
}


function send(event) {
    let text_obj=$(`#text`);
    let val=text_obj.val();
    let url=`${ip}/talk/talk/`;
    post(url, {'context':val}, post_success, talk_faild);
}



