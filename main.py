import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

df1 = pd.read_csv("insurance.csv")


def average_age(df):
    """ Returns average age in all records, rounded to 2 d.p. """
    return round(df.age.mean(), 2)


def plot_age(df):
    """ Plots age as a histogram.  """
    sns.histplot(df.age,
                 kde=False,
                 bins=list(range(0, 100, 10)),
                 color="darkorchid")
    plt.title("Age Distribution", y=1.05, fontsize=15)
    plt.xlabel("Age", labelpad=10, fontsize=11)
    plt.ylabel("Frequency", labelpad=10, fontsize=11)

    plt.show()


def plot_age_costs(df):
    """ Plots age against insurance cost. """
    x_values = df.age
    y_values = df.charges
    x_label = "age (years)"
    y_label = "charges ($)"

    sns.lineplot(x=x_values, y=y_values)
    plt.title("Age vs. Insurance cost", y=1.05, fontsize=15)
    plt.xlabel(x_label, labelpad=10, fontsize=11)
    plt.ylabel(y_label, labelpad=10, fontsize=11)

    plt.show()


def sex_ratio(df):
    """ Returns dictionary with freq of each sex. """
    return df.region.value_counts().to_dict()


def plot_sex(df):
    """ Plots sex ratio as pie chart. """
    series = df.sex.value_counts().to_dict()
    values = series.values()
    labels = series.keys()
    colors = ["tab:blue", "tab:pink"]
    title = "Sex ratio"

    plt.pie(x=values,
            labels=labels,
            colors=colors,
            explode=[0.04] * len(values),
            autopct="%.1f%%",
            pctdistance=0.5,
            startangle=90)
    plt.title(title, fontsize=14)

    plt.show()
 
    
def plot_sex_costs(df):
    """ Plots sex against insurance cost. """
    x_values = df.sex
    y_values = df.charges
    x_label = "Sex"
    y_label = "charges ($)"

    sns.barplot(x=x_values, y=y_values, capsize=0.1)
    plt.title("Sex vs. Insurance cost", y=1.05, fontsize=15)
    plt.xlabel(x_label, labelpad=10, fontsize=11)
    plt.ylabel(y_label, labelpad=10, fontsize=11)

    plt.show()


def region_ratio(df):
    """ Returns dictionary with num of records in each region. """
    return df.region.value_counts().to_dict()


def plot_region(df):
    """ Plots region ratio as pie chart. """
    series = df.region.value_counts().to_dict()
    values = series.values()
    labels = series.keys()
    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red"]
    title = "Regions"

    plt.pie(x=values,
            labels=labels,
            colors=colors,
            explode=[0.04] * len(values),
            autopct="%.1f%%",
            pctdistance=0.5,
            startangle=90)
    plt.title(title, fontsize=14)

    plt.show()
    
    
def plot_region_costs(df):
    """ Plots region against insurance cost. """
    x_values = df.region
    y_values = df.charges
    x_label = "region"
    y_label = "charges ($)"

    sns.barplot(x=x_values, y=y_values, capsize=0.1)
    plt.title("Region vs. Insurance cost", y=1.05, fontsize=15)
    plt.xlabel(x_label, labelpad=10, fontsize=11)
    plt.ylabel(y_label, labelpad=10, fontsize=11)

    plt.show()


def average_bmi(df):
    """ Returns average BMI, rounded to to d.p. """
    return round(df.bmi.mean(), 2)


def plot_bmi(df):
    """ Plots BMI as a histogram. """
    sns.histplot(df.bmi,
                 kde=True,
                 bins=list(range(0, 60, 1)),
                 color="darkorchid")
    plt.title("BMI Distribution", y=1.05, fontsize=15)
    plt.xlabel("BMI", labelpad=10, fontsize=11)
    plt.ylabel("Frequency", labelpad=10, fontsize=11)

    plt.show()


def plot_bmi_costs(df):
    """ Plots bmi against insurance cost. """
    x_values = df.bmi.round()
    y_values = df.charges
    x_label = "BMI"
    y_label = "charges ($)"

    sns.lineplot(x=x_values, y=y_values)
    plt.title("BMI vs. Insurance cost", y=1.05, fontsize=15)
    plt.xlabel(x_label, labelpad=10, fontsize=11)
    plt.ylabel(y_label, labelpad=10, fontsize=11)

    plt.show()


def smoker_ratio(df):
    """ Returns dictionary of smoker status. """
    return df.smoker.value_counts().to_dict()


def plot_smoker(df):
    """ Plots smoker status as pie chart. """
    series = df.smoker.value_counts().to_dict()
    values = series.values()
    labels = series.keys()
    colors = ["tab:blue", "tab:red"]
    title = "Smoker status"

    plt.pie(x=values,
            labels=labels,
            colors=colors,
            explode=[0.04] * len(values),
            autopct="%.1f%%",
            pctdistance=0.5,
            startangle=90)
    plt.title(title, fontsize=14)

    plt.show()


def plot_smoker_costs(df):
    """ Plots smoker status against insurance cost. """
    x_values = df.smoker
    y_values = df.charges
    x_label = "Smoker status"
    y_label = "charges ($)"

    sns.barplot(x=x_values, y=y_values, capsize=0.1)
    plt.title("Smoker status vs. Insurance cost", y=1.05, fontsize=15)
    plt.xlabel(x_label, labelpad=10, fontsize=11)
    plt.ylabel(y_label, labelpad=10, fontsize=11)

    plt.show()


def average_children(df):
    """ Returns average number of children per person, rounded to 2 d.p. """
    return round(df.children.mean(), 2)


def plot_children(df):
    """ Plots number of children per person as a histogram.  """
    sns.histplot(df.children,
                 kde=False,
                 bins=list(range(0, 10, 1)),
                 color="darkorchid")
    plt.title("Children Distribution", y=1.05, fontsize=15)
    plt.xlabel("Children", labelpad=10, fontsize=11)
    plt.xticks(list(range(0, 10, 1)))
    plt.ylabel("Frequency", labelpad=10, fontsize=11)

    plt.show()


def plot_children_costs(df):
    """ Plots number of children against insurance cost. """
    x_values = df.children
    y_values = df.charges
    x_label = "Children"
    y_label = "charges ($)"

    sns.barplot(x=x_values, y=y_values, capsize=0.1)
    plt.title("Children vs. Insurance cost", y=1.05, fontsize=15)
    plt.xlabel(x_label, labelpad=10, fontsize=11)
    plt.ylabel(y_label, labelpad=10, fontsize=11)

    plt.show()
