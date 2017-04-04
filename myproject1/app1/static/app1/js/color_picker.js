 $(function() {
     $('#color1').colorPicker({
         onColorChange: function(id, newValue) { console.log("ID: " + id + " has been changed to " + newValue); }
     });
     $('#color2').colorPicker({ transparency: true });
 });
