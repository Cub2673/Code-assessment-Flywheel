import pandas as pd
import matplotlib.pyplot as plt

def load_dataset(file_path):
    """
    Load the dataset from a CSV file.
    """
    return pd.read_csv(file_path,delimiter = ';')

def explore_dataset(df):
    """
    Explore the dataset by displaying the head, info, and description.
    """
    print(df.head())
    
    # To get information about the dataset, including data types and null values
    print(df.info())
    
    # To get summary statistics of the dataset like count, standard deviation, maximum value etc.,
    print(df.describe())




def plot_keyword_rankings(df, keyword_id_to_plot, search_engine_to_plot):
    """
    To plot 'keyword_rank' vs 'dates' for a specific 'keyword_id' and 'search_engine' to know how 'keyword_rankings' 
    vary with 'dates' considering a specific 'keyword_id' and 'search_engine'. Here the 'keyword_id' and 'search_engine'
    selected are 8341 and 2 respectively.
    """
    # Filter data for the specific 'keyword_id' and 'search_engine'
    filtered_data = df[(df['keyword_id'] == keyword_id_to_plot) & (df['search_engine'] == search_engine_to_plot)]

    # Plotting the data
    plt.figure(figsize=(12, 8))
    plt.plot(filtered_data['date'], filtered_data['keyword_rank'], marker='o', linestyle='-')

    # Set the title of the plot
    plt.title(f'keyword_rank vs dates for keyword_id:{keyword_id_to_plot} and search_engine:{search_engine_to_plot}', fontsize=16)

    # Set labels for the x and y axis
    plt.xlabel('dates', fontsize=14)
    plt.ylabel('keyword_rank', fontsize=14)

    # Set font size for x-axis tick labels
    plt.xticks(fontsize=12)

    # Display the grid on the plot
    plt.grid(True)

    # Show the plot
    plt.show()


def plot_max_searches(df):
    """
    Plot the sum of searches vs. search_engine for the 'keyword_id' with maximum 'searches' (i.e., rank=1)
    for that specific engine by aggregating the searches across all 'dates'.
    """
    plt.figure(figsize=(20, 12))

    max_ids, max_searches = [], []

    # Iterate over each unique search engine
    for engine in df['search_engine'].unique():
        
        # Filter data for the specific search engine
        engine_data = df[df['search_engine'] == engine]
        
        # Calculate the sum of searches across all the dates for each keyword_id filtered by 'search_engine'
        keyword_sum = engine_data.groupby('keyword_id')['searches'].sum()

        # Find the keyword_id with the maximum searches
        max_id = keyword_sum.idxmax()
        max_search = keyword_sum[max_id]

        # Plot the bar for the search engine
        plt.bar(engine * 4, max_search, width=3, label=f'SE {engine}')
        
        # Store max keyword_id and searches for annotation
        max_ids.append(max_id)
        max_searches.append(max_search)

    # Annotatation of the bars with the corresponding keyword_id and searches
    for i, (keyword_id, searches) in enumerate(zip(max_ids, max_searches)):
        plt.text(i * 4, searches + 50, f'{keyword_id}', ha='center', va='bottom', rotation=45, fontsize=8)

    # Set plot labels and title
    plt.xlabel('search_engine number')
    plt.ylabel('Number of searches')
    plt.title('Number of searches vs search_engine for the top-ranked keyword_id', pad=20)

    # Sett x-axis ticks and labels with increased spacing
    plt.xticks(range(0, 26 * 4, 4), labels=[str(i) for i in range(26)], rotation=45, ha='right')

    # Moving the legend outside the plot area
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    # Show the plot
    plt.show()



if __name__ == "__main__":
    file_path = r"Path to .csv file" #Add path here
    df = load_dataset(file_path)

    # Explore the dataset
    explore_dataset(df)

    # Selecting a specific keyword and search engine for the first plot
    selected_keyword_id = 8341
    selected_search_engine = 2

    # Plot the keyword_rankings for the selected keyword_id and search_engine
    plot_keyword_rankings(df, selected_keyword_id, selected_search_engine)

    # Plot the 'searches' corresponding to the top-ranked 'keyword_id' (rank=1) for all search engines
    plot_max_searches(df)