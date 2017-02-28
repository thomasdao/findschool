$('.country-dd-item').click(function(e) {
    var el = $(this);
    console.log(el.attr("data-name"));
    $("#country_input").attr("value", el.attr("data-name"));
});
