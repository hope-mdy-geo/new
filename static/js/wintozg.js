$(document).ready(function(){
  $("#myinput").css("font-family", "win_innwaregular");
  $('form').on('submit', function (event){
	$.ajax({
  		type: "POST",
		url: "/convert4",
		data: {
			myinput: $('#myinput').val()
		}
	})
  .done(function(data){
    if(data.error){
      //Do something
    }
    else{
      $("#output").css("font-family", "Zawgyi-One");
      $("#output").val(data.output).show();
    }
  });

  event.preventDefault();
});
});
