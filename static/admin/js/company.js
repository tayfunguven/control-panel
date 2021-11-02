django.jQuery(document).ready(function(){
    if (django.jQuery('#id_has_invoice').is(':checked')) {
            hide_field=true;
    } else {
        var element_tax_administration = document.getElementsByClassName("form-row field-tax_administration");
        var element_tax_number = document.getElementsByClassName("form-row field-tax_number");
        var element_company_title = document.getElementsByClassName("form-row field-company_title");
        var element_official_address = document.getElementsByClassName("form-row field-official_address");
        var i;
        for (i = 0; i < element_tax_administration.length; i++) {
            element_tax_administration[i].style ="display: none!important";
            element_tax_number[i].style ="display: none!important";
            element_company_title[i].style ="display: none!important";
            element_official_address[i].style ="display: none!important";
        }
        hide_field=false;
    }
    django.jQuery("#id_has_invoice").click(function(){
        hide_field=!hide_field;
        if (hide_field) {
            var element_tax_administration = document.getElementsByClassName("form-row field-tax_administration");
            var element_tax_number = document.getElementsByClassName("form-row field-tax_number");
            var element_company_title = document.getElementsByClassName("form-row field-company_title");
            var element_official_address = document.getElementsByClassName("form-row field-official_address");
            var i;
            for (i = 0; i < element_tax_administration.length; i++) {
                element_tax_administration[i].style ="display: block!important";
                element_tax_number[i].style ="display: block!important";
                element_company_title[i].style ="display: block!important";
                element_official_address[i].style ="display: block!important";
            }
        } else {
            
            var element_tax_administration = document.getElementsByClassName("form-row field-tax_administration");
            var element_tax_number = document.getElementsByClassName("form-row field-tax_number");
            var element_company_title = document.getElementsByClassName("form-row field-company_title");
            var element_official_address = document.getElementsByClassName("form-row field-official_address");
            var i;
            for (i = 0; i < element_tax_administration.length; i++) {
                element_tax_administration[i].style ="display: none!important";
                element_tax_number[i].style ="display: none!important";
                element_company_title[i].style ="display: none!important";
                element_official_address[i].style ="display: none!important";
        }

        }
    })
})