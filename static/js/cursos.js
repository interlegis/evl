$(document).ready(function() {
  $("#list-tab a").click(function(){
    var selId = $(this).attr('id');
    var id = selId.substring(2,10);
    $("#nav-tabContent > *").css("display", "none")
    $("#"+id+"").css("display", "block");
  });
})
