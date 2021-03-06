from django.shortcuts import render
from django.http import Http404
from drugcombinator.models import Interaction
from drugportals.models import Portal


def portal(request, drug):

    try:
        portal = Portal.objects.get(drug__slug=drug)
    except Portal.DoesNotExist:
        raise Http404("Ce portail n'existe pas.")

    interactions = (
        portal.drug.interactions
        .filter(is_draft=False)
        .prefetch_related('from_drug', 'to_drug')
        .order_by_name()
    )
    for inter in interactions:
        inter.drug = inter.other_interactant(portal.drug)
    
    dummy_risks = Interaction.get_dummy_risks()
    
    return render(request, 'drugportals/portal.html', locals())
