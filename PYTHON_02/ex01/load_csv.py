import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """Loads a csv file into a pandas DataFrame"""
    assert os.path.exists(path), "File does not exist"
    if not path.endswith(".csv"):
        raise TypeError("Only .csv files are supported")
    try:
        data = pd.read_csv(path)
        print("Loading dataset of dimensions", data.shape)
        # modif = data.iloc[:, 1:]
        # print("modified data:\n", modif)
        # print("================")
        # print(data["country"])
        return data
    except FileNotFoundError:
        print("File not found")
        return None
    except PermissionError:
        print("Permission denied")
        return None
    except AssertionError as error:
        print(error)
        return None
