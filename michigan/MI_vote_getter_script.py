import pandas as pd

results_path = ''
turnout_path = ''

def main():

    # Read results from MI website
    df_results = pd.read_csv(results_path, delimiter='\t', header=1)

    #write to csv and excel
    df_results.to_csv('mi_results_by_county.csv', index=False)
    df_results.to_excel('mi_results_by_county.xlsx', index=False)

    # Read in voter turn out numbers from MI website
    df_turnout = pd.read_csv(turnout_path, delimiter='\t', header=1)

    #write to csv and excel
    df_turnout.to_csv('mi_turnout_by_county.csv', index=False)
    df_turnout.to_excel('mi_turnout_by_county.xlsx', index=False)




if __name__ == "__main__":
    main()