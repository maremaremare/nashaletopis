from django.shortcuts import render

# Create your views here.


def relatedCount(model, related_model, field, counter):
    return model.objects.add_related_count(
        model.objects.all(),
        related_model,
        field,
        counter,
        True
    )

