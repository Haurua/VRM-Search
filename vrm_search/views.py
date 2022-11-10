from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from .functions.dvla_api_request import dvla_api_request


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vrm_search/index.html')

    def post(self, request, *args, **kwargs):
        vrm = request.POST["vrm"]
        response = dvla_api_request(vrm)
        if response.status_code == 200:
            context = {
                "results": response.json()
            }
            return render(request, 'vrm_search/search_results.html', context)
        else:
            messages.error(request, "Invalid registration number, please try again.")
            return redirect('vrm-search')
