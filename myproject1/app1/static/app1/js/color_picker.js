 $(function() {  
   $('#color1').colorPicker( { onColorChange : function(id, newValue) 
   	{ console.log("ID: " + id + " has been changed to " + newValue); } } );
   $('#color2').colorPicker({transparency: true});   
  });

 $(function(){
    $("#color1").click(colorpicker);
})
 function colorpicker(){
 	$("#color1").each(function() {
        var $input = $(this);
        var inputFiles = this.files;
        if(inputFiles == undefined || inputFiles.length == 0) return;
        var inputFile = inputFiles[0];

        var reader = new FileReader();
        reader.readAsDataURL(inputFile);
        reader.onload= function(e){
        myarray.push(e.target.result);
        var template='<form action="/upload">'+
        '<img  src="'+e.target.result+'">'+ 
       '</form>';
         $('#display_color').append(template);
           };
        reader.onerror = function(event) {
            alert("I AM ERROR: " + event.target.error.code);
        };
        
    });

 }

