from pathlib import Path

from spamirai_dataset_common import dataset_paths, mkdirp


def _normalize_model(model: str):
    return model.replace("/", "_")


class ReportPaths:
    def __init__(self):
        mkdirp(self.reports_dir)
        mkdirp(self.compare_reports_dir)

        gitignore_path = self.reports_dir / ".gitignore"

        if not gitignore_path.exists():
            with open(gitignore_path, "w") as f:
                f.write("*\n")

    @property
    def reports_dir(self) -> Path:
        return dataset_paths.dataset_dir / "reports"

    @property
    def compare_reports_dir(self) -> Path:
        return self.reports_dir / "diffs"

    def get_report_path(self, model: str) -> Path:
        return self.reports_dir / f"{_normalize_model(model)}_report.csv"

    def get_compare_report_path(self, previous_model: str, current_model: str) -> Path:
        return (
            self.compare_reports_dir
            / f"{_normalize_model(current_model)}_diff_{_normalize_model(previous_model)}_report.csv"
        )


report_paths = ReportPaths()
