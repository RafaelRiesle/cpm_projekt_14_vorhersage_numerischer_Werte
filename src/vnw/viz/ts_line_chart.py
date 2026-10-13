import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class TimeSeriesPlots:
    def __init__(self, df: pd.DataFrame) -> pd.DataFrame:
        self.df = df.copy()

        plt.rcParams.update(
            {
                "font.family": "serif",
                "font.size": 11,
                "axes.labelsize": 12,
                "axes.titlesize": 14,
                "figure.dpi": 150,
                "axes.spines.top": False,
                "axes.spines.right": False,
                "figure.figsize": (10, 6),
            }
        )

    def plot_road_bike_prices(self) -> None:
        """Visualisiert die Stückpreise der Road-Bikes im Zeitverlauf."""

        r_bikes_df = self.df[self.df["ProductLine"] == "R"]

        fig, ax = plt.subplots()

        for model, group in r_bikes_df.groupby("Model"):
            group = group.sort_values("OrderDate")

            ax.plot(
                group["OrderDate"],
                group["UnitPrice"],
                label=model,
            )

        ax.set_title("Verkaufsbeträge von Road-Bikes über die Zeit")
        ax.set_xlabel("OrderDate")
        ax.set_ylabel("UnitPrice")

        ax.legend(title="Model")
        ax.tick_params(axis="x", labelrotation=45)
        ax.grid(axis="y", linestyle="--", alpha=0.5)

        fig.tight_layout()
        plt.show()

    def plot_sales_by_year_week(self) -> None:
        """Visualisiert den Verkaufsbetrag nach Jahr und Kalenderwoche."""

        data = (
            self.df.groupby("YearWeek")["SalesAmount"]
            .sum()
            .reset_index(name="Sales")
            .sort_values("YearWeek")
            .reset_index(drop=True)
        )

        data["Year"] = data["YearWeek"].astype(str).str[:4]

        fig, ax = plt.subplots(figsize=(12, 6))

        years = data["Year"].unique()
        colors = plt.cm.tab10(np.linspace(0, 1, len(years)))

        for year, color in zip(years, colors, strict=False):
            year_data = data[data["Year"] == year]

            ax.plot(
                year_data.index,
                year_data["Sales"],
                color=color,
                linewidth=1.5,
                marker="o",
                markersize=3,
                label=year,
            )

        # Jahresgrenzen markieren
        year_array = data["Year"].to_numpy()

        year_changes = np.where(year_array[1:] != year_array[:-1])[0] + 1

        for boundary in year_changes:
            ax.axvline(
                boundary - 0.5,
                color="grey",
                linestyle="--",
                linewidth=0.8,
                alpha=0.6,
            )

        tick_positions = np.arange(0, len(data), 5)

        ax.set_xticks(tick_positions)
        ax.set_xticklabels(
            data["YearWeek"].iloc[tick_positions],
            rotation=45,
            ha="right",
        )

        ax.set_title(
            "Verkaufsbeträge nach Jahr und Kalenderwoche",
            pad=14,
        )
        ax.set_xlabel("Jahr und Kalenderwoche")
        ax.set_ylabel("Verkaufsbetrag")

        ax.grid(
            axis="y",
            linestyle="--",
            linewidth=0.6,
            alpha=0.5,
        )
        ax.set_axisbelow(True)
        ax.legend(title="Jahr", frameon=False)

        ax.spines["left"].set_linewidth(0.8)
        ax.spines["bottom"].set_linewidth(0.8)

        fig.tight_layout()
        plt.show()

    def plot_monthly_sales_by_year(self) -> None:
        """Vergleicht monatliche Bestellmengen verschiedener Jahre
        und zeigt den jeweiligen Jahresmittelwert.
        """

        sales_per_year_week = (
            self.df.groupby(["Year", "Month", "Week"])["OrderQuantity"]
            .sum()
            .reset_index(name="Sales")
        )

        monthly_sales = sales_per_year_week.groupby(["Year", "Month"], as_index=False)[
            "Sales"
        ].sum()

        years = sorted(monthly_sales["Year"].unique())
        months = sorted(monthly_sales["Month"].unique())

        x = np.arange(len(months))
        width = 0.8 / len(years) if years else 0.8

        fig, ax = plt.subplots(figsize=(12, 6))

        colors = plt.cm.Blues(np.linspace(0.35, 0.9, max(len(years), 1)))

        max_value = 0

        for i, year in enumerate(years):
            data = (
                monthly_sales[monthly_sales["Year"] == year]
                .set_index("Month")["Sales"]
                .reindex(months, fill_value=0)
            )

            ax.bar(
                x + (i - (len(years) - 1) / 2) * width,
                data.values,
                width=width,
                label=str(year),
                color=colors[i],
                edgecolor="black",
                linewidth=0.4,
            )

            mean_value = data.mean()

            ax.axhline(
                y=mean_value,
                color=colors[i],
                linestyle="--",
                linewidth=1.5,
                alpha=0.9,
                label=f"{year} Mittelwert: {mean_value:,.0f}",
            )

            max_value = max(
                max_value,
                data.max(),
                mean_value,
            )

        ax.set_xlabel("Monat")
        ax.set_ylabel("Gesamte Bestellmenge")
        ax.set_title(
            "Monatliche Bestellmengen nach Jahr mit Jahresmittelwert",
            pad=14,
        )

        ax.set_xticks(x)
        ax.set_xticklabels(months)

        if max_value > 0:
            ax.set_ylim(0, max_value * 1.15)
            ax.set_yticks(np.linspace(0, max_value * 1.15, 8))

        ax.grid(
            axis="y",
            linestyle="--",
            linewidth=0.6,
            alpha=0.5,
        )
        ax.set_axisbelow(True)

        ax.legend(
            title="Jahr / Jahresmittelwert",
            frameon=False,
            ncol=2,
            loc="upper left",
            bbox_to_anchor=(1.02, 1),
        )

        ax.spines["left"].set_linewidth(0.8)
        ax.spines["bottom"].set_linewidth(0.8)

        fig.tight_layout()
        plt.show()
