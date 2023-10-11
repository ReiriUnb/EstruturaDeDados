def media_movel_simples(m, n, sequencia):
    medias_moveis = []
    janela = sum(sequencia[:n])

    for i in range(m - n + 1):
        media_movel = janela // n
        medias_moveis.append(media_movel)

        if i + n < m:
            janela = janela - sequencia[i] + sequencia[i + n]

    return medias_moveis

m, n = map(int, input().split())
sequencia = list(map(int, input().split()))

resultado = media_movel_simples(m, n, sequencia)
print(*resultado, sep="\n")
