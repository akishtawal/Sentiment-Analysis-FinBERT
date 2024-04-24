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
  $('#sentiment-fin-form').submit(function(event) {
      event.preventDefault();

      var formData = $(this).serialize();
      var csrftoken = getCookie('csrftoken');

      var $result = $('.result');
      $result.html('<span class="loading">Loading...</span>');

      $.ajax({
          type: 'POST',
          url: '/sentiment_fin/', // URL for the financial sentiment analysis view
          data: formData,
          headers: {
              'X-CSRFToken': csrftoken
          },
          timeout: 60000, // Set a timeout of 60 seconds (adjust as needed)
          success: function(response) {
              $result.html('Sentiment: ' + response.sentiment);
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