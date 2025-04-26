import pandas as pd

from grade_helper import get_ects_grade, get_national_grade, grade_to_mark

print("==============================================================================\n")
print("SUBTASK 1")
print('Reading the dataset...')
df = pd.read_excel('1_workshop_DataSet.xlsx', index_col=0, engine='openpyxl')

print("Printing after success reading file")
print(df)

print("==============================================================================\n")
print("SUBTASK 2")
df['Total score for subject 1'] = df['Subject1. Test 1'] + df['Subject1. Test2']
df['Total score for subject 2'] = df['Subject2. Test 1'] + df['Subject2. Test 2']

print("Printing after success calculating total score of the tests!")
print(df)

print("==============================================================================\n")
print("SUBTASK 3")
df['ECTS grading scale subject 1'] = df['Total score for subject 1'].apply(get_ects_grade)
df['The national grading scale subject 1'] = df['Total score for subject 1'].apply(get_national_grade)

df['ECTS grading scale subject 2'] = df['Total score for subject 2'].apply(get_ects_grade)
df['The national grading scale subject 2'] = df['Total score for subject 2'].apply(get_national_grade)

print("Printing after success calculating ECTS and National grades!")
print(df)

print("Printing df.info() for checking data types!")
df.info()

print("==============================================================================\n")
print("SUBTASK 4")
df = df.reset_index()

new_df = df[['Last name','first name', 'Group',
             'The national grading scale subject 1',
             'The national grading scale subject 2']].copy()
new_df = new_df.rename(columns={
    'The national grading scale subject 1': 'The national grading scale Artificial Intelligence',
    'The national grading scale subject 2': 'The national grading scale Object-Oriented Programming'
})

print("Printing new dataset with renames subjects")
print(new_df)

new_df.to_excel('2_workshop_DataSet.xlsx', index=False)

print("==============================================================================\n")
print("SUBTASK 5")
new_df['The national grading scale Artificial Intelligence'] \
    = new_df['The national grading scale Artificial Intelligence'].map(grade_to_mark)
new_df['The national grading scale Object-Oriented Programming']\
    = new_df['The national grading scale Object-Oriented Programming'].map(grade_to_mark)

print("Printing new dataset with replaced marks")
print(new_df)

new_df.to_excel('Lab_2_DataSet.xlsx', index=False)

print("==============================================================================\n")
print("SUBTASK 6")
last_names_unique = new_df['Last name'].unique().tolist()
first_names_unique = new_df['first name'].unique().tolist()
groups_unique = new_df['Group'].unique().tolist()
ai_national_grades_unique = new_df['The national grading scale Artificial Intelligence'].unique().tolist()
oop_national_grades_unique = new_df['The national grading scale Object-Oriented Programming'].unique().tolist()

print("Unique last names:", last_names_unique)
print("Unique first names:", first_names_unique)
print("Unique groups:", groups_unique)
print("Unique AI national grades:", ai_national_grades_unique)
print("Unique OOP national grades:", oop_national_grades_unique)

print("==============================================================================\n")
print("SUBTASK 7")
last_name_counts = new_df['Last name'].value_counts().reset_index()
last_name_counts.columns = ['Last name', 'Count']

first_name_counts = new_df['first name'].value_counts().reset_index()
first_name_counts.columns = ['First name', 'Count']

group_counts = new_df['Group'].value_counts().reset_index()
group_counts.columns = ['Group', 'Count']

ai_grade_counts = new_df['The national grading scale Artificial Intelligence'].value_counts().reset_index()
ai_grade_counts.columns = ['Artificial Intelligence Grade', 'Count']

oop_grade_counts = new_df['The national grading scale Object-Oriented Programming'].value_counts().reset_index()
oop_grade_counts.columns = ['Object-Oriented Programming Grade', 'Count']

print("Last name counts:\n", last_name_counts)
print("\nFirst name counts:\n", first_name_counts)
print("\nGroup counts:\n", group_counts)
print("\nAI grade counts:\n", ai_grade_counts)
print("\nOOP grade counts:\n", oop_grade_counts)

print("==============================================================================\n")
print("SUBTASK 8")
filtered_students = new_df[
    (new_df['The national grading scale Artificial Intelligence'].isin([4, 5])) &
    (new_df['The national grading scale Object-Oriented Programming'].isin([4, 5]))
]

total_students = filtered_students.shape[0]

print(f'The number of students with only excellent and good marks in all groups: {total_students}')

print("==============================================================================\n")
print("SUBTASK 9")
unsatisfactory_students = new_df[
    (new_df['The national grading scale Artificial Intelligence'].isin([1, 2])) &
    (new_df['The national grading scale Object-Oriented Programming'].isin([1, 2]))
]

unsatisfactory_by_group = unsatisfactory_students.groupby('Group').size().reset_index(name='Number of Unsatisfactory Students')

print("Printing unsatisfactory mark's count by groups")
print(unsatisfactory_by_group)

print("==============================================================================\n")
print("SUBTASK 10")
grade_counts_ai = new_df.groupby('The national grading scale Artificial Intelligence').size().reset_index(name='Count')
grade_counts_oop = new_df.groupby('The national grading scale Object-Oriented Programming').size().reset_index(name='Count')

print("AI grade counts:\n", grade_counts_ai)
print("\nOOP grade counts:\n", grade_counts_oop)

print("==============================================================================\n")
print("SUBTASK 11")
non_unsatisfactory_students = new_df[
    ~new_df['The national grading scale Artificial Intelligence'].isin([1, 2]) &
    ~new_df['The national grading scale Object-Oriented Programming'].isin([1, 2])
]

group_counts_non_unsatisfactory = non_unsatisfactory_students.groupby('Group').size().reset_index(name='Count')

groups_without_unsatisfactory = group_counts_non_unsatisfactory[group_counts_non_unsatisfactory['Count'] > 0]

print("Groups without any Unsatisfactory marks:\n", groups_without_unsatisfactory)