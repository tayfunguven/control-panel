if (!$) {
    $ = django.jQuery;
}
$(document).ready(function(){
    // Add event listener to input
    $("#id_amount").change(function(e){
        // Get entered value
        let amount = parseFloat($(this).val());
        // Get value from another field 
        let subtotal = parseFloat($("#id_subtotal").val());
        // Compute value in whatever way you want
        let grand_total = amount + subtotal;
        // Set value in read-only field.
        $("div.field-grand_total").find("div.readonly").text(grand_total);
    });

    $("#id_subtotal").change(function(e){
        // Get entered value
        let subtotal = parseFloat($(this).val());
        // Get value from another field 
        let amount = parseFloat($("#id_amount").val())
        // Compute value in whatever way you want
        let grand_total = amount + subtotal;
        // Set value in read-only field.
        $("div.field-grand_total").find("div.readonly").text(grand_total);
    });
})