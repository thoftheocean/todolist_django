#coding:utf-8
from django.shortcuts import render
from todolist.models import Todolist
from datetime import datetime

def todolist(request):
    from_source = request.session.get('from_source', 'unkown')
    print(from_source)
    if from_source == 'MSIE 6.0':
        return render(request, 'update_ie.html')
    elif from_source == 'MSIE 7.0':
        return render(request, 'update_ie.html')
    elif from_source == 'MSIE 8.0':
        print('hello')
        return render(request, 'update_ie.html')
    else:
        todolists=Todolist.objects.all()
        if request.method == 'POST':
            event = request.POST['event']
            Todolist.objects.create(event=event, status='undo')

        if request.GET.get('operate') == "delete":
            # 删除
            delete_event = Todolist.objects.filter(id=request.GET.get('id'))
            if delete_event != None:
                delete_event.delete()

        if request.GET.get('status'):
            # 保存状态
            Todolist.objects.filter(id=request.GET.get('id')).update(status = request.GET.get('status'))

    return render(request, 'todolist1.html', locals())


def edit(request, todolist_id):

    todolists = Todolist.objects.all()
    todolist = Todolist.objects.get(id=todolist_id)

    if request.method == 'POST':
        now=datetime.now()
        print('now；',now)

        Todolist.objects.filter(id=todolist_id).update(event=request.POST.get('event'), datetime_now=datetime.now())
        return render(request, 'todolist1.html', locals())

    return render(request, 'edit.html', locals())


