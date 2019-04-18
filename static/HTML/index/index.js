window.onload=start;


function start() {
    let index_obj=$('#index');
    let index_start_obj=$('#index_start');
    let index_census_obj=$('#index_census');
    let index_help_obj=$('#index_help');
    let index_exit_obj=$('#index_exit');
    let index_width=index_obj.css('width').replace('px','');
    let index_heigh=index_width*1.55;
    index_obj.css('height',index_heigh);
    let font_size=index_width*0.1;
    index_start_obj.css('font-size',font_size);
    index_census_obj.css('font-size',font_size);
    index_help_obj.css('font-size',font_size);
    index_exit_obj.css('font-size',font_size);
}