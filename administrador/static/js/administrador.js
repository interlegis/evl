$(document).ready(function() {
  $("#enviar-btn").click(function(){
    var id = $('#exampleFormControlSelect1').val();
    $("#enviar-btn").attr('href', $("#enviar-btn").attr('href').replace('/0', '/' + id));
  });
  $(".click-btn").click(function(){
    var id = jQuery(this).attr("id")
    $("#enviar-btn").attr('href', '/aprovar_curso/' + id + '/0/');
  });
})
