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
    $('#sentiment-form, #sentiment-fin-form').submit(function(event) {
        event.preventDefault();

        var formData = $(this).serialize();
        var csrftoken = getCookie('csrftoken');
        var $result = $('.result');
        var $loadingSpinner = $('<span class="loading-spinner"></span>'); // Animated spinner

        $result.html($loadingSpinner); // Display the loading spinner

        var url = $(this).attr('id') === 'sentiment-form' ? '/sentiment/' : '/sentiment_fin/';

        $.ajax({
            type: 'POST',
            url: url,
            data: formData,
            headers: {
                'X-CSRFToken': csrftoken
            },
            timeout: 60000,
            success: function(response) {
                var sentiment = response.sentiment.toLowerCase();
                var sentimentOutput = sentiment.charAt(0).toUpperCase() + sentiment.slice(1); // Capitalize the first letter
                var sentimentColor = sentiment === 'positive' ? 'green' : (sentiment === 'negative' ? 'red' : 'gray');
                $result.html('<span style="font-size: 24px; font-weight: bold; color: ' + sentimentColor + ';">' + sentimentOutput + '</span>');
            },
            error: function(xhr, status, error) {
                if (status === 'timeout') {
                    $result.html('The request timed out. Please try again.');
                } else {
                    $result.html('An error occurred while processing the request.');
                }
            }
        });
    });
});