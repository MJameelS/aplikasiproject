from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.
class CustomersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'contact_name', 'address', 'city', 'postal_code', 'country', 'image_tag')
    list_filter = ('customer_name','contact_name', 'address', 'city', 'postal_code', 'country')
    search_fields = ('customer_name','contact_name', 'address', 'city', 'postal_code', 'country')

admin.site.register(Customers, CustomersAdmin)

class CategoriesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'category_name', 'description')
    list_filter = ('category_name', 'description')

admin.site.register(Categories, CategoriesAdmin)

class EmployeesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date', 'photo', 'notes')
    list_filter = ('first_name', 'last_name', 'birth_date', 'photo', 'notes')

admin.site.register(Employees, EmployeesAdmin)

class OrderDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'order_id', 'product_id', 'quantity')
    list_filter = ('order_id', 'product_id', 'quantity')

admin.site.register(OrderDetails, OrderDetailsAdmin)

class OrdersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'order_id', 'customer_id', 'employee_id', 'order_date', 'shipper_id')
    list_filter = ('order_id', 'customer_id', 'employee_id', 'order_date', 'shipper_id')

admin.site.register(Orders, OrdersAdmin)

class ProductsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'product_name', 'supplier_id', 'category_id', 'unit', 'price', 'image_tag', 'description')

admin.site.register(Products, ProductsAdmin)

class ShippersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'shipper_name', 'phone')
    list_filter = ('shipper_name', 'phone')

admin.site.register(Shippers, ShippersAdmin)

class SuppliersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'supplier_name', 'contact_name', 'address', 'city', 'postal_code', 'country', 'phone')
    list_filter = ('supplier_name', 'contact_name', 'address', 'city', 'postal_code', 'country', 'phone')

admin.site.register(Suppliers, SuppliersAdmin)

class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id_buku', 'kategori', 'nama_buku', 'harga', 'stok', 'penerbit')

admin.site.register(Book, BookAdmin)

class PenerbitAdmin(admin.ModelAdmin):
    list_display = ('id_penerbit', 'nama', 'alamat', 'kota', 'telepon')

admin.site.register(Penerbit, PenerbitAdmin)

class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nama', 'email', 'pesan')

admin.site.register(Contact, ContactAdmin)

class CustomersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('product_id', 'customer_name', 'customer_email', 'customer_review', 'rate', 'date')
    search_fields = ('curstomer_email_startswith')
    list_filter = ('customer_email')


# class CarouselAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ('image_tag')

# admin.site.register(Carousel, CarouselAdmin)
