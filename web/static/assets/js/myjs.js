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

