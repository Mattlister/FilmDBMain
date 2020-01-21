const IMAGE URLS = {
    films : 'https://da641f8a-74ec-4607-982a-5e597c0231a5.ws-eu01.gitpod.io/files/download/?id=5c0a6d7a-5182-4a87-84c6-f684d072324f',
    TV: 'https://da641f8a-74ec-4607-982a-5e597c0231a5.ws-eu01.gitpod.io/files/download/?id=a663aee9-9fa2-4300-a1a1-4cdaeb1e2bca',
};

function getMovies(searchText){
  axios.get('http://www.omdbapi.com?s='+searchText)
    .then((response) => {
       console.log(response);
        let movies = response.data.Search;
        let output = '';
        $.each(movies, (index, movie) => {
           output += `
          <div class="col-md-3">
            <div class="well text-center">
              <img src="${movie.Poster}">
              <h5>${movie.Title}</h5>
              <a onclick="movieSelected('${movie.imdbID}')" class="btn btn-primary" href="#">Movie Details</a>
            </div>
           </div> 
            `;
    });

    $('#movies').htmnl(output);
})
    .catch((err) => {
        console.log(err);
    });
}
function movieSelected(id){
    sessionStorage.setItem('movieID', id);
    window.location = 'movie.html';
    return false;
}

function getMovie(){
    let movieID = sessionStorage.getItem('movieID';)

    axios.get('http://www.omdbapi.com?i='+movieId)
    .then((response) => {
       console.log(response);
       let movie = response.data;

      

    let output =`
        <div class="row">
          <div class="col-md-4">
            <img src="${movie.Poster}" class="thumbnail">
          </div>
          <div class="col-md-8">
            <h2>${movie.Title}</h2>
            <ul class="list-group">
              <li class="list-group-item"><strong>Genre:</strong> ${movie.Genre}</li>
              <li class="list-group-item"><strong>Released:</strong> ${movie.Released}</li>
              <li class="list-group-item"><strong>Rated:</strong> ${movie.Rated}</li>
              <li class="list-group-item"><strong>IMDB Rating:</strong> ${movie.imdbRating}</li>
              <li class="list-group-item"><strong>Director:</strong> ${movie.Director}</li>
              <li class="list-group-item"><strong>Writer:</strong> ${movie.Writer}</li>
              <li class="list-group-item"><strong>Actors:</strong> ${movie.Actors}</li>
            </ul>
          </div>
        </div>
        <div class="row">
          <div class="well">
            <h3>Plot</h3>
            ${movie.Plot}
            <hr>
            <a href="http://imdb.com/title/${movie.imdbID}" target="_blank" class="btn btn-primary">View IMDB</a>
            <a href="index.html" class="btn btn-default">Go Back To Search</a>
          </div>
        </div>
      `;

      $('#movie').html(output);
    })
    .catch((err) => {
        console.log(err);
    });
}

}

function changeImage(img){
    
    document.body.style.backgroundImage = 'url(http://placehold.it/'+../img/suits9.jpg++')';
    
}
