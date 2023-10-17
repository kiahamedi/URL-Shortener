console.log("Can you find me?");


$(document).on('click', '#btn-link-one', function(){ 
    navigator.clipboard.writeText($("#link-one").text());
    $("#btn-link-one").text("Copied");
});

$(document).on('click', '#btn-link-two', function(){ 
    navigator.clipboard.writeText($("#link-two").text());
    $("#btn-link-one").text("Copied");
});

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
            $("#short-one").append('URL Short 1: <a id="link-one" href="http://127.0.0.1:8000/' +data+ '">http://127.0.0.1:8000/' + data + '</a> <button id="btn-link-one">Copy</button>');
            $("#short-two").html('');
            $("#short-two").append('URL Short 2: <a id="link-two" href="https://short.kiahamedi.ir/' +data+ '">https://short.kiahamedi.ir/' + data + '</a> <button id="btn-link-two">Copy</button>');
        }
    });
});

