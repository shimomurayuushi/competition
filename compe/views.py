from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from compe.models import Category, Problem, Choice, Choice
from compe.forms import ChoiceForm


class CategoryListView(ListView):
    model = Category
    template_name = 'compe/category_list.html'
    context_object_name = 'categories'


class ProblemListView(ListView):
    model = Problem
    template_name = 'compe/problem_list.html'
    context_object_name = 'problems'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['pk']
        category = get_object_or_404(Category, id=category_id)
        problems = category.Categorys.all()
        context['category'] = category
        context['problems'] = problems
        return context


class ChoiceDetailView(DetailView):
    model = Choice
    template_name = 'compe/choice_detail.html'
    context_object_name = 'choice'
    form_class = ChoiceForm

    def get_queryset(self):
        query = super().get_queryset()
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        problem_id = self.kwargs['pk']
        problem = get_object_or_404(Problem, id=problem_id)
        choices = problem.Problems.all()
        context['problem'] = problem
        context['choices'] = choices
        return context


@login_required
def choice(request, problem_id):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            selected = form.cleaned_data['selected']
            choice = Choice.objects.first()
            if selected == 'completed':
                choice.completed += 1
            elif selected == 'unfinished':
                choice.unfinished += 1
            elif selected == 'zone':
                choice.zone += 1
            choice.total = choice.completed + choice.unfinished + choice.zone
            choice.save()
            print(form.cleaned_data)
            return redirect('results')
    else:
        form = ChoiceForm()
    return render(request, 'choice.html', {'form': form})

@login_required
def results_view(request):
    choice = Choice.objects.first()
    return render(request, 'results.html', {'choice': choice})