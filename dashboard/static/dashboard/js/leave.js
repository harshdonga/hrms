$(document).ready(function () {

    $('#ajax_leave_query').click(function () {
        console.log('Leave queried');

        $.ajax({
            type: 'POST',
            url: '/leave_query',
            data: {
                csrfmiddlewaretoken: window.CSRF_TOKEN
            },
            success: function (data) {
                console.log("POST REQ MADE");
            }
        })
    });
});