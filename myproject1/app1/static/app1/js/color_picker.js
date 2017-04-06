 var colors = [];
 $(function() {
     $('#color1').colorPicker({
         onColorChange: function(id, newValue) {
             var template1 = newValue;
             colors.push(template1);
             $('#colors').append('<div class="color-tab">' + template1 + '<button class="close" aria-label="Close">'+
             	 '<span class="close-btn" >&times;</span>' +
                 '</button></div>');
             
             console.log("ID: " + id + " has been changed to " + newValue);
             $('.close').on('click', function() {
                $(this).parent().remove(); 
                              
                
             });

             $('#selected_colors').append('<option>' + template1 + '</option>');
         }
     });

 });
