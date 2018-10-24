$(document).ready(function(){
    $('#minhaTabela').DataTable({
        "language": {
            "lengthMenu": " ",
            "zeroRecords": "Nada encontrado",
            "info": "Mostrando página _PAGE_ de _PAGES_",
            "infoEmpty": "Nenhum registro disponível",
            "loadingRecords": "Carregando...",
            "processing":     "Processando...",
            "search":         "Pesquisar:",
            "infoFiltered": "(filtrado de _MAX_ registros no total)",
            "paginate": {
                "first":      "Primeira",
                "last":       "Última",
                "next":       "Próxima",
                "previous":   "Anterior"
            },
        },
        "scrollY": "220px"
    });
});
