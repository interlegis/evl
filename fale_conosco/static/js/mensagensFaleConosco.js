$(document).ready(function(){
    $('#minhaTabela tbody').on('click', 'tr', function(){
        var minhaTabela = $("#minhaTabela").DataTable();
        if ( $(this).hasClass('selected') ) {
            $(this).removeClass('selected');
        }
        else {
            minhaTabela.$('tr.selected').removeClass('selected');
            $(this).addClass('selected');
        }
        $('#mensagens').removeClass('active');
        $('#detalhes').addClass('active');
        data = minhaTabela.row(this).data();

        $.ajax({
            type: "POST",
            dataType: 'json',
            url: "/faleConoscoMensagens/",
            data: {
                id: data[0],
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function(data){
                mensagens = "";
                mensagens += '<div style="overflow-y:scroll; overflow-x:hidden; margin-top:30px; height:300px;">';
                for (var i = 0, len = data.length; i < len; i++) {
                    var data_mensagem = data[i].data_mensagem.substring(8, 10) + '/' + data[i].data_mensagem.substring(5, 7) + '/' + data[i].data_mensagem.substring(0, 4);
                    var hora_mensagem = data[i].data_mensagem.substring(11, 16)
                    mensagens += '<div class="row">'
                    if (data[i].aluno != false) {
                        mensagens += '<div class="col-sm-7">'
                        mensagens += '<div style="background:#ffffff; border-radius: 15px;"> ';
                        mensagens +=
                            '  <div class="panel-heading">'+
                            '      <div class="panel-title" style="font-weight:650; color:green; font-size: 18px;">' + data[i].cpf + '</div>'+
                            '  </div>'+
                            ' <hr> ';
                    }
                    else {
                        mensagens += '<div class="col-sm-11">'
                        mensagens += '<div class="col-sm-7 float-right" style="background:#ffffff; border-radius: 15px;"> ';
                        mensagens +=
                            '  <div class="panel-heading">'+
                            '      <div class="panel-title" style="font-weight:650; color:blue; font-size: 18px;">' + data[i].cpf + '</div>'+
                            '  </div>'+
                            ' <hr> ';
                    }
                    mensagens += '  <div class="panel-body" style="word-break: break-all; font-weight:450;">'+
                        data[i].texto_mensagem +
                        ' <br><br> '+
                        '  </div><div class="text-right" style="font-style: italic; color:gray; font-weight:400; font-size:13px; margin-right:10px;">'+
                        data_mensagem + '  ' +
                        hora_mensagem +
                        '</div></div></div></div><hr>';
                };
                mensagens += '</div>';
                mensagens +=
                    '<div style="display:flex; align-items: center; overflow-y:hidden; overflow-x:hidden; margin-left:20px; margin-top:20px; width:1000px; height:75px;">' +
                    '<textarea style="background:white;" class="form-control" id="comment"></textarea>'+
                    '<button type="button" style="display: inline; text-align:center; margin-left: 20px;" id="sendMessage">Enviar</button>' +
                    '</div>';
                $('#sendMessage').click(function (){
                    description = ($('#comment').val());
                    description = description.replace(/(?:\r\n|\r|\n)/g, '<br>');
                    $('#comment').attr('value', "")

                });
                $('#tab2').html(mensagens);
                $('#tabs').tabs({ active: 1})
            },
            error: function(data){
                console.log("failure");
                console.log(data);
            },
        });
    });
})