$(document).ready(function () {

    $('#ajax_leave_query').click(function () {
        console.log('Leave queried');
        // start_date = $('#start_date').val()
        // end_date = $('#end_date').val()

        $.ajax({
            type: 'POST',
            url: '/leave_query',
            data: {
                csrfmiddlewaretoken: window.CSRF_TOKEN,
                'start_date' : $('#start_date').val(),
                'end_date' : $('#end_date').val()
            },
            success: function (data) {
                console.log("POST REQ MADE");
            }
        })
    });
});