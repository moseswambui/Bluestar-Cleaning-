$("#category").change(function(){
    const url_category = $("#category").attr("category-queries-url");
    const typeId = $(this).val();

    $.ajax({
        url : url_category,
        data :{'type_id': typeId},
        success: function(data){
            $("#category".html(data))
        }


    });
});