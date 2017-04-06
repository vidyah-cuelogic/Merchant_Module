
$(document).ready(function() {
	$('#show-me').hide(); 
   $('input[type="radio"]').click(function() {
       if($(this).attr('id') == 'watch-me') {
       	$('#show-me').show();                      
       }
       else {
            $('#show-me').hide();   
       }
   });

   $('#close_btn').click(function(){
   		
   		$('this').parent.remove();

   	});

});




