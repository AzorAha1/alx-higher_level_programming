$(document).ready(function () {
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json",  
    function (data, textStatus, jqXHR) {
     for (var i = 0; i < data.results.length; i++)
     {
        // $('<li>').text(data.results[i].title).appendTo('UL#list_movies');
        $(`<li>${data.results[i].title}</li>`).appendTo('UL#list_movies');
     }
    });
});