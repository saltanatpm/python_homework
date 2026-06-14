import plotly.express as px
import plotly.data as pldata
import pandas as pd

df = pldata.wind(return_type="pandas").copy()

print("FIRST 10 ROWS")
print(df.head(10))

print("\nLAST 10 ROWS")
print(df.tail(10))

print("\nDATA TYPES")
print(df.dtypes)

# Clean strength column only if needed
if df["strength"].dtype == "object":
    df.loc[:, "strength"] = pd.to_numeric(
        df["strength"]
        .astype(str)
        .str.replace(r"[^0-9.]", "", regex=True),
        errors="coerce"
    )

# Scatter plot
fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind Strength vs Frequency"
)

fig.write_html("wind.html")

print("\nwind.html created successfully.")

fig.show()