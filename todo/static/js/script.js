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

// add delete handler to todo item
function addDeleteHandler (element) {
    element.click(function () {
        var taskId = element.parent().data('task-id');
        var task = element.parent();
        $.post(
            '/todo/delete_task',
            {
                task_id: taskId
            },
            function (data, textStatus, jqXHR) {
                task.remove();
            }
        )
    })
}

// add edit handler to todo item
function addEditHandler (element) {
    element.click(function () {
        var taskId = element.parent().data('task-id');
        var task = element.parent();
        var taskInput = task.children('input[type="text"]')
        var taskDescription = task.children('.description')
        if (taskDescription.is(':visible')) {
            taskDescription.hide();
            taskInput.show().focus()
            var strLength= taskInput.val().length;
            taskInput[0].setSelectionRange(strLength, strLength);
            taskInput.blur(function () {
                $.post(
                    '/todo/edit_task',
                    {
                        task_id: taskId,
                        description: taskInput.val()
                    },
                    function (data, textStatus, jqXHR) {
                        taskInput.hide();
                        taskInput.val(data[0].fields.description);
                        taskDescription.text(data[0].fields.description);
                        taskDescription.show();
                    },
                    'json'
                )
                
            });
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
                todoHeader.after('<article class="todo-item" data-task-id="' + data[0].pk + '"><input type="checkbox">' + data[0].fields.description + '<button name="Delete Task"></button></article>');
                addToggleCompletedHandler($('.todo-item input').first());
                addDeleteHandler($('.todo-item button').first());
            },
            'json'
        );
    });

    // apply checkbox handler to all existing todo items
    $('input[type="checkbox"]').each(function () {
        addToggleCompletedHandler($(this));
    });

    // apply delete handler to all existing todo items
    $('article button[name="Delete Task"]').each(function () {
        addDeleteHandler($(this));
    })

    // apply edit handler to all existing todo items
    $('article button[name="Edit Task"]').each(function () {
        addEditHandler($(this));
    })

});