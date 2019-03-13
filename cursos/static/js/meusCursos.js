function mostrar_itens(obj) {
    document.getElementById('emAndamento').hidden="none";
    document.getElementById('trancados').hidden="true";
    document.getElementById('finalizados').hidden="true";
    document.getElementById('emAndamento_message').hidden="none";
    document.getElementById('trancados_message').hidden="none";
    document.getElementById('finalizados_message').hidden="none";
    switch (obj.id) {
        case 'emAndamento_click':
            document.getElementById('emAndamento').hidden = false;
            document.getElementById('trancados').hidden = true;
            document.getElementById('finalizados').hidden = true;
            document.getElementById('emAndamento_message').hidden = false;
            document.getElementById('trancados_message').hidden = true;
            document.getElementById('finalizados_message').hidden = true;
            break;
        case 'trancados_click':
            document.getElementById('emAndamento').hidden = true;
            document.getElementById('trancados').hidden = false;
            document.getElementById('finalizados').hidden = true;
            document.getElementById('emAndamento_message').hidden = true;
            document.getElementById('trancados_message').hidden = false;
            document.getElementById('finalizados_message').hidden = true;
            break;
        case 'finalizados_click':
            document.getElementById('emAndamento').hidden = true;
            document.getElementById('trancados').hidden = true;
            document.getElementById('finalizados').hidden = false;
            document.getElementById('emAndamento_message').hidden = true;
            document.getElementById('trancados_message').hidden = true;
            document.getElementById('finalizados_message').hidden = false;
            break;
    }
}
function MudarEstado(el) {
    var display = document.getElementById(el).style.display;
    if (display == "none")
        document.getElementById(el).style.display = 'block';
}