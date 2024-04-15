$(document).ready(function(){
    $('#commentForm').submit(function(event){
        event.preventDefault(); // Prevent default form submission
        
        var comment = $('#id_content').val(); // Get the comment from the textarea
        
        // Send POST request to the endpoint
        console.log('Submitting Data')
        $.ajax({
            url: '/comment/', // Change this to your endpoint URL
            type: 'POST',
            contentType: 'text/html',
            data: JSON.stringify({ comment: comment }),
            success: function(response) {
                // Handle success
                console.log('Comment submitted successfully');
                console.log(response); // Log the response from the server
            },
            error: function(xhr, status, error) {
                // Handle errors
                console.error('Error submitting comment');
                console.error(response); // Log the error response
            }
        });
    });
});