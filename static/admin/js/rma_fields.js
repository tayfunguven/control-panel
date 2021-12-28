django.jQuery(document).ready(function(){
    if (django.jQuery('#product_category').is(':Computer')) {
            hide_field=true;
    } else {
        var category = document.getElementsByClassName("form-row field-computer_components");
        var i;
        for (i = 0; i < category.length; i++) {
            category[i].style ="display: none!important";
        }
        hide_field=false;
    }
    django.jQuery("#product_category").click(function(){
        hide_field=!hide_field;
        if (hide_field) {
            var category = document.getElementsByClassName("form-row computer_components");
            var i;
            for (i = 0; i < category.length; i++) {
                category[i].style ="display: block!important";
            }
        } else {
            
            var category = document.getElementsByClassName("form-row computer_components");
            var i;
            for (i = 0; i < category.length; i++) {
                category[i].style ="display: none!important";
            }

        }
    })
})
