function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function() {
    $('#sentiment-form').submit(function(event) {
        event.preventDefault();

        var formData = $(this).serialize();
        var $result = $('.result');
        $result.html('<span class="loading">Loading...</span>'); // Display the loading icon

        $.ajax({
            type: 'POST',
            url: '/sentiment/', 
            data: formData,
            success: function(response) {
                $result.html('Sentiment: ' + response.sentiment); // Update the result div with the sentiment
            },
            error: function() {
                $result.html('An error occurred while processing the request.');
            }
        });
    });
});