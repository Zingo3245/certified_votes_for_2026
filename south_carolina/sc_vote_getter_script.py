import pandas as pd

excel_file=""

def main():
    # Setting up for list
    str_list = []
    for x in list(range(2, 71)):
        str_list.append(str(x))

    # Putting everything together
    for page in str_list:
        # Get the excel file into something more usable.
        title = pd.read_excel(excel_file, sheet_name=page, header=0).columns[0]
        header = pd.read_excel(excel_file, sheet_name=page, header=1)
        df = pd.read_excel(excel_file, sheet_name=page, header=2)

        # Get the amount of epochs of each sheet
        epoch = int(len(df.columns) / 7)

        # Get starting values
        candidate = 2
        start = 2
        end = 9
        dfs = []

        # secondary loop
        for x in range(epoch):
            # Get the candidate
            race = header.columns[candidate]
            
            # Get county and registered voters
            ref_df = df[df.columns[:2]]
        
            # Get main vote totals
            main_df = df[df.columns[start:end]]
        
            # Put all of them together
            com_df = pd.concat([ref_df, main_df], axis=1)
        
            # Attach candidate
            com_df['candidate'] = race
        
            # Correct columns
            com_df.columns = ['County', 'Registered_Voters', 'Election_Day', 'Early_Voting', 'Absentee_By_Mail', 'Failsafe', 'Provisional',
                            'Failsafe_Provisional', 'Total_Votes', 'Candidate']
        
            # Set up next epoch
            dfs.append(com_df)
            candidate += 7
            start += 7
            end += 7
        
        # Process files
        file_title = title.replace('(', '').replace(')', '').replace(' ', '_')
        csv_title = file_title + '.csv'
        excel_title = file_title + '.xlsx'
        total_df = pd.concat([x for x in dfs])
        total_df.to_csv(csv_title, index=False)
        total_df.to_excel(excel_title, index=False)

if __name__ == "__main__":
    main()