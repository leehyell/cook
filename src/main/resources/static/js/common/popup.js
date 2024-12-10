//팝업
//팝업 공통 닫기
function commonHide(){
    $('body').css('overflow', 'auto');
    $('.common_pop').hide();
}
//alert
function alertHide(){
    $('body').css('overflow', 'auto');
    $('.alert_whole').hide();
}
function alertShow(title, subtitle){
    $('body').css('overflow', 'hidden');
    $('.alert_whole').show();
    $('#alert_title').html(title);
    $('#alert_subtitle').html(subtitle);
}
//confirm
function confirmHide(){
    $('body').css('overflow', 'auto');
    $('.confirm_whole').hide();
}
function confirmShow(title, subtitle, type){
    $('body').css('overflow', 'hidden');
    $('.confirm_whole').show();
    $('#confirm_title').html(title);
    $('#confirm_subtitle').html(subtitle);
    $('#confirm_message').attr('value', type);
}
function popConfirm(){
    let confirm_message = $('#confirm_message').val();
    if(confirm_message == 'none'){
        commonHide();
    }
    else{
        confirmHide();
        confirmOk(confirm_message);
    }
}
//standby
function standbyHide(){
    $('body').css('overflow', 'auto');
    $('.standby_whole').hide();
}
function standbyShow(title, subtitle){
    $('body').css('overflow', 'hidden');
    $('.standby_whole').show();
    $('#standby_title').html(title);
    $('#standby_subtitle').html(subtitle);
}

function mypageChk() {
    $("body").css('overflow', 'hidden');
    $('.pwchk_whole').show();
}
function mypageHide() {
    $('body').css('overflow', 'auto');
    $('.pwchk_whole').hide();
}
//mypage 들어갈 때 pwchk
function mypagepwchk() {
    var chkpw = $("#chkpw").val();
    if(chkpw!='') {
        var id = $("#header_mypage").text();
        var pw= $("#chkpw").val();
        $.ajax({
            type:"post",
            url:"/pwchk",
            async:true,
            data:{"id":id,"pw":pw},
            success:function(data){
                if(data){
                    if(data=='true'){
                        location.href="/mypage?id="+id;
                    }else{
                        alertShow("오류","비밀번호가 다릅니다");
                        return false;
                    }
                }
            },
            error:function(data){
                alertShow("오류","다시 한 번 시도해주세요");
                return false;
            }
        });
    }else{
        alertShow("비밀번호를 입력해주세요!","");
    }
    //비밀번호 보기 구현
     $('.pw i').on('click',function(){
         $('input').toggleClass('active');
         if($('input').hasClass('active')){
             $(this).attr('class',"fa fa-eye fa-lg")
             .prev('input').attr('type',"text");
         }else{
             $(this).attr('class',"fa fa-eye-slash fa-lg")
             .prev('input').attr('type','password');
         }
     });
}
function addrCheck(id,orderitem,price) {
    $("body").css('overflow', 'hidden');
    $('.address_whole').show();
    $('#id').val(id);
    $('#orderitem').val(orderitem);
    $('#price').val(price);
    $.ajax({
        url:"/cart/orderAddress",
        type:"post",
        async:"true",
        data:{"id":id},
        success:function(data){
            var str = data.split('+');
            $('#addr').val(str[0]);
            $('#streetaddr').val(str[1]);
            $('#detailaddr').val(str[2]);
       },
       error:function(){alertShow("에러","");}
    });
}
function addrChange(){
    execDaumPostcode();
    $('#detailaddr').val("");
    $('#detailaddr').attr('readonly',false);
}
function addressConfirm(){
    var address = '['+$('#addr').val()+']' + '\t' + $('#streetaddr').val() + "\t" + $('#detailaddr').val();
    var id = $('#id').val();
    var orderitem = $('#orderitem').val();
    var price = $('#price').val();
    $.ajax({
        url:"/cart/order",
        type:"post",
        async:"true",
        data:{"id":id,"orderitem":orderitem,"price":price,"address":address},
        success:function(data){
            addrHide();
            $('.btn_hide').hide();
            confirmShow("주문이 완료되었습니다.","","reloadok");
       },
       error:function(){alertShow("에러","");}
    });
}
function addrHide(){
    $('body').css('overflow', 'auto');
    $('.address_whole').hide();
}