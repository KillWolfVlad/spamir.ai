import pandas as pd

from .report_paths import report_paths


class ReportsComparator:
    def compare(self, previous_model: str, current_model: str):
        previous_report_map = dict()
        current_report_map = dict()

        previous_report_path = report_paths.get_report_path(previous_model)
        current_report_path = report_paths.get_report_path(current_model)

        previous_report = pd.read_csv(previous_report_path)
        current_report = pd.read_csv(current_report_path)

        results = []

        for index, row in previous_report.iterrows():
            previous_report_map[row["id"]] = row.to_dict()

        for index, row in current_report.iterrows():
            current_report_map[row["id"]] = row.to_dict()

        for current_id, current_item in current_report_map.items():
            if current_id not in previous_report_map:
                current_item["status"] = "new_error"
                current_item["previous_actual_label"] = None
                current_item["previous_actual_score"] = None
            else:
                previous_item = previous_report_map[current_id]

                current_item["status"] = (
                    "still_error"
                    if current_item["actual_label"] == previous_item["actual_label"]
                    else "changed_error"
                )

                current_item["previous_actual_label"] = previous_item["actual_label"]
                current_item["previous_actual_score"] = previous_item["actual_score"]

            results.append(current_item)

        for previous_id, previous_item in previous_report_map.items():
            if previous_id not in current_report_map:
                previous_item["status"] = "fixed"
                previous_item["previous_actual_label"] = None
                previous_item["previous_actual_score"] = None

                results.append(previous_item)

        pd.DataFrame.from_records(results).to_csv(
            report_paths.get_compare_report_path(previous_model, current_model),
            index=False,
        )


reports_comparator = ReportsComparator()
