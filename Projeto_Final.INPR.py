def linha(mensagem):
    tam = len(mensagem) + 4
    print("." * tam)
    print(f"  {mensagem}")
    print("." * tam)
    
    
def enfeite():
    print("-" * 130)


def links():
    
    import webbrowser 
     
    while True:
        
        print("\n1 - Site:Toda Matéria")
        print("2 - Site: Brazil Escola")
        print("3 - Site: Escola Kids")
        print("4 - Vídeo do Canal: Redação e Gramática Zica")
        print("5 - Vídeo do Canal: Português com Letícia")
        print("6 -  EU QUERO SAIR!!!")
        
        escolha = int(input("Digite uma das opções acima:"))
     
        if escolha == 1:
            webbrowser.open("https://www.todamateria.com.br/frase-oracao-e-periodo/")
            
        elif escolha == 2:
            webbrowser.open("https://brasilescola.uol.com.br/gramatica/frase-oracao-periodo.htm")
            
        elif escolha == 3:
            webbrowser.open("https://escolakids.uol.com.br/portugues/aprendendo-o-conceito-de-frase-oracao-e-periodo.htm")
            
        elif escolha == 4:
            webbrowser.open("https://www.youtube.com/watch?v=FStoeRppxhs")
            
        elif escolha == 5:
            webbrowser.open("https://www.youtube.com/watch?v=L-HyRNdfIhU")
            
        elif escolha == 6:
            print("VOCÊ ESCOLHEU SAIR!!!")
            break 
        
        else:
            Inv = str(input("Opção Inválida!! Você digitou uma opção diferente! Por favor, digite novamente:"))
            links()
            continue
        
        
def conteúdo():
    
    
    print("\nUm período pode ser composto com uma relação de Coordenação ou de Subordinação!\nQuando falamos que o período possui uma relação de coordenação, estamos dizendo que as orações deste período são coordenadas!")
    print("Mas o que são Orações Coordenadas?")
    print("\nOrações Coordenadas são orações INDEPENDENTES!!!!\n")
    print("São orações que estão juntas, porém são independentes, ou seja, são duas orações, que sozinhas, possuem um sentido completo, porém, que se juntam para se complementarem!")
    print("Para coompreender melhor, você pode associar com um relacionamento.Suponhamos que duas pessoas estejam em um relacionameto, elas estão juntas certo? Porém, elas também não são independentes individualmente?")
    print("As duas pessoas tem suas obrigações particulares, as quais só elas podem cumprir, ou seja, cada um exerce a sua função individualmente")
    print("Elas não precisam estarem juntas para serem completas, elas devem ACRECSENTAR na vida do outro.\nElas são independentes, mas escolheram se conectar, viver em uma relação!")
    print("Tá, mas... O que isso tem a ver com orações coordenadas?")
    print("TUDO A VEEEEEER!!!\nSACA SÓ!")
    enfeite()
    print("Da mesma forma que, as duas pessoas do relacionamento conceguem viver sozinhas, individualmente, sem precisar necessariamente do outro, porém, escolheram viver juntas, estabelecendo uma relação direta e se complemetando, assim são as orações coordenadas!")
    print("Elas possuem sentidos completos individualmente, conseguindo passar uma mensagem completa sozinhas, contudo, estão unidas em prol de gerar um sentido maior do que elas provocariam separadamente!")
    print("\nExemplo: - O tempo corria, ela crescia rápido demais.")
    print("Veja que, a primeira oração (O tempo corria), possui um sentido completo, ao lêla é possível compreender a mensagem que ela quer passar!\nDa mesma forma, a segunda oração (ela crescia rápido demais) também possui seu sentido completo!")
    print("Se eu estiver em uma conversa e te disser: O tempo corria, você certamente não entenderá o porquê de eu ter falado isso, mas você comprrenderá o sentido da minha mensagem!\nO mesmo ocorerá com a segunda oração!")
    print("Elas tem sentido próprio individualmte, sintaticamente, elas não precisam de nenhum outro complemento para isso, mas perceba que juntas, elas produzem um sentido maior e mais completo do que quando separadas")
    enfeite()
    print("Existem dois tipos de Orações coordenadas!\nAs Orações Coordenadas Sindéticas e as Orações Coordenadas Assindéticas")
    print("O ponto chave para entender estes tipos é saber que as orações, para estarem juntas, necessitam de algo que as una! Essa -união-, é caracterizada por um determinado elemento\nE são estes -elementos- que dividem as Orações Coordenadas em duas! ")
    print("As Orações Coordenadas Sindéticas são aquelas que possuem conjunções ligando as orações, estas conjunções servem de conectivos entre as duas orações, unindo o sentido delas\nElas são subdividas em 5:\n*Oração Coordenada Sindética Aditiva\n*Oração Coordenada Sindética Adversativa\n*Oração Coordenada Sindética Alternativa\n*Oração Coordenada Sindética Conclusiva\n*Oração Coordenada Sindética Explicativas")
    Tipos_de_OCS()
    print("\nJá as Orações Coordenadas Assindéticas são aquelas orações coordenadas que são ligadas por sinais de pontuação, como por exemplo vígula, dois pontos, ponto e vígula etc...\nOu seja, o que faz a união das duas orações são justamente estes sinais.")
    print("\nEx: Fui ao mercado,comprei frutas e verduras")
    print("Veja que, as duas orações possuem seu sentido commpleto individualmente,porém juntas, por um elemento que, neste caso foi a vírgula, elas possuem um sentido maior!")
    print("\nDICA: Na hora de saber se a oração é Sindética ou Assindética é muito simples!\nBasta você lembrar que a palavra -Sindética- caracteriza a presença de um síndeto, ou seja, de um conectivo")
    print("Enquanto que a palavra -Assindética-, por possuir o prefixo -a-, que serve para NEGAR, vai caracterizar a Oração Coordenada que não possui a presença de um síndeto,ou seja de uma conjunção.")
    
    
