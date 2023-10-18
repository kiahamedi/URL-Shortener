console.log("Can you find me?");


$(document).on('click', '#btn-link-one', function(){ 
    navigator.clipboard.writeText($("#link-one").text());
    $("#btn-link-one").text("Copied");
});

$(document).on('click', '#btn-link-two', function(){ 
    navigator.clipboard.writeText($("#link-two").text());
    $("#btn-link-two").text("Copied");
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
            $("#short-one").append('URL Short 1: <a target="_blank" id="link-one" href="http://kiay.ir/' +data+ '">http://kiay.ir/' + data + '</a> <button id="btn-link-one">Copy</button>');
            $("#short-two").html('');
            $("#short-two").append('URL Short 2: <a target="_blank" id="link-two" href="https://short.kiahamedi.ir/' +data+ '">https://short.kiahamedi.ir/' + data + '</a> <button id="btn-link-two">Copy</button>');
        }
    });
});

