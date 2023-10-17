console.log("Can you find me?");

$(document).on('submit', '#post-form', function(e){
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '/create/',
        data: {
            link: $("#link").val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },
        success: function(data){
            $("#short-one").html('');
            $("#short-one").append('URL Short 1: <a href="http://127.0.0.1:8000/' +data+ '">http://127.0.0.1:8000/' + data + '</a>');
            $("#short-two").html('');
            $("#short-two").append('URL Short 2: <a href="https://short.kiahamedi.ir/' +data+ '">https://short.kiahamedi.ir/' + data + '</a>');
        }
    });
});