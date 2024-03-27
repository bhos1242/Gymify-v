from django.urls import path
from Members.views import *

urlpatterns = [
    path('enquiries', Enquiries.as_view(), name='enquiries'),
    path('addenquiry', AddEnquiry.as_view(), name='addenquiry'),
    path('members', AllMembers.as_view(), name='members'),
    path('addmember', AddMember.as_view(), name='addmember'),
    path('addmemberfromenq', AddMemberfromEnquiry.as_view(), name='addmemberfromenq'),
    path('member/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
    path('plan/create/', PlanCreateView.as_view(), name='memberplancreate'),
    path('member/<int:member_id>/deactivate/', DeactivateMemberView.as_view(), name='deactivate-member'),
]

app_name = 'Members'