def Tipos_de_OCS():
    
    while True:
        
        print("\nAnalise os Tipos de orações sindéticas abaixo:")
        
        print("\n")
        print("0 - Oração Coordenada Sindética Aditiva ")
        print("1 - Oração Coordenada Sindética Adversativa")
        print("2 - Oração Coordenada Sindética Alternativa")
        print("3 - Oração Coordenada Sindética Conclusiva")
        print("4 - Oração Coordenada Sindética Explicativas")
        print("5 - Sair!")
        print("\n")
        
        choose = int(input("Escolha uma das possibilidades acima e vem comigo entender as orações coordenadas sindéticas!!"))
        #linha()
        
        if choose == 0:
            print("\nOrações Coordenadas Sindéticas Aditivas ")
            print("\nEssas orações possuem conjunções que estabelecem um sentido de adição à frase,por isso o nome de aditiva")
            print("Esse tipo de oração pede conjunções como -e-, não só, como também e etc...")
            print("\nEx1: Não só lavou os pratos,como também não limpou a pia")
            print("Veja que, nesta oração, o indivíduo não realizou duas ações; além de não ter feito uma coisa ele não fez a outra")
            print("Veja que as expressões -Não só- e -Como também- dão a idéia de que o sentido de uma oração está se adicionando ao da outra!")
            print("\nEx2:A comunidade estava unida e muitos eventos ocorreram")
            print("Perceba que o conectivo da frase dá a ela um sentido de adição de sentido?")
            print("Este conectivo tem o poder de adicionar o sentido de uma frase ao da outra!\nLegal né?")
            
        elif choose == 1: 
            print("\nOração Coordenada Sindética Adversativa")
            print("A palavra -adversativa- remete à idéias contrárias, um adversário, um algo contrário.")
            print("Por isso, este tipo de oração Coordenada Sindética pede conjunções que expressem idéias contrárias")
            print("Um ponto característico dessa oração é que tudo o que foi dito antes da conjunção, será contrariado após ela.")
            print("Algumas das conjunçõies utilizadas são: -mas-, -contudo-, -entretanto-, -porém- e etc..")
            print("\nEx1: Paulo era muito rico, mas vivia de forma bastante modésta")
            print("Veja que, o texto nos mostra que Paulo era muito rico,porém ela dá uma idéia de contraste quando fala que a vida dele não denunciava a sua situação financeira.")
            print("\nEx2:A esposa estava muito triste mas conversava com o marido")
            print("Perceba que esta idéia está apresentando uma adversidade,um embora, um apesar de..., uma idéia de contrariedade!")
            
        elif choose == 2:
            print("\nOração Coordenada Sindética Alternativa")
            print("Alternatiava, dá um sentido de alternância ou exclusão")
            print("Estas orações pedem o uso de conjunções que expressem uma idéia de exclusão ou alternância, sendo que, normalmete elas podem aparecer em dupla,uma conjunção em conjunto á outra")
            print("EX1:Ora eu estudo matemática,ora  eu estudo Português")
            print("Veja que esta oração está querendo dizer que o sujeito da oração está alternado seu estudo entre essas duas matérias!")
            print("EX2: Ou você estuda ou não aprende!")
            print("Nesta oração perceba que o sujeito, ao escolher uma das opções, descarta a outra automaticamente,ou seja ao escolher uma (alternância) a outra será excluída (Exclusão)")
            
        elif choose == 3:
            print("\nOração Coordenada Sindética Conclusiva")
            print("Essas orações são marcadas pelo uso de comjunções que expressem um sentido de conclusão, onde uma idéia será apresentada e logo após, uma conjunção concluirá a tese  apresentada anteriormente!  ")
            print("Algumas das conjunções mais utilizadas neste tipo de oração são: portanto, logo, por fim, pois, por conseguinte e etc")
            print("\nEx1: Ela não assistiu ao vídeo, portanto, não entendeu o assunto")
            print("Note que, a segunda oração está, concluindo o sentido da outra através da conjunção utilizada.")
            print("\nEx2:O plano foi bem elaborado, portanto não haverá problemas!")
            print("Veja que a segunda oração dá uma conclusão ao que foi disposto na oração anterior!\nCaracterizando assim, uma Oração Coordenada Sindética Conclusiva!")
            
        elif choose == 4:
            print("\nOração Coordenada Sindética Explicativas")
            print("É o período composto por coordenação que é caracterizado pelo uso de conjunções que expressem um sentido de explicação!")
            print("Essas conjunções tem a função de explicar o que foi dito anteriormente!")
            print("Algumas das conjunções mais usadas são: por que, porque, por quê, porquê, isto é, ou seja, na verdade e etc... ")
            print("\nEx1: Arrume o quarto, pois teremos visitas")
            print("Veja que é dada uma ordem e, logo em seguida esta ordem é justificada!")
            print("\nEx2:Não assine o contrato,pois você irá se arrepender!")
            print("Observe que, neste período composto por Coordenação, a sua primeira oração expressa uma órdem, e, logo após a ela é dada a explicação da ordem da oração anterior")
            
        elif choose == 5:
            print("\nVOCÊ ECOLHEU SAIR!!")
            break
            
        else:
            
            print("\nOpção Inválida!! Você digitou uma opção diferente! Por favor,digite novamente:")
            print()
            
            
