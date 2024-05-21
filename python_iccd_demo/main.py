import pandas as pd


def from_dict(data: dict[str:str]):
    return pd.DataFrame.from_records(data)


def main():
    data = {"col1": [1, 2], "col2": [3, 4]}
    print(from_dict(data))


if __name__ == "__main__":
    main()
