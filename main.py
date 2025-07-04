import pandas as pd
from funcoes import read_csv, mostrar_resultado_anual, mostrar_resultado_total_acumulado, mostrar_volatilidade, localizar_datas_e_cotas_iniciais_e_finais, encerrar_programa, mostrar_menu, mostrar_indice_sharpe, mostrar_maior_cota, mostrar_menor_cota, mostrar_maior_rentabilidade_mensal, mostrar_menor_rentabilidade_mensal

def main():

    # valida o recebimento do arquivo
    while True:
        file_path: str = input('''
            Bem-vindo(a) à calculadora! 
                                    
            Informe o nome do seu arquivo csv, contendo as cotações a serem analisadas:
            ''')
        try:
            open_file: pd.DataFrame = read_csv(file_path)
            if open_file is not None:
                break
        except:
            pass
        print('''
                Não foi possível ler o arquivo. \n
                ''')

    initial_date, initial_quote, final_date, final_quote = localizar_datas_e_cotas_iniciais_e_finais(open_file)

    # lógica principal do código
    while True:
        action = mostrar_menu()

        if action == 0:
            encerrar_programa()
            break

        elif action == 1:
            mostrar_resultado_total_acumulado(initial_date, initial_quote, final_date, final_quote)

        elif action == 2:
            mostrar_volatilidade(open_file, initial_date, final_date)

        elif action == 3:
            mostrar_resultado_anual(open_file)

        elif action == 4:
            mostrar_indice_sharpe(open_file)

        elif action == 5:
            mostrar_maior_cota(open_file)

        elif action == 6:
            mostrar_menor_cota(open_file)

        elif action == 7:
            mostrar_maior_rentabilidade_mensal(open_file)
        
        elif action == 8:
            mostrar_menor_rentabilidade_mensal(open_file)
            
        else:
            print("Escolha uma opção válida. \n")
            continue

        input("\nPressione Enter para voltar ao menu: \n")

if __name__ == "__main__":
    main()