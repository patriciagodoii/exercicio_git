# Exercício GIT HUB - Calcule a média de quilômetros percorridos nos projetos Micropoluentes e Hidrosfera
# Faça o erxercício para fixação

"""

O Hidrosfera e Micropoluentes são dois convênios do IT.DT que possuem muitos campos para coleta de dados.
Para essas coletas, os analistas precisam percorrer diferentes pontos amostrais.
Contudo, para um relatório de campo, é necessário quantificar o caminho percorrido até o final das campanhas.
Pensando que o hidrosfera possui 12 campanhas no ano e o micropoluentes 8, sendo que cada campanha percorre em média 7 km.
Quantos km percorridos teremos ao final do ano?

"""

campanhas_hidrosfera_ano = 12
campanhas_micropoluentes_ano = 8
media_percorrida_camapanhas_km = 7

media_percorrida_km_ano = (campanhas_hidrosfera_ano + campanhas_micropoluentes_ano) * media_percorrida_camapanhas_km
print(f" A média de quilômetros percorridos nos projetos Micropoluentes e Hidrosfera é de: \n {media_percorrida_km_ano} km/ano")
