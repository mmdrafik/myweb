from django.shortcuts import render
from django.http import HttpResponse
from .forms import GroupForm
from .forms_member import MemberForm
from django.shortcuts import redirect
from .models import Group, Member

def index(request):
    return render(request, 'group/index.html')

def group_new(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            return redirect('group_detail', group_id=group.pk)
    else:
        form = GroupForm()
        return render(request, 'group/group_edit.html', {'form': form})

def group_detail(request, group_id):
    group = Group.objects.get(pk=group_id)
    return render(request, 'group/group_detail.html',{'group': group})

def group_edit(request, group_id):
    if request.method == "POST":
        group = Group.objects.get(pk=group_id)
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save()
            return redirect('group_detail', group_id=group.pk)
    else:
        group = Group.objects.get(pk=group_id)
        form = GroupForm(instance=group)
        return render(request, 'group/group_edit.html',{'form':form})

def member_new(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.group_id=1
            member = form.save()
            return redirect("member_detail", member_id=member.pk)
    else:
        form = MemberForm()
        return render(request, 'group/member_edit.html',{'form':form})

def member_detail(request, member_id):
    member = Member.objects.get(pk=member_id)
    return render(request, 'group/member_detail.html',{'member':member})

def member_edit(request, member_id):
    if request.method == "POST":
        member = Member.objects.get(pk=member_id)
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            member = form.save()
            return redirect('member_detail', member_id=member.pk)
    else:
        member = Member.objects.get(pk=member_id)
        form = MemberForm(instance=member)
        return render(request, 'group/member_edit.html',{'form':form})
