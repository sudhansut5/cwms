from django.urls import path
from .views import home,production_tracker, reports, data_utilities,query_tracker,display_data,display_production_data,randomizer,display_quality_tracker,quality_tracker,data_extraction,get_sub_process,get_analyst_name,dashboard,tests

urlpatterns = [
    path('home/', home, name='home'),
    path('production_tracker/', production_tracker, name='production_tracker'),
    path('reports/', reports, name='reports'),
    path('data_utilities/', data_utilities, name='data_utilities'),
    path('quality_tracker/',quality_tracker,name='quality_tracker'),
    path('quality_tracker/<int:id>/', quality_tracker, name='quality_tracker'),
    path('display_quality_tracker/', display_quality_tracker, name='display_quality_tracker'),
    path('display_production_data/<str:id>/',display_production_data, name='display_production_data'), 
    path('query_tracker/',query_tracker,name='query_tracker'),
    path('display_data/<str:analyst_name>/', display_data, name='display_data'),
    path('randomizer/', randomizer, name='randomizer'),
    path('data_extraction/', data_extraction, name='data_extraction'),
    path('get_analyst_name/', get_analyst_name, name='get_analyst_name'),
    path('get_sub_process/', get_sub_process, name='get_sub_process'),
    path('dashboard/',dashboard,name='dashboard'),
    path('tests/', tests, name= 'tests'),
]

     
