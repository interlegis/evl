function habilitar() {
    var objtxt = document.getElementsByClassName("enable_btn");
    for(var i=0; i<7; i++) {
        objtxt[i].disabled = false;
    }
    var objEditar = document.getElementById("editarDadosBtn");
    objEditar.hidden = true;

    var objSalvar = document.getElementById("salvarDadosBtn");
    objSalvar.hidden = false;

    var objPhoto = document.getElementById("userPhoto");
    objPhoto.classList.remove('disabled');
}
function salvar() {
    var objtxt = document.getElementsByClassName("enable_btn");
    for(var i=0; i<7; i++) {
        objtxt[i].disabled = true;
    }
    var objEditar = document.getElementById("editarDadosBtn");
    objEditar.hidden = false;

    var objSalvar = document.getElementById("salvarDadosBtn");
    objSalvar.hidden = true;

    var objPhoto = document.getElementById("userPhoto");
    objPhoto.classList.add('disabled');
}