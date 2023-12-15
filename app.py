import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Automated EDA with Streamlit')

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

# Load data if a file is uploaded
if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the loaded DataFrame
    st.write('## DataFrame:')
    st.write(df)

    # Sidebar for user input
    st.sidebar.header('Select Options:')
    selected_columns = st.sidebar.multiselect('Select columns:', df.columns)
    if not selected_columns:
        selected_columns = df.columns

    # Display descriptive statistics
    st.sidebar.subheader('[Descriptive Statistics:](#descriptive-statistics)')
    st.write('### Descriptive Statistics:')
    st.write(df[selected_columns].describe())

    

    # Display pair plot using Seaborn
    st.sidebar.subheader('[Pair Plot:](#pair-plot)')
    st.write('### Pair Plot:')
    pair_plot = sns.pairplot(df[selected_columns])
    st.pyplot(pair_plot)

    # Display distribution plots
    st.sidebar.subheader('[Distribution Plots:](#distribution-plots)')
    st.write('### Distribution Plots:')
    for column in selected_columns:
        st.write(f'#### {column} Distribution:')
        plt.hist(df[column], bins=20, color='skyblue', edgecolor='black')
        st.pyplot(plt.gcf())

    # Display correlation heatmap
    st.sidebar.subheader('[Correlation Heatmap:](#correlation-heatmap)')
    st.write('### Correlation Heatmap:')
    corr_matrix = df[selected_columns].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig.figure)

else:
    st.warning("Please upload a CSV file to analyze.")
