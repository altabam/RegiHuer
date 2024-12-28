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
        minLength: 2,
        select: function( event, ui ) {
            return false;
        },
        open: function() {
            $('.results .wrapper').html($(this).autocomplete("widget").html());
            $(this).autocomplete("widget").hide();
        },
        source: function( request, response ) {

            if (cache[request.term]) {
                response(cache[request.term]);
                return;
            }

            $.ajax({
                dataType : 'json',
                method : 'POST',
                url : '/configuracion/cultivo_buscar/',
                data : {
                    q : encodeURIComponent(request.term),
                    csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
                },
                success : function(data) {
                    var users = [];

                    for(var x in data)
                    {
                        users.push({
                            username : data[x].fields['nombre'],
                            CI : data[x].fields['especie'],
                            email : data[x].fields['descripcion']
                        });
                    }

                    cache[request.term] = users;
                    response(users);
                }
            });
        },
        response: function(event, ui) {

            if (ui.content.length === 0) {
                $('.results .error').html('No se encontraron resultados').show();
                $('.results .wrapper').empty();
            }
            else
                $('.results .error').empty().hide();
        }
    }).autocomplete('instance')._renderItem = function(ul, item) {

        var user_tmpl = $('<div />')
                        .addClass('user')
                        .append('<a href="/" />').find('a').addClass('username').html(item.username)
                        .parent()
                        .append('<span class="identity"><strong>Identidad:</strong><span></span></span>')
                        .find('.identity > span').append(item.CI)
                        .parent().parent()
                        .append('<span class="email"><strong>Email:</strong><span></span></span>')
                        .find('.email > span').append(item.email)
                        .parent().parent();

        return $('<div></div>')
            .data('item.autocomplete', item)
            .append(user_tmpl)
            .appendTo(ul);
    };
}

