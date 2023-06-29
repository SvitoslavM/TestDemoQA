data1 = ['commands', 'react', 'private', 'classified', 'general', 'downloads', 'wordFile', 'excelFile']

data2 = ['Commands', 'React', 'Private', 'Classified', 'General', 'Downloads', 'Word File.doc', 'Excel File.doc']

data2 = str(data2).replace(' ', '').replace('doc', '').replace('.', '').lower()
data1 = str(data1).lower()
data1 = str(data1).replace(" ", "").lower()
"""How to change text if we have different results"""
assert data2 == data1
