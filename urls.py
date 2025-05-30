"""epharmanew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('login/',views.login),
    path('login_post/',views.login_post),
    path('admin_home/',views.admin_home),
    path('admin_view_pharma_accept/',views.admin_view_pharma_accept),
    path('acceptpharma_post/<id>',views.acceptpharma_post),
    path('rejectpharma_post/<id>',views.rejectpharma_post),
    path('admin_view_pharma_accept_post/',views.admin_view_pharma_accept_post),
    path('admin_view_registered_pharma/',views.admin_view_registered_pharma),
    path('admin_view_pharma_approved/',views.admin_view_pharma_approved),
    path('admin_view_pharma_approved_post/',views.admin_view_pharma_approved_post),
    path('admin_view_pharma_rejected/',views.admin_view_pharma_rejected),
    path('admin_view_pharma_rejected_post/',views.admin_view_pharma_rejected_post),
    path('admin_view_customer/',views.admin_view_customer),
    path('admin_view_customer_post/',views.admin_view_customer_post),
    path('admin_view_review/',views.admin_view_review),
    path('admin_view_review_post/',views.admin_view_review_post),
    path('admin_change_password/',views.admin_change_password),
    path('admin_change_password_post/',views.admin_change_password_post),
    path('admin_view_complaint/',views.admin_view_complaint),
    path('admin_view_complaint_post/',views.admin_view_complaint_post),
    path('pahrma_send_replay/<id>',views.pahrma_send_replay),
    path('pharma_send_replay_post/',views.pharma_send_replay_post),
    path('pharma_home/',views.pharma_home),
    path('logout/',views.logout),
    path('pharma_signup/',views.pharma_signup),
    path('pharma_signup_post/',views.pharma_signup_post),
    path('pharma_view_order_update_status/',views.pharma_view_order_update_status),
    path('pharma_view_order_update_status_post/',views.pharma_view_order_update_status_post),
    path('pharma_view_prescription/',views.pharma_view_prescription),
    path('pharma_view_prescription_post/',views.pharma_view_prescription_post),
    path('pharma_order_status/<id>',views.pharma_order_status),
    path('pharma_oder_sub/<id>',views.pharma_oder_sub),
    path('pharma_order_status_post/',views.pharma_order_status_post),
    path('pharma_manage_medicine_view/',views.pharma_manage_medicine_view),
    path('pharma_manage_madicine_view_post/',views.pharma_manage_medicine_view_post),
    path('pharma_manage_medicine_edit/<id>',views.pharma_manage_medicine_edit),
    path('pharma_manage_medicine_edit_post/',views.pharma_manage_medicine_edit_post),
    path('pharma_delete_medicine/<id>',views.pharma_delete_medicine),
    # path('pharma_manage_medicine_delete/<id>',views.pharma_manage_medicine_delete),
    path('pharma_manage_stock_delete/<id>',views.pharma_manage_stock_delete),
    path('pharma_manage_stock_view/',views.pharma_manage_stock_view),
    path('pharma_manage_stock_view_post/',views.pharma_manage_stock_view_post),
    path('pharma_view_complaint_replay/',views.pharma_view_complaint_replay),
    path('pharma_view_complaint_replay_post/',views.pharma_view_complaint_replay_post),
    path('pharma_manage_medicine_add/',views.pharma_manage_medicine_add),
    path('pharma_manage_medicine_add_post/',views.pharma_manage_medicine_add_post),
    path('pharma_manage_stock_update/',views.pharma_manage_stock_update),
    path('pharma_manage_stock_update_post/',views.pharma_manage_stock_update_post),
    path('pharma_view_order_payment/',views.pharma_view_order_payment),
    path('pharma_bill_entry/<id>',views.pharma_bill_entry),
    path('pharma_bill_entry_post/',views.pharma_bill_entry_post),
    path('pharma_view_bill_entry/<id>',views.pharma_view_bill_entry),
    path('pharma_view_bill_entry_post/',views.pharma_view_bill_entry_post),
    path('pharma_bill_history/',views.pharma_bill_history),
    path('pharma_bill_history_post/',views.pharma_bill_history_post),
    path('pharma_bill_history2/',views.pharma_bill_history2),
    path('pharma_bill_history2_post/',views.pharma_bill_history2_post),
    path('pharma_view_profile/',views.pharma_view_profile),
    path('pharma_edit_profile/',views.pharma_edit_profile),
    path('pharma_edit_profile_post/',views.pharma_edit_profile_post),
    path('pharma_view_review/',views.pharma_view_review),
    path('pharma_view_review_post/',views.pharma_view_review_post),
    path('pharma_change_password/',views.pharma_change_password),
    path('pharma_change_password_post/',views.pharma_change_password_post),
    path('pharma_notification/',views.pharma_notification),
    path('pharma_notification_post/',views.pharma_notification_post),
    path('customer_home/',views.customer_home),
    path('customer_signup/',views.customer_signup),
    path('customer_signup_post/',views.customer_signup_post),
    path('customer_search_medicine/<id>',views.customer_search_medicine),
    path('customer_search_medicine_post/',views.customer_search_medicine_post),
    path('customer_addtocart/<id>',views.customer_addtocart),
    path('customer_addtocart_post/',views.customer_addtocart_post),
    path('customer_view_cart/',views.customer_view_cart),
    path('customer_remove_cart/<id>',views.customer_remove_cart),
    path('customer_uploads/<id>',views.customer_uploads),
    path('customer_uploads_post/',views.customer_uploads_post),
    path('customer_view_uploads/',views.customer_view_uploads),
    path('customer_view_bill_payment/',views.customer_view_bill_payment),
    path('customer_raz_pay/<amount>',views.customer_raz_pay),
    path('raz_pay2/<amount>/<id>',views.raz_pay2),
    path('customer_view_cart_payment/',views.customer_view_cart_payment),
    path('customer_send_complaint_replay/',views.customer_send_complaint_replay),
    path('customer_send_complaint_replay_post/',views.customer_send_complaint_replay_post),
    path('customer_view_replay/',views.customer_view_replay),
    path('customer_view_replay_post/',views.customer_view_replay_post),
    path('customer_send_review/',views.customer_send_review),
    path('customer_send_review_post/',views.customer_send_review_post),
    path('customer_view_profile/',views.customer_view_profile),
    path('customer_edit_profile/',views.customer_edit_profile),
    path('customer_edit_profile_post/',views.customer_edit_profile_post),
    path('customer_change_password/',views.customer_change_password),
    path('customer_change_password_post/',views.customer_change_password_post),
    path('user_view_pharma_approved/',views.user_view_pharma_approved),
    path('user_view_pharma_approved_post/',views.user_view_pharma_approved_post),
    path('customer_view_notification/',views.customer_view_notification),
    path('customer_view_notification_post/',views.customer_view_notification_post),

]
