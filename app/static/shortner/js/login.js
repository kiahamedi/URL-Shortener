console.log("login!")

var input = document.querySelector("#phone");
window.intlTelInput(input, {
    // show dial codes too
    separateDialCode: true,
    // If there are some countries you want to show on the top.
    // here we are promoting russia and singapore.
    preferredCountries: ["ir", "us"],
    //Default country
    initialCountry:"ir",
    // If there are some countries you want to execlde.
    // here we are exluding india and israel.
    excludeCountries: ["in","il"]
});

function getCodeNumber(){
    const input = document.querySelector('#phone')
    const iti = window.intlTelInputGlobals.getInstance(input);
    var code = iti.getSelectedCountryData().dialCode;
    var number = $("#phone").val();
    return code + number; 
}

$(document).on('click', '#btn-login', function(){ 
    var userNumber = getCodeNumber();
    $.ajax({
        type: 'POST',
        url: '/login_or_register/',
        data: {
            phone: userNumber,
        },
        success: function(data){
            var status = data.status;
            if (status == "success"){
                $("#login-part").hide()
                $("#verify-part").show()
            }
        }
    });
});


$(document).on('click', '#btn-Verify', function(){ 
    var userNumber = getCodeNumber();
    $.ajax({
        type: 'POST',
        url: '/verify_otp/',
        data: {
            phone: userNumber,
            otp: $("#verify").val()
        },
        success: function(data){
            console.log(data)
            var status = data.status;
            if (status == "success"){
                setCookie("login", true, 2)
                setCookie("phone", userNumber, 2)
                setCookie("user_token", data.token, 2)
                $(location).prop('href', '/')
            } else {
                setCookie("login", false, 2)
                setCookie("user_token", "", 2)
                $("#login-part").show()
                $("#verify-part").hide()
            }
        }
    });
});