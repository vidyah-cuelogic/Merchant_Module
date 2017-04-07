var colors = [];
var images = [];



$(function() {
    $('#color1').colorPicker({
        onColorChange: function(id, newValue) {
            var template1 = newValue;
            colors.push(template1);
            $('#colors_list').append('<div class="color-tab">' + '<span style="background-color:' + template1 + '; height:16px; width:16px; display:inline-block; margin-right:5px"></span>' + template1 + '<button class="close" aria-label="Close" >' +
                '<span class="close-btn" >&times;</span>' +
                '</button></div>');

            console.log("ID: " + id + " has been changed to " + newValue);
            

            console.log(color_mapping);
            $('.close').on('click', function() {
                $(this).parent().remove();
            });

            $('#selected_colors').append('<option value=' + template1 + '>' + template1 + '</option>');
        }
    });


});


console.log(colors);

$("#myform").submit(function(e) {
    console.log(colors);
    e.preventDefault();
    formdata = new FormData(this);
    selected_cat = $('#first').val();
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
                $('#error-message').text(response.message);
            } else{
                $('#error-message').text(response.message);
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
