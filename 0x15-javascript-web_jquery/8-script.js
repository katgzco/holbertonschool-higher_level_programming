$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (movies) {
      for (const movie of movies.results) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      }
    }
  });
});
