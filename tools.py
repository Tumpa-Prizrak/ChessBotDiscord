import matplotlib.pyplot as plt


class Plots:
    @staticmethod
    def create_joins_leaves_plot(joins: dict[str, int], leaves: dict[str, int], type_: str) -> None:
        return Plots._create_plit([(joins, "blue"), (leaves, "red")], "joines/leaves", type_)
    
    @staticmethod
    def create_joins_plot(joins: dict[str, int], type_: str) -> None:
        return Plots._create_plit([(joins, "blue")], "joines", type_)
    
    @staticmethod
    def create_leaves_plot(leaves: dict[str, int], type_: str) -> None:
        return Plots._create_plit([(leaves, "red")], "leaves", type_)
    
    @staticmethod
    def create_channel_plot(messages: dict[str, int], channel_name: str, type_: str) -> None:
        return Plots._create_plit([(messages, "blue")], f"Channel {channel_name}", type_)
    
    @staticmethod
    def _create_plit(data: list[tuple[dict[str, int], str]], title: str, type_: str) -> None:
        for plot_data in data:
            match type_:
                case "bar":
                    func = plt.bar
                case "scatter":
                    func = plt.scatter
                case "plot":
                    func = plt.plot
                case _:
                    raise TypeError
            func(plot_data[0].keys(), plot_data[0].values(), color = f"tab:{plot_data[1]}")  # type: ignore
        plt.xticks(rotation=90)
        plt.title(title)

        plt.savefig("output.png")

        plt.close()
