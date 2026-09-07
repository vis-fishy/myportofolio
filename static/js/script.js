const cards = document.querySelectorAll('.experience-card');

cards.forEach(card => {
    card.addEventListener('click', () => {
        card.classList.toggle('expanded');
    });
});