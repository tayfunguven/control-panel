django.jQuery(document).ready(function(){
    if (django.jQuery('#id_has_serial').is(':checked')) {
            hide_field=true;
    } else {
        var element_product_id = document.getElementsByClassName("form-row field-product_id");
        var element_product_id_inv = document.getElementsByClassName("form-row field-product_id_inv");
        var i;
        for (i = 0; i < element_product_id.length; i++) {
            element_product_id[i].style ="display: none!important";
            element_product_id_inv[i].style ="display: block!important";
        }
        hide_field=false;
    }
    django.jQuery("#id_has_serial").click(function(){
        hide_field=!hide_field;
        if (hide_field) {
            var element_product_id = document.getElementsByClassName("form-row field-product_id");
            var element_product_id_inv = document.getElementsByClassName("form-row field-product_id_inv");
            var i;
            for (i = 0; i < element_product_id.length; i++) {
                element_product_id[i].style ="display: block!important";
                element_product_id_inv[i].style ="display: none!important";
            }
        } else {
            
            var element_product_id = document.getElementsByClassName("form-row field-product_id");
            var element_product_id_inv = document.getElementsByClassName("form-row field-product_id_inv");
            var i;
            for (i = 0; i < element_product_id.length; i++) {
                element_product_id[i].style ="display: none!important";
                element_product_id_inv[i].style ="display: block!important";
            }

        }
    })
})
