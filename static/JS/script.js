const IMAGE URLS = {
    films : 'https://da641f8a-74ec-4607-982a-5e597c0231a5.ws-eu01.gitpod.io/files/download/?id=5c0a6d7a-5182-4a87-84c6-f684d072324f',
    TV: 'https://da641f8a-74ec-4607-982a-5e597c0231a5.ws-eu01.gitpod.io/files/download/?id=a663aee9-9fa2-4300-a1a1-4cdaeb1e2bca',
};

// Sets the background image
const setBackground = (image) => {
    document.body.style.background = "url('"+IMAGE_URLS.[image]+"')";
};

if (isfilms) {
    setBackground('films');
} else {
    setBackground('TV')
}

