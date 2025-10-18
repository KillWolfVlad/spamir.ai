import os

import pandas as pd
from dotenv import load_dotenv
from spamirai_dataset_common import DataLabel, dataset_paths
from src import DatasetLayersLoader


def main():
    load_dotenv()

    validation_dataset_sources = os.getenv("VALIDATION_DATASET_SOURCES").split(",")
    train_size_multiplier = float(os.getenv("TRAIN_SIZE_MULTIPLIER"))
    random_state = int(os.getenv("RANDOM_STATE"))

    df = DatasetLayersLoader().load_all()

    df_validation = df[df["source"].isin(validation_dataset_sources)]

    df_main = (
        df.drop(df_validation.index)
        .drop_duplicates(
            subset=["text"],
            keep="first",
        )
        .reset_index(drop=True)
    )

    df_validation = df_validation.drop_duplicates(
        subset=["text"],
        keep="first",
    ).reset_index(drop=True)

    df_spam = df_main[df_main["label"] == DataLabel.SPAM.value]
    df_not_spam = df_main[df_main["label"] == DataLabel.NOT_SPAM.value]

    train_size_spam = int(len(df_spam) * train_size_multiplier)
    train_size_not_spam = int(len(df_not_spam) * train_size_multiplier)

    df_train = pd.concat(
        [
            df_spam.sample(train_size_spam, random_state=random_state),
            df_not_spam.sample(train_size_not_spam, random_state=random_state),
        ]
    ).sample(frac=1, random_state=random_state)

    df_test = df_main.drop(df_train.index).sample(
        frac=1,
        random_state=random_state,
    )

    df_tune = pd.concat([df_test, df_validation]).sample(
        frac=1,
        random_state=random_state,
    )

    df_train.to_csv(dataset_paths.train_dataset_path, index=False)
    df_test.to_csv(dataset_paths.test_dataset_path, index=False)
    df_validation.to_csv(dataset_paths.validation_dataset_path, index=False)
    df_tune.to_csv(dataset_paths.tuning_dataset_path, index=False)

    print(f"train size: {len(df_train)}")
    print(f"test size: {len(df_test)}")
    print(f"validation size: {len(df_validation)}")
    print(f"tune size: {len(df_tune)}")


if __name__ == "__main__":
    main()
