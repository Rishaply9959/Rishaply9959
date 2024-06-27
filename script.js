document.addEventListener('DOMContentLoaded', function () {
    const videoList = [
        { title: 'Sample Video 1', src: 'sample-video.mp4', thumbnail: 'thumbnail1.jpg' },
        { title: 'Sample Video 2', src: 'sample-video2.mp4', thumbnail: 'thumbnail2.jpg' },
        // Add more video objects here
    ];

    const videoListElement = document.getElementById('video-list');
    const mainVideo = document.getElementById('main-video');

    videoList.forEach(video => {
        const img = document.createElement('img');
        img.src = video.thumbnail;
        img.alt = video.title;
        img.addEventListener('click', () => {
            mainVideo.src = video.src;
            mainVideo.play();
        });
        videoListElement.appendChild(img);
    });

    const searchButton = document.getElementById('search-button');
    const searchInput = document.getElementById('search-input');

    searchButton.addEventListener('click', () => {
        const query = searchInput.value.toLowerCase();
        const filteredVideos = videoList.filter(video => video.title.toLowerCase().includes(query));
        
        videoListElement.innerHTML = '';
        filteredVideos.forEach(video => {
            const img = document.createElement('img');
            img.src = video.thumbnail;
            img.alt = video.title;
            img.addEventListener('click', () => {
                mainVideo.src = video.src;
                mainVideo.play();
            });
            videoListElement.appendChild(img);
        });
    });
});
          
