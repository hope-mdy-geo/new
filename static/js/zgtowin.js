$(document).ready(function(){
  $("#myinput").css("font-family", "Zawgyi-One");
  $('form').on('submit', function (event){
	$.ajax({
  		type: "POST",
		url: "/convert5",
		data: {
			myinput: $('#myinput').val()
		}
	})
  .done(function(data){
    if(data.error){
      //Do something
    }
    else{
      $("#output").css("font-family", "win_innwaregular");
      $("#output").val(data.output).show();
    }
  });

  event.preventDefault();
});
});
