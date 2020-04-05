from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from django.db import NotSupportedError
from drugcombinator.exceptions import Http400
from drugcombinator.models import Drug, Category, Interaction
from drugcombinator.forms import CombinatorForm


def main(request):

    drugs = Drug.objects.all()
    common_drugs = drugs.filter(common=True)
    uncategorized_drugs = drugs.filter(category=None)
    categories = Category.objects.all()

    if request.method == 'POST':
        combinator_form = CombinatorForm(request.POST)
        
        if combinator_form.is_valid():
            drugs = combinator_form.cleaned_data['drugs_field']
            slugs = [drug.slug for drug in drugs]
            
            return redirect('combine', slugs=slugs, permanent=True)

    else:
        combinator_form = CombinatorForm()
    
    return render(request, 'drugcombinator/main.html', locals())


def combine(request, slugs):

    if len(slugs) < 2:
        raise Http400(
                "Au moins deux substances sont nécéssaires."
        )

    drugs = Drug.objects.filter(slug__in=slugs)
    interactions = (
            Interaction.objects
            .filter(from_drug__in=drugs, to_drug__in=drugs)
            .order_by('sym_id')
    )
    
    try:
        # Trigger DB query using list()
        interactions = list(interactions.distinct('sym_id').order_by('-risk'))
    
    except NotSupportedError:
        # Fallback if distinct() is not supported by current DB engine
        interactions = interactions.order_by('-risk')[::2]
    
    combination_name = ' + '.join([str(d) for d in drugs])

    expected_interactions = len(drugs) * (len(drugs)-1) // 2
    unknown_interactions = expected_interactions - len(interactions)

    return render(request, 'drugcombinator/combine.html', locals())


def drug(request, name):

    name = name.strip().lower()

    try:
        drug = Drug.objects.get(slug=name)
    
    except Drug.DoesNotExist:
        drugs = Drug.objects.filter(_aliases__contains=name)
        
        try:
            return redirect(drugs[0], permanent=True)
        
        except IndexError:
            raise Http404(
                    f"La substance {name} n'est pas dans la base de données."
            )
    
    interactions = (Interaction.objects
            .filter(from_drug=drug)
            .order_by('-risk')
    )
    
    return render(request, 'drugcombinator/drug.html', locals())