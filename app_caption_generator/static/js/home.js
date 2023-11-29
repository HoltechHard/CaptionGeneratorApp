$(document).ready(function(){
    
    // upload image
    $('#imageUpload').change(function(){
        const image = $(this)[0].files[0];
        if(image){
            const reader = new FileReader();
            reader.onload = function(e){                
                $('#uploadedImage').attr('src', e.target.result);
            }

            reader.readAsDataURL(image);
        }
    });

    // make prediction and save data in database
    $('#btnPredict').click(function(){
        const formData = new FormData();
        formData.append('image', $('#imageUpload')[0].files[0]);

        $.ajax({
            url: '/',  
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(res) {
                console.log('Image uploaded successfully!');
                $('#txtDescription').text(res.description);
            },
            error: function(xhr, status, error) {
                console.error('Error uploading image:', error);                
            }
        });
    });

    // refresh web page
    $('#btnRefresh').click(function(){
        $('#uploadedImage').attr('src', '');
        $('#uploadedImage').attr('src', 'static/images/default.jpg');
        $('#txtDescription').text('the text predicted...');
    });
});
