
from datasets import load_dataset


class HFDatasetLoader:
    """Carga un dataset de Hugging Face y lo convierte en pandas."""

    def __init__(self, dataset_id, split="train"):
        self.dataset_id = dataset_id
        self.split = split

    def load_data(self):
        dataset = load_dataset(
            self.dataset_id,
            split=self.split
        )

        dataframe = dataset.to_pandas()

        return dataframe

