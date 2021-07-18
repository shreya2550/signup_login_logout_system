from django.urls import path
from . import views
urlpatterns=[
   path('',views.home,name='home'),
   path('add-beneficiary',views.addBeneficiary,name='add-beneficiary'),
   path('update-beneficiary/<int:id>',views.updateBeneficiary,name='update-beneficiary'),
   path('delete-beneficiary/<int:id>',views.deleteBeneficiary,name='delete-beneficiary'),
   path('send-email/<int:id>',views.sendEmail,name='send-email'),
]