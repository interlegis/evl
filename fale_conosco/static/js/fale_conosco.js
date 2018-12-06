$(".dropdown-menu li a").click(function(){
  var selText = $(this).text();
  console.log( selText);
  select_staff.innerHTML = selText
});