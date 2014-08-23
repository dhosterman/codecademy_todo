$(document).ready(function () {

    // handle csrf
    var csrftoken = $.cookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    
    // add task button handler
    var addTaskButton = $('button[name="Add Task"]');
    addTaskButton.click(function () {
        $.post(
            '/todo/add_task', 
            {
                description: $('#id_description').val()
            }, 
            function (data, textStatus, jqXHR) {
                console.log(data[0].pk);
            },
            'json'
        );
    })

});