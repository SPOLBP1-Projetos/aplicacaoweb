document.addEventListener("DOMContentLoaded", () => {
  const containerCliente = document.getElementById("noticias-cliente");

  // Função para renderizar cards
  function renderNoticias(noticias) {
    containerCliente.innerHTML = ""; // limpa
    noticias.forEach(noticia => {
      const card = document.createElement("div");
      card.classList.add("card");
      card.innerHTML = `
        <div class="card-content">
          <h3>${noticia.titulo}</h3>
          <p>${noticia.conteudo}</p>
        </div>
      `;
      containerCliente.appendChild(card);
    });
  }

  // Clique no menu
  document.querySelectorAll(".nav-a").forEach(link => {
    link.addEventListener("click", (e) => {
      e.preventDefault(); // evita reload da página
      const categoria = link.textContent.trim().toLowerCase();

      if (categoria === "home") {
        containerCliente.innerHTML = "<p>Escolha uma categoria acima para ver mais notícias.</p>";
        return;
      }

      fetch(`/api/ccr_categoria/${categoria}`)
        .then(res => res.json())
        .then(noticias => {
          renderNoticias(noticias);
        })
        .catch(err => console.error("Erro ao carregar notícias:", err));
    });
  });
});