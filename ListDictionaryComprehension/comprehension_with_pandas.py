import pandas as pd

student_dict = {
    "names": ["Tom", "Jerry", "Harry"],
    "scores": [91, 83, 67]
}

student_data_frame = pd.DataFrame(student_dict)

# loop through rows of data frame
for index, row in student_data_frame.iterrows():
    print(row.names)


