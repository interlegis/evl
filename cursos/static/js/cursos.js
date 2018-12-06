$(document).ready(function() {
  $("#list-tab a").click(function(){
    var selId = $(this).attr('id');
    var id = selId.substring(2,10);
    $("#nav-tabContent > *").css("display", "none")
    $("#"+id+"").css("display", "block");
  });
});

function selectEstado(){
    estado = $("#id_status").val();
    console.log("ESTADO = ", $("#id_status").val());
    if($('#id_status').val() == 'Aprovado'){
      $('#categoria').css({'display': 'block'})
    }
    else {
      $('#categoria').css({'display': 'none'})
    }
}
