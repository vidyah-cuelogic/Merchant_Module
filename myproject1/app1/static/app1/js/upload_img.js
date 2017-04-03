var myarray = []; 

$(function(){
    $("#images").change(loadPreviews_click);
})
function loadPreviews_click(e) {
    $("#images").each(function() {
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
         $('#image_to_upload').append(template);
           };
        reader.onerror = function(event) {
            alert("I AM ERROR: " + event.target.error.code);
        };
        
    });
} 

$(function(){
    $(".btnLoadPreviews").click(loadPreviews);
})
function loadPreviews(){
    for (i = 0; i < myarray.length; i++) { 
        var template1='<form action="/upload">'+
        '<img  src="'+myarray[i]+'">'+ 
       '</form>'; 
       $('#image_upload').append(template1);  
    }
}
    
$(function(){
    $("#demo").click(msg);
})
function msg(){

message: 'Please provide a valid email address'
alert( "Handler for .click() called." );
}