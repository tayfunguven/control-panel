from import_export import resources
from Finance.models import *

class PersonalIncomeResource(resources.ModelResource):
    class Meta:
        model = PersonalIncome
        fields = ('income_code', 'income_name', 'amount', 'unit_id', 'currency_price',
            'currency_type', 'price', 'subtotal', 'vat_rate', 'vat_amount','grand_total', 'log_date', 'user')

class PersonalExpenseResource(resources.ModelResource):
    class Meta:
        model = PersonalExpense
        fields = ('expense_code', 'expense_name', 'amount', 'unit_id', 'currency_price',
            'currency_type', 'price', 'subtotal', 'vat_rate', 'vat_amount','grand_total', 'log_date', 'user')

class CompanyIncomeResource(resources.ModelResource):
    class Meta:
        model = CompanyIncome
        fields = ('income_code', 'income_name', 'amount', 'unit_id', 'currency_price',
            'currency_type', 'price', 'subtotal', 'vat_rate', 'vat_amount','grand_total', 'payment_type', 'log_date', 'income_to')

class CompanyExpenseResource(resources.ModelResource):
    class Meta:
        model = CompanyExpense
        fields = ('expense_code', 'expense_name', 'amount', 'unit_id', 'currency_price',
            'currency_type', 'price', 'subtotal', 'vat_rate', 'vat_amount','grand_total', 'payment_type', 'log_date', 'expense_to')