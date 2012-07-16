$(document).ready(function(){
    filepicker.setKey('FILEPICKER_KEY');

    $('.filepicker_url').each(function(){
        $(this).hide();
        var file_url = $(this);
        var file_name = $(this).siblings('input.filepicker_name');
        var file_key = $(this).siblings('input.filepicker_key');

        var picker_display = $('<span class="btn btn-success">Choose</span><span class="help-inline">'+file_name.val()+'</span>').insertAfter(file_url);

        $(picker_display[0]).click(function(){
            filepicker.getFile('image/*', {"modal": true}, function(url, metadata){
                if( url && 'key' in metadata && 'filename' in metadata){
                    file_url.val(url);
                    file_name.val(metadata.filename);
                    file_key.val(metadata.key);
                    $(picker_display[1]).text(metadata.filename);

                } else{
                    console.log('error in uploading image');
                }
            });

        });
    });
});
