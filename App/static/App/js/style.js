// // Example using jQuery for AJAX request
// $.ajax({
//     url: "{% url 'signup' %}",
//     type: "POST",
//     headers: { "X-CSRFToken": Cookies.get('csrftoken') },
//     // Other parameters...
// });


var csrftoken = getCookie('csrftoken');

// Example using jQuery
$.ajax({
    type: "POST",
    url: "{% url 'signup' %}",
    data: { your_data: 'some_data' },
    headers: { "X-CSRFToken": csrftoken },
    success: function(response) {
        // Handle success
    }
});


const toggle = document.querySelector(".toggle"),
input = document.querySelector("input");

toggle.addEventListener("click", () =>{
    if(input.type ==="password"){
      input.type = "text";
      toggle.classList.replace("uil-eye-slash", "uil-eye");
    }else{
      input.type = "password";
    }
})


$.ajaxSetup({
  beforeSend: function(xhr, settings) {
      if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
          // Only send the token to relative URLs i.e. locally.
          xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
      }
  }
});


if (window.location.search.indexOf('reloaded') === -1) {
  var hash = window.location.hash;
  window.location.replace(window.location + '?reloaded' + hash);
}
