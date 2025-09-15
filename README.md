# Repositório da atividade aula "Tipos de renderização HTML"

<h3>Tipos usados neste projeto:</h3>

<ul>
<li> <strong>MPA</strong> --> Cada clique recarrega uma nova página HTML (rotas separadas). Cada ação do usuário, como um clique, faz com que o navegador solicite e carregue uma página inteira nova do servidor. É o modelo mais tradicional e simples, ótimo para SEO, mas a navegação é mais lenta.
  
<li> <strong>CSR</strong> --> O navegador baixa um arquivo HTML básico e um arquivo JavaScript. O JavaScript é responsável por construir e renderizar todo o conteúdo. A navegação entre páginas é muito mais rápida, pois apenas as partes necessárias são atualizadas, sem recarregar a página toda. A fluidez é maior, mas pode apresentar desafios para SEO e para o carregamento inicial.
  
<li> <strong>SSR</strong> --> O servidor gera a página HTML completa e a envia ao navegador. A página aparece rapidamente, mas a interatividade (botões, formulários) só funciona depois que o JavaScript é carregado no navegador. Ideal para SEO e sites que precisam de carregamento inicial rápido. <br>
  
  - <strong>SSR sem JavaScript:</strong> Em um site puramente estático (como um blog, uma página de notícias ou um portfólio simples sem nenhuma funcionalidade avançada), pode-se usar o SSR para gerar o HTML no servidor e enviá-lo. Ele funcionará perfeitamente, já que não há necessidade de interatividade. <br>
  
  - <strong>SSR com JavaScript:</strong> O servidor envia o HTML completo para o carregamento rápido e o JavaScript, em seguida, "hidrata" a página para que ela se comporte como uma aplicação moderna. Isso é a melhor combinação dos dois mundos: carregamento inicial rápido (ótimo para SEO) com fluidez e interatividade de um aplicativo de uma única página.
</ul>
