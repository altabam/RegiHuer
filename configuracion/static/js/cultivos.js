function __init()
{
    $('#search_input')
        .val('')
        .focus()
        .keyup(function(){

            if(!$.trim($(this).val()))
                $('.results .error').empty().hide();
        });

    var cache = {};
    $('#search_input').autocomplete({
        minLength: 0,
        select: function( event, ui ) {
            return false;
        },
        open: function() {
            $('.resultados .listCultivos').html($(this).autocomplete("widget").html());
            $(this).autocomplete("widget").hide();
        },
        source: function( request, response ) {

         /*   if (cache[request.term]) {
                response(cache[request.term]);
                return;
            }
         */ $("#listCultivos").remove();
            $("#resultados").append("<tbody id=listCultivos> </tbody>");
            console.log("pasa por remove listcultivos")

            $.ajax({
                dataType : 'json',
                method : 'GET',
                url : '/configuracion/cultivo_buscar/',
                data : {
                    q : encodeURIComponent(request.term),
                    csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
                },
                success : function(data) {
                    var so = [];

                    for(var x in data)
                    {
                        cultivos.push({
                            
                            indice : x,
                            id : data[x].pk,
                            familia : data[x].fields['familia'],
                            nombre : data[x].fields['nombre'],
                            nombre_cientifico : data[x].fields['nombre_cientifico'],
                            imagen : data[x].fields['imagen'],
                            variedad : data[x].fields['variedad'],
                            descripcion : data[x].fields['descripcion']
                        });
                    }
                    console.log(cultivos)
                    cache[request.term] = cultivos;
                    response(cultivos);
                }
            });
        },
        response: function(event, ui) {

            if (ui.content.length === 0) {
                $('.results .error').html('No se encontraron resultados').show();
                $('.results .listCultivos').empty();
            }
            else
                $('.results .error').empty().hide();
        }
    }).autocomplete('instance')._renderItem = function(table, item) {

        var user_tmpl = $('<tr />')
                        .addClass('tr');

        user_tmpl.append('<td>'+item.indice+'</td>');
        user_tmpl.append('<td>'+item.familia+'</td>');
        user_tmpl.append('<td>'+item.nombre+'</td>');
        user_tmpl.append('<td>'+item.nombre_cientifico+'</td>');
        user_tmpl.append('<td><img src=/archivos/'+item.imagen+' width="70" height="70"></td>');
        user_tmpl.append('<td>'+item.variedad+'</td>');
        user_tmpl.append('<td>'+item.descripcion+'</td>');
        user_tmpl.append('<td colspan=3><a href=/configuracion/cultivo_editar/'+item.id+
            '><img src=/static/img/editar.png alt=Editar title=Editar/>'+ 
            '<a href=/configuracion/cultivo_eliminar/'+item.id + 
            '><img src=/static/img/eliminar.png alt=Eliminar title=Eliminar></a> </td>'
        );

                        
        return $('#listCultivos')
            .append(user_tmpl)
            
    };
}

