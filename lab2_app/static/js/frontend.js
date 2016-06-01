$("#tab-3-load").click(function(){
    $.get('load_crud', function(data){
        $('#tab-3').children().remove();
        $('#tab-3').append(data)
    })
});
$(".save-btn").click(function(){

    var line = $(this).parent().parent();
    line.find(".save-btn").hide();
    console.log("HELLO FROM SAVE");

    var number = line.find(".number");
    var name = line.find(".edit-name");
    var place = line.find(".edit-place", "option:selected");
    var photoalbum = line.find(".edit-photoalbum", "option: selected");
    var author = line.find(".edit-author", "option:selected");
    var format = line.find(".edit-format", "option:selected");



    console.log("PLACE ID = " + place.val());
    console.log(place.text(), photoalbum.text(), author.text(), format.text());

    line.find(".edit-name").hide().siblings(".name").show().val(name.val());
    line.find(".edit-place").hide().siblings(".place").show().val(place.text());
    line.find(".edit-photoalbum").hide().siblings(".photoalbum").show().val(photoalbum.text());
    line.find(".edit-author").hide().siblings(".author").show().val(author.text());
    line.find(".edit-format").hide().siblings(".format").show().val(format.text());

    $.get('update_photo', {
        "number": number.text(),
        "name": name.val(),
        "place": place.val(),
        "photoalbum": photoalbum.val(),
        "author": author.val(),
        "format": format.val()
    }, function(res){
        $.get('load_crud', function(data){
            $('#tab-3').children().remove();
            $('#tab-3').append(data)
        });

    });

});

$(".edit-btn").click(function() {
    console.log("HELLO FROM EDIT!");
    var line = $(this).parent().parent();

    var name = line.find(".name");
    var place = line.find(".place");
    var photoalbum = line.find(".photoalbum");
    var author = line.find(".author");
    var format = line.find(".format");

    $.get('get_places', function(json){
        console.log("GET_PLACES " + json);
        $.each(json, function(i, value) {
            console.log(value);
            line.find('.edit-place')
                  .append($('<option></option>', {text:value[2]}).attr("value", i+1))
        });

        $.get('get_photoalbums', function(json){
            $.each(json, function(i, value) {
                console.log(value);
                line.find('.edit-photoalbum')
                      .append($('<option></option>', {text:value[1]}).attr("value", i+1))
            });

            $.get('get_authors', function(json){
                $.each(json, function(i, value) {
                console.log(value);
                line.find('.edit-author')
                  .append($('<option></option>', {text:value[2]}).attr("value", i+1))
                });
                $.get('get_formats', function(json){
                    $.each(json, function(i, value) {
                    console.log(value);
                    line.find('.edit-format')
                        .append($('<option></option>', {text:value[1]}).attr("value", i+1))
                    });
                });
             });
        });

    });

    line.find(".save-btn").show();
    line.find(".name").hide().siblings(".edit").show().val(name.text());
    line.find(".place").hide().siblings(".edit").show().val(place.val());
    line.find(".photoalbum").hide().siblings(".edit").show().val(photoalbum.val());
    line.find(".author").hide().siblings(".edit").show().val(author.val());
    line.find(".format").hide().siblings(".edit").show().val(format.val());

    return 0;


});

$(".delete-btn").click(function(){
    var line = $(this).parent().parent();

    var number = line.find(".number").text();
    $.get('delete_photo', {"number": number});
});

$("#search-photo").click(function(){
    var from_price = $('#from_price').val();
    var to_price  = $('#to_price').val();

    $.get('search_photo', {"from_price": from_price, "to_price": to_price}, function(data){
        //$('.search-photo-res').children().remove();
        $('.search-author-res').children().remove();
        $('.search-photo-res').children().remove();
        $('.search-photo-res').append(data);
    })

});

$("#search-author").click(function(){
    gender = $('#gender').val();

    console.log("GENDER " + gender);

    $.get('search_author', {"gender": gender}, function(data){
        $('.search-photo-res').children().remove();
        $('.search-author-res').children().remove();
        console.log(data);
        $('.search-author-res').append(data);
    })

});

$("#get-match-photo").click(function(){
    var name = $('#match-photo').val();
    console.log(name)



    $.get('match_photo', {"name": name}, function(data){
        //$('.search-author-res').children().remove();
        $('#fulltext-res').children().remove();
        $('#fulltext-res').append(data);
    })

});

$("#get-not-match-photo").click(function(){
    var name = $('#not-match-photo').val();
    console.log(name)



    $.get('not_match_photo', {"name": name}, function(data){
        //$('.search-author-res').children().remove();
        $('#fulltext-res').children().remove();
        $('#fulltext-res').append(data);
    })

});

$("#addPhoto").click(function(){

    $.get('get_places', function(json){
        console.log("GET_PLACES " + json);
        $.each(json, function(i, value) {
            console.log(value);
            $('.add-place')
                  .append($('<option></option>', {text:value[2]}).attr("value", i+1))
        });

        $.get('get_photoalbums', function(json){
            $.each(json, function(i, value) {
                console.log(value);
                $('.add-photoalbum')
                      .append($('<option></option>', {text:value[1]}).attr("value", i+1))
            });

            $.get('get_authors', function(json){
                $.each(json, function(i, value) {
                console.log(value);
                $('.add-author')
                  .append($('<option></option>', {text:value[2]}).attr("value", i+1))
                });
                $.get('get_formats', function(json){
                    $.each(json, function(i, value) {
                    console.log(value);
                    $('.add-format')
                        .append($('<option></option>', {text:value[1]}).attr("value", i+1))
                    });
                });
             });
        });

    });
});
