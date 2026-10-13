import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.container import BarContainer
from matplotlib.figure import Figure


class ScientificBarChart:
    def __init__(
        self,
        df: pd.DataFrame,
        category_col: str = "category_col",
        value_col: str = "value_col",
        title: str = "title",
        xlabel: str = "x_label",
        ylabel: str = "y_label",
    ) -> None:
        self.df: pd.DataFrame = df.copy()
        self.category_col: str = category_col
        self.value_col: str = value_col
        self.title: str = title
        self.xlabel: str = xlabel
        self.ylabel: str = ylabel
        self.figsize: tuple[int, int] = (10, 6)
        self.dpi: int = 150

    def plot(self) -> None:
        data: pd.DataFrame = self._prepare_data()
        _, ax = self._create_figure()
        bars: BarContainer = self._create_bars(ax, data)
        self._add_labels(ax, bars, data)
        self._configure_axes(ax, data)
        self._finalize_plot()

    def _prepare_data(self) -> pd.DataFrame:
        return self.df.sort_values(
            by=self.value_col,
            ascending=True,
        )

    def _create_figure(self) -> tuple[Figure, Axes]:
        return plt.subplots(
            figsize=self.figsize,
            dpi=self.dpi,
        )

    def _create_bars(
        self,
        ax: Axes,
        data: pd.DataFrame,
    ) -> BarContainer:
        return ax.barh(
            data[self.category_col],
            data[self.value_col],
            color="#4472A8",
            linewidth=0.6,
            height=0.7,
        )

    def _add_labels(
        self,
        ax: Axes,
        bars: BarContainer,
        data: pd.DataFrame,
    ) -> None:
        ax.bar_label(
            bars,
            labels=[f"{value:,.2f}" for value in data[self.value_col]],
            padding=5,
            fontsize=9,
        )

    def _configure_axes(
        self,
        ax: Axes,
        data: pd.DataFrame,
    ) -> None:
        ax.set_title(
            self.title,
            fontsize=14,
            fontweight="bold",
            pad=15,
        )
        ax.set_xlabel(self.xlabel, fontsize=11)
        ax.set_ylabel(self.ylabel, fontsize=11)

        ax.xaxis.grid(True, linestyle="--", alpha=0.4)
        ax.set_axisbelow(True)

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        max_value = data[self.value_col].max()

        if max_value > 0:
            ax.set_xlim(0, max_value * 1.18)

        ax.tick_params(axis="both", labelsize=9)

    def _finalize_plot(self) -> None:
        plt.tight_layout()
        plt.show()
