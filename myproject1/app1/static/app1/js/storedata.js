$("#myform").submit(function(e) {
    e.preventDefault();
    var $form = $(this);
    console.log($form);
    console.log($(this).serialize());
    $.ajax({
        type: "POST",
        url: 'create_product/',
        data: new FormData(this),
        dataType: "JSON",
        processData: false,
        contentType: false,
        success: function() {
            alert("vgsf")

        }
    });
    return false;
});