def Questionário ():
    
    Gab = ['a']
    Answers = []
    print("\nAssinale a única alternativa que possui uma oração coordenada assindética:")
    print("a) - Defenda a vida, denuncie a violência contra a mulher.")
    print("b) - Ele trabalha em casa e possui um escritório de advocacia.")
    print("c) - A tecnologia é um bem, mas é instrumento de muitos crimes.")
    print("d) - Quer chova, quer não, iremos à igreja.")
    print("e) - Cuidado com seus pensamentos, pois eles se realizam.")
    
    Recebe_answer = str(input())
    Answers.append(Recebe_answer)
    print(Answers)
    
    for i in range(0,len(Gab),1):
        if Gab[i] == Recebe_answer:
            print("Acertoooooou\nVamos para a próxima questão!")
            
        else:
            print("Errou!!! Deixa eu explicar!!")
            print("Perceba que a única alternativa que não possi nenhuma conjunção com a função de unir as orações é a alternativa (a)")
            print("A letra b, possui uma oração coordenada sindética aditiva")
            print("A letra c, uma adversativa")
            print("A letra d, uma alternativa")
            print("A letra e, uma explicativa")
            print("\nMas vamos para a próxima questão")
            
            
    Gab2= ['d']
    Answers2 = []
    print("\nA oração -Negro e branco designam, portanto, categorias essencialmente políticas- é coordenada:")
    print("a) - Assindética.")
    print("b) - Aditiva.")
    print("c) - Adversativa.")
    print("d) - Conclusiva.")
    print("e) - Completiva nominal.")
    
    Recebe_answer2 = str(input())
    Answers2.append(Recebe_answer2)
    print(Answers2)
    
    for i in range(0,len(Gab2),1):
        if Gab2[i] == Recebe_answer2:
            print("Acertoooooou!!! Vamos para a próxima questão!")
            
        else:
            print("Errou!!! Deixa eu explicar!")
            print("Perceba que a conjunção utilizada (Portanto), tem a função de auxiliar as orações a terem um sentido de conclusão\nUma oração está justificando a outra por meio da conjunção!")
            print("\nMas vamos para a próxima questão")
            
    
    Gab3= ['b']
    Answers3 = []
    print("\nO trecho destacado em *Wolton justifica-se dizendo que a internet é incrível para a comunicação entre pessoas e grupos que tenham os mesmos interesses,\033[1;35mmas está longe de ser uma ferramenta de comunicação de coesão entre pessoas e grupos diferentes*\033[mé uma oração:")
    print("a) - Coordenada sindética aditiva.")
    print("b) - Coordenação sindética adversativa.")
    print("c) - Coordenação sindética conclusiva.")
    print("d) - Coordenada assindética.")
    print("e) - Coodenada sindética explicativa.")
    
    Recebe_answer3 = str(input())
    Answers2.append(Recebe_answer3)
    print(Answers3)
    
    for i in range(0,len(Gab3),1):
        if Gab3[i] == Recebe_answer3:
            print("Acertoooooou!!Obrigada por participar deste questionário!!")
            
        else:
            print("Errou!!!")
            print("A oração é sindética porque possui uma conjunção conectando as frases e adversativa, porque esta conjunção estabelece um sentido de adversidade entre as duas orações ") 
            print("Obrigada por ter feito este questionário")
            
            

