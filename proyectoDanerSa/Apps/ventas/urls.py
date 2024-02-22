from django.urls import path

from . import views

app_name = "Apps.ventas"
urlpatterns = [
    path('', views.ListaVentasView, name='lista_ventas'),
    path('agregar', views.VistaAgregarVentas, name='agregar_ventas'),
    path('Abonar/<str:id_venta>/', views.abonar_transaccion, name='agregar_abono'),

    #-----reportes---    
    path('report', views.VentasView, name='report'),
    path('reportC', views.ClientesView, name='reportC'),
    path('reportCT', views.ClientesCTView, name='reportCT'),
    
    path('generar_reporte_excel/<str:start_date>/<str:end_date>/', views.generar_reporte_excel, name='generar_reporte_excel'),
    path('generar_reporte_cliente_excel/<int:id_cliente>/', views.generar_reporte_cliente_excel, name='generar_reporte_cliente_excel'),
   
    path('generar_reporte_abonos_cliente/<str:start_date>/<str:end_date>/', views.generar_reporte_abonos_clientes_excel, name='generar_reporte_abonos_cliente'),

    # Nueva ruta para generar reporte en formato PDF y mostrar datos preliminares
    path('generar_reporte_pdf/<str:start_date>/<str:end_date>/', views.generar_reporte_pdf, name='generar_reporte_pdf'),
    path('generar_reporte_cliente_pdf/<int:id_cliente>/', views.generar_reporte_cliente_pdf, name='generar_reporte_cliente_pdf'),
    path('generar_reporte_abonos_cliente_pdf/<str:start_date>/<str:end_date>/', views.generar_reporte_abonos_clientes_pdf, name='generar_reporte_abonos_cliente_pdf'),
    path('obtener_datos_filtrados/<str:start_date>/<str:end_date>/', views.obtener_datos_filtrados, name='obtener_datos_filtrados'),


    path('obtener_datos_abonos_filtrados/<str:start_date>/<str:end_date>/', views.obtener_datos_abonos_filtrados, name='obtener_datos_abonos_filtrados'),
    path('obtener_datos_abonos_filtrados_id/<int:id_cliente>/', views.obtener_datos_abonos_filtrados_id, name='obtener_datos_abonos_filtrados_id'),
]
