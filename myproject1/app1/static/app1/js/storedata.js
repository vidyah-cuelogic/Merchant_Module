var colors = [];
var images = [];



$(function() {
    $('#color1').colorPicker({
        onColorChange: function(id, newValue) {
            var template1 = newValue;
            colors.push(template1);
            $('#colors_list').append('<div class="color-tab">' + '<span style="background-color:' + template1 + '; height:16px; width:16px; display:inline-block; margin-right:5px"></span>' + template1 + '</div>');

            console.log("ID: " + id + " has been changed to " + newValue);
            $('#selected_colors').append('<option value=' + template1 + '>' + template1 + '</option>');
        }
    });
    $('.close').on('click', function() {
        $(this).parent().remove();
    });



});
$(function() {
    $('[data-toggle="tooltip"]').tooltip()
});


$("#myform").submit(function(e) {
    e.preventDefault();
    formdata = new FormData(this);
    formdata.append('color_list', JSON.stringify(colors));
    
    $.ajax({
        type: "POST",
        url: '/app1/dashboard/products/create_product/',
        data: formdata,
        dataType: "JSON",
        processData: false,
        contentType: false,
        success: function(response) {
            if (response.success) {
                $.notify(response.message);

                window.location.href = "/app1/dashboard/products/";
            } else {
                $.notify(response.message);
                $('#myform')[0].reset();
            }
        }
    });

});

$(document).ready(function() {
    $('#show-me').hide();
    $('input[type="radio"]').click(function() {
        if ($(this).attr('id') == 'watch-me') {
            $('#show-me').show();
        } else {
            $('#show-me').hide();
        }
    });
});
