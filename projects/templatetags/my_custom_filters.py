from django import template
from users.models import Category, Project, Donation, Project_pictures
from django.db.models import Sum, Avg


register = template.Library()

@register.filter(name='quarter')
def quarter(value):
    return (0.25 * value)


@register.filter(name='get_donations')
def get_donations(id):
    p = Project.objects.get(id=id)
    # print(p)
    donations = p.donation_set.values('project_id').aggregate(total_donations = Sum('amount'))
    return donations['total_donations']

@register.filter(name='get_url')
def get_url(id):
    p = Project.objects.get(id=id)
    picture_url = p.project_pictures_set.first().picture.url
    # print(project_pic)
    return picture_url

