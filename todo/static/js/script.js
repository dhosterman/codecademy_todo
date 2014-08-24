// add checkbox handler to todo item
function addToggleCompletedHandler (element) {
    element.change(function () {
        var taskId = element.parent().data('task-id');
        var task = element.parent();
        if (this.checked) {
            $.post(
                '/todo/complete_task',
                {
                    task_id: taskId
                },
                function (data, textStatus, jqXHR) {
                    var doneHeader = $('.done h2');
                    doneHeader.after(task.detach());
                    task.removeClass('todo-item');
                    task.addClass('done-item');
                }
            );
        } else {
            var taskId = element.parent().data('task-id');
            $.post(
                '/todo/uncomplete_task',
                {
                    task_id: taskId
                },
                function (data, textStatus, jqXHR) {
                    var todoHeader = $('.to-do h2');
                    todoHeader.after(task.detach());
                    task.removeClass('done-item');
                    task.addClass('todo-item');
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
                var todoHeader = $('.to-do h2');
                todoHeader.after('<article class="todo-item" data-task-id="' + data[0].pk + '"><input type="checkbox">' + data[0].fields.description + '</article>');
                addToggleCompletedHandler($('.todo-item input').first());
            },
            'json'
        );
    });

    // apply checkbox handler to all existing todo items
    $('input[type="checkbox"]').each(function () {
        addToggleCompletedHandler($(this));
    });

});