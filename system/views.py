from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from system.models import Visit, Patient

# Create your views here.
class UserViewAllPatients(TemplateView):
    template_name = 'patients.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient_list'] = Patient.objects.all()
        return context

class UserViewOnePatient(TemplateView):
    template_name = 'view.html'

    def get_context_data(self, **kwargs):
        caseID = self.kwargs['caseID']

        context = super().get_context_data(**kwargs)
        patient = Patient.objects.get(id = caseID)
        context['patient'] = patient
        context['visit_list'] = patient.visit_set.all()
        return context