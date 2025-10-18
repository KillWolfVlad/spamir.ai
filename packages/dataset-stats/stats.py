from spamirai_dataset_common import dataset_paths
from src import print_stats


def main():
    paths = dataset_paths.get_all_dataset_layer_paths() + [
        dataset_paths.train_dataset_path,
        dataset_paths.test_dataset_path,
        dataset_paths.validation_dataset_path,
        dataset_paths.tuning_dataset_path,
    ]

    for path in paths:
        print_stats(path)


if __name__ == "__main__":
    main()
