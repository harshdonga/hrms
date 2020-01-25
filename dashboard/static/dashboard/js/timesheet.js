$(document).ready(function () {
    $('#ajax_time_in').click(function() {
        console.log('time_in clicked');

        $.ajax({
            type: 'POST',
            url: '/res',
            data: { 
                csrfmiddlewaretoken: window.CSRF_TOKEN
            },
            success: function (data) {
                console.log(data.result);
            }
        })
    });


    $('#ajax_time_out').click(function () {
        console.log('time_out clicked');

        $.ajax({
            type: 'POST',
            url: '/res2',
            data: {
                csrfmiddlewaretoken: window.CSRF_TOKEN
            },
            success: function (data) {
                console.log(data.result);
            }
        })
    });    


});