from earnings.spreadsheet import build_csv_rows


def test_build_csv_rows_normalizes_bmo_amc_labels():
    rows = build_csv_rows(
        [
            {
                "company": "Acme Corp",
                "date": "2026-04-13",
                "bmo_amc": "time-pre-market",
                "coverage": "Core",
                "reporter": "Analyst A",
            },
            {
                "company": "Beta Inc",
                "date": "2026-04-14",
                "bmo_amc": "after-hours",
                "coverage": "Extended",
                "reporter": "Analyst B",
            },
        ]
    )

    assert rows[1]["BMO/AMC"] == "BMO"
    assert rows[3]["BMO/AMC"] == "AMC"
