import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use("Agg")  # Headless mode for saving files


# 1. Bar Chart - Compare Avg Salary by Country (Side-by-Side Bars)
def plot_salary_comparison(df):
    """
    Create a side-by-side bar chart comparing onsite vs remote salaries.
    Using MELT to reshape data for plotting.
    """
    print("Plotting Salary Comparison...")

    # 1. MELT the data
    df_long = df.melt(
        id_vars="country",
        value_vars=["salary_remote", "salary_onsite"],
        var_name="salary_type", 
        value_name="amount"
    )

    print("Melted DataFrame Preview:")
    print(df_long.head())
    
    plt.figure(figsize=(12, 6))

    sns.barplot(
        data=df_long, 
        x="country", 
        y="amount",
        hue="salary_type",    
        palette=["#e74c3c", "#2c3e50"],
        errorbar=None
    )

    plt.title("Average Salary Comparison: Remote vs Onsite")
    plt.xlabel("Country")
    plt.ylabel("Avg Salary (USD)")
    plt.grid(axis="y", alpha=0.3)
    
    plt.savefig("salary_comparison.png", bbox_inches="tight")
    print("Chart saved: salary_comparison.png")
    
    # Returning the melted dataframe
    return df_long


# 2. Scatter Plot - Multi-variable
def plot_salary_vs_experience(df):
    """
    Scatter plot with semantic mapping.
    """
    print("Plotting Salary vs Experience...")

    fig = plt.figure(figsize=(10, 6))

    plt.scatter(
        df["experience_years"],
        df["salary_remote"],
        s=df["remote_ratio"] * 5,
        alpha=0.7,
        edgecolors="black"
    )
    
    plt.title("Experience vs Remote Salary (Size = Remote Ratio)")
    plt.xlabel("Years of Experience")
    plt.ylabel("Remote Salary (USD)")
    plt.grid(True, alpha=0.3)

    plt.savefig("salary_experience_scatter.png", bbox_inches='tight')
    print("Chart saved: salary_experience_scatter.png")

    # Returning the figure object
    return fig


# 3. KDE Plot - Distribution Analysis
def plot_salary_kde(df):
    """
    Plot KDE density estimate.
    """
    print("Plotting Salary Density (KDE)...")

    fig = plt.figure(figsize=(10, 6))

    sns.kdeplot(
        data=df,
        x="salary_onsite",
        hue="job_role",
        fill=True,
        alpha=0.4,
    )

    plt.title("Salary Distribution by Job Role (KDE)")
    plt.xlabel("Onsite Salary (USD)")
    plt.grid(True, alpha=0.3)

    plt.savefig("salary_kde.png", bbox_inches='tight')
    print("Chart saved: salary_kde.png")
    
    return fig


# 4. Faceted Plot - Role Trends
def plot_faceted_relplot(df):
    """
    Multiple scatter plot using figure-level relplot.
    """
    print("Plotting Faceted Role Trends...")

    g = sns.relplot(
        data=df,
        x="experience_years",
        y="salary_onsite",
        hue="country",
        col="job_role",
        kind="scatter",
    )

    g.fig.suptitle("Global Salary Trends by Role & Experience", y=1.03)
    
    plt.savefig("faceted_salary_roles.png", bbox_inches="tight")
    print("Chart saved: faceted_salary_roles.png")
    
    return g


if __name__ == "__main__":
    print("Global Salary Index Analyzer Project...\n")

    path = "global_salaries.csv"
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"Error: {path} not found.")
        df = None

    if df is not None:
        plot_salary_comparison(df)
        plot_salary_vs_experience(df)
        plot_salary_kde(df)
        plot_faceted_relplot(df)


