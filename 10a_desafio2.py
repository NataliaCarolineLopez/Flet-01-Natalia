import flet as ft

def main(page: ft.Page):
    # Configurações iniciais
    page.title = "Loja Virtual Mini"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = ft.Colors.GREY_50

    # Estado do carrinho
    carrinho = []
    total_carrinho = 0.0

    # Elementos da interface
    area_produtos = ft.GridView(
        expand=1,
        runs_count=2,
        max_extent=180,
        child_aspect_ratio=0.9,
        spacing=15,
        run_spacing=15
    )
    contador_carrinho = ft.Text("Carrinho (0)", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700)
    total_texto = ft.Text("Total: R$ 0,00", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700)
    lista_carrinho = ft.ListView(height=150, spacing=5)
    notificacao = ft.Text(size=14, color=ft.Colors.BLUE_600, text_align=ft.TextAlign.CENTER)

    # Lista de produtos
    produtos = [
        {"nome": "Paletó", "preco": 200.00, "categoria": "Social", "emoji": "👔", "cor": ft.Colors.RED_400},
        {"nome": "Vestido", "preco": 90.00, "categoria": "Social", "emoji": "👗", "cor": ft.Colors.BLUE_400},
        {"nome": "Casaco", "preco": 125.00, "categoria": "Inverno", "emoji": "🧥", "cor": ft.Colors.GREEN_400},
        {"nome": "Cachecol", "preco": 45.00, "categoria": "Inverno", "emoji": "🧣", "cor": ft.Colors.PURPLE_400},
        {"nome": "Luvas", "preco": 30.00, "categoria": "Inverno", "emoji": "🧤", "cor": ft.Colors.ORANGE_400},
        {"nome": "Cropped", "preco": 30.00, "categoria": "Verão", "emoji": "👚", "cor": ft.Colors.YELLOW_700},
        {"nome": "Camiseta", "preco": 35.00, "categoria": "Verão", "emoji": "👕", "cor": ft.Colors.CYAN_400},
        {"nome": "Bermuda", "preco": 50.00, "categoria": "Verão", "emoji": "🩳", "cor": ft.Colors.BROWN_400},
        {"nome": "Maiô ", "preco": 70.00, "categoria": "Verão", "emoji": "🩱", "cor": ft.Colors.PINK_400},
        {"nome": "Biquíni", "preco": 80.00, "categoria": "Verão", "emoji": "👙", "cor": ft.Colors.BLACK},
        {"nome": "Calça", "preco": 95.00, "categoria": "Inverno", "emoji": "👖", "cor": ft.Colors.GREY_700},
        {"nome": "Chinelo", "preco": 60.00, "categoria": "Verão", "emoji": "🩴", "cor": ft.Colors.BLUE_GREY_400},
        {"nome": "Salto", "preco": 150.00, "categoria": "Social", "emoji": "👠", "cor": ft.Colors.RED_700},
        {"nome": "Tênis", "preco": 170.00, "categoria": "Social", "emoji": "👟", "cor": ft.Colors.GREEN_700},
        {"nome": "Óculos de Sol", "preco": 200.00, "categoria": "Verão", "emoji": "🕶️", "cor": ft.Colors.PINK_100},
        {"nome": "Chapéu ", "preco": 85.00, "categoria": "Verão", "emoji": "👒", "cor": ft.Colors.RED_200},
        {"nome": "Boné", "preco": 50.00, "categoria": "Verão", "emoji": "🧢", "cor": ft.Colors.GREEN_300},
        {"nome": "Sunga", "preco": 45.00, "categoria": "Verão", "emoji": "🩲", "cor": ft.Colors.YELLOW_300},
        {"nome": "Bolsa", "preco": 160.00, "categoria": "Social", "emoji": "👛", "cor": ft.Colors.PURPLE_300},
        {"nome": "Bolsinha", "preco": 165.00, "categoria": "Social", "emoji": "👝", "cor": ft.Colors.BLUE_300},
        {"nome": "Anel", "preco": 300.00, "categoria": "Social", "emoji": "💍", "cor": ft.Colors.WHITE60}
    ]

    # Filtros
    filtro_categoria = ft.Dropdown(
        label="Categoria",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=150,
        value="Todas",
        color=ft.Colors.BLACK,
        options=[
            ft.dropdown.Option("Todas"),
            ft.dropdown.Option("Social"),
            ft.dropdown.Option("Inverno"),
            ft.dropdown.Option("Verão")

        ]
    )
    filtro_preco = ft.Dropdown(
        label="Preço",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        width=150,
        value="Todos",
        options=[
            ft.dropdown.Option("Todos")
        ]
    )
    campo_busca = ft.TextField(
        label="Buscar produto",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        width=200,
        prefix_icon=ft.Icons.SEARCH
    )

    # Funções principais
    def mostrar_notificacao(msg):
        notificacao.value = msg
        page.update()

    def atualizar_carrinho():
        contador_carrinho.value = f"Carrinho ({len(carrinho)})"
        total_texto.value = f"Total: R$ {total_carrinho:.2f}"
        lista_carrinho.controls.clear()
        for i, item in enumerate(carrinho):
            linha = ft.Row([
                ft.Text(item["nome"], expand=True),
                ft.Text(f"R$ {item['preco']:.2f}", color=ft.Colors.GREEN_600),
                ft.IconButton(
                    ft.Icons.DELETE,
                    icon_color=ft.Colors.RED,
                    on_click=lambda e, idx=i: remover_do_carrinho(idx)
                )
            ], spacing=10)
            lista_carrinho.controls.append(linha)
        page.update()

    def adicionar_ao_carrinho(nome, preco):
        nonlocal total_carrinho
        carrinho.append({"nome": nome, "preco": preco})
        total_carrinho += preco
        atualizar_carrinho()
        mostrar_notificacao(f"{nome} adicionado!")

    def remover_do_carrinho(idx):
        nonlocal total_carrinho
        if 0 <= idx < len(carrinho):
            produto = carrinho.pop(idx)
            total_carrinho -= produto["preco"]
            atualizar_carrinho()
            mostrar_notificacao(f"{produto['nome']} removido")

    def criar_card_produto(nome, preco, categoria, emoji, cor):
        return ft.Container(
            content=ft.Column([
                ft.Text(emoji, size=40, text_align=ft.TextAlign.CENTER),
                ft.Text(
                    nome,
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                    max_lines=2,
                    overflow=ft.TextOverflow.ELLIPSIS
                ),
                ft.Text(
                    f"R$ {preco:.2f}",
                    size=14,
                    color=ft.Colors.WHITE70,
                    text_align=ft.TextAlign.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
            ),
            bgcolor=cor,
            padding=20,
            border_radius=15,
            width=160,
            height=180,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=8,
                color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK)
            ),
            on_click=lambda e, n=nome, p=preco: adicionar_ao_carrinho(n, p),
            ink=True
        )

    def carregar_produtos(e=None):
        area_produtos.controls.clear()
        categoria = filtro_categoria.value
        preco_faixa = filtro_preco.value
        busca = (campo_busca.value or "").lower()
        for produto in produtos:
            # Filtro categoria
            if categoria != "Todas" and produto["categoria"] != categoria:
                continue
            # Filtro preço
            if preco_faixa == "Até R$ 10" and produto["preco"] > 10:
                continue
            elif preco_faixa == "R$ 10-20" and not (10 < produto["preco"] <= 20):
                continue
            elif preco_faixa == "Acima R$ 20" and produto["preco"] <= 20:
                continue
            elif preco_faixa == "Acima R$ 50" and produto["preco"] <= 50:
                continue

            # Filtro busca
            if busca and busca not in produto["nome"].lower():
                continue
            card = criar_card_produto(
                produto["nome"], produto["preco"], produto["categoria"], produto["emoji"], produto["cor"]
            )
            area_produtos.controls.append(card)
        page.update()

    def finalizar_compra(e):
        nonlocal total_carrinho
        if len(carrinho) > 0:
            carrinho.clear()
            total_carrinho = 0.0
            atualizar_carrinho()
            mostrar_notificacao("Compra finalizada! Obrigado!")
        else:
            mostrar_notificacao("Carrinho vazio!")

    def limpar_filtros(e):
        filtro_categoria.value = "Todas"
        filtro_preco.value = "Todos"
        campo_busca.value = ""
        carregar_produtos()
        mostrar_notificacao("Filtros limpos!")
        page.update()

    # Eventos dos filtros
    for controle in [filtro_categoria, filtro_preco, campo_busca]:
        controle.on_change = carregar_produtos

    # Carrega produtos inicialmente
    carregar_produtos()

    # Interface
    page.add(
        ft.Column([
            ft.Text(
                "Loja Virtual da Nati 🛍️",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_800,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Encontre os melhores produtos!",
                size=14,
                color=ft.Colors.GREY_600,
                text_align=ft.TextAlign.CENTER
            ),
            # Filtros
            ft.Row(
                [filtro_categoria, filtro_preco],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            ),
            ft.Row(
                [
                    campo_busca,
                    ft.ElevatedButton(
                        "🧹 Limpar Filtros",
                        on_click=limpar_filtros,
                        bgcolor=ft.Colors.ORANGE_400,
                        color=ft.Colors.WHITE,
                        height=40,
                        style=ft.ButtonStyle(
                            text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD)
                        )
                    )
                ]
            ),
            # Produtos
            ft.Container(
                content=area_produtos,
                height=400,
                border=ft.border.all(1, ft.Colors.GREY_300),
                border_radius=10,
                padding=10
            ),
            # Carrinho
            ft.Container(
                content=ft.Column([
                    ft.Row(
                        [contador_carrinho, total_texto],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    lista_carrinho,
                    ft.Row([
                        ft.ElevatedButton(
                            "Finalizar Compra",
                            on_click=finalizar_compra,
                            bgcolor=ft.Colors.GREEN,
                            color=ft.Colors.WHITE,
                            width=200
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    notificacao
                ], spacing=10),
                bgcolor=ft.Colors.WHITE,
                padding=20,
                border_radius=10,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=3,
                    color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK)
                )
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
        )
    )

ft.app(target=main)