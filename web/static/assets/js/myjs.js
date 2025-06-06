$(document).ready(function() {


  $('#name').mouseenter(function() {
    $('.dropdown-menu').toggle("slow");
  });

  $('#categories-menu').mouseout(function() {
    $('.dropdown-menu').toggle("slow");
  });

  $('.dropdown-item').click(function(){
    $('.dropdown-menu').toggle("slow");
  });


/*--------------------------------------------------------------
# AJAX REQUEST IN Products view
--------------------------------------------------------------*/
    $('#category_form').submit(function(event){
        event.preventDefault();
        $.ajax({
            url: '/products',
            type: 'POST',
            data: data,
            processData: False,
            contentType: False,
            success: function(result){

            }
        });
    });

});


/*--------------------------------------------------------------
# LOGIN Form validation
--------------------------------------------------------------*/
document.addEventListener("DOMContentLoaded", function() {
  var loginForm = document.getElementById("loginForm");
  if (loginForm) {
    loginForm.addEventListener('submit', loginValidation);
  }
});

function loginValidation(event){
    event.preventDefault();
    var user = document.getElementById('typeEmailX').value;
    if(user.length <= 5){
        document.getElementById('emailAlert').innerHTML = "Debe ingresar un email mayor a 5 caracteres.";
        document.getElementById('emailAlert').style.display = 'block';
        return;
    }

    var pass = document.getElementById('typePasswordX').value;
    if(pass.length <= 5){
        document.getElementById('passAlert').innerHTML = "Debe ingresar una clave mayor a 5 caracteres.";
        document.getElementById('passAlert').style.display = 'block';
        return;
    }
    this.submit();
}

/*--------------------------------------------------------------
# REGISTER Form validation
--------------------------------------------------------------*/
document.addEventListener("DOMContentLoaded", function() {
  var registerForm = document.getElementById("registerForm");
  if (registerForm) {
    registerForm.addEventListener('submit', RegisValidation);
  }
});

function RegisValidation(event){
    event.preventDefault();
    var patternText = /[^a-zA-Z]+/i;
    var patternAddress = /[^A-Za-z0-9\s\,]/;
    var name = document.getElementById('name').value;
    var lastname = document.getElementById('lastname').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var address = document.getElementById('address').value;
    var city = document.getElementById('city').value;
    var zip = document.getElementById('zip').value;
    var company_name = document.getElementById('company_name').value;

    if(isNaN(zip)){
        document.getElementById('dangerAlert').innerHTML = "Debe ingresar un número para el campo <strong>ZIP</strong>";
        document.getElementById('dangerAlert').style.display = 'block';
        return;
    }

    if(patternText.test(name)){
        document.getElementById('dangerAlert').innerHTML = "Debe ingresar solo letras para el campo <strong>Nombre</strong>";
        document.getElementById('dangerAlert').style.display = 'block';
        return;
    }

        if(patternText.test(lastname)){
        document.getElementById('dangerAlert').innerHTML = "Debe ingresar solo letras para el campo <strong>Apellido</strong>";
        document.getElementById('dangerAlert').style.display = 'block';
        return;
    }

        if(patternText.test(city)){
        document.getElementById('dangerAlert').innerHTML = "Debe ingresar solo letras para el campo <strong>Ciudad</strong>";
        document.getElementById('dangerAlert').style.display = 'block';
        return;
    }

        if(patternAddress.test(company_name)){
        document.getElementById('dangerAlert').innerHTML = "Debe ingresar solo letras para el campo <strong>Compañía</strong>";
        document.getElementById('dangerAlert').style.display = 'block';
        return;
    }

        if(patternAddress.test(address)){
        document.getElementById('dangerAlert').innerHTML = "Debe ingresar solo letras y números para el campo <strong>Dirección</strong>";
        document.getElementById('dangerAlert').style.display = 'block';
        return;
    }

    this.submit();


}