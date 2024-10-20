import pandas as pd
import sweetviz as sv

loan_test_set = pd.read_csv("../data/Loan_test_set.csv")

loan_test_set['id'] = loan_test_set['id'].astype(str)

report = sv.analyze(loan_test_set)

report.show_html("../reports/sweetviz_report.html")
