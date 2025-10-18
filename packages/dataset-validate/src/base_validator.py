from abc import ABC, abstractmethod

import pandas as pd
from spamirai_dataset_common import dataset_paths, mkdirp


class BaseValidator(ABC):
    def __init__(self, model: str):
        self._model = model

    @abstractmethod
    def get_predict(self, text: str) -> dict:
        pass

    def run(self):
        reports_dir = dataset_paths.dataset_dir / "reports"
        mkdirp(reports_dir)

        gitignore_path = reports_dir / ".gitignore"

        if not gitignore_path.exists():
            with open(gitignore_path, "w") as f:
                f.write("*\n")

        report_path = reports_dir / f"{self._model.replace('/', '_')}_report.csv"

        df = pd.read_csv(dataset_paths.validation_dataset_path)
        results = []

        count = len(df)

        for index, item in df.iterrows():
            predict = self.get_predict(item.text)

            if predict["label"] != item.label:
                is_spam = predict["label"] == "spam" and predict["score"] >= 0.99

                if is_spam or predict["label"] == "not_spam":
                    results.append(
                        {
                            "text": item.text,
                            "label": item.label,
                            "source": item.source,
                            "id": item.id,
                            "actual_label": predict["label"],
                            "actual_score": predict["score"],
                        }
                    )

            print(f"{index + 1}/{count}")

        pd.DataFrame.from_records(results).to_csv(report_path, index=False)
