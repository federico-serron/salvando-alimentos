/*--------------------------------------------------------------
# EDIT PRODUCT Form validation
--------------------------------------------------------------*/
document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("editProductForm").addEventListener('submit', editValidation);
});

function editValidation(event){
    event.preventDefault();
    var title = document.getElementById('title').value;
    var description = document.getElementById('description').value;
    var available_quant = document.getElementById('available_quant').value;
    var price = document.getElementById('price').value;

    var patternText = /[^a-zA-Z\s]+/i;
    var patternAddress = /[^A-Za-z0-9\s\,\.]/;


    if(patternText.test(title)){
        document.getElementById('alertEdit').innerHTML = "Debe ingresar solo letras para el campo <strong>Título</strong>.";
        document.getElementById('alertEdit').style.display = 'block';
        return;
    }

        if(patternAddress.test(description)){
        document.getElementById('alertEdit').innerHTML = "Carácteres incorrectos en el campo <strong>Descripción</strong>.";
        document.getElementById('alertEdit').style.display = 'block';
        return;
    }

        if(available_quant < 1){
        document.getElementById('alertEdit').innerHTML = "Debe ingresar una cantidad mayor a 0 en el campo <strong>Cantidad Disponible</strong>.";
        document.getElementById('alertEdit').style.display = 'block';
        return;
    }

        if(price < 1){
        document.getElementById('alertEdit').innerHTML = "Debe ingresar una precio mayor a 0 en el campo <strong>Precio</strong>.";
        document.getElementById('alertEdit').style.display = 'block';
        return;
    }

    this.submit();
}


/*--------------------------------------------------------------
# CREATE PRODUCT Form validation
--------------------------------------------------------------*/
document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("createProductForm").addEventListener('submit', createValidation);
});

function createValidation(event){
    event.preventDefault();
    var title = document.getElementById('title').value;
    var description = document.getElementById('description').value;
    var available_quant = document.getElementById('available_quant').value;
    var price = document.getElementById('price').value;
    var time = document.getElementById('pickup_time').value;

    var patternText = /[^a-zA-Z\s]+/i;
    var patternAddress = /[^A-Za-z0-9\s\,\.]/;


    if(patternText.test(title)){
        document.getElementById('alertEdit').innerHTML = "Debe ingresar solo letras para el campo <strong>Título</strong>.";
        document.getElementById('alertEdit').style.display = 'block';
        return;
    }

        if(patternAddress.test(description)){
        document.getElementById('alertEdit').innerHTML = "Carácteres incorrectos en el campo <strong>Descripción</strong>.";
        document.getElementById('alertEdit').style.display = 'block';
        return;
    }

        if(available_quant < 1){
        document.getElementById('alertEdit').innerHTML = "Debe ingresar una cantidad mayor a 0 en el campo <strong>Cantidad Disponible</strong>.";
        document.getElementById('alertEdit').style.display = 'block';
        return;
    }

        if(price < 1){
        document.getElementById('alertEdit').innerHTML = "Debe ingresar una precio mayor a 0 en el campo <strong>Precio</strong>.";
        document.getElementById('alertEdit').style.display = 'block';
        return;
    }

        if(time == 0 ){
        document.getElementById('alertEdit').innerHTML = "Debe ingresar horario de <strong>Recoleccion</strong>.";
        document.getElementById('alertEdit').style.display = 'block';
        return;
    }

    this.submit();
}