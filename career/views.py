from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)

from career.forms import Candidateform
from career.models import *

# Create your views here.

class CareerPage(ListView):
    model = Career
    template_name = "career-template/list.html"
    context_object_name = "careers"
    paginate_by = 3

class CareerDetail(DetailView):
    model = Career
    context_object_name = "careerd"
    template_name = "career-template/career-detail.html"

class CandidateFormView(LoginRequiredMixin, TemplateView):
    template_name = "career-template/candidate-form-info.html"

    def get(self, request, *args, **kwargs):
        form = Candidateform()


        context = {"form": form}

        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        form = Candidateform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Request has been sent to Soft Skill Space, "
            )

            return redirect("career:career-page")
        context = {"form": form}
        return render(request, self.template_name, context)
