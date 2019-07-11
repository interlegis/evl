function habilitar() {
    $('input[name="birth_date"]').mask('20/30/1000', {'translation': {
        0: {pattern: /[0-9*]/},
        1: {pattern: /[1-2*]/},
        2: {pattern: /[0-3]/},
        3: {pattern: /[0-1]/}
    }});
    $('input[name="cpf"]').mask('000.000.000-00');

    var objtxt = document.getElementsByClassName("enable_btn");
    for(var i=0; i<7; i++) {
        objtxt[i].disabled = false;
    }

    var objEditar = document.getElementById("editarDadosBtn");
    console.log(objEditar)
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
