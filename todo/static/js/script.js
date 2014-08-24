// add checkbox handler to todo item
    function addCheckHandlerUnfinished (element) {
        element.change(function () {
            if (this.checked) {
                var taskId = element.parent().data('task-id');
                $.post(
                    '/todo/complete_task',
                    {
                        task_id: taskId
                    },
                    function (data, textStatus, jqXHR) {
                        var doneGroup = $('.done-item');
                        var doneItem = element.parent().clone();
                        element.parent().remove();
                        doneItem.removeClass('todo-item');
                        doneItem.addClass('done-item');
                        doneItem.off('click');
                        doneGroup.first().before(doneItem);
                    }
                );
            }
        })
    }

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

    // dom elements
    var addTaskButton = $('button[name="Add Task"]');
    var addTaskInput = $('#id_description');
    
    // add task button handler
    addTaskButton.click(function () {
        $.post(
            '/todo/add_task', 
            {
                description: addTaskInput.val()
            }, 
            function (data, textStatus, jqXHR) {
                addTaskInput.val('');
                var todoGroup = $('.todo-item');
                todoGroup.first().before('<article class="todo-item"><input type="checkbox">' + data[0].fields.description + '</article>');
            },
            'json'
        );
    });

    // apply checkbox handler to all existing todo items
    $('.to-do input[type="checkbox"]').each(function () {
        addCheckHandlerUnfinished($(this));
    });

});