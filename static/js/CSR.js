// Passo 1: Simular um banco de dados com 4 notícias por categoria
const bancoDeDadosSimulado = {
    home: [
        { id: 1, titulo: "Como a tecnologia está mudando o trabalho remoto", conteudo: "Novas ferramentas e plataformas prometem revolucionar o home office..." },
        { id: 2, titulo: "Guia de viagem: os melhores destinos para 2025", conteudo: "Planeje suas próximas férias com nossa lista de lugares incríveis..." },
        { id: 3, titulo: "A importância da saúde mental no dia a dia", conteudo: "Especialistas dão dicas de como manter o equilíbrio e o bem-estar..." },
        { id: 4, titulo: "Mercado de games continua em forte expansão", conteudo: "A indústria de jogos eletrônicos deve bater novos recordes de faturamento este ano..." }
    ],
    entretenimento: [
        { id: 5, titulo: "Novo filme de super-herói quebra recordes de bilheteria", conteudo: "A aguardada sequência arrecadou mais de $100 milhões em seu primeiro fim de semana..." },
        { id: 6, titulo: "Série baseada em livro best-seller ganha data de estreia", conteudo: "A adaptação era uma das mais esperadas pelos fãs da saga literária..." },
        { id: 7, titulo: "Festival LollaPalooza anuncia atrações para o próximo ano", conteudo: "Grandes nomes da música nacional e internacional estão confirmados no evento..." },
        { id: 8, titulo: "Crítica: 'O Labirinto de Espelhos' é um suspense inteligente", conteudo: "Com um roteiro cheio de reviravoltas, o filme prende a atenção do espectador..." }
    ],
    politica: [
        { id: 9, titulo: "Acordo comercial entre blocos econômicos é assinado", conteudo: "O acordo histórico deve impulsionar as exportações e fortalecer a economia..." },
        { id: 10, titulo: "Reforma tributária entra em nova fase de votação no congresso", conteudo: "O texto-base foi aprovado na comissão especial e segue para o plenário..." },
        { id: 11, titulo: "Cúpula do clima define novas metas para redução de emissões", conteudo: "Líderes mundiais se comprometeram a acelerar a transição para energias limpas..." },
        { id: 12, titulo: "Governo lança programa de incentivo a micro e pequenas empresas", conteudo: "O objetivo é facilitar o acesso ao crédito e estimular a geração de empregos..." }
    ],
    esporte: [
        { id: 13, titulo: "Na final da Champions, Real Madrid vence o Liverpool", conteudo: "Com gol de Vinicius Jr, o time espanhol conquistou o título europeu mais uma vez..." },
        { id: 14, titulo: "Seleção Brasileira é convocada para os próximos amistosos", conteudo: "O técnico anunciou a lista com algumas novidades e retornos importantes..." },
        { id: 15, titulo: "Recorde mundial é quebrado na maratona de Berlim", conteudo: "O atleta queniano completou a prova em um tempo impressionante, fazendo história..." },
        { id: 16, titulo: "Temporada da NBA começa com jogos eletrizantes", conteudo: "As principais equipes estrearam com vitórias e grandes atuações de suas estrelas..." }
    ],
    receitas: [
        { id: 17, titulo: "Receita de Risoto de Camarão cremoso e fácil", conteudo: "Aprenda o passo a passo para um prato sofisticado e delicioso para qualquer ocasião..." },
        { id: 18, titulo: "Bolo de Fubá com goiabada: o lanche da tarde perfeito", conteudo: "Uma receita tradicional que agrada a todos, fofinha e com um sabor irresistível..." },
        { id: 19, titulo: "Como fazer um Hambúrguer artesanal suculento em casa", conteudo: "Surpreenda a todos com um lanche de qualidade, feito por você mesmo..." },
        { id: 20, titulo: "Moqueca Baiana: tradição e sabor em um só prato", conteudo: "Descubra os segredos para preparar uma moqueca autêntica e cheia de dendê..." }
    ]
};

// Espera o HTML carregar completamente para começar a executar o script
document.addEventListener('DOMContentLoaded', () => {

    // Passo 2: Selecionar os elementos do HTML que vamos manipular
    const navLinks = document.querySelectorAll('.nav-a');
    const mainContainer = document.querySelector('.main');
    const categoriaTituloEl = document.querySelector('.categoria-titulo h2');

    // Função para normalizar o texto (remove acentos e transforma em minúsculas)
    const normalizarTexto = (texto) => {
        return texto.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    };

    // Passo 3: Função principal que busca e renderiza as notícias na tela
    const carregarNoticias = (categoriaKey) => {
        
        // Exibe o título da categoria e a mensagem de carregamento
        const nomeCategoria = categoriaKey.charAt(0).toUpperCase() + categoriaKey.slice(1);
        categoriaTituloEl.textContent = `Notícias de ${nomeCategoria}`;
        mainContainer.innerHTML = '<h3 class="carregando">Carregando notícias...</h3>';

        // Simula um atraso de rede (como se estivesse buscando em uma API real)
        setTimeout(() => {
            const noticias = bancoDeDadosSimulado[categoriaKey];
            mainContainer.innerHTML = ''; // Limpa a mensagem "Carregando..."

            const secaoCards = document.createElement('section');
            secaoCards.className = 'cards';

            if (noticias && noticias.length > 0) {
                noticias.forEach(noticia => {
                    // Cria o HTML para cada card
                    const cardHTML = `
                        <div class="card" data-id="${noticia.id}">
                            <div class="card-content">
                                <h3>${noticia.titulo}</h3>
                                <p>${noticia.conteudo.substring(0, 100)}...</p> 
                            </div>
                        </div>
                    `;
                    secaoCards.innerHTML += cardHTML;
                });
            } else {
                secaoCards.innerHTML = '<p>Nenhuma notícia encontrada para esta categoria.</p>';
            }

            mainContainer.appendChild(secaoCards);
        }, 500); // Meio segundo de atraso simulado
    };

    // Passo 4: Adicionar o "ouvinte de clique" a cada link do menu
    navLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault(); // Impede o recarregamento da página

            // Pega o texto do link clicado (ex: "Política")
            const categoriaTexto = event.target.textContent;
            
            // Normaliza o texto para usar como chave (ex: "politica")
            const categoriaKey = normalizarTexto(categoriaTexto);
            
            // Chama a função para carregar as notícias da categoria correspondente
            carregarNoticias(categoriaKey);
        });
    });

    // Passo 5: Carregar as notícias da "Home" por padrão ao abrir a página
    carregarNoticias('home');
});