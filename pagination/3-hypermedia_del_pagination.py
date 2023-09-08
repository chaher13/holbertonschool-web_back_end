import csv
from typing import List, Dict


class Server:
    """
    The `Server` class represents a server that provides access to a dataset of popular baby names.

    Attributes:
        DATA_FILE (str): The filename of the CSV file containing the popular baby names dataset.
        __dataset (List[List]): The dataset of popular baby names.
        __indexed_dataset (Dict[int, List]): The indexed dataset of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes a new instance of the `Server` class.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Retrieves the dataset of popular baby names.

        Returns:
            List[List]: The dataset of popular baby names.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Retrieves the indexed dataset of popular baby names.

        Returns:
            Dict[int, List]: The indexed dataset of popular baby names.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves a subset of the indexed dataset based on the given index and page size.

        Args:
            index (int, optional): The starting index of the subset. Defaults to None.
            page_size (int, optional): The size of the subset. Defaults to 10.

        Returns:
            Dict: A dictionary containing the subset of data along with the index, next index, and page size.
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        total_rows = len(indexed_data)

        assert index < total_rows

        end_index = index + page_size

        if end_index > total_rows:
            end_index = total_rows

        page_data = [indexed_data[i] for i in range(index, end_index)]

        next_index = end_index

        return {
            "index": index,
            "next_index": next_index if next_index < total_rows else None,
            "page_size": page_size,
            "data": page_data,
        }
