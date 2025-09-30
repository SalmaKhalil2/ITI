document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const projectCards = document.querySelectorAll('.project-card');

    searchInput.addEventListener('input', () => {
        const filter = searchInput.value.toLowerCase();
        projectCards.forEach(card => {
            const title = card.querySelector('.project-title').textContent.toLowerCase();
            if(title.includes(filter)) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    });
});
