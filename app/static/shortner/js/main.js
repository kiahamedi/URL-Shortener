console.log("Can you find me?");


$(document).on('click', '#btn-link-one', function(){ 
    navigator.clipboard.writeText($("#link-one").text());
    $("#btn-link-one").text("Copied");
});

$(document).on('click', '#btn-link-two', function(){ 
    navigator.clipboard.writeText($("#link-two").text());
    $("#btn-link-two").text("Copied");
});

$(document).on('click', '#btn-download-qr', function(){ 
    const qrdata = $('#qrcode').children('img').attr('src');
    console.log(qrdata)
    const anchor = document.createElement("a");
    anchor.href = qrdata;
    anchor.download = "QR.png";
    document.body.appendChild(anchor);
    anchor.click();
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
            $("#short-one").append('URL 1: <a target="_blank" id="link-one" href="https://kiay.ir/' +data+ '">https://kiay.ir/' + data + '</a> <button id="btn-link-one">Copy</button>');
            $("#short-two").html('');
            $("#short-two").append('URL 2: <a target="_blank" id="link-two" href="https://short.kiahamedi.ir/' +data+ '">https://short.kiahamedi.ir/' + data + '</a> <button id="btn-link-two">Copy</button>');

            $("#short-qr").html('');
            $("#short-qr").append('<div id="qrcode"></div>');
            const qrcode = new QRCode(document.getElementById('qrcode'), {
                text: 'https://kiay.ir/' + data,
                width: 128,
                height: 128,
                colorDark : '#000',
                colorLight : '#fff',
                correctLevel : QRCode.CorrectLevel.H
              });
            $("#short-qr").append('<button class="downloadqr" id="btn-download-qr">Download QR</button></a>');
            
        }
    });
});

