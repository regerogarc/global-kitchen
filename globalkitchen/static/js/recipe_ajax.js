
$(document).ready(function(){

    $("#favourite").click(function(){
        alert($(this).attr("data-token"))

        $.ajax({
            type: "POST",
            url: $(this).attr("data-url"),
            dataType:"json",
            headers: {
                "X-CSRFToken": $(this).attr("data-token")
              },
            data: {recipe: $(this).attr("data"),},
            success: function(data){
                alert($(this).attr("data-token"))
            }
        })
    })
})