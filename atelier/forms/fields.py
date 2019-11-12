# to change allowance_discount field and complication element field in order form 
# doesn't work yet !!!

from crispy_forms.layout import Field


class CustomCheckbox(Field):
    template = 'custom_checkbox.html'
