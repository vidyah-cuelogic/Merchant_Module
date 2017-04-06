
$("#myform").submit(function(e) {
    console.log()
    e.preventDefault();
    formdata = new FormData(this)
    formdata.append('color_list', JSON.stringify(colors));
    $.ajax({
        type: "POST",
        url: '/app1/dashboard/products/create_product/',
        data: formdata,
        dataType: "JSON",
        processData: false,
        contentType: false,
        success: function(response) {
        if(response.success== true)
        {   console.log(response['message'])
            $.notify("success true");
        }
        else
        { 
            $.notify("success false");        
            console.log(response['message'])
        }
    }
    });
  
});

