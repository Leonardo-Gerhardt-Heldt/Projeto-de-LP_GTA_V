init python:
    escolhaD1 = False
    escolhaD2 = False
    escolhaD3 = False
    escolhaD4 = False
    escolhaD5 = False
    escolhaD6 = False
    escolhaD7 = False
    escolhaE1 = False
    escolhaE2 = False

define e = Character("Loirão")

define p = Character("Pavel")

image aleluia = "images/ggwp.png"

image se fodeu = "images/sefodeu.png"

image morto torre = "images/pracima.png"

image porta chaves = "images/porta.png"

image finalmente = "images/win2.png"

image fundo pavel = "images/fundopavel.png"

image ajudante pavel = "images/Pavel.png"

label start:

    play music "audio/HoldTheLine.mp3"
    queue music "audio/HorseNoName.mp3" noloop
    scene banner
    with dissolve

    e "Você tem como objetivo realizar o Golpe de Cayo Perico do GTA 5."

    e "Você não deve ser exposto a nenhum guarda, pois quando descoberto, finalizar o golpe torna-se extremamente difícil."

    e "O Pavel nos ajudará a concluir o golpe, iremos começar logo depois de nos infiltrarmos na propriedade"

    scene fundopavel

    show ajudante pavel at left:
        zoom 0.5
        yalign 0.1
    with fade

    p "Dale pra mais uma dessas!"

    hide ajudante pavel

    stop music

    scene inicio
    with dissolve

    play music "audio/Theme.mp3"

    menu:
        "Ir a Direita":
            scene direita1
            with fade

            menu:
                "Silenciosamente a Esquerda":
                    $escolhaD1 = True

                "Matar o NPC":
                    $escolhaD1 = True


            if escolhaD1 == True:
                scene npccomcamera
                with fade

                menu:
                    "Silenciosamente a direita":
                        $escolhaD2 = True

                    "Matar outro NPC":
                        $escolhaD2 = False

                if escolhaD2 == True:
                    scene corredordir
                    with fade

                    menu:
                        "Silenciosamente a Direita":
                            $escolhaD3 = False


                        "Matar ambos NPC's com HS":
                            $escolhaD3 = True

                    if escolhaD3 == True:
                        scene 1guardaverm
                        with fade

                        menu:
                            "Matar o NPC de camisa vermelha":
                                $escolhaD4 = True

                            "Continuar reto":
                                $escolhaD4 = False

                        if escolhaD4 == True:
                            scene matar1
                            with fade

                            show ajudante pavel at center:
                                zoom 0.5
                                yalign 0.1
                            with dissolve
                            p "Tu conseguiu um dos cartões para usar o elevador, mas não de muita atenção pra isso...Continue procurando pela chave."

                            hide ajudante pavel

                            menu:
                                "Seguir até o portão de saída":
                                    $escolhaD5 = False

                                "Pegar a esquerda e subir as escadas":
                                    $escolhaD5 = True

                            if escolhaD5 == True:
                                scene matou1verm
                                with fade

                                menu:
                                    "Matar outro NPC":
                                        $escolhaD6 = True

                                    "Se esgueirar de fininho por trás":
                                        $escolhaD6 = False

                                if escolhaD6 == True:
                                    scene pracima
                                    with fade

                                    show ajudante pavel at center:
                                        zoom 0.5
                                        yalign 0.1
                                    with dissolve
                                    p "Que sorte caralho, achou a chave!!"
                                    p "Não precisa procurar pelas chaves, vá até o cofre no subterrâneo."

                                    hide ajudante pavel

                                    scene esqescada
                                    with fade

                                    menu:
                                        "Seguir pela esquerta até o porão":
                                            $escolhaD7 = True

                                        "Dar uma averiguada no ambiente ao redor":
                                            $escolhaD7 = False

                                    if escolhaD7 == True:
                                        show porta chaves
                                        with fade
                                        p "Use a chave para ter acesso ao subterrâneo."

                                        scene win1
                                        with fade

                                        p "Prossiga com o código que lhe enviei para abrir o cofre."

                                        show finalmente

                                        p "Cacetada!! Finalmente concluímos o golpe."

                                        show aleluia
                                        with fade

                                        e "Good game, well played."

                                    if escolhaD7 == False:
                                        play music "audio/Wasted.mp3" noloop
                                        scene se fodeu
                                        with fade


                                        p "Loirão.... nessa altura do campeonato e você ta querendo dar uma banda por aí."
                                        p "Tu ta literalmente no meio de todo mundo!! Pensa direito da próxima vez."

                                if escolhaD6 == False:
                                    play music "audio/Wasted.mp3" noloop
                                    scene se fodeu
                                    with fade


                                    p "Ta se achando com corpo de minhoca pra passar por esse espaço?? Se enxerga poha!!"

                            if escolhaD5 == False:
                                play music "audio/Wasted.mp3" noloop
                                scene se fodeu
                                with fade


                                p "Tá indo pra onde carai??? Terminou ainda não poha!!"

                        if escolhaD4 == False:
                            play music "audio/Wasted.mp3" noloop
                            scene se fodeu
                            with fade


                            p "O cara tava olhando bem na direção que tu foi, presta atenção aí poh. Ninguém deles é cego, caralho!!"

                    if escolhaD3 == False:
                        play music "audio/Wasted.mp3" noloop
                        scene se fodeu
                        with fade


                        p "Qualquer pessoa é vista se esgueirando por esse arbustinhos pequenos, pensa em outra!"



                if escolhaD2 == False:
                    play music "audio/Wasted.mp3" noloop
                    scene se fodeu
                    with fade


                    p "Presta atenção no minimapa.Tinha uma camera bem em cima dele!!"

                    hide ajudante pavel
        "Ir a Esquerda":
            scene esquerda1
            with fade

            menu:
                "Ir em frente":
                    $escolhaE1 = False

                "Continuar pela esquerda":
                    $escolhaE1 = True

            if escolhaE1 == True:
                scene esquerdaesq
                with fade

                menu:
                    "Matar ambos NPC's":
                        $escolhaE2 = True

                    "Entrar no corredor a direita":
                        $escolhaE2 = False

                if escolhaE2 == True:
                    play music "audio/Wasted.mp3" noloop
                    scene se fodeu
                    with fade


                    p "Eitaaa Loirão!Parece que tu não estava com o reflexo bom, deu tempo de um deles avisar todo mundo."


                if escolhaE2 == False:
                    play music "audio/Wasted.mp3" noloop
                    scene se fodeu
                    with fade


                    p "Cacetada Loirão!!! Tu não chega o minimapa não?? Tinha uma cara no meio do corredor!!!"

            if escolhaE1 == False:
                play music "audio/Wasted.mp3" noloop
                scene se fodeu
                with fade


                p "Parece que tu não cuidou o minimapa, tinha um segurança logo atrás dos coqueiros."

    return
