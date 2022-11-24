$(document).ready(function(){
    var type = $("#category");
    var category = $("#service");
    var $options = category.find('option')
    type.on('change', function(){
        category.html($options.filter('[value="'+ this.value + '"]'))
    }).trigger('change');
});