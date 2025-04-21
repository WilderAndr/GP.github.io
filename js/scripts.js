// En tu script.js
document.addEventListener('DOMContentLoaded', function() {
    // Cargar miembros del equipo desde la API
    fetch('/api/members')
        .then(response => response.json())
        .then(members => {
            const teamGrid = document.querySelector('.team-grid');
            members.forEach(member => {
                teamGrid.innerHTML += `
                    <div class="team-card">
                        <div class="team-card-inner">
                            <div class="team-card-front">
                                <img src="https://picsum.photos/200/200?random=${member.id}" alt="${member.name}">
                                <h3>${member.name}</h3>
                                <p>${member.role}</p>
                            </div>
                            <div class="team-card-back">
                                <h3>${member.name}</h3>
                                <p>${member.bio}</p>
                                <a href="${member.portfolio_url}" class="btn-small">Ver portafolio</a>
                            </div>
                        </div>
                    </div>
                `;
            });
        });
    
    // Cargar tecnologías
    fetch('/api/technologies')
        .then(response => response.json())
        .then(techs => {
            const techGrid = document.querySelector('.tech-grid');
            techs.forEach(tech => {
                techGrid.innerHTML += `
                    <div class="tech-item">
                        <img src="https://picsum.photos/100/100?random=${tech.id}" alt="${tech.name}">
                        <h3>${tech.name}</h3>
                        <p>${tech.description}</p>
                    </div>
                `;
            });
        });
});
