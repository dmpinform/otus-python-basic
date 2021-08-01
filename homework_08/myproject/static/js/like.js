$(document).ready(function(){
    $(".like").click(function(){
        const attr_id = $(this).attr('attr_id');
        const action_url = $(this).attr('action_url')
        const that = $(this)

        $.ajax({
            url: action_url,
            type: "POST",
            data: {'attr_id': attr_id },
            headers: { "X-CSRFToken": $.cookie("csrftoken") },
            success: function (result) {
                console.log("Success")
                that.toggleClass("heart");
            },
            error: function () {
                alert("Please login");
            }

        });
    });
});