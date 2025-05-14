# 🌸 Iris Dataset Analysis with Plot Customization and Error Handling

# 🔧 Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# 🎨 Plot style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# 📥 Load Dataset with Error Handling
try:
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({i: name for i, name in enumerate(iris.target_names)})
    print("✅ Iris dataset loaded successfully.")
except Exception as e:
    print("❌ Failed to load dataset:", e)

# 👁️ Preview
df.head()

# 🌸 Scatter Plot
try:
    sns.scatterplot(
        data=df,
        x='sepal length (cm)',
        y='sepal width (cm)',
        hue='species',
        palette='Set2'
    )
    plt.title("Sepal Length vs Sepal Width by Species")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    plt.legend(title="Species")
    plt.show()
except Exception as e:
    print("❌ Error generating scatter plot:", e)

# 📈 Histogram
try:
    sns.histplot(data=df, x='petal length (cm)', hue='species', kde=True, palette='Set1')
    plt.title("Petal Length Distribution by Species")
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Frequency")
    plt.legend(title="Species")
    plt.show()
except Exception as e:
    print("❌ Error generating histogram:", e)

# 📦 Boxplots for All Features
try:
    features = iris.feature_names
    for feature in features:
        sns.boxplot(data=df, x='species', y=feature, palette='pastel')
        plt.title(f"{feature.title()} by Species")
        plt.xlabel("Species")
        plt.ylabel(feature.title())
        plt.show()
except Exception as e:
    print("❌ Error generating boxplots:", e)

# 🔗 Pairplot
try:
    sns.pairplot(df, hue='species', palette='husl')
    plt.suptitle("Pairwise Feature Relationships in Iris Dataset", y=1.02)
    plt.show()
except Exception as e:
    print("❌ Error generating pairplot:", e)


# 🧠 Summary
print("✅ Analysis Completed")
print("- Sepal dimensions vary distinctly by species.")
print("- Petal length is especially useful for differentiating classes.")
print("- The dataset is well-balanced and suitable for classification.")


week-8-project-development-python/
│
├── README.md              # (With project title, objectives, instructions)
├── iris_analysis.ipynb    # (This notebook file)
└── requirements.txt       # (Optional: list of libraries)




