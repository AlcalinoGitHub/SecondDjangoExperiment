from django.shortcuts import render, redirect
from Tasks.models import Task
from django.contrib import messages

# Create your views here.

def main(request):
    if request.method == 'POST':
        Title = request.POST['Title']
        Description = request.POST['Description']
        Date = request.POST['DueDate']
        try:
            NewTask = Task.objects.create(Title = Title, Description = Description, DueDate = Date, Owner = request.user)
            NewTask.save()
            messages.info(request, f'Task {Title} has been created')
            return redirect('/tasks/')
        except:
            messages.info(request, 'Fields cant be empty')
            return redirect('/tasks/')
    else:
        Data = Task.objects.filter(Owner = request.user)
        context = {'tareas': Data}
        return render(request, 'Main.html', context)
    
def delete(request):
    if request.method == 'POST':
        taskID = request.POST.get('task_id')
        task = Task.objects.get(id = taskID)
        task.delete()
        print(taskID)
        return redirect('/tasks/')