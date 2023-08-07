from enum import Enum
from typing import Callable
import matplotlib.pyplot as plt


class PlotType(Enum):
    """
    Defines constants for different types of plots.

    Attributes:
        BAR: Used for bar charts.
        SCATTER: Used for scatter plots. 
        PLOT: Used for line plots.
    """
    BAR = "bar"
    SCATTER = "scatter"
    PLOT = "plot"


class Plots:
    """
    Plots contains static methods for creating different types of plots.
    
    The key methods are:
    
    - create_joins_leaves_plot: Creates a combined bar plot for join/leave data.
    - create_joins_plot: Creates a bar plot for join data.
    - create_leaves_plot: Creates a bar plot for leave data.
    - create_channel_plot: Creates a bar plot for channel messages.
    
    These methods call the _create_plot method to generate the actual plot 
    based on provided data and settings.
    
    _create_plot handles the plot generation using matplotlib. 
    _get_plot_func maps the plot type to the corresponding matplotlib plot function.
    """
    @staticmethod
    def create_joins_leaves_plot(joins_data: dict[str, int], leaves_data: dict[str, int]) -> None:
        """
    Create a bar plot with joins_data in blue and leaves_data in red.
    
    Args:
        joins_data (dict[str, int]): Dictionary of join data 
            e.g. {'Mon': 12, 'Tue': 18, 'Wed': 22}
        leaves_data (dict[str, int]): Dictionary of leave data
            e.g. {'Mon': 5, 'Tue': 7, 'Wed': 10}
            
    Returns:
        None
    """
        Plots._create_plot(
            plot_data=[(joins_data, "blue"), (leaves_data, "red")],
            plot_title="Joins/Leaves", 
            plot_type=PlotType.BAR
        )

    @staticmethod
    def create_joins_plot(joins_data: dict[str, int]) -> None:
        """
        Create a blue bar plot for the join data.
        
        Args:
            joins_data (dict[str, int]): Dictionary of join data
                e.g. {'Mon': 12, 'Tue': 18, 'Wed': 22}
            
        Returns:
            None
        """
        Plots._create_plot(
            plot_data=[(joins_data, "blue")], 
            plot_title="Joins",
            plot_type=PlotType.BAR
        )

    @staticmethod
    def create_leaves_plot(leaves_data: dict[str, int]) -> None:
        """
        Create a red bar plot for the leave data.
        
        Args:
            leaves_data (dict[str, int]): Dictionary of leave data 
                e.g. {'Mon': 5, 'Tue': 7, 'Wed': 10}
                
        Returns:
            None
        """
        Plots._create_plot(
            plot_data=[(leaves_data, "red")],
            plot_title="Leaves",
            plot_type=PlotType.BAR
        )

    @staticmethod
    def create_channel_plot(channel_messages: dict[str, int], channel_name: str) -> None:
        """
        Create a blue bar plot for the channel's messages data.
        
        Args:
            channel_messages (dict[str, int]): Dictionary of channel message data
                e.g. {'Mon': 102, 'Tue': 87, 'Wed': 90}
            channel_name (str): Name of the channel
                e.g. 'general'
                
        Returns:
            None
        """
        Plots._create_plot(
            plot_data=[(channel_messages, "blue")],
            plot_title=f"Channel {channel_name}",
            plot_type=PlotType.BAR
        )

    @staticmethod
    def _create_plot(
        plot_data: list[tuple[dict[str, int], str]],
        plot_title: str,
        plot_type: PlotType
    ) -> None:
        """
        Generate the actual plot based on provided data, title, and plot type.
        
        Args:
            plot_data (list[tuple[dict, str]]): List of (data, color) tuples
            plot_title (str): Title for the plot
            plot_type (PlotType): Enum specifying plot type 
                e.g. PlotType.BAR
    Returns:
        Returns:
            None
        """
        for data_color in plot_data:
            plot_func = Plots._get_plot_func(plot_type)
            plot_func(
                data_color[0].keys(),
                data_color[0].values(),
                color=f"tab:{data_color[1]}"
            )

        plt.xticks(rotation=90)
        plt.title(plot_title)
        plt.savefig("output.png")
        plt.close()

    @staticmethod
    def _get_plot_func(plot_type: PlotType) -> Callable:
        """
        Return matplotlib plot function for the given plot type.
        
        Args:
            plot_type (PlotType): Enum specifying plot type
                
        Returns:
            Callable: Matplotlib plot function
        """
        match plot_type:
            case PlotType.BAR:
                return plt.bar
            case PlotType.SCATTER:
                return plt.scatter
            case PlotType.PLOT:
                return plt.plot
            case _:
                raise ValueError(f"Invalid plot type: {plot_type}")
