$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    dataType: 'json',
    success: function (salutation) {
      $('#hello').text(salutation.hello);
    }
  });
});
