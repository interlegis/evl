$(document).ready(function() {
  $("#enviar-btn").click(function(){
    var id = $('#exampleFormControlSelect1').val();
    $("#enviar-btn").attr('href', $("#enviar-btn").attr('href').replace('/0', '/' + id));
  });
  $(".click-btn").click(function(){
    var id = jQuery(this).attr("id")
    $("#enviar-btn").attr('href', '/aprovar_curso/' + id + '/0/');
  });
  $(".click-btn-categoria").click(function(){
    var id = jQuery(this).attr("id")
    var name = jQuery(this).attr("myvalue")
    $("#categoriaName").val(name);
    $("#enviar-btn-categoria").attr('href', '/editar_categoria/' + id + '/0/');
  });
  $("#enviar-btn-categoria").click(function(){
    var name = $('#categoriaName').val();
    $("#enviar-btn-categoria").attr('href', $("#enviar-btn-categoria").attr('href').replace('/0', '/' + name));
  });
  $("#enviar-btn-categoriaNova").click(function(){
    var name = $('#categoriaNameNova').val();
    $("#enviar-btn-categoriaNova").attr('href', $("#enviar-btn-categoriaNova").attr('href').replace('/0', '/' + name));
  });

})