linha("\033[1;45;30mOlá a todos os ilustres indivíduos que necessitam de uma forcinha com o assunto: Orações Coordenadas!\033[m")
print("\033[1;45;30mMas você é único não é mesmo?")
name = str(input("Me diga seu nome:"))
print(f"Sinta-se muito bem-vindo(a) {name}")
print('''\033[45;32mEu me chamo Evelyn e espero que, a partir de agora, você sinta este conteúdo adentrando nas profundezas do seu ser de tal forma\nque você finalmente possa comprrender esse assunto tão importante de uma vez por todas!\033[m''')
linha("\033[1;35mPegue seus materiais, arregasse as mangas e como diz uma bela composição:Quem sua mão ao arado já pôs, constante precisa ser!\033[m")
linha("\033[1;35mEu te convido a embarcar nessa linda jornda que é o conhecer!\033[m ")
print("Antes de entrar na explicação do conteúdo, escolha uma das seguintes opções:")
print("\033[1;35m\n1 - Tenho conhecimento sobre oração, frase e período\033[m")
print("\033[1;36m2 - Não tenho conhecimento sobre oração, frase e período!\033[m")

opc = int(input("\033[1;33mDigite a opção desejada:\033[m"))

if opc == 1:
    
    print("\nOk, tendo em vista que você tem uma boa base sobre orações, vamos para o conteúdo!")
    conteúdo()
    print("\n")
    Questionário()
    
else:
    
    opc == 2
    print("\nRecomendo que você estude este conteúdo porque ele é de suma importância para a compreensão deste!")
    print("Vamos fazer uma revisão rápida!")
    linha("\033[1;33mFRASE é toda sentença COMPLETA, ou seja, que possui o seu sentido completo, sem precisar necessariamente de um verbo!\nEx: Que dia lindo!, perceba que esta sentença não possui verbo, porém, ela tem o seu sentido completo!\033[m")
    print("\n")
    linha("\033[1;36mORAÇÃO é uma sentença que gira em torno de um verbo, ou seja, todos os elementos da sentença se relacionam com o verbo!\nEx:A casa está suja - Perceba que todos os elementos desta senteça se relacionam com o verbo, tanto é, que se ele for restirado, ela não fará sentido algum\n Logo, esta sentença é uma oração!\033[m")
    print("\n")
    linha("\033[1;35mPERÍODO - é simplesmente a presença da oração em uma sentença!\n Pode ser simples, que é quando possui a presença de uma única oração\nE pode ser composta, que é quando a sentença possui duas ou mais orações!\033[m")
    print("Para a melhor comprrensão, segue alguns links abaixo caso você estudar melhor esse assunto!")
    links()
    enfeite()

    print("\033[1;33mAgora que você já revisou este conteúdo, vamos às Orações Coordenadas!\033[m")
    conteúdo()
    enfeite()
    print("\n")
    Questionário()
    
print("\n")
print(f"Muito obrigada por ter aprendido comigo {name}!")
print("Eu espero que esta explicação tenha sido capaz de sanar pelo menos algumas das suas dúvidas!")
print("Continue se esforçando e estudando constantemente, afinal, vencedor não é aquele que ultrapassa a todos e chega em primeiro lugar!")
print("O verdadeiro vencedor é aquele que, mesmo caindo, mesmo tropeçando, mesmo mancando, não desiste de caminhar e chega ao seu tão almejado destino !")
print("Pois ele sabe que não é sobre chegar primeiro, é sobre respeitar seu ritmo e manter a constância na caminhada pois é a soma de pequenos esforços diários que nos fazem alcançar grandes coisas! ")


    
    
    