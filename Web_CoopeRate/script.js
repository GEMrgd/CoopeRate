document.addEventListener("DOMContentLoaded", function() {
    const selectedProfessor = JSON.parse(localStorage.getItem('selectedProfessor'));
    if (selectedProfessor) {
        document.getElementById('professor-image').src = selectedProfessor.image;
        document.getElementById('professor-name').textContent = selectedProfessor.name;
        document.getElementById('professor-university').textContent = selectedProfessor.university;
        document.getElementById('professor-bio').textContent = selectedProfessor.bio;
    }

    const ratingSlider = document.getElementById('rating-slider');
    const ratingValue = document.getElementById('rating-value');
    ratingSlider.addEventListener('input', function() {
        ratingValue.textContent = this.value;
    });

    const submitReviewBtn = document.getElementById('submit-review-btn');
    submitReviewBtn.addEventListener('click', function() {
        const reviewText = document.getElementById('review-text').value;
        const rating = ratingSlider.value;
        console.log('Review Text:', reviewText);
        console.log('Rating:', rating);

        document.getElementById('review-text').value = '';

        ratingSlider.value = 50;
        ratingValue.textContent = '50';
    });

    const profileLinks = document.querySelectorAll('.professor-card a');
    profileLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault();
        });
    });
});
